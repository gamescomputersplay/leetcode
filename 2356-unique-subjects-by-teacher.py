''' https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
'''

import pandas as pd

def count_unique_subjects(teacher):
    teacher = teacher.groupby(["teacher_id", "subject_id"]).agg("first")
    teacher.reset_index(drop=False, inplace=True)
    teacher = teacher.groupby(["teacher_id"]).agg("count")
    teacher.reset_index(drop=False, inplace=True)
    teacher.rename(columns={"subject_id":"cnt"}, inplace=True)
    return teacher[["teacher_id", "cnt"]]

if __name__ == "__main__":
    data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
    Teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})
    result = count_unique_subjects(Teacher)
    print(result)
