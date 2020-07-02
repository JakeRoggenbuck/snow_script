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

    def test_str_amp(self):
        import src.ssc

        ssc = src.ssc.commands()
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

    def test_int(self):
        import src.ssc

        ssc = src.ssc.commands()
        ints = [
            [["123", "456", "789"],["int", "0"],["123", "456", "789", 123]],
            [["4", "5", "6"],["int", "1"],["4", "5", "6", 5]],
        ]
        for _int in ints:
            mem = _int[0]
            c = _int[1]
            ans = _int[2]
            ssc.int_(mem,c)
            self.assertEqual(mem, ans)

    def test_int_amp(self):
        import src.ssc

        ssc = src.ssc.commands()
        ints = [
            [["123", "456", "789"],["str&", "0"],[123, "456", "789"]],
            [["4", "5", "6"],["str&", "1"],["4", 5, "6"]],
        ]
        for _int in ints:
            mem = _int[0]
            c = _int[1]
            ans = _int[2]
            mem[int(c[int(1)])] = ssc.int_(mem,c)
            self.assertEqual(mem, ans)

    def test_calc(self):
        import src.ssc

        ssc = src.ssc.commands()
        calcs = [
            [[123, 456, 789],["calc", "0", "+", "1"],[123, 456, 789, 579]],
            [[4, 5, 6],["calc", "1", "+", "2"],[4, 5, 6, 11]],
            [[123, 456, 789],["calc", "0", "-", "1"],[123, 456, 789, -333]],
            [[4, 5, 6],["calc", "1", "-", "2"],[4, 5, 6, -1]],
            [[123, 456, 789],["calc", "0", "*", "1"],[123, 456, 789, 56088]],
            [[4, 5, 6],["calc", "1", "*", "2"],[4, 5, 6, 30]],
            [[100, 10, 789],["calc", "0", "/", "1"],[100, 10, 789, 10.0]],
            [[50, 200, 5],["calc", "1", "/", "2"],[50, 200, 5, 40]],
        ]
        for calc in calcs:
            mem = calc[0]
            c = calc[1]
            ans = calc[2]
            ssc.calc_(mem,c)
            self.assertEqual(mem, ans)

    def test_calc_hash(self):
        import src.ssc

        ssc = src.ssc.commands()
        calcs = [
            [[123, 456, 789],["calc#", "0", "0", "+", "1"],[579, 456, 789]],
            [[4, 5, 6],["calc#", "0", "1", "+", "2"],[11, 5, 6]],
            [[123, 456, 789],["calc#", "0", "0", "-", "1"],[-333, 456, 789]],
            [[4, 5, 6],["calc#", "1", "1", "-", "2"],[4, -1, 6]],
            [[123, 456, 789],["calc#", "0", "0", "*", "1"],[56088, 456, 789]],
            [[4, 5, 6],["calc#", "1", "1", "*", "2"],[4, 30, 6]],
            [[100, 10, 789],["calc#", "0", "0", "/", "1"],[10.0, 10, 789]],
            [[50, 200, 5],["calc#", "1", "1", "/", "2"],[50, 40.0, 5]],
        ]
        for calc in calcs:
            mem = calc[0]
            c = calc[1]
            ans = calc[2]
            ssc.calc_(mem,c)
            self.assertEqual(mem, ans)

    def test_val(self):
        import src.ssc

        ssc = src.ssc.commands()
        vals = [
            [["123", "456", "789"],["val", "hey"],["123", "456", "789", "hey"]],
            [["4", "5", "6"],["val", 1],["4", "5", "6", 1]],
        ]
        for val in vals:
            mem = val[0]
            c = val[1]
            ans = val[2]
            ssc.val_(mem,c)
            self.assertEqual(mem, ans)
                
    def test_val_hash(self):
        import src.ssc

        ssc = src.ssc.commands()
        vals = [
            [["123", "456", "789"],["val#", "0", "lol"],["lol", "456", "789"]],
            [["4", "5", "6"],["val#", "2", 1],["4", "5", 1]],
        ]
        for val in vals:
            mem = val[0]
            c = val[1]
            ans = val[2]
            ssc.val_(mem,c)
            self.assertEqual(mem, ans)

    def test_out(self):
        import src.ssc

        ssc = src.ssc.commands()
        outs = [
            [["123", "456", "789"],["out", "0"],"123"],
            [["4", "5", "6"],["out", "2"],"6"],
        ]
        for out in outs:
            mem = out[0]
            c = out[1]
            ans = out[2]
            result = ssc.out_(mem,c)
            self.assertEqual(result, ans)

    def test_push(self):
        import src.ssc

        ssc = src.ssc.commands()
        pushs = [
            [["123", "456", "789"],["push", "0", "1"],["123", "456", "789", "123456"]],
            [["4", "5", "6"],["push", "1", "2"],["4", "5", "6", "56"]],
        ]
        for push in pushs:
            mem = push[0]
            c = push[1]
            ans = push[2]
            ssc.push_(mem,c)
            self.assertEqual(mem, ans)



if __name__ == "__main__":
    unittest.main()
