impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut ans = Vec::new();
        for i in 1..=n {
            match i % 15 {
               0 => ans.push("FizzBuzz".to_string()),
               3 | 6 | 9 | 12 => ans.push("Fizz".to_string()),
               5 | 10 => ans.push("Buzz".to_string()),
               _ => ans.push(i.to_string()),
            }
        }

        ans
    }
}