print("Taylor launches her photography Instagram account!")

# Feed: list of post dictionaries (complex type containing primitives + lists)
feed = [
    {
        "caption": "First shot of the mountains at sunrise!",
        "likes": 42,
        "comments": ["Love this!", "Stunning view"],
        "hashtags": ["#photography", "#nature"]
    },
    {
        "caption": "City lights never disappoint.",
        "likes": 28,
        "comments": [],
        "hashtags": ["#urban", "#night"]
    }
]

print("Initial feed ready with " + str(len(feed)) + " posts.")

# Followers: dictionary mapping username (string) to mutual friends count (number)
followers = {
    "photo_fan123": 5,
    "naturelover": 2,
    "citysnapper": 8
}

print("Starting with " + str(len(followers)) + " followers tracked.")

# Story evolves: Taylor posts a new photo → append a new dict to the list
new_post = {
    "caption": "Golden hour magic in the forest.",
    "likes": 15,
    "comments": ["Beautiful!", "Where is this?"],
    "hashtags": ["#forest", "#goldenhour"]
}
feed.append(new_post)

print("New post added! Feed now has " + str(len(feed)) + " posts.")

# A fan likes the very first post → number operation on the dict
feed[0]["likes"] = feed[0]["likes"] + 23

print("First post now has " + str(feed[0]["likes"]) + " likes.")

# Someone adds a comment to the newest post → append to the inner list inside the dict
feed[2]["comments"].append("Incredible lighting!")

print("New comment added to latest post.")

# Combine data to show real-world total engagement (manual addition of numbers from dicts)
total_likes = feed[0]["likes"] + feed[1]["likes"] + feed[2]["likes"]
total_comments = len(feed[0]["comments"]) + len(feed[1]["comments"]) + len(feed[2]["comments"])

print("Total likes across feed: " + str(total_likes))
print("Total comments across feed: " + str(total_comments))
print("Taylor's Instagram story is growing thanks to lists and dicts!")