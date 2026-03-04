def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    test_num = 10
    print(f"The number {test_num} is {check_even_odd(test_num)}")
