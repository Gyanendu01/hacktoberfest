print("\tWelcome To The Multiplication/Exponent Table App")

#Input Data
usr_name = input("\tWhat is your name: ")
num = float(input("\tWhat number would you like to work with? "))

#Program Logic and Output Data
print("\n\tMultiplication Table For {}".format(num))
print("\t_"*5)
for i in range(1,10):
    print("\t\t{} * {} = {}".format(float(i),num,round((i*num),2)))

print("\n\tExponent Table For {}".format(num))
print("\t_"*5)
for i in range(1,10):
    print("\t\t{} ** {} = {}".format(num,i,round((num**i),4)))

print("\t{} Math is cool!".format(usr_name))
print("\t\t{} Math is cool!".format(usr_name))
print("\t\t\t{} Math is cool!".format(usr_name))
print("\t\t\t\t{} Math is cool!".format(usr_name))

