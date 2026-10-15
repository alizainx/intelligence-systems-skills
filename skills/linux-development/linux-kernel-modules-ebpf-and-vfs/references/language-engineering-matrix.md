# Linux Kernel Module & eBPF Verifier Reference

Adding a variable offset to a packet pointer resets the eBPF verifier's `max_range` tracking; re-check against `data_end` before dereferencing.
