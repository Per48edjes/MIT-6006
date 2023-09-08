module Lib (module Lib) where

import Data.Function.Memoize (memoize)
import Data.Vector (Vector, (!))

canWin :: Vector Int -> Vector Int -> Bool
canWin zs ds
    | length zs /= length ds = error "mismatched input array lengths"
    -- NOTE: I have no idea if this is actually memoized...
    | otherwise = delegatesNeededToWin ds <= memoize (x zs ds) 0

x :: Vector Int -> Vector Int -> Int -> Int
x zs ds i
    | i < 0 || i > end = error "index out of bounds"
    | i == end = ds ! i
    | i == end - 1 = max ((ds ! i) + (zs ! (i + 1))) ((zs ! i) + (ds ! (i + 1)))
    | i == end - 2 = max ((ds ! i) + (zs ! (i + 1)) + (zs ! (i + 2))) ((zs ! i) + x zs ds (i + 1))
    | otherwise = max ((ds ! i) + (zs ! (i + 1)) + (zs ! (i + 2)) + x zs ds (i + 3)) ((zs ! i) + x zs ds (i + 1))
  where
    end = length zs - 1

delegatesNeededToWin :: Vector Int -> Int
delegatesNeededToWin ds = sum ds `div` 2 + 1
