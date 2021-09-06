
def add_func(num1, num2):
    print("afunc begin")
    sum = num1 + num2
    print("afunc end")
    return sum

def main():
    print("Hello Main Begins")
    s = add_func(34, 50)
    print(s)
    print("Hello Main Ends")


if __name__ == "__main__":
    # execute only if run as a script
    main()