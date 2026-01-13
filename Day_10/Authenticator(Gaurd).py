user = "admin"
# user = "a"
def admin_required(func):
    def wrap():
        if user != "admin": raise PermissionError("Access Denied")
        return func()
    return wrap

@admin_required
def dashboard(): print("Admin Panel")

dashboard()
