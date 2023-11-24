import unittest

from exo2 import solution_true
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)
fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
class solution(unittest.TestCase):

    def test_solution(self):
        

        for i in fixed_tests_True:
            self.assertEqual(True, solution_true(i[0],i[1]))
        
    def test_solution(self):
            for i in fixed_tests_False:
                self.assertEqual(False, solution_true(i[0],i[1]))