fn main() {
    println!("{}", part_a());
    println!("{}", part_b());
}

fn part_a() -> usize {
    include_str!("../../input.txt")
        .lines()
        .map(|n| n.parse().unwrap())
        .collect::<Vec<u16>>()
        .windows(2)
        .filter(|n| n[0] < n[1])
        .count()
}

fn part_b() -> usize {
    include_str!("../../input.txt")
        .lines()
        .map(|n| n.parse().unwrap())
        .collect::<Vec<u16>>()
        .windows(4)
        .filter(|n| n[3] > n[0])
        .count()
}
