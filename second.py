def find_max_substring(search_query):
    search_query = search_query.lower()
    max_substring = ""
    max_count = 0

    for i in range(len(search_query)):
        for j in range(i + 1, len(search_query) + 1):
            substring = search_query[i:j]
            count = search_query.count(substring)

            if count > max_count or (count == max_count and len(substring) > len(max_substring)):
                max_substring = substring
                max_count = count

    return max_substring, max_count

user_input = input("write a word: ")
max_substring, max_count = find_max_substring(user_input)

print(f"max substring : {max_substring}, multiplicity: {max_count}")