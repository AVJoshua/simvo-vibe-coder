print("Simulating a backyard pond ecosystem evolving over 5 days!")

# Pond environment as a readable dict
pond = {
    "water_level": 100,
    "food_available": True,
    "clean": True
}

# Creatures as a list of dicts (complex nesting with inner lists)
creatures = [
    {
        "species": "Frog",
        "count": 8,
        "energy": 70,
        "alive": True,
        "events": ["hopped onto lily pad"]
    },
    {
        "species": "Fish",
        "count": 15,
        "energy": 60,
        "alive": True,
        "events": ["swam near the surface"]
    }
]

print("Ecosystem initialized with " + str(len(creatures)) + " species.")

# Outer loop: each day of evolution
for day in range(1, 6):
    print("\n--- Day " + str(day) + " ---")

    # Nested loop: process every creature
    for creature in creatures:
        if creature["alive"]:
            print("  " + creature["species"] + " population: " + str(creature["count"]))
            
            if pond["food_available"]:
                creature["energy"] = creature["energy"] + 15
                creature["events"].append("ate well")
                if creature["energy"] > 90:
                    creature["count"] = creature["count"] + 3
                    creature["events"].append("bred new offspring")
            else:
                creature["energy"] = creature["energy"] - 25
                if creature["energy"] < 20:
                    creature["alive"] = False
                    creature["events"].append("could not survive")

    # Update pond after all creatures act
    pond["water_level"] = pond["water_level"] - 20
    if pond["water_level"] < 60:
        pond["food_available"] = False
        pond["clean"] = False
        print("  Pond water low — food now scarce!")
    else:
        pond["food_available"] = True

print("\nFinal ecosystem after 5 days:")
for creature in creatures:
    print(creature["species"] + " final count: " + str(creature["count"]) + " | Alive: " + str(creature["alive"]))
print("Pond status — Water: " + str(pond["water_level"]) + ", Food: " + str(pond["food_available"]))
print("All core data types + loops/conditionals modeled real ecosystem change!")