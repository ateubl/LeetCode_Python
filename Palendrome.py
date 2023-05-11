# This program detertmines if an integer is a palendrome
# See LeetCode Problem: https://leetcode.com/problems/palindrome-number/
# This code was written by Andrew Teubl on May 1 2023

x = 121

# Converting to a String
bool_array = []
s_x = str(x)
rev_x = s_x[::-1]
for i in range(len(s_x)):
    if s_x[i] != rev_x[i]:
        bool_array += ["F"]
    
if bool_array != []:
    print("False", bool_array)
else:
    print("True")