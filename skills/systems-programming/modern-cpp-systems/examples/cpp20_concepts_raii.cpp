#include <cassert>
#include <concepts>
#include <cstddef>
#include <cstdint>
#include <iostream>
#include <span>
#include <utility>

template <typename T>
concept TrivialMetric = std::integral<T> || std::floating_point<T>;

template <TrivialMetric T, std::size_t Capacity>
class FixedRingBuffer {
    T storage_[Capacity]{};
    std::size_t head_{0};
    std::size_t tail_{0};
    std::size_t count_{0};
public:
    constexpr FixedRingBuffer() noexcept = default;
    [[nodiscard]] constexpr bool push(T val) noexcept {
        if (count_ == Capacity) return false;
        storage_[head_] = val;
        head_ = (head_ + 1U) % Capacity;
        ++count_;
        return true;
    }
    [[nodiscard]] constexpr bool pop(T& out) noexcept {
        if (count_ == 0U) return false;
        out = storage_[tail_];
        tail_ = (tail_ + 1U) % Capacity;
        --count_;
        return true;
    }
    [[nodiscard]] constexpr std::size_t size() const noexcept { return count_; }
};

consteval std::uint32_t compile_time_selftest() {
    FixedRingBuffer<std::uint32_t, 4> rb;
    if (!rb.push(10U) || !rb.push(20U)) return 0U;
    std::uint32_t a = 0, b = 0;
    if (!rb.pop(a) || !rb.pop(b)) return 0U;
    return a + b;
}

int main() {
    static_assert(compile_time_selftest() == 30U, "consteval ring buffer test");
    FixedRingBuffer<std::int64_t, 2> rt;
    assert(rt.push(7) && rt.push(9) && !rt.push(11));
    std::int64_t out = 0;
    assert(rt.pop(out) && out == 7);
    std::cout << "VERIFIED: C++20 Concepts, consteval, noexcept & RAII ring buffer passed\n";
    return 0;
}
