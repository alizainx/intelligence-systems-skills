# Nontrivial Implementation & Multi-File Engineering Walkthrough: `llvm-ir-ssa-codegen`

- **Target File**: `examples/opaque_ptr_ssa_dot.ll`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
; ModuleID = 'opaque_ptr_ssa_dot'
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

define dso_local i64 @dot_product_i64(ptr noalias nocapture noundef readonly %a,
                                      ptr noalias nocapture noundef readonly %b,
                                      i64 noundef %n) local_unnamed_addr #0 {
entry:
  %cmp_zero = icmp eq i64 %n, 0
  br i1 %cmp_zero, label %exit, label %loop

loop:
  %idx = phi i64 [ 0, %entry ], [ %idx_next, %loop ]
  %acc = phi i64 [ 0, %entry ], [ %acc_next, %loop ]
  %pa = getelementptr inbounds i64, ptr %a, i64 %idx
  %pb = getelementptr inbounds i64, ptr %b, i64 %idx
  %va = load i64, ptr %pa, align 8
  %vb = load i64, ptr %pb, align 8
  %prod = mul i64 %va, %vb
  %acc_next = add i64 %acc, %prod
  %idx_next = add nuw i64 %idx, 1
  %done = icmp eq i64 %idx_next, %n
  br i1 %done, label %exit, label %loop

exit:
  %res = phi i64 [ 0, %entry ], [ %acc_next, %loop ]
  ret i64 %res
}
attributes #0 = { nofree norecurse nosync nounwind memory(argmem: read) }

```
