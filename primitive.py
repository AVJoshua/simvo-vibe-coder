# Story: Lily's real-life lemonade stand adventure (using strings, numbers, booleans)
print("Lily opens her first lemonade stand on a sunny day!")

name = "Lily"                    # string: person's name
price = 1.5                      # number (float): dollars per glass
is_open = True                   # boolean: stand status

print(name + " is ready to sell.")  # string + concatenation

glasses = 20                     # number: how many she prepared
cost = 10.0                      # number: setup cost in dollars

is_ready = is_open and True      # boolean operation: AND to combine states
print("Stand ready? " + str(is_ready))

sales = 8                        # number: glasses sold so far
earnings = sales * price         # number operation: multiply to get money

print("Sold " + str(sales) + " glasses for $" + str(earnings) + ".")

sales = sales + 12               # number operation: add more sales (story evolves!)
earnings = earnings + (12 * price)  # number ops: update total with multiply + add

print("Now " + name + " sold " + str(sales) + " total, earned $" + str(earnings) + ".")

profit = earnings - cost         # number operation: subtract to show real profit

feedback = "so refreshing!"      # string: customer comment
full_story = name + "'s lemonade was " + feedback  # string concatenation evolves the tale

print(full_story)
print("Profit today: $" + str(profit) + " — a great day thanks to these data types!")