fn f(i: u64) -> u64 {
    println!("{}", i);
    1 + if i == u64::MAX { 0 } else { f(i + 1) }
}

fn main() {
    println!("{}", f(0));
}
