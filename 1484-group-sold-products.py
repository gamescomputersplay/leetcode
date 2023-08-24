''' https://leetcode.com/problems/group-sold-products-by-the-date/
'''

import pandas as pd

def categorize_products(activities):

    def process(data):
        aggregated.append((list(data["sell_date"])[0], len(data), ",".join(data["product"])))
        return data
    
    aggregated = []
    activities.drop_duplicates(["sell_date", "product"], inplace=True)
    activities.sort_values(["sell_date", "product"], inplace=True)
    activities = activities.groupby("sell_date").apply(process)
    result = pd.DataFrame(aggregated, columns=['sell_date', 'num_sold', 'products']).astype({'sell_date':'datetime64[ns]', 'num_sold':'int64', 'products':'str'})
    return result

if __name__ == "__main__":
    data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
    Activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})
    result = categorize_products(Activities)
    print(result)
