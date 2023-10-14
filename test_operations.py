from operations import fibonacci_recursive, factorial_recursive


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


### Run to see failed test
# def test_hello_add():
#     assert add(test_hello_add.x) == 12


def test_operations_fibonacci():
    assert fibonacci_recursive(test_operations_fibonacci.x) == 55


def test_operations_factorial():
    assert factorial_recursive(test_operations_factorial.x) == 340
