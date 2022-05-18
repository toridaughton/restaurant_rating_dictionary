"""Restaurant rating lister."""


# put your code here

# Create an empty dictionary
ratings_dict = {}

# Allow python to read scores.txt:
scores = open("scores.txt")

# Accessing each line in the scores file, split into key-value pairs at the ":"
for line in scores:
# Naming our variables at the indices before and after the ":"
    key, value = line[:-1].split(":")


# Stating that the variable [index] we named key will be used as the key in our ratings dictionary and its value will = the variable we named value (why we named them this way)
    ratings_dict[key] = value


def restaurant_rater():
# We are looping through our dicitionary and accessing the items in our ratings dictionary asking it to print key and value next to each other (not in dictionary format). So that it looks more human
    for key, value in sorted(ratings_dict.items()): # using sorted on the dictionary being called on in the for loop.
        print(f"{key} is rated at {value}.")


def add_new_rating():
    new_restaurant = input("\nKnow a good restaurant not on the list? Enter it here:\n")
    new_restaurant_rating = input("\nWhat would you rate this restaurant?\n")
    ratings_dict.update({new_restaurant : new_restaurant_rating})
    restaurant_rater()


restaurant_rater()
add_new_rating()