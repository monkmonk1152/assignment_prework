my_players = {
    "name":"Troy Aikman",
    "position":"QB",
    "team":"Dallas Cowboys",
    "age":54,
    "weight":220.,
    "superbowls":["XXVII","XXVIII","XXX"],
    "awards":{
        "super_bowl_mvp":"XXVII",
        "probowl":[1991, 1992, 1993, 1994, 1995,1996],
        "man_of_the_year":1997
        }
    }
print(
    my_players['name'] + " has won", len(my_players["superbowls"])
    )

