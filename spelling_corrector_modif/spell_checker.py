
from spell import *

def do_correction():
    print("enter 0 to exit the menu:")
    while True:
        print("\nenter a word to correct it : ")
        text = input()
        if text == '0':
            return False 
        
        res = correction(text)
        print("corrected word : ", res)

def do_correction_new():
    "to correct words in sentences as well"
    print("enter 0 to exit the menu:")
    while True:
        print("\nenter a word/sentence to correct it : ")
        text = input()
        if text == '0':
            return False

        res = correct_sentence(text)
        print("corrected is: ", res)


if __name__ == "__main__":
    #do_correction()
    do_correction_new()
