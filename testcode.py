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
    input: 15000
    expect output: 65
    """
    def test_case0(self):
        path = self.test_path + '/' + self.files[0]
        expected_output = "65"
        with open(path) as f:
            input = f.readlines()

        print("testing: {}".format(path))
        print("input:\n{}".format(''.join(input)))
        print("expected output:\n{}".format(expected_output))

        fd = os.open(path, os.O_RDONLY)
        os.dup2(fd,sys.stdin.fileno())

        with captured_stdout() as stdout:
            solve()
            lines = stdout.getvalue().splitlines()
            # 期待するstdout 複数行あるときは注意
            self.assertEqual(expected_output,lines[0])
        os.close(fd)

    """
    input: 75000
    expect output: 89
    """
    def test_case1(self):
        path = self.test_path + '/' + self.files[1]
        expected_output = "89"
        with open(path) as f:
            input = f.readlines()

        print("testing: {}".format(path))
        print("input:\n{}".format(''.join(input)))
        print("expected output:\n{}".format(expected_output))

        fd = os.open(path, os.O_RDONLY)
        os.dup2(fd,sys.stdin.fileno())

        with captured_stdout() as stdout:
            solve()
            lines = stdout.getvalue().splitlines()
            # 期待するstdout 複数行あるときは注意
            self.assertEqual(expected_output,lines[0])
        os.close(fd)

    """
    input: 200
    expect output: 02
    """
    def test_case2(self):
        path = self.test_path + '/' + self.files[2]
        expected_output = "02"
        with open(path) as f:
            input = f.readlines()

        print("testing: {}".format(path))
        print("input:\n{}".format(''.join(input)))
        print("expected output:\n{}".format(expected_output))

        fd = os.open(path, os.O_RDONLY)
        os.dup2(fd,sys.stdin.fileno())

        with captured_stdout() as stdout:
            solve()
            lines = stdout.getvalue().splitlines()
            self.assertEqual(expected_output,lines[0])
        os.close(fd)

    """
    input: 40000
    expect output: 82
    """
    def test_case3(self):
        path = self.test_path + '/' + self.files[3]
        expected_output = "82"
        with open(path) as f:
            input = f.readlines()

        print("testing: {}".format(path))
        print("input:\n{}".format(''.join(input)))
        print("expected output:\n{}".format(expected_output))

        fd = os.open(path, os.O_RDONLY)
        os.dup2(fd,sys.stdin.fileno())

        with captured_stdout() as stdout:
            solve()
            lines = stdout.getvalue().splitlines()
            self.assertEqual(expected_output,lines[0])
        os.close(fd)

if __name__ == '__main__':
    unittest.main()
