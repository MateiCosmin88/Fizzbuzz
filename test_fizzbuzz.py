from fizzbuzz import fizzbuzz
def test_number_1():
    assert fizzbuzz(1) == "1"

test_number_1
print("Test compleeted")

#red -> Shows import error name fizzbuzz

#Make it green 
def fizzbuzz(n):
    if n % 15 == 0:
        return "1"