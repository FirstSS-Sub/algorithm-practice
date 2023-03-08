impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut ans = 0;
        let mut before_c = ' ';
        s.chars().rev().for_each(|c| {
            match c {
                'I' => match before_c {
                    'V' | 'X' => ans -= 1,
                    _ => ans += 1
                },
                'X' => match before_c {
                    'L' | 'C' => ans -= 10,
                    _ => ans += 10
                }
                'C' => match before_c {
                    'D' | 'M' => ans -= 100,
                    _ => ans += 100
                }
                'V' => ans += 5,
                'L' => ans += 50,
                'D' => ans += 500,
                'M' => ans += 1000,
                _ => panic!()
            }
            before_c = c
        });
        ans
    }
}
