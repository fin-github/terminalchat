from tinydb import TinyDB, Query
from os import path, curdir
from string import ascii_letters
from random import random

cd = path.abspath(curdir)
class Paths:
    chatdb = path.join(cd, "chat.db")
    accdb = path.join(cd, "accounts.db")

def chatdb_new(chatdb: TinyDB): # defaults
    ...
def accdb_new(accdb: TinyDB): # defaults
    ...

# check if chat.db is a thing
if not path.isfile(Paths.chatdb):
    open(Paths.chatdb, 'w').close() # creates that file
    print("chat.db created")

# check if accounts.db is a thing
if not path.isfile(Paths.accdb):
    open(Paths.accdb, 'w').close() # creates that file
    print("accounts.db created")

db = TinyDB(Paths.chatdb)
chatdb_new(db)
accdb = TinyDB(Paths.accdb)
accdb_new(accdb)

def login(name: str, password: str):
    # check if this user even exists
    if isinstance(accdb.search(Query().name == name), None):
        print("This User does not exist.")
        return False
    
    print("User Exists")
    
    document = accdb.search(Query().name == name)
    accid, real_password = document["accid"], document["password"]
    
    if real_password == password:
        print("Success!")
        return True
    else:
        print("This password is incorrect.")
        return False

def random_acc_id():
    accid = ""
    for i in range(6):
        accid += random(ascii_letters)
    return accid

def signup(name: str, password: str):
    if not isinstance(accdb.search(Query().name == name), None):
        print("This Name is Taken.")
        return False
    print("Username is not taken...")
    
    if not isinstance(accdb.search(Query().password == name), None):
        print("This Password is already taken.")
        return False
    
    accdb.insert({"name": name, "accid": random_acc_id(),  # TODO: add check if acc id already exists
                  "password": password})
    
    print("Account Created")

    