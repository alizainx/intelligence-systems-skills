# LFS Toolchain Bootstrap & Sysroot Isolation Reference

Attempting to build hosted `libstdc++` before target `libc` and Linux API headers are installed in `$LFS/usr/include` fails due to missing POSIX types.
