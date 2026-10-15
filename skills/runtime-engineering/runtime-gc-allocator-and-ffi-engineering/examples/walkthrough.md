# Verified Example: `runtime-gc-allocator-and-ffi-engineering` (`tricolor_gc_barrier.py`)

```
#!/usr/bin/env python3
"""
Verifies a Tri-Color Mark-and-Sweep Garbage Collector with Dijkstra/Steele Write Barrier
preserving the Strong Tri-Color Invariant (no Black object points directly to a White object).
"""
WHITE, GREY, BLACK = 0, 1, 2

class TriColorHeap:
    def __init__(self) -> None:
        self.color: dict[int, int] = {}
        self.edges: dict[int, set[int]] = {}
        self.grey_stack: list[int] = []

    def alloc(self, obj_id: int) -> None:
        self.color[obj_id] = WHITE
        self.edges[obj_id] = set()

    def mark_roots(self, roots: list[int]) -> None:
        for r in roots:
            if self.color.get(r) == WHITE:
                self.color[r] = GREY
                self.grey_stack.append(r)

    def step_mark(self) -> bool:
        if not self.grey_stack:
            return False
        obj = self.grey_stack.pop()
        for child in self.edges.get(obj, set()):
            if self.color[child] == WHITE:
                self.color[child] = GREY
                self.grey_stack.append(child)
        self.color[obj] = BLACK
        return True

    def write_barrier_store_edge(self, src: int, dst: int) -> None:
        """Dijkstra Write Barrier: if mutator stores a pointer from a BLACK object to a WHITE object, shade dst GREY!"""
        self.edges[src].add(dst)
        if self.color.get(src) == BLACK and self.color.get(dst) == WHITE:
            self.color[dst] = GREY
            self.grey_stack.append(dst)

    def sweep(self) -> list[int]:
        reclaimed = [oid for oid, c in list(self.color.items()) if c == WHITE]
        for oid in reclaimed:
            del self.color[oid]
            del self.edges[oid]
        for oid in self.color:
            self.color[oid] = WHITE
        return sorted(reclaimed)

heap = TriColorHeap()
for i in (1, 2, 3, 4):
    heap.alloc(i)
heap.edges[1].add(2)
heap.mark_roots([1])
heap.step_mark()  # Object 1 is now BLACK, Object 2 is GREY, Object 3 (reachable later) & Object 4 (garbage) are WHITE
# Mutator links BLACK object 1 -> WHITE object 3 during incremental marking!
heap.write_barrier_store_edge(1, 3)
while heap.step_mark():
    pass
freed = heap.sweep()
assert freed == [4] and 3 in heap.color, f"Write barrier failed to protect newly linked object 3: freed={freed}"
print("RUNTIME TRI-COLOR GARBAGE COLLECTOR & WRITE BARRIER INVARIANT VERIFIED")

```
