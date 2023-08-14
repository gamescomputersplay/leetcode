''' https://leetcode.com/problems/customers-who-never-order/
'''

import pandas as pd

def find_customers(customers, orders):

    joined_df = customers.merge(orders, how="left", left_on="id", right_on="customerId")
    joined_df = joined_df[joined_df["customerId"].isnull()]
    joined_df = joined_df[["name"]]
    joined_df.rename(columns={"name":"Customers"}, inplace=True)

    return joined_df

if __name__ == "__main__":
    data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
    data = [[1, 3], [2, 1]]
    Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

    result = find_customers(Customers, Orders)
    print(result)