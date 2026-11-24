def list():
    users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Charlie", "role": "admin"},
        {"name": "David"},
        {"name": "Eve", "role": "moderator"}
    ]
    for user in users:
        try:
            if user["role"] == "admin":
                print(user["name"])
        except KeyError:
            continue
list()
#     role=[]
#     while True:
#         user=(["role: admin"])
#         role.append
#         print(role)
#         break
# list()



#Print only the users who have the role "admin" via a loop