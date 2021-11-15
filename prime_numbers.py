def is_prime(number: int) -> bool:
    result = [i for i in range(2, number + 1) if number % i == 0]        
    
    if len(result) == 1:
        return True
    else:
        return False

def run():
    print(is_prime("q"))


if __name__ == "__main__":
    run()