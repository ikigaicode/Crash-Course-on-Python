def hit_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Valid username")

hit_username("ajira")
hit_username("ak")
