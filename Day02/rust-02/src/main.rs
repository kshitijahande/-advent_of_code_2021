fn main() {
    println!("{}", part_a());
    println!("{}", part_b());
}

fn part_a() -> i32 {
    let (fp, dp) = include_str!("../../input.txt")
        .lines()
        .map(|line| line.split_once(" ").unwrap())
        .fold((0, 0), |(fp, dp), (k, v)| {
            match (k, v.parse::<i32>().unwrap()) {
                ("forward", v) => (fp + v, dp),
                ("down", v) => (fp, dp + v),
                ("up", v) => (fp, dp - v),
                _ => panic!(),
            }
        });
    fp * dp
}

fn part_b() -> i32 {
    let (fp, dp, _) = include_str!("../../input.txt")
        .lines()
        .map(|l| l.split_once(" ").unwrap())
        .fold((0, 0, 0), |(fp, dp, aim), (k, v)| {
            match (k, v.parse::<i32>().unwrap()) {
                ("forward", v) => (fp + v, dp + aim * v, aim),
                ("down", v) => (fp, dp, aim + v),
                ("up", v) => (fp, dp, aim - v),
                _ => unreachable!(),
            }
        });
    fp * dp
}
