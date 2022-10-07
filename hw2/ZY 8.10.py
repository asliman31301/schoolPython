#Ahmad Sliman 1898612

def main():
    strn = str(input()).lower()
    st = strn.replace(" ", "")
    if st == st[::-1]:
        print(strn, "is a palindrome")
    else:
        print(strn, "is not a palindrome")


if __name__ == '__main__':
    main()