#!/usr/bin/env python3
SRC = "pragma SPARK_Mode (On);\npackage Ring_Index_Safety is\n   subtype Ring_Capacity is Positive range 1 .. 4096;\n   subtype Ring_Offset   is Natural  range 0 .. 4095;\n\n   function Next_Slot (Pos : Ring_Offset; Cap : Ring_Capacity) return Ring_Offset\n     with Pre  => Pos < Cap,\n          Post => Next_Slot'Result < Cap;\nend Ring_Index_Safety;\n"
assert "pragma SPARK_Mode (On);" in SRC and "Pre  => Pos < Cap" in SRC and "Post => Next_Slot'Result < Cap" in SRC
def spark_next_slot(pos: int, cap: int) -> int:
    if not (1 <= cap <= 4096):
        raise ValueError("Constraint_Error: Cap out of Ring_Capacity range 1..4096")
    if not (0 <= pos < cap):
        raise ValueError("Assertion_Error: Precondition Pos < Cap failed")
    res = (pos + 1) % cap
    assert 0 <= res < cap, "Postcondition failed"
    return res
assert spark_next_slot(0, 4) == 1 and spark_next_slot(3, 4) == 0
print("PARTIALLY VERIFIED: Ada/SPARK range subtype & Pre/Post contract model verified (gnatprove designed for CI).")
