def joprob(n, c):
    if (n==1):
        return 1
    else:
        return (joprob(n-1,c)+c-1)%n+1
#I got the equation from
#https://cs.stackexchange.com/q/7048
def main():
   n = int(input("Enter the size of your troop: "))
   c = int(input("Enter the number you wish to count by: "))
   safe = joprob(n,c)
   print("The safe spot for Jo is: ",safe)

main()

