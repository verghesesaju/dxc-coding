#used pytest framework for testing
from fibonacci import *
#since my program is printing the output to console, i have used capsys
#which is used to capture standard input output
def test_fibo_1(capsys):
    fibonacci(2)
    captured = capsys.readouterr()
    assert captured.out == '0\n1\n'
    
def test_fibo_2(capsys):
    fibonacci(4)
    captured = capsys.readouterr()
    assert captured.out == '0\n1\n1\n2\n'