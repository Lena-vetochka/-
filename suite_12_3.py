import unittest
import tests_12_1, tests_12_2


ranST = unittest.TestSuite()
ranST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
ranST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)

runner.run(ranST)

