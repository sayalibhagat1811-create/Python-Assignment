CheckLength = lambda Str: len(Str) > 5

def main():
    Data = ["Python","C","Java","Marvellous","Programming"]

    print("Input Data is :", Data)

    FData = list(filter(CheckLength, Data))
    print("Data after filter :", FData)

if __name__ == "__main__":
    main()