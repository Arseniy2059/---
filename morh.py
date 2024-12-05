import homework
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.y = homework.Runner('Усэйн', 10)
        self.a = homework.Runner('Андрей', 9)
        self.n = homework.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for x, all_value in cls.all_results.items():
            slovar = {}
            for key, value in all_value.items():
                znach = {key: value.name}
                slovar.update(znach)
            print(slovar)


    def test_1(self):
        g = homework.Tournament(90, self.y, self.n)
        self.distance = g.start()
        self.all_results['Первый забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    def test_2(self):
        s = homework.Tournament(90, self.a, self.n)
        self.distance = s.start()
        self.all_results['Второй забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    def test_3(self):
        z = homework.Tournament(90, self.y, self.a, self.n)
        self.distance = z.start()
        self.all_results['Третий забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

if __name__ == '__main__':
    unittest.main()