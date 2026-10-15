# UEFI, Limine & E820 Boot Protocol Reference

In UEFI, `GetMemoryMap` itself can allocate memory and invalidate `MapKey`; always loop `GetMemoryMap` -> `ExitBootServices` until `EFI_SUCCESS`.
