use std::collections::HashMap;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut ans: Vec<i32> = vec![];
        nums1.iter().for_each(|x| { map.insert(*x, 1); } );
        nums2.iter().for_each(|x| {
            if let Some(v) = map.get_mut(x) {
                *v += 1;
                if *v == 2 { ans.push(*x); }
            }
        });

        ans
    }
}

