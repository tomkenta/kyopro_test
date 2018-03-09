"""
testcode.py: kenta yokota

プロコンでよくある標準入出力系の問題のテストコード

- 1. テストケースを /test_cases に入れる。このときのファイル名はソートで並べるようにする。
    例: case0.input , case1.input ...
- 2. テストケースに対応して下記のメソッドtest_case0をコピーして期待する出力をself.assertEqual()に設定する
    しっかり書くテストケースごと入力、出力ごとに書くとよい
- 3. 実行!!

"""
import unittest
import sys, os
from test.support import captured_stdout
from solution import solve

class MyTestCase(unittest.TestCase):

    test_path = 'test_cases'
    files = sorted(os.listdir(test_path))

    """
    input: 3 2 1
    expect output: NO
    """
    def test_case0(self):
        path = self.test_path + '/' + self.files[0]
        expected_output = "NO"
        with open(path) as f:
            input = f.readlines()

        print("testing: {}".format(path))
        print("input:\n{}".format(''.join(input)))

        fd = os.open(path, os.O_RDONLY)
        os.dup2(fd,sys.stdin.fileno())

        with captured_stdout() as stdout:
            solve()
            lines = stdout.getvalue().splitlines()
            # 期待するstdout 複数行あるときは注意
            self.assertEqual(lines[0], expected_output)

        os.close(fd)

    """
    input: 1 3 2
    expect output: YES
    """
    def test_case1(self):
        path = self.test_path + '/' + self.files[1]
        expected_output = "YES"
        with open(path) as f:
            input = f.readlines()

        print("testing: {}".format(path))
        print("input:\n{}".format(''.join(input)))

        fd = os.open(path, os.O_RDONLY)
        os.dup2(fd,sys.stdin.fileno())

        with captured_stdout() as stdout:
            solve()
            lines = stdout.getvalue().splitlines()
            # 期待するstdout 複数行あるときは注意
            self.assertEqual(lines[0], expected_output)

        os.close(fd)

if __name__ == '__main__':
    unittest.main()
