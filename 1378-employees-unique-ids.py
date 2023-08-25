''' https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
'''

import pandas as pd

def replace_employee_id(employees, employee_uni):
    employees = employees.merge(employee_uni, on="id", how="left")
    return employees[["unique_id", "name"]]

if __name__ == "__main__":
    data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]
    Employees = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'int64', 'name':'object'})
    data = [[3, 1], [11, 2], [90, 3]]
    EmployeeUNI = pd.DataFrame(data, columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})
    result = replace_employee_id(Employees, EmployeeUNI)
    print(result)
