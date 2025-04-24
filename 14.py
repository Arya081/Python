def count_vowel(s1, c=0, i=0):
    vowel="aeiouAEIOU"
    if i==len(s1):
        return c
    elif s1[i] in vowel:
        return c + 1 + count_vowel(s1,c,i+1)
    else:
        return count_vowel(s1,c,i+1)

s1=input("Enter a string: ")
print("Number of vowels in the string are:", {count_vowel(s1)})



output

Enter a string: Arya
Number of vowels in the string are: {2}

=== Code Execution Successful ===
