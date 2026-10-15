# HDL Synthesis Rules, WebAssembly Stack Typing & LLVM IR Reference

Never mix blocking `=` and non-blocking `<=` on the same signal in `always_ff`, and never cross asynchronous clock domains without a 2-FF synchronizer or gray-coded FIFO.
