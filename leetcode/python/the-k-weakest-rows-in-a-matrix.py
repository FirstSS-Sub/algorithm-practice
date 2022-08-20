from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans_list = []
        count_list = []
        for i in range(len(mat)):
            count_list.append(mat[i].count(1))
            ans_list.append(i)
        sorted_zip_list = sorted(zip(count_list, ans_list))
        _, sorted_ans_list = zip(*sorted_zip_list)
        
        return sorted_ans_list[:k]