''' https://leetcode.com/problems/count-salary-categories/
'''

import pandas as pd

def count_salary_categories(accounts):

    # Cut into 3 buckets
    intervals = [0, 20000, 50000, 10000000]
    labels = ["Low Salary", "Average Salary", "High Salary"]
    accounts["cat"] = pd.cut(accounts["income"], intervals, labels=labels, right = False, include_lowest=True)

    # Fix 50_000 (move to the middle bucket)
    accounts.loc[accounts["income"] == 50_000, "cat"] = labels[1]

    groupped = accounts.groupby("cat").agg("count")
    result = pd.DataFrame(zip(labels, groupped["income"]), columns=["category", "accounts_count"])
    return result

if __name__ == "__main__":
    data = [[3, 108939], [2, 12747], [8, 87709], [6, 50000]]
    Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})
    result = count_salary_categories(Accounts)
    print(result)
