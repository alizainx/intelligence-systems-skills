#include <array>
#include <cassert>
#include <concepts>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <span>

template <std::integral T>
[[nodiscard]] constexpr bool safe_mul_size(T a, T b, T& out) noexcept {
    if (a < 0 || b < 0) return false;
    if (a == 0 || b == 0) { out = 0; return true; }
    if (a > (static_cast<T>(-1) / b)) return false;
    out = static_cast<T>(a * b);
    return true;
}

int main() {
    std::size_t res = 0U;
    static_assert(std::integral<std::size_t>);
    assert(safe_mul_size<std::size_t>(1024U, 64U, res) && res == 65536U);
    assert(!safe_mul_size<std::size_t>(static_cast<std::size_t>(-1) / 2U + 2U, 2U, res));
    std::array<std::uint32_t, 8> buf{1, 2, 3, 4, 5, 6, 7, 8};
    std::span<std::uint32_t> sp{buf};
    assert(sp.subspan(2, 4).size() == 4U && sp.subspan(2, 4)[0] == 3U);
    std::printf("MODERN C++20 SYSTEMS VERIFIED\n");
    return 0;
}
