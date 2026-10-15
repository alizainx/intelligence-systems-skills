# Portable Linux User-Space (`glibc`/`musl`/`relibc`) & Wayland Protocol Reference

Allocating multi-megabyte arrays on local thread stacks crashes on `musl` Linux distributions where default `pthread` stack size is 128 KiB.
