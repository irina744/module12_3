import unittest

import runner
from runner import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        rn = Runner(name='John')
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе зaморожены")
    def test_run(self):
        rn = Runner(name='John1')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе зaморожены")
    def test_challenge(self):
        runner1 = Runner(name='John2')
        runner2 = Runner(name='John3')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner.Runner('Усэйн', 10)
        self.andrey = runner.Runner('Андрей', 9)
        self.nick = runner.Runner('Ник', 3)

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе зaморожены")
    def test_usain_vs_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results["Usain vs Nick"] = results
        last_runner = max(results.keys())
        self.assertTrue(last_runner == 2 and results[last_runner].name == "Ник")

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе зaморожены")
    def test_andrey_vs_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results["Andrey vs Nick"] = results
        last_runner = max(results.keys())
        self.assertTrue(last_runner == 2 and results[last_runner].name == "Ник")

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе зaморожены")
    def test_all_three(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results["All Three"] = results
        last_runner = max(results.keys())
        self.assertTrue(last_runner == 3 and results[last_runner].name == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            formatted_result = {k: v.name for k, v in value.items()}
            print(formatted_result)

    if __name__ == "__main__":
        unittest.main()
