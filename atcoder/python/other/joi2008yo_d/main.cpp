#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++(i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++(i))
#define REP_R(i, n) for (int i = (int)(n)-1; (i) >= 0; --(i))
#define REP3R(i, m, n) for (int i = (int)(n)-1; (i) >= (int)(m); --(i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

std::pair<int64_t, int64_t> solve(int a, const std::vector<int64_t> &b, const std::vector<int64_t> &c, int d, const std::vector<int64_t> &e, const std::vector<int64_t> &f) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int a, d;
    std::cin >> a;
    std::vector<int64_t> b(a), c(a);
    REP (i, a) {
        std::cin >> b[i] >> c[i];
    }
    std::cin >> d;
    std::vector<int64_t> e(d), f(d);
    REP (i, d) {
        std::cin >> e[i] >> f[i];
    }
    auto [m, n] = solve(a, b, c, d, e, f);
    std::cout << m << ' ' << n << '\n';
    return 0;
}
