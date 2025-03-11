import unittest
from app import sum

class TestApp(unittest.TestCase):
        def Test_add(self):
            self.assertEqual(sum(2,3),5)
            self.assertEqual(sum(1,3),4)
            self.assertEqual(sum(12,13),25)
            self.assertEqual(sum(5,5),10)
            self.assertEqual(sum(6,6),12)




if __name__=='__main__':
    unittest.main()