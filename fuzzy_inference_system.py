import member_functions as mf
import numpy as np

class FuzzyInferenceSystem:
    def __init__(self):
        pass

    def fuzzify_data(self,data:list):
        """
        Obtain a membership value for each element in data\n

        >>>`- params -`\n
        `data`: list of 2-elements tupples (x,y), each element represents a student\n 
        x: average grade \n
        y: professor opinion
        """
        fuzzyfied_set = []
        for student in data:
            fuzzyfied_set.append((mf.fuzzify_grade(student[0]),mf.fuzzify_opinion(student[1])))
        return fuzzyfied_set

# opinions = np.arange(0,100,0.5)
# grades = np.arange(0,5,0.025)
# students = []

# for i in range(min(len(opinions),len(grades))):
#     students.append((grades[i],opinions[i]))

# a = FuzzyInferenceSystem()
# b = a.fuzzify_data(students)
# print(b)