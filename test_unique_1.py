from unique_element import unique_element, np

def test_unique_element():
    test_case=[5,5,2,2,7,9,9,4,4]
    test_solution=7
    assert unique_element(test_case) == test_solution