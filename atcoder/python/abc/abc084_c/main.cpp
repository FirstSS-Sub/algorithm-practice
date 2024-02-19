#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++(i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++(i))
#define REP_R(i, n) for (int i = (int)(n)-1; (i) >= 0; --(i))
#define REP3R(i, m, n) for (int i = (int)(n)-1; (i) >= (int)(m); --(i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

auto solve(int N, const std::vector<int64_t> &C, const std::vector<int64_t> &S, const std::vector<int64_t> &F) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int N;
    std::cin >> N;
    std::vector<int64_t> C(N - 1), S(N - 1), F(N - 1);
    REP (i, N - 1) {
        std::cin >> C[i] >> S[i] >> F[i];
    }
    auto ans = solve(N, C, S, F);
    REP (i, N) {
        std::cout << ans[i] << '\n';
    }
    return 0;
}
