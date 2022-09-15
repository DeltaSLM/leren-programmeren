# Joshua Slui
# Pizza Calculator
import datetime

#small_prize = 7.99
#medium_prize = 9.99
#large_prize = 12.99

#order = []

#while True:
    #pizza_choice = input("What size pizza would you like? You can choose between small, medium and large.").lower()

    #def function(price):
        #amount = int(input(f"How many {pizza_choice} pizzas would you like?"))
        #print(f"Your order of {amount} {pizza_choice} pizzas will be ready shortly.")

    #if pizza_choice == 'small':
        #function(small_prize)
    #if pizza_choice == 'medium':
        #function(medium_prize)
    #if pizza_choice == 'large':
        #function(large_prize)
    #if pizza_choice == 'done':
        #current_time = datetime.datetime.now()
        #total_price = amount * price

prices = {"small":1, "medium":2, "large":10} # Prices for the pizzas
selected = {x.lower() : 0 for x in input("What pizzas would you like? Small, Medium, large (Separated by ',')").replace(" ", '').split(",") if x.lower() in prices.keys()} # Ask for what pizzas they want, split prices with commas and remove spaces if provided
orders = {} # The order list
for size in selected:
  while not (i:= input(f"How many {size} pizzas do you want?")).isdigit(): #ask how many they want of each requested size
    pass
  selected[size] = int(i)

current_time = datetime.datetime.now()

print(f"""
---------------
| Happy Italy |
|    1405     |
   {current_time.strftime("%d/%m/%y")}
---------------
|             |
""")
print("\n".join([f"{c}x {s} €{prices[s]}" for s, c in selected.items()]))
print(f"""
|             |
---------------
|    Total    |
      €{sum([prices[s]*c for (s, c) in selected.items()])}
---------------
""")


#        {current_time.strftime("%d-%m-%y")}
