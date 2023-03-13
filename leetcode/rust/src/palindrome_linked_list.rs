use std::collections::VecDeque;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val,
        }
    }
}

impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut current = head;
        let mut q1 = VecDeque::new();
        let mut q2 = VecDeque::new();
        while current.is_some() {
            let c = current.unwrap();
            q1.push_front(c.val);
            q2.push_back(c.val);
            current = c.next;
        }
        while !q1.is_empty() {
            if q1.pop_back().unwrap() != q2.pop_back().unwrap() { return false }
        }

        true
    }
}
