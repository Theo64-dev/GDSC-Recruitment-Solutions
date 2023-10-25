"""Question 1: Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only"""

# Solution:
def length_last_word(s):
    words = s.split()

    if words:
        return len(words[-1])
    else:
        return 0


# Example 1:
s1 = "Hello World"
print("Example 1: "+str(length_last_word(s1)))

# Example 2:
s2 = "   fly me   to   the moon  "
print("Example 1: "+str(length_last_word(s2)))

