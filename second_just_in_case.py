def max_substring_count(word, substring):
    count = 0
    i = 0
    while i < len(word):
        if word[i:i + len(substring)] == substring:
            count += 1
            i += len(substring)
        else:
            i += 1
    return count

word = input("write a word: ")
substring = input("write a substring for analysis: ")

max_count = max_substring_count(word, substring)
print(f"max multiplicity of a substring '{substring}' in word '{word}' is {max_count}")