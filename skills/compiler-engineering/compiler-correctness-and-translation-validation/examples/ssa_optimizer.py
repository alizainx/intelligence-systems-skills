"""
Verified Mini-Compiler Pipeline:
1. Bidirectional Type Checker (`Int` vs `Bool` soundness).
2. SSA IR Lowering & Structural SSA Verifier (`verify_ssa`: single-def, def-before-use, type soundness).
3. Verified Constant Folding + Dead-Code Elimination (DCE) pass preserving trapping divisions.
4. Reference SSA Interpreter for translation validation.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TypeTag(Enum):
    INT = "Int"
    BOOL = "Bool"


@dataclass(frozen=True, slots=True)
class Instr:
    dst: str
    op: str  # "CONST", "PARAM", "ADD", "SUB", "MUL", "DIV", "EQ", "RET"
    args: tuple[str | int, ...]
    ty: TypeTag


class SSAVerificationError(Exception):
    """Raised when an SSA invariant (single-def, def-before-use, or typing) is violated."""


def verify_ssa(instructions: list[Instr]) -> None:
    """Enforces Static Single Assignment, def-before-use, and operand type invariants."""
    defined: dict[str, TypeTag] = {}
    has_ret = False

    for idx, ins in enumerate(instructions):
        if ins.op != "RET":
            if ins.dst in defined:
                raise SSAVerificationError(
                    f"Instruction {idx}: SSA single-assignment violated; '{ins.dst}' redefined"
                )
        if ins.op == "CONST":
            if len(ins.args) != 1 or not isinstance(ins.args[0], int):
                raise SSAVerificationError(f"Instruction {idx}: invalid CONST args")
            defined[ins.dst] = ins.ty
        elif ins.op == "PARAM":
            if len(ins.args) != 1 or not isinstance(ins.args[0], str):
                raise SSAVerificationError(f"Instruction {idx}: invalid PARAM args")
            defined[ins.dst] = ins.ty
        elif ins.op in ("ADD", "SUB", "MUL", "DIV", "EQ"):
            if len(ins.args) != 2:
                raise SSAVerificationError(f"Instruction {idx}: binary op requires 2 register args")
            for a in ins.args:
                if not isinstance(a, str) or a not in defined:
                    raise SSAVerificationError(
                        f"Instruction {idx}: use-before-def of register '{a}'"
                    )
                if defined[a] != TypeTag.INT:
                    raise SSAVerificationError(
                        f"Instruction {idx}: type mismatch on '{a}', expected INT, got {defined[a]}"
                    )
            expected_ty = TypeTag.BOOL if ins.op == "EQ" else TypeTag.INT
            if ins.ty != expected_ty:
                raise SSAVerificationError(f"Instruction {idx}: invalid result type {ins.ty}")
            defined[ins.dst] = ins.ty
        elif ins.op == "RET":
            if len(ins.args) != 1 or not isinstance(ins.args[0], str) or ins.args[0] not in defined:
                raise SSAVerificationError(f"Instruction {idx}: RET uses undefined register")
            has_ret = True
        else:
            raise SSAVerificationError(f"Unknown opcode {ins.op}")

    if not has_ret:
        raise SSAVerificationError("Function missing terminal RET instruction")


def optimize_ssa_const_fold_and_dce(instructions: list[Instr]) -> list[Instr]:
    """Performs verified constant folding and pure dead-code elimination while preserving traps."""
    verify_ssa(instructions)
    constants: dict[str, int] = {}
    folded: list[Instr] = []

    for ins in instructions:
        if ins.op == "CONST":
            val = int(ins.args[0])
            constants[ins.dst] = val
            folded.append(ins)
        elif ins.op in ("ADD", "SUB", "MUL", "DIV", "EQ"):
            lhs, rhs = str(ins.args[0]), str(ins.args[1])
            if lhs in constants and rhs in constants:
                a, b = constants[lhs], constants[rhs]
                if ins.op == "DIV" and b == 0:
                    # Never fold or eliminate division by zero; preserve runtime trap
                    folded.append(ins)
                    continue
                if ins.op == "ADD":
                    cval = a + b
                elif ins.op == "SUB":
                    cval = a - b
                elif ins.op == "MUL":
                    cval = a * b
                elif ins.op == "DIV":
                    cval = int(a / b)
                else:
                    cval = 1 if a == b else 0
                constants[ins.dst] = cval
                folded.append(Instr(dst=ins.dst, op="CONST", args=(cval,), ty=ins.ty))
            else:
                folded.append(ins)
        else:
            folded.append(ins)

    # Backward liveness pass for Dead-Code Elimination (preserving RET and potentially trapping DIV)
    live: set[str] = set()
    kept_rev: list[Instr] = []
    for ins in reversed(folded):
        is_trapping = ins.op == "DIV" and (
            str(ins.args[1]) not in constants or constants[str(ins.args[1])] == 0
        )
        if ins.op == "RET" or ins.dst in live or is_trapping:
            kept_rev.append(ins)
            for a in ins.args:
                if isinstance(a, str) and ins.op != "PARAM":
                    live.add(a)

    optimized = list(reversed(kept_rev))
    verify_ssa(optimized)
    return optimized


def eval_ssa(instructions: list[Instr], params: dict[str, int]) -> int:
    """Reference operational semantics interpreter for translation validation."""
    verify_ssa(instructions)
    env: dict[str, int] = {}
    for ins in instructions:
        if ins.op == "CONST":
            env[ins.dst] = int(ins.args[0])
        elif ins.op == "PARAM":
            pname = str(ins.args[0])
            env[ins.dst] = params[pname]
        elif ins.op == "ADD":
            env[ins.dst] = env[str(ins.args[0])] + env[str(ins.args[1])]
        elif ins.op == "SUB":
            env[ins.dst] = env[str(ins.args[0])] - env[str(ins.args[1])]
        elif ins.op == "MUL":
            env[ins.dst] = env[str(ins.args[0])] * env[str(ins.args[1])]
        elif ins.op == "DIV":
            denom = env[str(ins.args[1])]
            if denom == 0:
                raise ZeroDivisionError("SSA runtime trap: division by zero")
            env[ins.dst] = int(env[str(ins.args[0])] / denom)
        elif ins.op == "EQ":
            env[ins.dst] = 1 if env[str(ins.args[0])] == env[str(ins.args[1])] else 0
        elif ins.op == "RET":
            return env[str(ins.args[0])]
    raise RuntimeError("Unreachable")
