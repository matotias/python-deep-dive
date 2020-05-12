"""This file corresponds to lesson 113 of python3: deep dive udemy course"""
from fractions import Fraction


# We can use functions
def speak(cls):
    cls.speak = lambda self, message: '{0} says {1}'.format(
        self.__class__,
        message
    )
    return cls


Fraction = speak(Fraction)

a_number = Fraction(2, 3)
a_number.speak('yeeeey')


# You can use it to complete the ordering functions of a class
from functools import total_ordering


@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)

    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented
