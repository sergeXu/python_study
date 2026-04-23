import pytest

from employee import Employee


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 15000

def test_give_custon_raise(employee):
    employee.give_raise(8000)
    assert employee.salary == 18000

@pytest.fixture
def employee():
    employee = Employee("serge",'male',10000)
    return employee