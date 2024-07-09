
if __name__=='__main__':
    try:#Firstpart of qsn (no3)
        num=int(input("Give your number to calculate Multiplication table\n"))
        list=[num*i for i in range(1,11)]
        print(list)
        #secondpart of qsn (no5)
        f = open("tables.txt", "a")
        f.write("the multiplicaion tables is-\n")
        f.write(str(list))
        f.close()
    except ValueError:
        print("\nInvalid input\n")
        exit()
    else:
        print("\nMultiplication table is printed on text file\n")
    finally:
        print("\nThank you for using this program\n")


    