# Nontrivial Implementation & Multi-File Engineering Walkthrough: `csharp-dotnet-engineering`

- **Target File**: `examples/ZeroAllocSpanParser.cs`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
using System;

namespace Iss.DotNet;

public readonly record struct MetricFrame(uint SensorId, long Value);

public static class ZeroAllocSpanParser
{
    public static bool TryParseHeader(ReadOnlySpan<byte> buffer, out MetricFrame frame)
    {
        frame = default;
        if (buffer.Length < 12 || buffer[0] != 0xA5) return false;
        uint id = System.Buffers.Binary.BinaryPrimitives.ReadUInt32LittleEndian(buffer.Slice(4, 4));
        long val = System.Buffers.Binary.BinaryPrimitives.ReadInt64LittleEndian(buffer.Slice(8, 4));
        frame = new MetricFrame(id, val);
        return true;
    }
}

```
