#add function
def add(a,b) : return (a+b)

#subtract function
def sub(a,b) : return (a-b)

#multiply function
def multi(a,b) : return (a*b)

#divide function
def div(a,b) : return (a/b)
 
while True : 
    print("Select operation.\n" "1.Add\n" "2.Subtract\n" "3.Multiply\n" "4.Divide\n")
    print("Enter choice: (1/2/3/4):")
    #casting the number into integer because if not it will read it as string and the sring can't be compared with some operators
    NumChoice = int(input()) 
    #checking if the number is between 1 and 4
    if(NumChoice > 0 and NumChoice <=4) :
        print("Enter first number:")
        #using casting to make sure the numbers are read in float
        a = float(input())
        print("Enter second number:")
        b = float(input())
        #checking what operation the user wants and shows them the result formated with 2 decimals with the specific function called for each operation
        if(NumChoice == 1) : print("%.2f" % a,"+","%.2f" % b,"=","%.2f" % add(a,b))
        elif(NumChoice == 2) : print("%.2f" % a,"-","%.2f" % b,"=","%.2f" % sub(a,b))
        elif(NumChoice == 3) : print("%.2f" % a,"*","%.2f" % b,"=","%.2f" % multi(a,b))
        elif(NumChoice == 4) : print("%.2f" % a,"/","%.2f" % b,"=","%.2f" % div(a,b))
        print("Would you like to do a new calculation ? (yes/no):")
        NewCalc = input()
        #checking if the user wants to countinue or not
        if(NewCalc == "yes") : continue
        else : break
    #if there is no valid number the program will terminate
    else : print("That is not a valid number!")
    break

