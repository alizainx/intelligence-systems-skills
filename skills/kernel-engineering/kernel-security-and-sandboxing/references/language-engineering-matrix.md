# Kernel Syscall Boundary & TOCTOU Prevention Reference

Reading `user_ptr->len` to validate bounds and then reading `user_ptr->len` a second time for `memcpy` allows a concurrent user thread to race and overflow the kernel buffer.
