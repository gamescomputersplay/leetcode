''' https://leetcode.com/problems/find-total-time-spent-by-each-employee/
'''

import pandas as pd

def total_time(employees):
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(["event_day", "emp_id"]).agg("sum")
    employees.reset_index(drop=False, inplace=True)
    employees.rename(columns={"event_day": "day"}, inplace=True)

    return employees[["day", "emp_id", "total_time"]]

if __name__ == "__main__":
    data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
    Employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})
    result = total_time(Employees)
    print(result)
