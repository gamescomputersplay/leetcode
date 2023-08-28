''' https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
'''

import pandas as pd

def find_managers(employee):
    groupped = employee.groupby("managerId").agg(count=("id","count"))
    groupped.reset_index(inplace=True)
    groupped = groupped[groupped["count"] >= 5]
    result = groupped.merge(employee, left_on="managerId", right_on="id")
    return result[["name"]]

if __name__ == "__main__":
    data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
    Employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})
    result = find_managers(Employee)
    print(result)
