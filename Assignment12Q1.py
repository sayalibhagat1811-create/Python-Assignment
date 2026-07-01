def ChkVowel(ch):
    if ch in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")

char = input("Enter character: ")
ChkVowel(char)