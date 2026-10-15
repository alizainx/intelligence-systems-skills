# PCIe, NVMe Queue Phase Protocol & DMA Barrier Reference

Forgetting to invert the expected Phase Tag when `cq_head` wraps to `0` causes the driver to re-consume stale completions from the previous ring epoch.
