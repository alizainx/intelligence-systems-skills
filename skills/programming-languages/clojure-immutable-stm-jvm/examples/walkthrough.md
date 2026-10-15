# Nontrivial Implementation & Multi-File Engineering Walkthrough: `clojure-immutable-stm-jvm`

- **Target File**: `examples/transducer_stm_ledger.clj`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
(ns iss.clojure.transducer-stm-ledger
  (:require [clojure.edn :as edn]))

(set! *warn-on-reflection* true)
(set! *unchecked-math* :warn-on-boxed)

(defn transfer-atomic! [from-ref to-ref ^long amount]
  (when (<= amount 0)
    (throw (ex-info "Transfer amount must be positive" {:amount amount})))
  (dosync
    (let [bal (long @from-ref)]
      (if (< bal amount)
        {:ok false :reason :insufficient-funds}
        (do
          (alter from-ref - amount)
          (alter to-ref + amount)
          {:ok true :remaining (- bal amount)})))))

(defn sum-valid-amounts [coll]
  (transduce (comp (filter pos-int?) (map long)) + 0 coll))

```
