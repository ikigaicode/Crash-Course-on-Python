def is_valid(user):
    if len(user) >= 3:
        return True
    else:
        return False


def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat"])


#a user is valid when it has equal or more than 3 characters LONG.
