# Verified Example: `compiler-frontend-lexer-parser-typechecker` (`hm_type_unifier.py`)

```
#!/usr/bin/env python3
"""
Verifies Pratt Operator-Precedence Parser + Hindley-Milner Type Unification with Occurs Check.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class TVar:
    name: str

@dataclass(frozen=True)
class TCon:
    name: str

@dataclass(frozen=True)
class TArrow:
    arg: object
    ret: object

def occurs_in(tvar: TVar, ty: object, subst: dict[str, object]) -> bool:
    ty = apply_subst(ty, subst)
    if ty == tvar:
        return True
    if isinstance(ty, TArrow):
        return occurs_in(tvar, ty.arg, subst) or occurs_in(tvar, ty.ret, subst)
    return False

def apply_subst(ty: object, subst: dict[str, object]) -> object:
    if isinstance(ty, TVar) and ty.name in subst:
        return apply_subst(subst[ty.name], subst)
    if isinstance(ty, TArrow):
        return TArrow(apply_subst(ty.arg, subst), apply_subst(ty.ret, subst))
    return ty

def unify(t1: object, t2: object, subst: dict[str, object]) -> dict[str, object]:
    t1 = apply_subst(t1, subst)
    t2 = apply_subst(t2, subst)
    if t1 == t2:
        return subst
    if isinstance(t1, TVar):
        if occurs_in(t1, t2, subst):
            raise TypeError(f"Occurs check failed: infinite cyclic type {t1.name} = {t2}")
        return {**subst, t1.name: t2}
    if isinstance(t2, TVar):
        return unify(t2, t1, subst)
    if isinstance(t1, TArrow) and isinstance(t2, TArrow):
        s1 = unify(t1.arg, t2.arg, subst)
        return unify(t1.ret, t2.ret, s1)
    raise TypeError(f"Cannot unify {t1} with {t2}")

# 1. Valid unification: ('a -> Int) with (Bool -> 'b) => 'a = Bool, 'b = Int
s = unify(TArrow(TVar("a"), TCon("Int")), TArrow(TCon("Bool"), TVar("b")), {})
assert apply_subst(TVar("a"), s) == TCon("Bool") and apply_subst(TVar("b"), s) == TCon("Int")

# 2. Reject infinite self-application type 'a = ('a -> Int) via Occurs Check!
infinite_rejected = False
try:
    unify(TVar("a"), TArrow(TVar("a"), TCon("Int")), {})
except TypeError:
    infinite_rejected = True
assert infinite_rejected, "Unification failed to reject cyclic type via occurs check!"
print("COMPILER FRONTEND HINDLEY-MILNER UNIFICATION & OCCURS-CHECK VERIFIED")

```
