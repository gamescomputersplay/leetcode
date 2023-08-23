''' https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
'''

import pandas as pd

def largest_orders(orders):
    orders = orders.groupby("customer_number").agg("count").reset_index()
    orders.sort_values("order_number", ascending=False, inplace=True)
    orders = orders[:1]
    return orders[["customer_number"]]

if __name__ == "__main__":
    data = [[1, 1], [2, 2], [3, 3], [4, 3]]
    orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})
    result = largest_orders(orders)
    print(result)
