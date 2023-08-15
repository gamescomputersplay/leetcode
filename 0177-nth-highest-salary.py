''' https://leetcode.com/problems/nth-highest-salary/
'''

import pandas as pd

def nth_highest_salary(employee, N):

    employee.drop_duplicates(subset=["salary"], inplace=True)
    employee.sort_values("salary", inplace=True, ascending=False)
    data_filter = [False for _ in range(len(employee))]
    if N <= len(employee):
        data_filter[N-1] = True

    return employee[["salary"]][data_filter]

if __name__ == "__main__":
    data = [[1, 100], [2, 100], [3, 200], [4, 300], [5, 10]]
    Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'salary', 'id':'int64'})
    result = nth_highest_salary(Employee, 2)
    print(result)
