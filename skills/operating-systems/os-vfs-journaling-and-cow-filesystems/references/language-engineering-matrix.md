# Filesystem Journaling & CoW Crash Consistency Reference

Never replay WAL records belonging to a transaction that lacks a valid checksummed commit block.
