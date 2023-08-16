''' https://leetcode.com/problems/delete-duplicate-emails/
'''

import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person):
    person.sort_values("id", inplace=True)
    person.drop_duplicates(subset="email", inplace=True)
    return None

if __name__ == "__main__":
    data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
    Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})
    delete_duplicate_emails(Person)
    print(Person)
