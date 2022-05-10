import pytest

@pytest.mark.do
def test1():
    print('test1')

@pytest.mark.undo
def test2():
    print('test2')

if __name__ == '__main__':
    pytest.main(['test02.py'])

# pytest -m do test02.py