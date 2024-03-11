print("Factorial Finding Program\n"
      "Press 'q' for exit.")
while True:
    number = input("Enter the number whose factorial you want to find: ")
    multiplication = 1
    if (number == 'q'):
        print("We hope you come again.")
        break
    else:
        number = int(number)
    for i in range(2,number+1):
        multiplication *= i
    print("Factorial: ",multiplication)
    print("------------")

