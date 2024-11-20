import unittest
import tests12_3

runtest = unittest.TestSuite()
runtest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_3.RunnerTest))
runtest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_3.TournamentTest))

run1 = unittest.TextTestRunner(verbosity=2)
run1.run(runtest)