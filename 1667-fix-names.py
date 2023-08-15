''' https://leetcode.com/problems/fix-names-in-a-table/
'''

import pandas as pd

def fix_names(users):
    users["name"] = users["name"].apply(lambda x: x[:1].upper() + x[1:].lower())
    users = users.sort_values("user_id")
    return users

if __name__ == "__main__":
    data = [[1, 'aLice'], [2, 'bOB']]
    Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
    result = fix_names(Users)
    print(result)
