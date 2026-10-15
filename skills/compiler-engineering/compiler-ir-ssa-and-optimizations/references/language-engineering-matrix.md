# SSA Optimization & Register Allocation Reference

When spilling a register in linear-scan allocation, spill the active interval whose live range ends furthest in the future (Belady's optimal heuristic).
