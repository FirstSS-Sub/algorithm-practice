#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++(i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++(i))
#define REP_R(i, n) for (int i = (int)(n)-1; (i) >= 0; --(i))
#define REP3R(i, m, n) for (int i = (int)(n)-1; (i) >= (int)(m); --(i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

auto solve(auto a, auto b, const std::vector<auto> &c, const std::vector<std::vector<auto> > &d, const std::vector<auto> &e) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    auto a, b;
    std::cin >> a >> b;
    std::vector<auto> c(b);
    std::vector<std::vector<auto> > d(b, std::vector<auto>((c_i)));
    std::vector<auto> e(b);
    REP (i, b) {
        std::cin >> c[i];
        REP (j, c_i) {
            std::cin >> d[i][j];
        }
        std::cin >> e[i];
    }
    auto ans = solve(a, b, c, d, e);
    // failed to analyze output format
    // TODO: edit here
    std::cout << ans << '\n';
    return 0;
}
