from unique_element import unique_element, np

def test_unique_element():
    test_case=[1,5,5,2,2,7,7,4,4]
    test_solution=1
    assert unique_element(test_case) == test_solution