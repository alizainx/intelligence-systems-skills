# Verified Example: `jvm-dotnet-managed-systems` (`JmmBoundedQueue.java`)

```
// Java 17/21 & C# CLR Memory Model (JMM Happens-Before & Bounded Ring Queue)
public final class JmmBoundedQueue<T> {
    private final Object[] items;
    private int head = 0, tail = 0, count = 0;
    public JmmBoundedQueue(int capacity) {
        if (capacity <= 0) throw new IllegalArgumentException("capacity <= 0");
        this.items = new Object[capacity];
    }
}

```
