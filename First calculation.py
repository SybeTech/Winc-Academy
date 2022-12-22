broccoli = 2.00
leek = 2.00
potato = 3.00
brussel_sprout = 7.00

num_broccolis = 5
num_leeks = 2
num_potatoes = 7
num_brussel_sprouts = 10

sum_one_each = (broccoli + leek + potato + brussel_sprout)
sum_total = ((num_broccolis * broccoli) + (num_leeks * leek) + (num_potatoes * potato) + (num_brussel_sprouts * brussel_sprout))

avg_price = (sum_one_each/4)

# calculate 30% discount.

discount_percentage = 30
percentage_100 = 100
discount = ((sum_total/percentage_100) * discount_percentage)
discounted_sum_total = (sum_total - discount)

round_sum_total = round(discounted_sum_total, 2 )

print (round_sum_total)