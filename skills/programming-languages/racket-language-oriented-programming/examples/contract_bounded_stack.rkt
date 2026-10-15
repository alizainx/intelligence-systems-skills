#lang racket/base
(require racket/contract/base)

(struct bounded-stack (cap items) #:transparent)

(provide
 (contract-out
  [make-bounded-stack (-> exact-positive-integer? bounded-stack?)]
  [stack-push (->i ([s bounded-stack?] [v any/c])
                   #:pre (s) (< (length (bounded-stack-items s)) (bounded-stack-cap s))
                   [result bounded-stack?])]))

(define (make-bounded-stack cap)
  (bounded-stack cap '()))

(define (stack-push s v)
  (bounded-stack (bounded-stack-cap s) (cons v (bounded-stack-items s))))
