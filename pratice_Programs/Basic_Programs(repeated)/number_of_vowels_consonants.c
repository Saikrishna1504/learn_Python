given_statement = "Saveetha School of Engineering"
vowel_count = 0
consonant_count = 0
vowels = "aeiouAEIOU"
for char in given_statement:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Number of vowels = {vowel_count}")
print(f"Number of consonants = {consonant_count}")
if vowel_count > consonant_count:
    print("Vowels are maximum.")
elif consonant_count > vowel_count:
    print("Consonants are maximum.")
else:
    print("Both vowels and consonants are equal.")
