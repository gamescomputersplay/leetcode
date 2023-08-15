''' https://leetcode.com/problems/find-users-with-valid-e-mails/
'''

import pandas as pd

def valid_emails(users):

    allowed_start = "abcdefghijklmnopqrstuvwxyz"
    allowed_other = "._-0123456789"

    def check_email(emails):
        result = []
        for email in emails:

            if email.count("@") != 1:
                result.append(False)
                continue

            first, last = email.lower().split("@")
            if last != "leetcode.com" or  first == "" or first[0] not in allowed_start:
                result.append(False)
                continue

            # Check allowed letter in the name part
            for letter in first:
                if letter not in allowed_start and letter not in allowed_other:
                    result.append(False)
                    break
            else:
                result.append(True)

        return result

    users = users[check_email(users["mail"])]
    return users

if __name__ == "__main__":
    data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
    Users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

    result = valid_emails(Users)
    print(result)
