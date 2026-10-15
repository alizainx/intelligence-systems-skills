# Language Semantics, Type Soundness & Borrow Checking Reference

Never allow a resource to be moved while an active reference (`&T` or `&mut T`) aliases it.
