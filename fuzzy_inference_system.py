import member_functions as mf
import matplotlib.pyplot as plt
import scipy.integrate as integrate
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

    def run_mamdani(self, student, plott = False):
        print("Starting Fuzzy System using Mamdami")
        self.fuzzify(student)
        self.rulify()
        if plott:
            self.plot_mamdani_agregation()
        function = self.mamdani_agregation
        self.run_defuzzyfiers(function)
        return self.mamdani_agregation
    def run_larsen(self, student, plott = False):
        print("Starting Fuzzy System using Larsen")
        self.fuzzify(student)
        self.rulify()
        if plott:
            self.plot_larsen_agregation()
        function = self.larsen_agregation
        self.run_defuzzyfiers(function)
        return self.larsen_agregation
     
    def rulify(self):
        self.coeficient = {}
        for rule in self.rules:
            if not rule[0] in self.coeficient.keys():
                self.coeficient[rule[0]] = 0

            value = float(1)
            for fv in rule[1:]:
                value *= self.fuzzified[fv]

            if value > self.coeficient[rule[0]]:
                self.coeficient[rule[0]] = value
    ##### Mamdani #####
    def plot_mamdani_agregation(self):
        print("Plotting Mamdani Agregation")
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
    
    ##### Larsen #####
    def plot_larsen_agregation(self):
        print("Plotting Larsen Agregation")
        vb_coef = self.coeficient["very bad aproval chance"]
        b_coef = self.coeficient["bad aproval chance"]
        r_coef = self.coeficient["regular aproval chance"]
        g_coef = self.coeficient["good aproval chance"]
        vg_coef = self.coeficient["very good aproval chance"]

        xs = np.arange(0, 100, 0.5)

        cvbys = [self.scalate(vb_coef,mf.very_bad_chance,x) for x in xs]
        cbys = [self.scalate(b_coef,mf.bad_chance,x) for x in xs]
        crys = [self.scalate(r_coef,mf.regular_chance,x) for x in xs]
        cgys = [self.scalate(g_coef,mf.good_chance,x) for x in xs]
        cvgys = [self.scalate(vg_coef,mf.very_good_chance,x) for x in xs]

        plt.plot(xs, cvbys, xs, cbys, xs, crys, xs, cgys, xs, cvgys)
        plt.title("scaled plots")
        plt.show()

        vbys = [mf.very_bad_chance(x) for x in xs]
        bys = [mf.bad_chance(x) for x in xs]
        rys = [mf.regular_chance(x) for x in xs]
        gys = [mf.good_chance(x) for x in xs]
        vgys = [mf.very_good_chance(x) for x in xs]

        plt.plot(xs, vbys, xs, bys, xs, rys, xs, gys, xs, vgys)
        plt.title("non scaled plots")
        plt.show()
        print("coeficient vals: %s, %s, %s, %s, %s" %(vb_coef, b_coef, r_coef, g_coef, vg_coef))
    def larsen_agregation(self, chance):
        vb_coef = self.coeficient["very bad aproval chance"]
        b_coef = self.coeficient["bad aproval chance"]
        r_coef = self.coeficient["regular aproval chance"]
        g_coef = self.coeficient["good aproval chance"]
        vg_coef = self.coeficient["very good aproval chance"]
        return max([self.scalate(vb_coef, mf.very_bad_chance, chance),
                    self.scalate(b_coef, mf.bad_chance, chance),
                    self.scalate(r_coef, mf.regular_chance, chance),
                    self.scalate(g_coef, mf.good_chance, chance),
                    self.scalate(vg_coef, mf.very_good_chance, chance)])
    def scalate(self, coeficient, consecuent, chance):
        return coeficient*consecuent(chance)

    ##### Defuzzify #####
    def run_defuzzyfiers(self, agregation_func):
        x = self.get_left_max(agregation_func)
        vg, g, r, b, vb  = mf.eval_chances_func(x)
        print("using left-most max value:\n\
               x = %s\n\
               f(x) = {very good aproval chance = %s,\n\
                       good aproval chance = %s,\n\
                       regular aproval chance = %s,\n\
                       bad aproval chance = %s,\n\
                       very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))

        x = self.get_right_max(agregation_func)
        vg, g, r, b, vb  = mf.eval_chances_func(x)
        print("using right-most max value:\n\
               x = %s\n\
               f(x) = {very good aproval chance = %s,\n\
                       good aproval chance = %s,\n\
                       regular aproval chance = %s,\n\
                       bad aproval chance = %s,\n\
                       very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))

        x = self.get_median_max(agregation_func)
        vg, g, r, b, vb  = mf.eval_chances_func(x)
        print("using median max value:\n\
               x = %s\n\
               f(x) = {very good aproval chance = %s,\n\
                       good aproval chance = %s,\n\
                       regular aproval chance = %s,\n\
                       bad aproval chance = %s,\n\
                       very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))
        
        x = self.centroid_method(agregation_func)
        vg, g, r, b, vb  = mf.eval_chances_func(x)
        print("using centroid method value:\n\
               x = %s\n\
               f(x) = {very good aproval chance = %s,\n\
                       good aproval chance = %s,\n\
                       regular aproval chance = %s,\n\
                       bad aproval chance = %s,\n\
                       very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))
        
        x = self.bisector_method(agregation_func)
        vg, g, r, b, vb  = mf.eval_chances_func(x)
        print("using bisector method value:\n\
               x = %s\n\
               f(x) = {very good aproval chance = %s,\n\
                       good aproval chance = %s,\n\
                       regular aproval chance = %s,\n\
                       bad aproval chance = %s,\n\
                       very bad aproval chance = %s\n" %(str(x), str(vg), str(g), str(r), str(b), str(vb)))
    # Max method
    def get_left_max(self, f, precission = 0.01):
        max_value = -1
        max_x = 0
        xs = np.arange(0, 100, precission)
        for x in xs:
            if f(x) > max_value:
                max_value = f(x)
                max_x = x
        return max_x
    def get_right_max(self, f, precission = 0.01):
        max_value = -1
        max_x = 0
        xs = np.arange(0, 100, precission)
        for x in xs:
            if f(x) >= max_value:
                max_value = f(x)
                max_x = x
        return max_x
    def get_median_max(self, f, precission = 0.01):
        xs = np.arange(0,100,precission)
        max_value = -1
        max_xs = []
        for x in xs:
            if f(x) > max_value:
                max_xs = [x]
                max_value = f(x)
            elif f(x) == max_value:
                max_xs.append(x)
        return max_xs[int(len(max_xs)/2)]
    # Centroid
    def centroid_method(self, f):
        self.f = f
        def func(x):
            return x*self.f(x)
        return integrate.quad(func, 0, 100)[0]/integrate.quad(f, 0, 100)[0]
    # Bisector
    def bisector_method(self, f):
        return self._binary_search(f, 0, 100)
    def _binary_search(self, f, a, b):
        m = (b + a)/2
        left_val = integrate.quad(f, 0, m)[0]
        right_val = integrate.quad(f, m, 100)[0]
        if abs(left_val - right_val) < 0.1:
            return m
        if left_val < right_val:
            return self._binary_search(f, m, b)
        return self._binary_search(f, a, m)

student = (random.uniform(0,5), random.uniform(0,100))
print("student %s" %str(student))
a = FuzzyInferenceSystem()
agregation_func = a.run_mamdani(student, True)

chances = np.arange(0, 100, 0.5)
ys = [agregation_func(ch) for ch in chances]
plt.plot(chances, ys)
plt.title("Union Mamdani")
plt.show()

agregation_func = a.run_larsen(student, True)

chances = np.arange(0, 100, 0.5)
ys = [agregation_func(ch) for ch in chances]
plt.plot(chances, ys)
plt.title("Union Larsen")
plt.show()