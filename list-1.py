x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


    words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    # Strategy:  Iterate over a copy
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]
            print(users)


    # Strategy:  Create a new collection
    active_users = {}
    for user, status in users.items():
        if status == 'inactive':
            active_users[user]= status


class Point:
    def __init__(self, x, y):
        self.x = x
        self,y = y
        
def where_is(point):
    match point:
        case (0, 0):
             print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
    

    