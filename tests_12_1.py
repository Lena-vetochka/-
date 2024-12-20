import unittest
import runner as rn
from tests_12_3 import frozen


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen
    def test_walk(self):
        runner1 = rn.Runner('walk')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @frozen
    def test_run(self):
        runner2 = rn.Runner('run')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @frozen
    def test_challenge(self):
        runner3 = rn.Runner('walk1')
        runner4 = rn.Runner('run1')
        for i in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)

if __name__ == '__main__':
    unittest.main()


