impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut ans, mut min_price) = (0, prices[0]);
        prices.iter().enumerate().for_each(|(i, price)| {
            if i != 0 {
                ans = if price - min_price > ans {
                    price - min_price
                } else {
                    ans
                };
                min_price = if price - min_price < 0 {
                    *price
                } else {
                    min_price
                };
            }
        });
        ans
    }
}
