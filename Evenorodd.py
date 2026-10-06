#check even or odd with fixed values
import sys
def evenorodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == "__main__":
    num=int(sys.argv[1])
    print("number is", evenorodd(num))