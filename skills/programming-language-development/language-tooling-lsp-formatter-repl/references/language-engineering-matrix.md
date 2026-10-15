# LSP Framing & Formatter Idempotency Reference

Using character length instead of UTF-8 byte length in `Content-Length` desynchronizes the LSP stream as soon as a file contains a non-ASCII UTF-8 character.
