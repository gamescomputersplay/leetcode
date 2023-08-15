''' https://leetcode.com/problems/calculate-special-bonus/
'''

import pandas as pd

def calculate_special_bonus(employees):
    employees["bonus"] = 0
    employees.loc[lambda x: (x["name"].str[0] != "M") & (x["employee_id"]%2 == 1), "bonus"] = employees["salary"]
    employees = employees[["employee_id", "bonus"]]
    employees = employees.sort_values("employee_id")
    return employees

if __name__ == "__main__":
    data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
    Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})
    result = calculate_special_bonus(Employees)
    print(result)
