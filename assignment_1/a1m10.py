# in a town, the percentage of men is 52. The percentage of total literacy is 48. If totalpercentage of literate men is 35 of the total population, write a program to find the totalnumber of illiterate men and women if the population of the town is 80,000.
town = 80000
men_per = town*0.52
women_per = town*0.48
total_lit = town*0.48
men_lit = town*0.35
women_lit = total_lit-men_lit
print("total no of illiterate men is:",men_per-men_lit)
print("total no of illiterate women is:",women_per-women_lit)