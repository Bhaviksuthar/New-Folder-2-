# Program to check the string contains vowels or not.
# Vowels=a,e,i,o,u

def vowelTracker(str, size):
    if 'a' or 'e' or 'i' or 'o' or 'u' in str:
        print("\nYour string contains vowels")
    
    elif 'A' or 'E' or 'I' or 'O' or 'U' in str:
        print("\nYour string contains vowels")
    
    else:
        print("\nYour string contains normal letters")


str = input("Enter the string : ")
size = len(str)
vowelTracker(str,size)