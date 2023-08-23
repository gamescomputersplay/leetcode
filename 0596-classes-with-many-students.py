''' https://leetcode.com/problems/classes-more-than-5-students/
'''

import pandas as pd

def find_classes(courses):
    courses = courses.groupby("class").agg("count")
    courses.reset_index(inplace=True)
    courses = courses[courses["student"] >= 5]
    return courses[["class"]]

if __name__ == "__main__":
    data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
    Courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})
    result = find_classes(Courses)
    print(result)
