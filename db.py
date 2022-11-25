
from cmath import inf
import re
import sqlite3

con = sqlite3.connect("3301.db",check_same_thread=False)

cur = con.cursor()

def db():
    cur.execute("CREATE TABLE Users(User UNIQUE,Pass,Email UNIQUE,Token UNIQUE,St,Level,Score) ")
    res = cur.execute("SELECT name FROM sqlite_master")

# db()
def create(U,P,E,T,ST,L,S):
    global cur
    try:
        x=cur.execute(f"""INSERT INTO Users VALUES ('{U.upper()}','{P}',{E},'{T}','{ST}',{L},{S})""")
        con.commit()
        
        return x.fetchone()
    except:
        return False

# print(create('fsc','fsc3301@1033','NULL','=fsc@*#Y*EHI3301','free','12345','500'))

def info(U,P=''):
    global cur
    
    try:
        if P!='':
            res=cur.execute("SELECT User,Pass,Email,Token,St,Level,Score FROM Users WHERE User='{}' AND Pass='{}' ".format(U.upper(),P))
        else:
            res=cur.execute("SELECT User,Pass,Email,Token,St,Level,Score FROM Users WHERE User='{}'".format(U.upper()))
        return list(res.fetchall())[0]
    except:
        return False

def st(u):
    global cur
    res=cur.execute("SELECT St FROM Users WHERE User='{}' ".format(u.upper()))
    try:
        return res.fetchall()[0][0]
    except:
        return False


def token(i='User',T=''):
    global cur
    res=cur.execute("SELECT email,Token,Score FROM Users WHERE {}='{}' ".format(i,T))
    try:
        x=list(res.fetchone())
        return x
    except:
        return [None,None]

def email(E,T):
    global cur
    cur.execute(f"UPDATE Users SET email = {E} WHERE Token= '{T}'")
    con.commit()
    return True

# email(f"null",'@$SDSD')
# print(info('x'))

def ban(S,U):
    global cur
    cur.execute(f"UPDATE Users SET St = '{S}' WHERE User='{U.upper()}'")
    
    return st(U)

def level(S,U):
    global cur
    res=cur.execute("SELECT Level FROM Users WHERE {}='{}' ".format(S,U))
    try:
        x=list(res.fetchone())
        print(x)
        return x
    except:
        return []

def add_level(L,U):
    global cur
    l=level('Token',U)[0]
    x=cur.execute(f"UPDATE Users SET Level == {l if l!=None else '' }{L},Score=={token('Token',U)[2]+100} WHERE Token='{U}'")
    con.commit()
    
    try :
        return True
    except:
        return False


def add_level_admin(S,U):
    global cur
    x=cur.execute(f"UPDATE Users SET Level == '{S}' WHERE User='{U}'")
    con.commit()
    try :
        return True
    except:
        return False

def log():
    global cur
    x=cur.execute("SELECT * FROM Users")

    rows = x.fetchall()
    return rows

def delete(U):
    global cur
    try:
        if U.upper()  == info(U)[0]:
            x=cur.execute(f"""DELETE FROM Users where User= '{U.upper()}' """)
            con.commit()
            return True
        
    except:
        return 'None'
    




# print(info('test'))
# print(add_level_admin('','X'))
# print(info('x'))

