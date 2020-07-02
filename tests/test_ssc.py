import unittest

class testCommands(unittest.TestCase):
    def test_commands_class(self):
        import src.ssc

        ssc = src.ssc.commands()
        self.assertTrue(ssc, "Created an instance of ssc")
    def test_str(self):
        import src.ssc

        ssc = src.ssc.commands()
        strings = [
            [[123, 456, 789],["str", "0"],[123, 456, 789, "123"]],
            [[4, 5, 6],["str", "1"],[4, 5, 6, "5"]],
        ]
        for string in strings:
            mem = string[0]
            c = string[1]
            ans = string[2]
            ssc.str_(mem,c)
            self.assertEqual(mem, ans)

        strings = [
            [[123, 456, 789],["str&", "0"],["123", 456, 789]],
            [[4, 5, 6],["str&", "1"],[4, "5", 6]],
        ]
        for string in strings:
            mem = string[0]
            c = string[1]
            ans = string[2]
            mem[int(c[int(1)])] = ssc.str_(mem,c)
            self.assertEqual(mem, ans)


if __name__ == "__main__":
    unittest.main()
