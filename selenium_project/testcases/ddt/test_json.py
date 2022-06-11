import pytest
import json


def get_data():
    with open(
            '/Users/jane-macPro/Documents/github/selenium/selenium_project/testcases/ddt/data.json'
    ) as f:
        lst = []
        data = json.load(f)
        lst.append(data['keys'])
        print(lst)


# @pytest.mark.parametrize('name', get_data())
# def test01(name):
#     print(name)

if __name__ == '__main__':
    get_data()
    # pytest.main(['-sv','test_json.py'])
