# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01

from unittest.mock import patch

from a6q1 import Conway

ls = []
# Test1
test = "Input1.txt"
expected = ['*-*', '*-*', '*-*']
with patch("builtins.input", side_effect=["n"]):
    Conway(test, 1)
with open("input1_1steps.txt", "r") as file:
    for i in file:
        ls.append(i.removesuffix('\n'))
if ls != expected:
    print("Testing Conway() with", test, "\nExpected:", expected, "\nGot:", ls)
else:
    print("Test1 Success...")

# Test2
ls = []

test = "Input2.txt"
expected = ['*Z','**']
with patch("builtins.input", side_effect=["n"]):
    Conway(test, 1)
with open("input2_1steps.txt", "r") as file:
    for i in file:
        ls.append(i.removesuffix('\n'))
if ls != expected:
    print("Testing Conway() with", test, "\nExpected:", expected, "\nGot:", ls)
else:
    print("Test2 Success...")

