# Nontrivial Implementation & Multi-File Engineering Walkthrough: `scala-functional-jvm`

- **Target File**: `examples/OpaqueDomainModel.scala`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
package com.iss.scala3
import scala.annotation.tailrec

object DomainTypes:
  opaque type NonEmptyToken = String
  object NonEmptyToken:
    def apply(s: String): Either[String, NonEmptyToken] =
      if s != null && s.trim.nonEmpty then Right(s.trim)
      else Left("Token cannot be empty")
    extension (t: NonEmptyToken) def value: String = t

  @tailrec
  def gcd(a: Long, b: Long): Long =
    if b == 0L then scala.math.abs(a) else gcd(b, a % b)

```
