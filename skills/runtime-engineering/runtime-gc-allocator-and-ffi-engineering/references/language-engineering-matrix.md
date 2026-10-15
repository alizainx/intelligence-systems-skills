# Tri-Color GC Write Barrier & FFI Marshaling Reference

Without a write barrier, linking a black object to a white object and unlinking the grey path causes the collector to prematurely free a live object!
