import sqlite3

con = sqlite3.connect("test.db")

# cur = con.cursor()
# cur.execute('SELECT SQLITE_VERSION()')
#
# res = cur.fetchone()
# cur.close()
#
# print(res)

# ===================================================================


def create_pets_table(con):
    try:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Pets(Id INTEGER PRIMARY KEY, Name TEXT, Price FLOAT)')
    except sqlite3.Error:
        if con:
            con.rollback()


def insert_pet(con, name, price):
    assert(isinstance(name, str))
    assert(isinstance(price, float))

    try:
        cur = con.cursor()
        cur.execute("INSERT INTO Pets(Name, Price) VALUES('{}', {})".format(name, price))
    except sqlite3.Error as sqle:
        print(sqle)
        if con:
            con.rollback()


def get_all_pets(con):
    try:
        cur = con.cursor()
        cur.execute('SELECT Name, Price from Pets')

        pets = cur.fetchall()

        cur.close()

        for pet in pets:
            print(pet[0], "costs", pet[1])

    except sqlite3.Error:
        if con:
            con.rollback()


def remove_pets(con):
    try:
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS Pets')
        cur.close()
    except sqlite3.Error:
        if con:
            con.rollback()


create_pets_table(con)

insert_pet(con, "Bhollu", 49.95)
insert_pet(con, "Maddy", 32.45)
insert_pet(con, "meow", 98.90)

get_all_pets(con)

remove_pets(con)
con.close()

print("============================================================")

con = sqlite3.connect("test.db")
create_pets_table(con)
con.commit()

num = input("No. of pets:\n")

for i in range(int(num)):
    name = input("Enter name of Pet[" + str(i + 1) + "] : ")
    price = input("Enter price: ")

    insert_pet(con, name, float(price))

con.commit()

get_all_pets(con)

# remove_pets(con)
con.close()

print("============================================================")
# Execute script and execute many


