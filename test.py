def function():
    #########################################################
    print("once you make this user you can never delete it.")
    #########################################################
    newuser = input("Enter new Username : ")
    check_newuser = newuser.isalpha()
    if check_newuser == True:
        officialnewuser = newuser
    else:
        error = "FATEL 101, SEE ERROR CODES FOR MORE INFO"
        return error
    #########################################################
    newpassword = input("Enter new Password : ")
    confirrmpass = input("Repeat new Password : ")
    if newpassword == confirrmpass:
        officialnewpass = newpassword
    else:
        print("FATEL ERROR")
    #########################################################
    newelevationlevel = int(input("Admin or no (1 or 0) : "))
    if newelevationlevel == 1:
        officialelvation = newelevationlevel
    elif newelevationlevel == 1:
        officialelvation = newelevationlevel
    elif newelevationlevel == 2:
        officialelvation = newelevationlevel
    else:
        print("FATEL ERROR")
        
function()