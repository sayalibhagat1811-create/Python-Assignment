from functools import reduce

Product = lambda A, B: A * B

def main():
    Data = [1,2,3,4,5]

    print("Input Data is :", Data)

    Ans = reduce(Product, Data)
    print("Product is :", Ans)

if __name__ == "__main__":
    main()