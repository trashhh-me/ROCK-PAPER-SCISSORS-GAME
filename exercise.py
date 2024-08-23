#. Write a Python function to find the maximum of three numbers.


def find_max(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
    
def main():
    x,y,z = map(int, input("Enter 3 numbers").split())
    print("the maximum from the three is", find_max(x,y,z))

if __name__ == "__main__":
    main()
