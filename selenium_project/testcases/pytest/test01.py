import pytest

class Testcast(object):

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

if __name__ == '__main__':
    pytest.main(['test01.py'])