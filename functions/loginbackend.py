import sqlite3 as sl
con = sl.connect('databases\\logininfo.sql')

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
        error = "INVALID(400), SEE ERROR CODES FOR MORE INFO"
        return error
    #########################################################
    newpassword = input("Enter new Password : ")
    confirrmpass = input("Repeat new Password : ")
    if newpassword == confirrmpass:
        officialnewpass = newpassword
    else:
        error = "INVALID(400), SEE ERROR CODES FOR MORE INFO"
        return error
    #########################################################
    newelevationlevel = int(input("Admin or no (1 or 0) : "))
    if newelevationlevel == 1:
        officialelvation = newelevationlevel
    elif newelevationlevel == 1:
        officialelvation = newelevationlevel
    elif newelevationlevel == 2:
        officialelvation = newelevationlevel
    else:
        error = "INVALID(400), SEE ERROR CODES FOR MORE INFO"
        return error
    #########################################################
    sql = 'INSERT INTO logininfo (USERNAME, PASSWORD, ELEVATION) values(?, ?, ?)'
    data = [
        (f'{officialnewuser}', f'{officialnewpass}', officialelvation),
    ]
    with con:
        con.executemany(sql, data)
    #########################################################

#### ------------------------------ D O   N O T   T O U C H -------------------------------------####   


        
#### ------------------------------ O N L Y   U S E   T H I S -------------------------------------####  
def login(): 
    user = input("- ")
    password = input("- ")        
    with con:
        data = con.execute(f"SELECT * FROM LOGININFO WHERE USERNAME like '{user}'")
        for row in data:
            if password in row:
                if 1 in row:
                    return 2
                elif 0 in row:
                    return 1
                elif 2 in row:
                    return 3
            else:
                return 0
        else:
            return 0
#### ------------------------------ O N L Y   U S E   T H I S -------------------------------------####  
            
login()