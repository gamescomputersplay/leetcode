''' https://leetcode.com/problems/patients-with-a-condition/
'''

import pandas as pd

def find_patients(patients):

    def find_condition(conditions_column):
        result = []
        for conditions in conditions_column:
            conditions_list = conditions.split(" ")
            for condition in conditions_list:
                if condition.startswith("DIAB1"):
                    result.append(True)
                    break
            else:
                result.append(False)
        return result

    patients = patients[find_condition(patients["conditions"])]
    return patients

if __name__ == "__main__":
    data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
    Patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})
    result = find_patients(Patients)
    print(result)
