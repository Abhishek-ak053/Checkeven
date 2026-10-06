#check even or odd with fixed values
def evenorodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == "__main__":
    print("Even and odd", evenorodd(10))