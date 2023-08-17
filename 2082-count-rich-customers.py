''' https://leetcode.com/problems/the-number-of-rich-customers/
'''

import pandas as pd

def count_rich_customers(store):
    store = store[store["amount"] > 500]
    store = store.groupby("customer_id").first()
    store = store.groupby(lambda x: True).count()
    store.reset_index(drop=True, inplace=True)
    # This part a little weird, that I reuse existing column
    store.rename(columns={"bill_id":"rich_count"}, inplace=True)
    return store[["rich_count"]]

if __name__ == "__main__":
    data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
    Store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})
    result = count_rich_customers(Store)
    print(result)
