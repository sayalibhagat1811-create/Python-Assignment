Square = lambda No: No * No

def main():
    Data = [1,2,3,4,5]

    print("Input Data is :", Data)

    MData = list(map(Square, Data))
    print("Data after map :", MData)

if __name__ == "__main__":
    main()