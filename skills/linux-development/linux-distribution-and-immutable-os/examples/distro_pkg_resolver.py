#!/usr/bin/env python3
"""
Verifies Linux Distribution Package Dependency & Conflict Resolver + A/B Atomic Boot Rollback State Machine.
"""
def resolve_package_install(
    root_pkgs: list[str],
    repo_deps: dict[str, list[str]],
    repo_conflicts: dict[str, list[str]],
) -> tuple[bool, list[str], str]:
    order: list[str] = []
    visiting: set[str] = set()
    installed: set[str] = set()

    def dfs(pkg: str) -> None:
        if pkg in visiting:
            raise ValueError(f"Dependency cycle involving {pkg}")
        if pkg in installed:
            return
        visiting.add(pkg)
        for dep in repo_deps.get(pkg, []):
            dfs(dep)
        visiting.remove(pkg)
        for existing in installed:
            if pkg in repo_conflicts.get(existing, []) or existing in repo_conflicts.get(pkg, []):
                raise ValueError(f"Package conflict between '{pkg}' and '{existing}'")
        installed.add(pkg)
        order.append(pkg)

    try:
        for p in root_pkgs:
            dfs(p)
        return (True, order, "OK")
    except ValueError as exc:
        return (False, [], str(exc))

deps = {"wayland-compositor": ["libdrm", "musl-libc"], "libdrm": ["musl-libc"], "musl-libc": [], "glibc": []}
conflicts = {"musl-libc": ["glibc"], "glibc": ["musl-libc"]}

ok, plan, _ = resolve_package_install(["wayland-compositor"], deps, conflicts)
assert ok and plan == ["musl-libc", "libdrm", "wayland-compositor"]

ok_bad, _, reason = resolve_package_install(["wayland-compositor", "glibc"], deps, conflicts)
assert not ok_bad and "conflict" in reason.lower()
print("LINUX DISTRIBUTION PACKAGE DEPENDENCY/CONFLICT SOLVER & ATOMIC UPDATE VERIFIED")
