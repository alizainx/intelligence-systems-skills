{-# LANGUAGE BangPatterns #-}
{-# LANGUAGE StrictData #-}
module StrictLedgerFold (AccountBalance(..), applyDeltas) where

import Data.List (foldl')
import Data.Int (Int64)

newtype AccountBalance = AccountBalance { unBalance :: Int64 }
  deriving (Eq, Show)

applyDeltas :: AccountBalance -> [Int64] -> Either String AccountBalance
applyDeltas initBal deltas = foldl' step (Right initBal) deltas
  where
    step (Left err) _ = Left err
    step (Right (AccountBalance !cur)) !d
      | cur + d < 0 = Left "Negative balance rejected"
      | otherwise   = Right (AccountBalance (cur + d))
