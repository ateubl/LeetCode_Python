# Clear ubuntu terminal with bash line "clear"
import os
os.system('clear')

# This program identfies the longest common prefix of an array of strings 
# See LeetCode Problem: https://leetcode.com/problems/longest-common-prefix/
# This code was written by Andrew Teubl

# example string array
strs = ["bbb","b"]

short = strs[0]
for x in strs:
    if len(x) < len(short):
        
        short = x

com_pref = ""

# Condition for only one string in strs and empty sets
if len(strs) > 1 and len(strs[0]) >= 1:
        c = 0 # char iterator
        s = 0 # string iterator

        # Loop through length of short
        while c < len(short):

            # Compare letter of shortest word with letter in strs string
            if short[c] == strs[s][c]:
                if s < len(strs) - 1: # Check if there is another string in array
                    s += 1
                else:
                    if c < len(strs[s]): # Check if the next word has characters
                        c += 1
                        s = 0
                        com_pref = short
                    else:
                        com_pref = short[:c] # Trim short to length c
                        break # break the while loop
            else:
                com_pref = short[:c]
                break 
else:
    com_pref = short


print("The shortest common prefix is", com_pref)