#!/usr/bin/env python3
"""
Verification runner for `compiler-and-pl-engineering`.
Tests:
1. SSA structural verifier rejection of double-definition, use-before-def, and Bool+Int type mismatch.
2. Constant folding + DCE instruction reduction and translation-validation equivalence across parameter inputs.
3. Preservation of runtime division-by-zero trap under dead-code elimination.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
MOD_PATH = HERE / "examples" / "ssa_optimizer.py"

def main() -> int:
    ns: dict = {}
    exec(MOD_PATH.read_text(), ns)
    Instr = ns["Instr"]
    TypeTag = ns["TypeTag"]
    SSAVerificationError = ns["SSAVerificationError"]
    verify_ssa = ns["verify_ssa"]
    optimize_ssa = ns["optimize_ssa_const_fold_and_dce"]
    eval_ssa = ns["eval_ssa"]

    # 1. Negative tests: double definition, use-before-def, and type error must be rejected
    bad_double_def = [
        Instr("%a", "CONST", (1,), TypeTag.INT),
        Instr("%a", "CONST", (2,), TypeTag.INT),
        Instr("_", "RET", ("%a",), TypeTag.INT),
    ]
    for bad_prog in [
        bad_double_def,
        [Instr("%a", "ADD", ("%undef", "%undef"), TypeTag.INT), Instr("_", "RET", ("%a",), TypeTag.INT)],
        [
            Instr("%a", "CONST", (1,), TypeTag.INT),
            Instr("%b", "EQ", ("%a", "%a"), TypeTag.BOOL),
            Instr("%c", "ADD", ("%a", "%b"), TypeTag.INT),  # Type error: Int + Bool
            Instr("_", "RET", ("%c",), TypeTag.INT),
        ],
    ]:
        caught = False
        try:
            verify_ssa(bad_prog)
        except SSAVerificationError:
            caught = True
        assert caught, "verify_ssa failed to reject invalid SSA program"

    # 2. Positive & translation validation: fold constants and eliminate dead temporaries
    prog = [
        Instr("%x", "PARAM", ("x",), TypeTag.INT),
        Instr("%c1", "CONST", (10,), TypeTag.INT),
        Instr("%c2", "CONST", (20,), TypeTag.INT),
        Instr("%c3", "MUL", ("%c1", "%c2"), TypeTag.INT),        # Folds to 200
        Instr("%dead1", "ADD", ("%c1", "%c3"), TypeTag.INT),     # Dead instruction -> eliminated
        Instr("%res", "ADD", ("%x", "%c3"), TypeTag.INT),
        Instr("_", "RET", ("%res",), TypeTag.INT),
    ]
    opt_prog = optimize_ssa(prog)
    assert len(opt_prog) < len(prog), "Optimization did not reduce instruction count"
    for x_val in [-50, 0, 7, 1024]:
        orig_out = eval_ssa(prog, {"x": x_val})
        opt_out = eval_ssa(opt_prog, {"x": x_val})
        assert orig_out == opt_out == x_val + 200

    # 3. Trapping division by zero in dead variable must NOT be silently DCE'd away
    trap_prog = [
        Instr("%c0", "CONST", (0,), TypeTag.INT),
        Instr("%c5", "CONST", (5,), TypeTag.INT),
        Instr("%trap_unused", "DIV", ("%c5", "%c0"), TypeTag.INT),
        Instr("_", "RET", ("%c5",), TypeTag.INT),
    ]
    opt_trap = optimize_ssa(trap_prog)
    trapped = False
    try:
        eval_ssa(opt_trap, {})
    except ZeroDivisionError:
        trapped = True
    assert trapped, "Optimizer unsoundly eliminated trapping division by zero!"

    print("ALL COMPILER & PL ENGINEERING SSA + TRANSLATION VALIDATION TESTS PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
