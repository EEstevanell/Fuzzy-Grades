import member_functions as mf
import matplotlib.pyplot as plt
import numpy as np
import random

class FuzzyInferenceSystem:
    def __init__(self):
        self.rules = [("very good aproval chance","gg","go"),
                      ("good aproval chance","gg"),
                      ("good aproval chance","rg","go"),
                      ("regular aproval chance","rg","ro"),
                      ("bad aproval chance","rg","bo"),
                      ("bad aproval chance","bg"),
                      ("very bad aproval chance","bg","bo"),]

    def fuzzify(self, student:tuple)->list:
        """
        Obtain a membership value for each element in data\n

        >>>`- params -`\n
        `data`: list of 2-elements tupples (x,y), each element represents a student\n 
        x: average grade \n
        y: professor opinion
        """

        fuzzy_grade = mf.fuzzify_grade(student[0])
        fuzzy_opinion = mf.fuzzify_opinion(student[1])

        self.fuzzified = {"bg":fuzzy_grade["bad"],
                          "rg":fuzzy_grade["regular"],
                          "gg":fuzzy_grade["good"],
                          "bo":fuzzy_opinion["bad"],
                          "ro":fuzzy_opinion["regular"],
                          "go":fuzzy_opinion["good"]}

    def run_mamdany(self, student):
        self.fuzzify(student)
        self.mamdany_rulify()
        return self.mamdani_agregation

    def mamdany_rulify(self):
        self.coeficient = {}
        for rule in self.rules:
            if not rule[0] in self.coeficient.keys():
                self.coeficient[rule[0]] = 0

            value = float(1)
            for fv in rule[1:]:
                value *= self.fuzzified[fv]

            if value > self.coeficient[rule[0]]:
                self.coeficient[rule[0]] = value

    def plot_mamdani_agregation(self):
        print("starting agregation plotting")
        vb_coef = self.coeficient["very bad aproval chance"]
        b_coef = self.coeficient["bad aproval chance"]
        r_coef = self.coeficient["regular aproval chance"]
        g_coef = self.coeficient["good aproval chance"]
        vg_coef = self.coeficient["very good aproval chance"]

        xs = np.arange(0, 100, 0.5)

        cvbys = [self.clipping(vb_coef,mf.very_bad_chance,x) for x in xs]
        cbys = [self.clipping(b_coef,mf.bad_chance,x) for x in xs]
        crys = [self.clipping(r_coef,mf.regular_chance,x) for x in xs]
        cgys = [self.clipping(g_coef,mf.good_chance,x) for x in xs]
        cvgys = [self.clipping(vg_coef,mf.very_good_chance,x) for x in xs]

        plt.plot(xs, cvbys, xs, cbys, xs, crys, xs, cgys, xs, cvgys)
        plt.title("clipped plots")
        plt.show()

        vbys = [mf.very_bad_chance(x) for x in xs]
        bys = [mf.bad_chance(x) for x in xs]
        rys = [mf.regular_chance(x) for x in xs]
        gys = [mf.good_chance(x) for x in xs]
        vgys = [mf.very_good_chance(x) for x in xs]

        plt.plot(xs, vbys, xs, bys, xs, rys, xs, gys, xs, vgys)
        plt.title("non clipped plots")
        plt.show()
        print("coeficient vals: %s, %s, %s, %s, %s" %(vb_coef, b_coef, r_coef, g_coef, vg_coef))
        
    def mamdani_agregation(self, chance):
        vb_coef = self.coeficient["very bad aproval chance"]
        b_coef = self.coeficient["bad aproval chance"]
        r_coef = self.coeficient["regular aproval chance"]
        g_coef = self.coeficient["good aproval chance"]
        vg_coef = self.coeficient["very good aproval chance"]
        return max([self.clipping(vb_coef,mf.very_bad_chance,chance),
                    self.clipping(b_coef,mf.bad_chance,chance),
                    self.clipping(r_coef,mf.regular_chance,chance),
                    self.clipping(g_coef,mf.good_chance,chance),
                    self.clipping(vg_coef,mf.very_good_chance,chance)])

    def clipping(self, coeficient, consecuent, chance):
        return min(coeficient, consecuent(chance))

    def scalate(self, coeficient, consecuent, chance):
        return coeficient*consecuent(chance)

# opinions = np.arange(0,100,0.5)
# grades = np.arange(0,5,0.025)
# students = []

# for i in range(min(len(opinions),len(grades))):
#     students.append((grades[i],opinions[i]))

student = (random.uniform(0,5), random.uniform(0,100))
a = FuzzyInferenceSystem()
agregation_func = a.run_mamdany(student)
a.plot_mamdani_agregation()
chances = np.arange(0, 100, 0.5)
ys = [agregation_func(ch) for ch in chances]
plt.plot(chances, ys)
plt.title("Union")
plt.show()
# b = a.fuzzify(student)
# a.rulify()
# print(b)