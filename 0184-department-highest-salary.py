''' https://leetcode.com/problems/department-highest-salary/
'''

import pandas as pd

def department_highest_salary(employee, department):

    merged = employee.merge(department, left_on="departmentId", right_on="id")
    merged.sort_values("salary", inplace=True, ascending=False)

    max_salary = merged.groupby(["departmentId"])[["salary"]].agg("max")
    max_salary.rename(columns={"salary":"max_salary"}, inplace=True)

    merged = merged.merge(max_salary, on="departmentId")
    merged = merged[merged["salary"] == merged["max_salary"]][["name_y", "name_x", "salary"]]
    merged.rename(columns={"name_y":"Department", "name_x":"Employee"}, inplace=True)
    
    return merged

if __name__ == "__main__":
    data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
    Employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
    data = [[1, 'IT'], [2, 'Sales']]
    Department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
    result = department_highest_salary(Employee, Department)
    print(result)
