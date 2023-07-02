# Python

## Recursion
Got a `RecursionError` after 1,000 recursive calls.
Got a `RecursionError` after 1,000 interleaved recursive calls.

# Rust

## Recursion
On a Linux machine with a maximum stack size of 8 MiB, an example recursive function that has a single `u64` parameter and returns a `u64` panics after
- a bit over 70,000 recursive calls in a debug build and
- a bit over 100,000 recursive calls in a release build.
