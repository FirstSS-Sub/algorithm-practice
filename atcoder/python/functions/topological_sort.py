from collections import defaultdict, deque

# v: 頂点の数, e: 辺の数, s_list: 辺の開始地点のリスト, t_list: 辺の向き先地点のリスト
def topological_sort(v, e, s_list, t_list):
    # 隣接リスト
    g = defaultdict(list)
    used = [False]*v
    # トポロジカルソートされた数列
    ans = deque()

    def dfs(u):
        if used[u]: return
        used[u] = True
        for i in g[u]: dfs(i)
        # 帰りがけ順で追加
        ans.appendleft(u)

    def tsort():
        for i in range(v): dfs(i)

    for i in range(e):
        g[s_list[i]].append(t_list[i])

    tsort()
    return ans