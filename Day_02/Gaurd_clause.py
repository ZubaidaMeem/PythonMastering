user = None
user_admin_access = True

try:
    if user is not None and user_admin_access:
        print("Access granted!")
    else : print("Access denied")
except AttributeError:
    print("Error")