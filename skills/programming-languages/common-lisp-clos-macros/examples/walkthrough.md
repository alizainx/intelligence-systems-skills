# Nontrivial Implementation & Multi-File Engineering Walkthrough: `common-lisp-clos-macros`

- **Target File**: `examples/safe_sexp_reader.lisp`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
(defpackage #:iss.safe-reader
  (:use #:cl)
  (:export #:safe-read-from-string #:with-gensyms))
(in-package #:iss.safe-reader)

(defmacro with-gensyms ((&rest names) &body body)
  `(let ,(loop for n in names collect `(,n (gensym ,(string n))))
     ,@body))

(declaim (ftype (function (string) (values t boolean)) safe-read-from-string))
(defun safe-read-from-string (input)
  (with-standard-io-syntax
    (let ((*read-eval* nil))
      (handler-case
          (values (read-from-string input nil nil) t)
        (error () (values nil nil))))))

```
