import unittest
import bot


class Test(unittest.TestCase):
    def testOperation(self):
        bot.first_num("3")
        bot.second_num("4")

        self.assertEqual(bot.operation("*"), 12)
        self.assertEqual(bot.operation("<>"), 5)


if __name__ == "__main__":
    unittest.main()