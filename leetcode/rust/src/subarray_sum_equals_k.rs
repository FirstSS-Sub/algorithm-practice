use std::collections::HashMap;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut map: HashMap<i32, i32> = HashMap::new();
        map.insert(0, 1);

        let (mut sum, mut ans) = (0, 0);
        nums.iter().for_each(|&num| {
            sum += num;
            *map.entry(sum).or_insert(0) += 1;
            if let Some(x) = map.get_mut(&(sum - k)) {
                ans += *x;
            }
        });

        ans
    }
}
