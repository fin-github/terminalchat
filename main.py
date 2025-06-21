from tinydb import TinyDB, Query
from os import path, curdir

cd = path.abspath(curdir)
class Paths:
    chatdb = path.join(cd, "chat.db")

# check if chat.db is a thing
if not path.isfile(Paths.chatdb):
    open(Paths.chatdb, 'w').close() # creates that file
    print("chat.db created")

db = TinyDB(Paths.chatdb)