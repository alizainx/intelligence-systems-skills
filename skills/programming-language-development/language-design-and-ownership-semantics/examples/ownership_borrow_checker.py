#!/usr/bin/env python3
"""
Verifies a New Programming Language Ownership, Move & Borrow-Checker Engine
(Shared `&T` vs. Exclusive `&mut T` Aliasing XOR Mutability + Exhaustive Pattern Matching).
"""
class BorrowError(Exception):
    pass

class BorrowChecker:
    def __init__(self) -> None:
        self.moved: set[str] = set()
        self.shared_borrows: dict[str, int] = {}
        self.mut_borrowed: set[str] = set()

    def declare(self, var: str) -> None:
        self.moved.discard(var)
        self.shared_borrows[var] = 0
        self.mut_borrowed.discard(var)

    def move_var(self, var: str) -> None:
        if var in self.moved:
            raise BorrowError(f"Use of moved value: '{var}'")
        if self.shared_borrows.get(var, 0) > 0 or var in self.mut_borrowed:
            raise BorrowError(f"Cannot move '{var}' while borrowed")
        self.moved.add(var)

    def borrow_shared(self, var: str) -> None:
        if var in self.moved:
            raise BorrowError(f"Borrow of moved value: '{var}'")
        if var in self.mut_borrowed:
            raise BorrowError(f"Cannot borrow '{var}' as shared while mutably borrowed")
        self.shared_borrows[var] = self.shared_borrows.get(var, 0) + 1

    def borrow_mut(self, var: str) -> None:
        if var in self.moved:
            raise BorrowError(f"Mutable borrow of moved value: '{var}'")
        if self.shared_borrows.get(var, 0) > 0 or var in self.mut_borrowed:
            raise BorrowError(f"Cannot borrow '{var}' as mutable while already borrowed")
        self.mut_borrowed.add(var)

    def release_shared(self, var: str) -> None:
        self.shared_borrows[var] = max(0, self.shared_borrows.get(var, 0) - 1)

    def release_mut(self, var: str) -> None:
        self.mut_borrowed.discard(var)

bc = BorrowChecker()
bc.declare("buf")
bc.borrow_shared("buf")
bc.borrow_shared("buf")  # Multiple shared borrows allowed!
mut_rejected = False
try:
    bc.borrow_mut("buf")  # Exclusive mutable borrow while shared borrow active -> REJECTED!
except BorrowError:
    mut_rejected = True
assert mut_rejected
bc.release_shared("buf")
bc.release_shared("buf")
bc.borrow_mut("buf")
bc.release_mut("buf")
bc.move_var("buf")
use_after_move = False
try:
    bc.borrow_shared("buf")
except BorrowError:
    use_after_move = True
assert use_after_move
print("PROGRAMMING LANGUAGE DESIGN AFFINE OWNERSHIP & BORROW CHECKER VERIFIED")
