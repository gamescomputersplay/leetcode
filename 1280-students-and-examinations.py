''' https://leetcode.com/problems/students-and-examinations/
'''

import pandas as pd

def students_and_examinations(students, subjects, examinations):
    examinations["attended_exams"] = 0
    examinations = examinations.groupby(["student_id", "subject_name"]).agg("count")
    examinations.reset_index(inplace=True)

    all_combinations = students.merge(subjects, how="cross")
    all_combinations = all_combinations.merge(examinations, how="left", on=["student_id", "subject_name"])
    all_combinations.fillna(0, inplace=True)
    all_combinations.sort_values(["student_id", "subject_name"], inplace=True)
    all_combinations = all_combinations[["student_id", "student_name", "subject_name",  "attended_exams"]]
    return all_combinations

if __name__ == "__main__":
    data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
    Students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
    data = [['Math'], ['Physics'], ['Programming']]
    Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
    data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
    Examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})

    result = students_and_examinations(Students, Subjects, Examinations)
    print(result)

    data = [[1, 'Alice']]
    Students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
    data = []
    Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
    data = []
    Examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})

    result = students_and_examinations(Students, Subjects, Examinations)
    print(result)