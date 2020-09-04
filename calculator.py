#calculator to find out how much food to buy for cats per month cuz they eat a lot and i need to keep track of it
#i have no idea what im doing
cat_1="Lexi"
cat_2="Ares"
#asking how much cups of food each cat eats
food_per_day_1 = float(input(F'How many cups does {cat_1} eat in a day? '))
food_per_day_2 = float(input(F'How many cups does {cat_2} eat in a day? '))
#calculate amount of food (in cups) per week
food_per_week= (food_per_day_1 + food_per_day_2) * 7
print("The amount of cups of food per week is ", food_per_week) #maybe figure out how to print the word cups after?
#show amount of cups they eat in a month
food_per_month= food_per_week * 4
print("Your cats eat", food_per_month , "cups per month.")

#maybe i'll add how many pounds per month
#1 lb = 2 cups

lbs_per_month= food_per_month / 2 
print("This amount is equal to", lbs_per_month , "pounds per month.")
#this will be the third commit
