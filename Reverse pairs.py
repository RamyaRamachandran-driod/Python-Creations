def reverse_pair():
        a = list(x)
        b = list(y)
        if a == b[::-1]:
                print("Aha! We got a reverse pair!")
        else:
                print("Okay, that not a reverse pair, but a good pair anyway!")

x = (input("Enter any word you fancy: ")).lower()
y = (input("Enter another word for company: ")).lower()

reverse_pair()
