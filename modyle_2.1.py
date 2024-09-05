first = input('Ведите 1-е число: ')
second = input('Ведите 2-е число: ')
third = input('Ведите 3-е число: ')

if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first or not second and second or not third:
    print(0)

