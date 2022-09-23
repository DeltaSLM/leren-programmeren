# Joshua Slui
# Pizza Calculator
import datetime

prices = {"small":7.99, "medium":9.99, "large":12.99} # Prices for the pizzas
selected = {x.lower() : 0 for x in input("What pizzas would you like? Small, Medium, large (Separated by ',')").replace(" ", '').split(",") if x.lower() in prices.keys()} # Ask for what pizzas they want, split prices with commas and remove spaces if provided
if selected == {}:
    print("U kunt alleen een small, medium en/of large pizza bestellen.")
    exit()

try:
    orders = {} # The order list
    for size in selected:
      while not (i:= int(input(f"Hoe veel {size} pizza's wil je?"))) or i == '0': #ask how many they want of each requested size
        pass
      selected[size] = int(i)
except:
    print("You need to input numbers.")
    exit()

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