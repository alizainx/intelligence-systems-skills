(* OCaml / Haskell / Erlang OTP Supervision Restart Intensity & Exhaustive ADT Evaluator *)
type expr =
  | Lit of int
  | Add of expr * expr
  | SafeDiv of expr * expr
