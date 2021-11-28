# Bismillah - AbubakarQ

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Average Price of Haircut

#--Total--#
total_price = 0
for i in prices:
  total_price = total_price + i
print("Total price of all haircuts: $" + str(total_price))

#--Number of Prices--#
numHaircuts = len(prices)
print("Total number of haircuts: " + str(numHaircuts))

#--Average Calculation--#
average = total_price /numHaircuts
print("Average cost of a haircut: $" + str(average))

#--Too expensive OH NO! | Removing 5 Dollars --#
new_prices = [price - 5 for price in prices]
print()
print("Reduced Prices:", new_prices)

#--Store Revenue--#
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  #print(total_revenue)
  #print("Last week: " + str(last_week[i]))
  # range(len(x)) chooses random from range

print()
print("Total Revenue: $" + str(total_revenue))

#-- Average Daily --#
average_daily_revenue = total_revenue/7
print("Average Daily: $" + str(average_daily_revenue))
print()

#--PROMO for cuts under 30--#
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print("Cuts under 30:", cuts_under_30)

