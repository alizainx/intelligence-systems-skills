# Nontrivial Implementation & Multi-File Engineering Walkthrough: `ocaml-modules-and-compilers`

- **Target File**: `examples/ssa_expr_simplifier.ml`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
module type EXPR_SIMPLIFIER = sig
  type expr =
    | Const of int
    | Var of string
    | Add of expr * expr
    | Mul of expr * expr

  val simplify : expr -> expr
end

module ExprSimplifier : EXPR_SIMPLIFIER = struct
  type expr =
    | Const of int
    | Var of string
    | Add of expr * expr
    | Mul of expr * expr

  let rec simplify = function
    | Const _ | Var _ as atom -> atom
    | Add (a, b) ->
        (match simplify a, simplify b with
         | Const 0, r -> r
         | l, Const 0 -> l
         | Const x, Const y -> Const (x + y)
         | l, r -> Add (l, r))
    | Mul (a, b) ->
        (match simplify a, simplify b with
         | Const 0, _ | _, Const 0 -> Const 0
         | Const 1, r -> r
         | l, Const 1 -> l
         | Const x, Const y -> Const (x * y)
         | l, r -> Mul (l, r))
end

```
