import sqlite3 as sl
con = sl.connect('databases\\logininfo.db')

#### ------------------------------ D O   N O T   T O U C H -------------------------------------####
def newtable():
    with con:
        con.execute("""
            CREATE TABLE LOGININFO (
                USERNAME TEXT PRIMARY KEY,
                PASSWORD VARCHAR(255),
                ELEVATION INTEGER
            );
        """)
#### ------------------------------ B R I D G E   L A Y E R -------------------------------------####         
def inputdata(newuser, newpassword, newelevationlevel):
    #########################################################
    print("once you make this user you can never delete it.")
    #########################################################
    newuser = input("Enter new Username : ")
    check_newuser = newuser.isalpha()
    if check_newuser == True:
        officialnewuser = newuser
    else:
        print("FATEL ERROR")
    #########################################################
    newpassword = input("Enter new Password : ")
    confirrmpass = input("Repeat new Password : ")
    if newpassword == confirrmpass:
        officialnewpass = newpassword
    else:
        print("FATEL ERROR")
    #########################################################
    newelevationlevel = int(input("Admin or no (1 or 0) : "))
    if newelevationlevel == 1 or 0:
        sql = 'INSERT INTO logininfo (USERNAME, PASSWORD, ELEVATION) values(?, ?, ?)'
        data = [
            (f'{officialnewuser}', f'{officialnewpass}', newelevationlevel),
        ]
        with con:
            con.executemany(sql, data)
        print("ok fine")
    else:
        print("FATEL ERROR")
    
    
#### ------------------------------ D O   N O T   T O U C H -------------------------------------####   


        
#### ------------------------------ O N L Y   U S E   T H I S -------------------------------------####  
def login(user, password):      
    with con:
        data = con.execute(f"SELECT * FROM LOGININFO WHERE USERNAME like '{user}'")
        for row in data:
            if password in row:
                print("YESSIR")
                if 1 in row:
                    print("admin")
                    return 2
                elif 0 in row:
                    print("non admin")
                    return 1
                elif 2 in row:
                    print("super admin")
                    return 3
            else:
                print("incorrect")
                return 0
        else:
            print("incorrect")
            return 0
#### ------------------------------ O N L Y   U S E   T H I S -------------------------------------####  
            
login()