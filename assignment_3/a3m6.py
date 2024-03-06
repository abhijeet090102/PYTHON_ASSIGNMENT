''' Write a program for a matchstick game being played between the computer and a user. Your
program should ensure that the computer always wins. Rules for the game are as follows:
 There are 21 matchsticks.
 The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
 After the person picks, the computer does its picking.
 Whoever is forced to pick up the last matchstick loses the game
'''
stick = 21
print('There are 21 matchsticks,you can take 1-4 number of stick at a time.')
while True:
    print("stick left :",stick)
    stick_taken = int(input("Take sticks(1-4):"))
    if stick ==1:
        print("You took the last stick,you loose")
        break
    if stick_taken >=5 or stick_taken <=0:
        print("wrong choice")
        continue
    p = 5-stick_taken
    print(f'computer took : {p} \n')
    stick -= 5
