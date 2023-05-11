# Clear ubuntu terminal with bash line "clear"
import os
os.system('clear')

# This program identfies whether an input string of parentheses are listed in the correct order
# See LeetCode Problem: https://leetcode.com/problems/valid-parentheses/
# This code was written by Andrew Teubl with help from Solutions page of LeetCode and ChatGPT on May 9 2023

def valid_string(s):
    stack = []
    for char in s:
        if char in ('(','[','{'):
            stack.append(char)
        elif char in (')',']','}'):
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return not stack

# Sample String
str = "[(])"
vs = valid_string(str)
print(vs)