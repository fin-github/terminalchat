from tinydb import TinyDB, Query
from os import path, curdir

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