import solov

if __name__ == "__main__":

    try:
        n = int(input("Which positive integer do you want to test? "))
        assert n > 1
    except:
        print("Integer must be >= 2")
    else:
        if solov.test_solovay(n):
            print(n, "is probably prime")
        else:
            print(n, "is not prime")
