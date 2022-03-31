# characters = {
#     "Shaggy" : {
#       "name": "Shaggy",
#       "age": 12,
#       "monies": 1,
#       "friends": ["Velma","Fred","Daphne", "Scooby"],
#       "favourites": {
#         "tv_show": "Friends",
#         "snacks": ["charcuterie"]
#       }
#     },

# "Velma" : {
#       "name": "Velma",
#       "age": 15,
#       "monies": 2,
#       "friends": ["Fred"],
#       "favourites": {
#         "tv_show": "Baywatch",
#         "snacks": ["soup","bread"]
#       }
#     },

# "Scooby" :   {
#       "name": "Scooby",
#       "age": 18,
#       "monies": 20,
#       "friends": ["Shaggy", "Velma"],
#       "favourites": {
#         "tv_show": "Pokemon",
#         "snacks": ["Scooby snacks"]
#       }
#     },


# "Fred" : {
#       "name": "Fred",
#       "age": 18,
#       "monies": 20,
#       "friends": ["Shaggy", "Velma", "Daphne"],
#       "favourites": {
#         "tv_show": "X-Files",
#         "snacks": ["spaghetti", "ratatouille"]
#       }
#     },

#   "Daphne" : {
#       "name": "Daphne",
#       "age": 20,
#       "monies": 100,
#       "friends": [],
#       "favourites": {
#         "tv_show": "X-Files",
#         "snacks": ["spinach"]
#       }
#     }
# }
    
#print(person1)
#Q1

def get_name(name):
    return name["name"]

#Q2
def get_favourite_tv_show(TV):
    return TV["favourites"]["tv_show"]

#Q3
def likes_to_eat(person,food):
    foundFood = False
    test = person["favourites"]["snacks"]
    for fds in test:
        if fds == food:
            foundFood = True
    return foundFood

#Q4
def add_friend(Velma,friend):
    friends_list = Velma["friends"]
    friends_list.append(friend)


#Q5
def remove_friend(Velma,friend):
    
    flist = Velma["friends"]
    flist.remove(friend)
    


