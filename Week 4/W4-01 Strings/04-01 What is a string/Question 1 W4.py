def double_word(word):
    word2 = word * 2
    return word2 + str(len(word2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
