''' https://leetcode.com/problems/rearrange-products-table/
'''

import pandas as pd

def rearrange_products_table(products):
    products = products.melt('product_id', ['store1', 'store2', 'store3']).dropna()
    products.rename(columns={"variable":"store", "value":"price"}, inplace=True)
    products = products.astype({"price":"int"})
    return products

if __name__ == "__main__":
    data = [[0, 95, 100, 105], [1, 70, None, 80]]
    Products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'int64', 'store1':'int', 'store2':'int', 'store3':'int'}, errors="ignore")
    result = rearrange_products_table(Products)
    print(result)
