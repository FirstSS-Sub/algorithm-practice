#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++(i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++(i))
#define REP_R(i, n) for (int i = (int)(n)-1; (i) >= 0; --(i))
#define REP3R(i, m, n) for (int i = (int)(n)-1; (i) >= (int)(m); --(i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

auto solve(int a, int64_t b, const std::vector<std::string> &c, int d, const std::vector<int64_t> &e, const std::vector<int64_t> &f, const std::vector<int64_t> &g) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int a;
    int64_t b;
    int d;
    std::cin >> a;
    std::vector<std::string> c(a);
    std::cin >> b;
    REP (i, a) {
        std::cin >> c[i];
    }
    std::cin >> d;
    std::vector<int64_t> e(d), f(d), g(d);
    REP (i, d) {
        std::cin >> e[i] >> f[i] >> g[i];
    }
    auto ans = solve(a, b, c, d, e, f, g);
    REP (j, d) {
        std::cout << h[j] << '\n';
    }
    return 0;
}