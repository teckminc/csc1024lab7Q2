import lab7q2
from io import StringIO
from sys import stderr

def generate_value(a=0, b=0):
  if a == 3 and b == 11:
    return 4
  else:
    return 6
  
def test_case1(monkeypatch, capsys):
    
    number_inputs = StringIO('3\n11\n3\n4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'low') != -1
    assert captured_stdout.strip().find(f'you win') != -1


def test_case2(monkeypatch, capsys):
    
    number_inputs = StringIO('3\n11\n6\n7\n4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'high') != -1
    assert captured_stdout.strip().find(f'you win') != -1

def test_case3(monkeypatch, capsys):
    
    number_inputs = StringIO('3\n11\n6\n7\n4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'high') != -1
    assert captured_stdout.strip().find(f'you win') != -1

def test_case4(monkeypatch, capsys):
    
    number_inputs = StringIO('3\n11\n4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    num = lab7q2.get_random()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert num == 4

def test_case5(monkeypatch, capsys):
    
    number_inputs = StringIO('4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    num = lab7q2.guess_number()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert num == 4

def test_case6(monkeypatch, capsys):
    
    number_inputs = StringIO('3\n11\n4\n')
    monkeypatch.setattr("random.randint", generate_value)
    monkeypatch.setattr('sys.stdin', number_inputs)
    num = lab7q2.display_result(4, 3)
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'low') != -1
    assert captured_stdout.strip().find(f'you win') != -1
