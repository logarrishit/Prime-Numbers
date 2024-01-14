Prime_File = open("PrimeNumbers.txt", "w+")

def Check_Number(Max_Range):
    init_var = 2
    if (Max_Range == init_var):
        print(str(Max_Range) + " is a Prime Number!")
        Prime_File.write(str(Max_Range) + "\n")
    else: 
        while (init_var < Max_Range):
            if (Max_Range % init_var == 0):
                print(str(Max_Range) + " is not a Prime Number!")
                break
            elif (init_var + 1 == Max_Range):
                print(str(Max_Range) + " is a Prime Number!")
                Prime_File.write(str(Max_Range)+ "\n")
            init_var += 1

Range_Numbers = int(input("Enter: "))
Start_Number = 0

while Start_Number <= Range_Numbers:
    Check_Number(Start_Number)
    Start_Number += 1
Prime_File.close()

PrimeFile_Read = open("PrimeNumbers.txt")
print(PrimeFile_Read.read())