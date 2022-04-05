while True:
    try:
        first = int(input("Give me a number.\n"))
        second = int(input("\nGive me another number.\n"))

        print("\nYour total is" ,first + second)
        break
    except:
        print("\nYou can't do that.\n")