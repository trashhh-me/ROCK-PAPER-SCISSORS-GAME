def max_from_list(lst):
    max = lst[0]
    for item in lst:
        if item>max:
            max = item
    return max


def main():
    number = []
    choice = "Y"
    while choice != "N":
        try:
            x = int(input("Enter a number"))
            number.append(x)
        except ValueError:
            print("Try Again with Valid Input")
            continue

        choice =input("Do you want to continue Y/N?").upper()
    print("the maximum number from the list you provided is", max_from_list(number))

        
if __name__ == "__main__":
    main()