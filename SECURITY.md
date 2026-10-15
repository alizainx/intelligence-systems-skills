# Security Policy — `intelligence-systems-skills`

All skills, C/C++/Assembly/Rust/Wasm reference implementations, OS/kernel subsystems, and compiler passes in `intelligence-systems-skills` enforce strict memory safety, `W^X` page protection, TOCTOU prevention, and sanitizer verification (`-fanalyzer`, `ASan`, `UBSan`). Report any security escape using the 6-field defect schema in `shared/verification/verification-gates.md`.
