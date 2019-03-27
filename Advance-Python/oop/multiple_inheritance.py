#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : multiple_inheritance.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 22.01.2019
# Last Modified Date: 22.01.2019
# Last Modified By  : Channith Am <amcnith@gmail.com>

class Researcher:

    def __init__(self, field):
        self.field = field

    def __str__(self):
        return "Research field: " + self.field + "\n"


class Teacher:

    def __init__(self, course_list):
        self.course_list = course_list

    def __str__(self):
        out = "Courses: "
        for c in self.course_list:
            out += c + ", "
            # the [:-2] select all the elements
            # but the last two
        return out[:-2] + "\n"


class Professor(Teacher, Researcher):

    def __init__(self, name, field, course_list):
        # This is not completetly right
        # Soon we will see why
        Researcher.__init__(self, field)
        Teacher.__init__(self, course_list)
        self.name = name

    def __str__(self):
        out = Researcher.__str__(self)
        out += Teacher.__str__(self)
        out += "Name: " + self.name + "\n"
        return out


p = Professor("Steve Iams",
	"Machine Learning",
	[
	    "Python Programming",
	    "Probabilistic Graphical Models",
	    "Bayesian Inference"
	])

print(p)
