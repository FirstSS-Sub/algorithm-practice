use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut map: HashMap<char, i32> = HashMap::new();
        s.chars().for_each(|c| *map.entry(c).or_insert(0) += 1);
        for (i, c) in s.chars().enumerate() {
            if *map.get(&c).unwrap() == 1 {
                return i as i32;
            }
        }

        -1
    }
}
