use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut ans: Vec<Vec<String>> = Vec::new();

        let mut use_flag_vec = vec![false; strs.len()];
        for (i, str1) in strs.iter().enumerate() {
            if use_flag_vec[i] { continue; }

            let mut group_vec: Vec<String> = Vec::new();
            group_vec.push(str1.to_string());
            use_flag_vec[i] = true;

            let mut m = HashMap::new();
            str1.chars().for_each(|c| m.insert(c, ()));

            for (j, str2) in strs.iter().enumerate() {
                if use_flag_vec[j] { continue; }

                let mut match_flag = true;
                str2.chars().map(|c| if !m.contains_key(&c) { match_flag = false });
                if match_flag {
                    group_vec.push(str2.to_string());
                }
                use_flag_vec[j] = true;
            }

            ans.push(group_vec);
        }

        ans
    }
}

