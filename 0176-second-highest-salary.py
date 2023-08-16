''' https://leetcode.com/problems/nth-highest-salary/
'''

import pandas as pd

def second_highest_salary(employee):

    n = 2
    employee.drop_duplicates(subset=["salary"], inplace=True)
    employee.sort_values("salary", inplace=True, ascending=False)
    employee = employee.rename(columns={"salary":"SecondHighestSalary"})

    data_filter = [False for _ in range(len(employee))]
    if n <= len(employee):
        data_filter[n-1] = True
        return employee[["SecondHighestSalary"]][data_filter]
    else:
        return pd.DataFrame([None], columns=['SecondHighestSalary'])

if __name__ == "__main__":
    data = [[1, 100], [2, 100], [3, 200], [4, 300], [5, 10]]
    Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    result = second_highest_salary(Employee)
    print(result)
