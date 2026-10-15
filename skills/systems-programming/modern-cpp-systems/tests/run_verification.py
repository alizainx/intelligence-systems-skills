#!/usr/bin/env python3
import subprocess, tempfile
from pathlib import Path
CODE = '#include <array>\n#include <cassert>\n#include <concepts>\n#include <cstddef>\n#include <cstdint>\n#include <cstdio>\n#include <span>\n\ntemplate <std::integral T>\n[[nodiscard]] constexpr bool safe_mul_size(T a, T b, T& out) noexcept {\n    if (a < 0 || b < 0) return false;\n    if (a == 0 || b == 0) { out = 0; return true; }\n    if (a > (static_cast<T>(-1) / b)) return false;\n    out = static_cast<T>(a * b);\n    return true;\n}\n\nint main() {\n    std::size_t res = 0U;\n    static_assert(std::integral<std::size_t>);\n    assert(safe_mul_size<std::size_t>(1024U, 64U, res) && res == 65536U);\n    assert(!safe_mul_size<std::size_t>(static_cast<std::size_t>(-1) / 2U + 2U, 2U, res));\n    std::array<std::uint32_t, 8> buf{1, 2, 3, 4, 5, 6, 7, 8};\n    std::span<std::uint32_t> sp{buf};\n    assert(sp.subspan(2, 4).size() == 4U && sp.subspan(2, 4)[0] == 3U);\n    std::printf("MODERN C++20 SYSTEMS VERIFIED\\n");\n    return 0;\n}\n'
with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp)
    (p / "test.cpp").write_text(CODE)
    subprocess.run(["g++", "-std=c++20", "-O2", "-Wall", "-Wextra", "-Werror", "-Wpedantic", "-Wconversion", "-Wold-style-cast", "-fsanitize=address,undefined", str(p / "test.cpp"), "-o", str(p / "test")], check=True)
    subprocess.run([str(p / "test")], check=True)
