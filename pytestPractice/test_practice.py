def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test passed"

# to test assert function
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

result = divide(10, 2)   # result = 5
result = divide(10, 0)   # AssertionError: Cannot divide by zero
