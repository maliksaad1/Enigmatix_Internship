def print_nextLine(num = None):
    if num != None:
        print_(num)
    else:
        num = int(input("Enter a number: "))
        print_(num)

def print_(num):
        while num > 0:
            digit = num % 10
            print(digit)
            num //= 10

def main():
    print_nextLine()
    print_nextLine(12345)

main()