while True:
    a = int(input("\tenter first number: "))
    b = int(input("\tenter second number: "))
    c = int(input("\tenter third number: "))
    if (a > 0 and b > 0 and c > 0):
        break
    print("\tEnter Valid Input")

lst = [a,b,c]
lst.sort(reverse = True)
print("{} Is The largest Of them".format(lst[0]))
print("{} Is The Smallest Of them".format(lst[-1]))
