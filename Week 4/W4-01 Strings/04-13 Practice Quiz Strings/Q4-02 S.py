# The is_palindrome function checks if a string is a palindrome.
# A palindrome is a string that can be equally read from left to right
# or right to left, omitting blank spaces, and ignoring capitalization.
# Examples of palindromes are words like kayak and radar,
# and phrases like "Never Odd or Even".
# Fill in the blanks in this function to return True if the passed
# string is a palindrome, False if not.
def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {kms:.1f} km".format(miles, kms = km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
