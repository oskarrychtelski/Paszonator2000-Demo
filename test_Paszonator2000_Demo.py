import unittest
import Paszonator2000_Demo


class Test(unittest.TestCase):
    def test_cows_data_entries(self):
        self.assertGreater(Paszonator2000_Demo.masa1, 0)
        self.assertIsInstance(Paszonator2000_Demo.masa1, float)

        self.assertGreater(Paszonator2000_Demo.wydajnosc1, 0)
        self.assertIsInstance(Paszonator2000_Demo.wydajnosc1, float)

        self.assertGreater(Paszonator2000_Demo.tluszcz1, 0)
        self.assertIsInstance(Paszonator2000_Demo.tluszcz1, float)

        self.assertGreater(Paszonator2000_Demo.bialko1, 0)
        self.assertIsInstance(Paszonator2000_Demo.bialko1, float)

        self.assertIn(Paszonator2000_Demo.zmiana_obory.get(), ("Wiolnostanowiskowa", "Uwięziowa"))

    def Test_final_results_of_nutritional_value(self):
        self.assertGreater(Paszonator2000_Demo.ileBialka, 0)
        self.assertIsInstance(Paszonator2000_Demo.ileBialka, float)
        self.assertGreater(Paszonator2000_Demo.ileJPM, 0)
        self.assertIsInstance(Paszonator2000_Demo.ileJPM, float)
        self.assertGreater(Paszonator2000_Demo.ileWlokna, 0)
        self.assertIsInstance(Paszonator2000_Demo.ileWlokna, float)
        self.assertGreater(Paszonator2000_Demo.ileTluszczu, 0)
        self.assertIsInstance(Paszonator2000_Demo.ileTluszczu, float)
        self.assertGreater(Paszonator2000_Demo.ileSM, 0)
        self.assertIsInstance(Paszonator2000_Demo.ileSM, float)
        self.assertGreater(Paszonator2000_Demo.ileNDF, 0)
        self.assertIsInstance(Paszonator2000_Demo.ileNDF, float)
        self.assertGreater(Paszonator2000_Demo.ileBTJN, 0)
        self.assertIsInstance(Paszonator2000_Demo.ileBTJN, float)
        self.assertGreater(Paszonator2000_Demo.ileBTJE, 0)
        self.assertIsInstance(Paszonator2000_Demo.ileBTJE, float)

    def Test_final_results_of_feed_dosage(self):
        self.assertIsInstance(Paszonator2000_Demo.wyniki, str)


if __name__ == '__main__':
    unittest.main()



