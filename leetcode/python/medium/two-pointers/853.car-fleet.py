#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        time_stack = []
        # position が先にいる順で処理
        # position が先の場合は speed が早ければ先に target につく
        # position が後ろの場合は speed が早くても前の遅い車に追いついたらその車と一緒に走ることになるため
        for p, s in sorted(pair)[::-1]:
            time_stack.append((target - p) / s)
            # time_stack[-2] -> 先の position にいる車
            # time_stack[-1] -> その後ろの position にいる車
            # 先にいる車の方が target までの時間がかかる（遅い）場合は、後ろにいる車が追い付いて一丸となる
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                # 後ろにいる車を pop する -> 先にいる車に取り込まれる
                time_stack.pop()
        # 残ったのは集団の数
        return len(time_stack)
# @lc code=end

