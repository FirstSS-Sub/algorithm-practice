use std::{collections::HashSet, hash::Hash};

impl Solution {
    pub fn num_unique_emails(emails: Vec<String>) -> i32 {
       let mut ans: HashSet<String> = HashSet::new();
       for email in emails.iter() {
           let a: Vec<String> = email.split("@").map(str::to_string).collect();
           let b: Vec<String> = a[0].split("+").map(str::to_string).collect();
           let c = b[0].replace(".", "");
           ans.insert(format!("{}@{}", c, a[2]).to_string());
       }
       
       ans.len() as i32
    }
}
