#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

#Example
#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice

###Solution
def duplicate_count(text):
    text_lower = text.lower()
    duplicates = []
    size_text = len(text_lower)
    for i in range(size_text):
        j = i + 1
        for k in range(j, size_text):
            if text_lower[i] == text_lower[k] and text_lower[i] not in duplicates:
                duplicates.append(text_lower[i])
    return len(duplicates)
