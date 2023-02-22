#add function
def add(a,b) : print("%.2f" % a,"+","%.2f" % b,"=","%.2f" % (a+b))

#subtract function
def sub(a,b) : print("%.2f" % a,"-","%.2f" % b,"=","%.2f" % (a-b))

#multiply function
def multi(a,b) : print("%.2f" % a,"*","%.2f" % b,"=","%.2f" % (a*b))

#divide function
def div(a,b) : print("%.2f" % a,"/","%.2f" % b,"=","%.2f" % (a/b))

 

while True : 
    print("Select operation.\n" "1.Add\n" "2.Subtract\n" 
      "3.Multiply\n" "4.Divide\n")
    print("Enter choice: (1/2/3/4):")
    NumChoice = int(input())
    if(NumChoice > 0 and NumChoice <=4) :
        print("Enter first number:")
        a = float(input())
        print("Enter second number:")
        b = float(input())
        if(NumChoice == 1) : add(a,b)
        elif(NumChoice == 2) : sub(a,b)
        elif(NumChoice == 3) : multi(a,b)
        elif(NumChoice == 4) : div(a,b)
        print("Would you like to do a new calculation ? (yes/no):")
        NewCalc = input()
        if(NewCalc == "yes") : continue
        elif(NewCalc == "no") : break
    else : print("That is not a valid number !")
    break

