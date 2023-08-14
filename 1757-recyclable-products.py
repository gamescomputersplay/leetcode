''' https://leetcode.com/problems/recyclable-and-low-fat-products/
'''

import pandas as pd

def find_products(products):

    filtered_products = products[
        (products["low_fats"] == "Y") &
        (products["recyclable"] == "Y")
        ]
    filtered_products = filtered_products[["product_id"]]
    return filtered_products

if __name__ == "__main__":
    data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
    Products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})
    result = find_products(Products)
    print(result)
