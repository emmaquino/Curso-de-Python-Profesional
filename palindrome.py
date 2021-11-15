
def is_palindrome(string: str) -> bool:
    if string == string[::-1]:
        return True
    else:
        return False

def run():
    print(is_palindrome(1000))


if __name__ == '__main__':
    run()