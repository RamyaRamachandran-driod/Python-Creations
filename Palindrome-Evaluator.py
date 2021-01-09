#palindromes
def is_palindrome():
        if len(word) >= 3:
                if word[-1] == word[0] and wordx == wordx[::-1]:
                        print("Boom, This is a palindrome!")
                else:
                        print("Bam, that's cool, but it isn't a palindrome! ")

word = (input("Enter the craziest word you know:")).lower()
wordx = word[1:-1]
is_palindrome()
