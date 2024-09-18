
#######################################################################################################################################
                                                #  CANTEEN MANAGEMENT SYSTEM  #
#######################################################################################################################################                                             

import mysql.connector as mysql
from tabulate import tabulate

def go_back(location):
    while True :
        print("\t"*5," --","PRESS ENTER TO GO BACK TO", location)
        print('\n'*2+"\t"*4,end='')
        choice = input()
        if choice == '' :
            break
        else :
            print('\n\n',"\t"*6,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*6,"PLEASE ! ENTER VALID CHOICE\n\n")

def invalid(attribute = ''):
    global x
    while x == 1 :                       
        print('\t'*7,1,"-","YES \n",'\t'*7,2,"-","NO")
        print('\n'*2+"\t"*4,end='')
        choice = input("CHOICE : ")
        print('\n\n')
        if choice == '1' :
            break
        elif choice == '2' :                      
            x = 0
            if attribute != '' :
                go_back(attribute)
        else :
            print('\n\n',"\t"*5,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*5,"PLEASE ! ENTER VALID CHOICE\n\n")
    return x

def display(table_name, headers_list):
    print('\n\n')
    cursor.execute("SELECT * FROM " + table_name)
    print(tabulate(cursor, headers = headers_list, tablefmt="psql"))
    print('\n\n')
    
def add(table_name, s, details, attribute = ''):
    print('\n\n')    
    cursor.execute("INSERT INTO " + table_name + str(attribute) + " VALUES " + s,details)             
    connector.commit()
    if attribute == '' :
        print('\n\n','\t'*6,"!!! ADDED SUCCESSFULLY !!!")


def search(table_name, i_d_type, headers_list):
    try :
        cursor.execute( "SELECT * FROM " + table_name + " WHERE " + i_d_type + " = " + i_d)
        details = cursor.fetchone()
        lst = []
        for i in details :
            lst.append(i)
        tup = tuple(lst)
        lst = [tup]
        print(tabulate(lst, headers = headers_list, tablefmt="psql"))
        print('\n\n')
    except :
        print('\n\n')
        print('\t'*6,"   !!! NOT FOUND !!!")
        print('\n\n')
        
def update_str(table_name, field, value, ID, i_d):
    cursor.execute("UPDATE " + table_name + " SET " + field + " = " +'\"' + value + '\"' + " WHERE " + ID + " = " + i_d)             
    connector.commit()
    print('\n\n','\t'*6,"!!! UPDATED SUCCESSFULLY !!! \n\n")
    
def update_num(table_name, field, value, ID, i_d):
    cursor.execute("UPDATE " + table_name + " SET " + field + " = " + str(value) + " WHERE " + ID + " = " + i_d)             
    connector.commit()
    print('\n\n','\t'*6,"!!! UPDATED SUCCESSFULLY !!! \n\n")
        
def delete(table_name, condition = ''):
    cursor.execute("DELETE FROM " + table_name + condition)
    connector.commit()
    print('\n\n','\t'*6,"!!! DELETED SUCCESSFULLY !!! \n\n")

connector = mysql.connect (host = 'localhost',
                    user = 'root',
                    password = 'harsh'
                    )   
cursor = connector.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS CANTEEN")
cursor.execute("USE CANTEEN")


while True :
    print('\n\n')
    print('\n\n','\t'*6,"--- KINDLY PROVIDE THE FOLLOWING --- \n\n")
    host = input('\t'*5+"HOST     :  ")
    print()
    username = input('\t'*5+"USER     :  ")
    print()
    password = input('\t'*5+"PASSWORD :  ")

    try : 
        connector = mysql.connect (host = host,
                            user = username,
                            password = password
                            )   
        cursor = connector.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS CANTEEN")
        cursor.execute("USE CANTEEN")

############################ TABLE CREATION ###########################################################################################

        cursor.execute("CREATE TABLE IF NOT EXISTS MENU \
                       (\
                       M_ID VARCHAR(10) PRIMARY KEY, \
                       ITEM VARCHAR(30) NOT NULL, \
                       QUANTITY VARCHAR(10), \
                       PRICE DECIMAL(7,2) \
                       )")
        
        cursor.execute("CREATE TABLE IF NOT EXISTS STUDENT_PROFILE \
                       (\
                       S_ID VARCHAR(10) PRIMARY KEY, \
                       ADM_NO VARCHAR(15) NOT NULL UNIQUE, \
                       NAME VARCHAR(30) NOT NULL, \
                       CLASS TINYINT(2) NOT NULL, \
                       SECTION CHAR(1), \
                       ROLL_NO INT(3) \
                       )")

        cursor.execute("CREATE TABLE IF NOT EXISTS ORDER_HISTORY \
                       (\
                       O_ID INT NOT NULL, \
                       S_ID VARCHAR(10) NOT NULL, \
                       M_ID VARCHAR(10) NOT NULL, \
                       QUANTITY TINYINT NOT NULL, \
                       AMOUNT DECIMAL(7,2) NOT NULL, \
                       DATE DATE, \
                       TIME TIME, \
                       PAY_STATUS VARCHAR(5) NOT NULL, \
                       FOREIGN KEY(M_ID) REFERENCES MENU(M_ID), \
                       FOREIGN KEY(S_ID) REFERENCES STUDENT_PROFILE(S_ID) \
                       )")
        break
    
    except Exception :
        print('\n\n','\t'*6,"  !!! SOMETHING WENT WRONG !!! \n\n")
        print('\n\n','\t'*6,"    !!! PLEASE TRY AGAIN !!! \n\n")       

#######################################################################################################################################
                                                    #  MAIN MENU  #
#######################################################################################################################################                                                   
while True:
    
    print('\n'+'-'*134+'\n'+"#"*134+'\n'+'-'*134+'\n'*4+"*"*52+"  CANTEEN MANAGEMENT SYSTEM  "\
          +"*"*53+'\n'*4+'-'*134+'\n'+"#"*134+'\n'+'-'*134+'\n'*4)
    while True :
        print('\t'*7+"     MAIN MENU"+'\n\n')
        print("\t"*5,1," -"," FOOD MENU \n")
        print("\t"*5,2," -"," STUDENT PROFILE \n")
        print("\t"*5,3," -"," ORDER HISTORY \n")
        print("\t"*5,4," -"," PLACE ORDER \n")
        print("\t"*5,5," -"," CLEAR DUES \n")
        print("\t"*5,6," -"," EXIT")
        print('\n\n'+"\t"*4,end='')    
        choice = input("CHOICE : ")
        print('\n\n')
        
#######################################################################################################################################
                                                    # CHOICE : 1 : FOOD MENU #
#######################################################################################################################################
                                                
        if choice == '1' :                           
            while True :
                print('\n'+'-'*134+'\n'+"#"*134+'\n'+'-'*134,'\n'*7)
                print('\t'*7+"  FOOD MENU"+'\n'*3)
                print('\t'*5,1," -","DISPLAY MENU ITEMS \n")
                print('\t'*5,2," -","ADD MENU ITEM \n")
                print('\t'*5,3," -","SEARCH MENU ITEM \n")
                print('\t'*5,4," -","UPDATE MENU ITEM \n")
                print('\t'*5,5," -","DELETE MENU ITEM \n")              
                print('\t'*5,6," -","CLEAR WHOLE MENU \n")             
                print('\t'*5,7," -","BACK \n")
                print("\t"*5,8," -","EXIT")
                print('\n'*3+"\t"*4,end='')
                choice = input("CHOICE : ")
      
################# DISPLAY MENU ITEMS ##################################################################################################

                if choice == '1' :       
                    headers_list = ["MENU I.D.","ITEM","QUANTITY","PRICE"]
                    display("MENU", headers_list)
                    go_back("FOOD MENU")

################# ADD MENU ITEMS ######################################################################################################
                    
                elif choice == '2' :
                    try : 
                        while True :
                            print('\n'+'-'*134+'\n'+"#"*134+'\n'+'-'*134,'\n'*7)
                            print('\t'*6+"   ENTER MENU ITEM DETAILS"+'\n'*3)                            
                            mid = input('\t'*5+"MENU I.D. : ")
                            dname = input('\n'+'\t'*5+"ITEM NAME : ").upper()
                            quantity = input('\n'+'\t'*5+"QUANTITY : ").upper()
                            price = float(input('\n'+'\t'*5+"PRICE : "))                                                                    
                            details = (mid,dname,quantity,price)
                            s = "(%s,%s,%s,%s)"                            
                            add("MENU", s, details)
                            x = 1
                            while x == 1 :      
                                print('\t'*5," DO YOU WISH TO ADD MORE ITEMS IN THE MENU ? \n")
                                x = invalid("FOOD MENU")                               
                                break                            
                            if x == 0 :
                                break                            
                    except Exception :                        
                        print('\n\n','\t'*6,"!!! SOMETHING WENT WRONG !!! \n\n")
                        print('\n\n','\t'*6,"  !!! PLEASE TRY AGAIN !!! \n\n")
                        go_back("FOOD MENU")                    

################### SEARCH MENU ITEMS #################################################################################################                      

                elif choice == '3' :
                    i_d = input('\n\n'+'\t'*5+"MENU I.D. : ")
                    print('\n\n')
                    headers_list = ["MENU I.D.","ITEM","QUANTITY","PRICE"]                    
                    try :
                        search("MENU", "M_ID", headers_list)                        
                    except Exception :
                        print('\n\n','\t'*6,"  !!! NO ITEM FOUND !!! \n\n")                        
                    finally : 
                        go_back("FOOD MENU")

################### UPDATE MENU ITEM #########$########################################################################################                    

                elif choice == '4' :
                    try :
                        while True :
                            print('\n'*4)
                            i_d = input('\t'*5+" MENU I.D. : ")
                            cursor.execute("SELECT M_ID FROM MENU")
                            m_id_list = cursor.fetchall()
                            m_id = "NOT FOUND"
                            for i in m_id_list :
                                if i[0] == i_d :
                                    m_id = "FOUND"                                    
                                    print('\n\n'+'\t'*6,"CHOOSE FIELD TO UPDATE \n")
                                    print('\t'*5, 1, "-", "ITEM NAME \n")
                                    print('\t'*5, 2, "-", "QUANTITY \n")
                                    print('\t'*5, 3, "-", "PRICE")
                                    print('\n'*3+"\t"*4,end='')
                                    choice = input("CHOICE : ")
                                    print('\n\n')
                                    if choice == '1' :                            
                                        value = input('\t'*5+"NEW ITEM NAME : ").upper()
                                        update_str("MENU", "ITEM", value, "M_ID", i_d)                                
                                        break
                                    elif choice == '2' :                                
                                        value = input('\t'*5+"NEW QUANTITY : ").upper()
                                        update_str("MENU", "QUANTITY", value, "M_ID", i_d)                                
                                        break
                                    elif choice == '3' :                                
                                        value = float(input('\t'*5+"NEW PRICE : "))
                                        update_num("MENU", "PRICE", value, "M_ID", i_d)                                
                                        break
                                    else :                                
                                        print('\n\n',"\t"*5,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*5,"PLEASE ! ENTER VALID CHOICE\n\n")
                                    break
                            if m_id == "NOT FOUND" :
                                print('\n\n',"\t"*5,"!!!", i_d, "IS NOT A VALID MENU I.D. !!!"+'\n'+"\t"*5,\
                                      "   PLEASE ! ENTER VALID MENU I.D.\n\n")
                            break
                                
                    except Exception :                        
                        print('\n\n','\t'*6,"!!! SOMETHING WENT WRONG !!! \n\n")
                        print('\n\n','\t'*6,"  !!! PLEASE TRY AGAIN !!! \n\n")
                    finally : 
                        go_back("FOOD MENU")
      

################### DELETE MENU ITEM ##################################################################################################

                elif choice == '5' :                   
                    print('\n\n')       
                    i_d = input('\t'*5+" MENU I.D. : ")
                    cursor.execute("SELECT M_ID FROM MENU")
                    m_id_list = cursor.fetchall()
                    m_id = "NOT FOUND"
                    for i in m_id_list :
                        if i[0] == i_d :
                            m_id = "FOUND"
                            condition = " WHERE M_ID = " + i_d
                            delete("MENU", condition)
                            break
                    if m_id == "NOT FOUND" :
                        print('\n\n',"\t"*5,"!!!", i_d, "IS NOT A VALID MENU I.D. !!!"+'\n'+"\t"*5,\
                              "   PLEASE ! ENTER VALID MENU I.D.\n\n")
                    go_back("FOOD MENU")                       
                                                                                    
################## CLEAR WHOLE MENU ##################################################################################################        

                elif choice == '6' :                    
                    delete("MENU")
                    go_back("FOOD MENU")
                    
################### BACK FROM MENU ####################################################################################################
                
                elif choice == '7' :
                    a = 1
                    break
                
######################## EXIT #########################################################################################################                

                elif choice == '8' :
                    a = 0
                    break
                        
################### INVALID CHOICE ####################################################################################################

                else:
                    print('\n\n',"\t"*6,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*6,"PLEASE ! ENTER VALID CHOICE\n\n")
                    go_back("FOOD MENU")

            if a == 0 :
                break

#######################################################################################################################################
                                                # CHOICE : 2 : STUDENT PROFILE #
#######################################################################################################################################
        

        elif choice == '2' :
            while True :                
                print('\n'+'-'*134+'\n'+"#"*134+'\n'+'-'*134,'\n'*7)
                print('\t'*7+"  STUDENT PROFILE"+'\n'*3)                
                print('\t'*5,1," -","DISPLAY STUDENT PROFILE DETAILS\n")
                print('\t'*5,2," -","ADD STUDENT PROFILE DETAILS \n")
                print('\t'*5,3," -","SEARCH STUDENT PROFILE DETAILS \n")
                print('\t'*5,4," -","UPDATE STUDENT PROFILE DETAILS \n")
                print('\t'*5,5," -","DELETE STUDENT PROFILE DETAILS \n")
                print('\t'*5,6," -","CLEAR ALL STUDENT PROFILES \n")
                print('\t'*5,7," -","BACK \n")
                print("\t"*5,8," -","EXIT")
                print('\n\n'+"\t"*4,end='')    
                choice = input("CHOICE : ")
                print('\n\n')
                
############### DISPLAY STUDENT PROFILES ##############################################################################################
                
                if choice == '1' :
                    headers_list = ["I.D.","ADM. NO.","NAME","CLASS","SECTION","ROLL NO."]
                    display("STUDENT_PROFILE", headers_list)
                    go_back("STUDENT PROFILE MENU")

############## ADD STUDENT PROFILE ####################################################################################################
                
                elif choice == '2' :
                    try : 
                        while True :                            
                            print('\n'+'-'*134+'\n'+"#"*134+'\n'+'-'*134,'\n'*7)
                            print('\t'*6+"     ENTER STUDENT DETAILS"+'\n'*3)                                                                                                   
                            sid = input('\t'*5+"I.D. : ")
                            adm = input('\t'*5+"ADM. NO. : ")
                            name = input('\t'*5+"NAME : ").upper()
                            cl = int(input('\t'*5+"CLASS : "))
                            sec = input('\t'*5+"SECTION : ").upper()
                            roll = int(input('\t'*5+"ROLL NO. : "))
                            details = (sid,adm,name,cl,sec,roll)
                            s = "(%s,%s,%s,%s,%s,%s)"
                            add("STUDENT_PROFILE", s, details)                            
                            x = 1
                            while x == 1 :            
                                print('\t'*5," DO YOU WISH TO ADD MORE RECORDS ? \n")
                                x = invalid("STUDENT PROFILE MENU")
                                break
                            if x == 0 :                            
                                break
                    except Exception :                        
                        print('\n\n','\t'*6,"!!! SOMETHING WENT WRONG !!! \n\n")
                        print('\n\n','\t'*6,"  !!! PLEASE TRY AGAIN !!! \n\n")
                        go_back("STUDENT PROFILE MENU")
                        
############# SEARCH STUDENT PROFILE ##################################################################################################          

                elif choice == '3' :
                    i_d = input('\n\n'+'\t'*5+"STUDENT I.D. : ")
                    print('\n\n')                    
                    headers_list = ["I.D.", "ADM. NO.", "NAME","CLASS", "SECTION", "ROLL NO."]
                    try :
                        search("STUDENT_PROFILE", "S_ID", headers_list)
                    except Exception :
                        print('\n\n','\t'*6,"  !!! NO ITEM FOUND !!! \n\n")                        
                    finally : 
                        go_back("STUDENT PROFILE MENU")

############# UPDATE STUDENT PROFILE ##################################################################################################                    

                elif choice == '4' :
                    try :
                        while True :
                            print('\n'*4)
                            i_d = input('\t'*5+" STUDENT I.D. : ")
                            cursor.execute("SELECT S_ID FROM STUDENT_PROFILE")
                            s_id_list = cursor.fetchall()
                            s_id = "NOT FOUND"
                            for i in s_id_list :
                                if i[0] == i_d :
                                    s_id = "FOUND"
                                    print('\n\n'+'\t'*6,"CHOOSE FIELD TO UPDATE \n")
                                    print('\t'*5, 1, "-", "NAME \n")
                                    print('\t'*5, 2, "-", "CLASS \n")
                                    print('\t'*5, 3, "-", "SECTION \n")
                                    print('\t'*5, 4, "-", "ROLL NO.")
                                    print('\n'*3+"\t"*4,end='')
                                    choice = input("CHOICE : ")
                                    print('\n\n')
                                    if choice == '1' :                            
                                        value = input('\t'*5+"NEW NAME : ").upper()
                                        update_str("STUDENT_PROFILE", "NAME", value, "S_ID", i_d)                                
                                        break
                                    elif choice == '2' :                                
                                        value = int(input('\t'*5+"NEW CLASS : "))
                                        update_num("STUDENT_PROFILE", "CLASS", value, "S_ID", i_d)                                
                                        break
                                    elif choice == '3' :                                
                                        value = input('\t'*5+"NEW SECTION : ").upper()
                                        update_str("STUDENT_PROFILE", "SECTION", value, "S_ID", i_d)                                
                                        break
                                    elif choice == '4' :                                
                                        value = int(input('\t'*5+"NEW ROLL NO. : "))
                                        update_num("STUDENT_PROFILE", "ROLL_NO", value, "S_ID", i_d)                                
                                        break
                                    else :                                
                                        print('\n\n',"\t"*5,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*5,"PLEASE ! ENTER VALID CHOICE\n\n")
                                    break
                            if m_id == "NOT FOUND" :
                                print('\n\n',"\t"*5,"!!!", i_d, "IS NOT A VALID STUDENT I.D. !!!"+'\n'+"\t"*5,\
                                      "   PLEASE ! ENTER VALID STUDENT I.D.\n\n")                        
                            break                               
                    except Exception :                        
                        print('\n\n','\t'*6,"!!! SOMETHING WENT WRONG !!! \n\n")
                        print('\n\n','\t'*6,"  !!! PLEASE TRY AGAIN !!! \n\n")
                    finally : 
                        go_back("STUDENT PROFILE MENU")
                    
############## DELETE STUDENT PROFILE #################################################################################################
                        
                elif choice == '5' :                   
                    print('\n\n')       
                    i_d = input('\t'*5+" STUDENT I.D. : ")
                    cursor.execute("SELECT S_ID FROM STUDENT_PROFILE")
                    s_id_list = cursor.fetchall()
                    s_id = "NOT FOUND"
                    for i in s_id_list :
                        if i[0] == i_d :
                            s_id = "FOUND"
                            condition = " WHERE S_ID = " + i_d
                            delete("STUDENT_PROFILE", condition)
                            break
                    if s_id == "NOT FOUND" :
                        print('\n\n',"\t"*5,"!!!", i_d, "IS NOT A VALID STUDENT I.D. !!!"+'\n'+"\t"*5,\
                              "   PLEASE ! ENTER VALID STUDENT I.D.\n\n")
                    go_back("STUDENT PROFILE MENU")
                    
############## CLEAR ALL STUDENT PROFILES ################################################################################################
                            
                elif choice == '6' :                    
                    delete("STUDENT_PROFILE")
                    go_back("STUDENT PROFILE MENU")

############## BACK FROM STUDENT PROFILES #############################################################################################  
                            
                elif choice == '7' :
                    b = 1
                    break
                
################### EXIT ##############################################################################################################

                elif choice == '8' :
                    b = 0
                    break
                
################### INVALID CHOICE ####################################################################################################                       

                else :
                    print('\n\n',"\t"*6,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*6,"PLEASE ! ENTER VALID CHOICE\n\n")                    
                    go_back("STUDENT PROFILE MENU")

            if b == 0 :
                break
                    
#######################################################################################################################################
                                                   # CHOICE : 3 : ORDER HISTROY #
#######################################################################################################################################

        elif choice == '3' :
            while True :                
                print('\n'+'-'*134+'\n'+"#"*134+'\n'+'-'*134,'\n'*7)
                print('\t'*7+"  ORDER HISTORY"+'\n'*3)                
                print('\t'*5,1," -","DISPLAY ALL TIME ORDER HISTORY \n")
                print('\t'*5,2," -","SEARCH ORDER HISTORY \n")
                print('\t'*5,3," -","BACK \n")
                print("\t"*5,4," -","EXIT")
                print('\n\n'+"\t"*4,end='')    
                choice = input("CHOICE : ")
                print('\n\n')

############### DISPLAY ALL TIME ORDER HISTORY ########################################################################################

                if choice == '1' :
                    headers_list = ["ORDER I.D.","STUDENT I.D.","MENU I.D.","QUANTITY","AMOUNT","DATE","TIME","PAY STATUS"]
                    display("ORDER_HISTORY", headers_list)
                    go_back("ORDER HISTORY MENU")

############### SEARCH ORDER HISTORY ##################################################################################################

                elif choice == '2' :
                    i_d = input('\n\n'+'\t'*5+"ORDER I.D. : ")
                    print('\n\n')                        
                    headers_list = ["ORDER I.D.","STUDENT I.D.","MENU I.D.","QUANTITY","AMOUNT","DATE","TIME","PAY_STATUS"]
                    try : 
                        search("ORDER_HISTORY", "O_ID", headers_list)
                    except Exception :
                        print('\n\n','\t'*6,"  !!! NO ITEM FOUND !!! \n\n")                        
                    finally : 
                        go_back("ORDER HISTROY MENU")

############### BACK FROM ORDER HISTORY ###############################################################################################

                elif choice == '3' :
                    c = 1 
                    break

################### EXIT ##############################################################################################################

                elif choice == '4' :
                    c = 0
                    break
                
################### INVALID CHOICE ####################################################################################################                

                else :
                    print('\n\n',"\t"*6,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*6,"PLEASE ! ENTER VALID CHOICE \n\n")                    
                    go_back("ORDER HISTORY MENU")

            if c == 0 :
                break

#######################################################################################################################################
                                                    # CHOICE : 4 : PLACE ORDER #
#######################################################################################################################################

        elif choice  == '4' :
            print('\n'+'-'*134+'\n'+"#"*134+'\n'+'-'*134,'\n'*7)
            print('\n'*4+'\t'*7+"  PLACE ORDER"+'\n'*3)            
            o_id = input('\t'*5+"ORDER I.D. : ")
            print()
            s_id = input('\t'*5+"STUDENT I.D. : ")
            print()
            order = []
            pay_amount = 0
            try :      
                while True :                            
                    m_id  = input('\t'*5+"MENU I.D. : ")
                    print()
                    quantity  = int(input('\t'*5+"QUANTITY : "))
                    print('\n'*3)
                    cursor.execute("SELECT PRICE FROM MENU WHERE M_ID = %s", (m_id,))
                    price = cursor.fetchone()
                    amount = quantity * float(price[0])
                    pay_amount += amount
                    order.append((m_id, quantity, amount))
                    x = 1
                    while x == 1 :                        
                        print('\t'*5," DO YOU WISH TO ORDER MORE ? \n")
                        x = invalid()                                       
                        break                                   
                    if x == 0 :
                        print('\n'+'\t'*6+"  TOTAL PAYABLE AMOUNT : Rs.", pay_amount, '\n')
                        print('\t'*5,1,"-","PAY NOW")
                        print('\t'*5,2,"-","PAY LATER")
                        
                        print('\n'*3+"\t"*4,end='')
                        choice = input("CHOICE : ")                        
                        if choice == '1':
                            pay = "PAID"                            
                        elif choice == '2':
                            pay = "DUE"                        
                        for i in range(len(order)):
                            add("ORDER_HISTORY", "(%s, %s, %s, %s, %s, %s)", (o_id, s_id, order[i][0], order[i][1], order[i][2], pay),\
                                " (O_ID, S_ID, M_ID, QUANTITY, AMOUNT, PAY_STATUS)")                            
                        cursor.execute("UPDATE ORDER_HISTORY SET DATE = CURDATE(), TIME = CURTIME() WHERE O_ID = %s", (o_id,))
                        connector.commit()                            
                        break
                print('\n\n'+'\t'*7+"!!! THANK YOU FOR YOU ORDER !!! \n\n")
            except Exception :
                print('\n\n','\t'*6,"!!! SOMETHING WENT WRONG !!! \n\n")
                print('\n\n','\t'*6,"  !!! PLEASE TRY AGAIN !!! \n\n")
            finally : 
                go_back("MAIN MENU")
            
#######################################################################################################################################
                                                    # CHOICE : 5 : CLEAR DUES #
#######################################################################################################################################

        elif choice  == '5' :
            print('\n'+'-'*134+'\n'+"#"*134+'\n'+'-'*134,'\n'*2)
            print('\n'*4+'\t'*7+"  PAY DUES"+'\n'*3)            
            i_d = input('\t'*5+"STUDENT I.D. : ")
            print('\n'*4)
            try :
                cursor.execute("SELECT SUM(AMOUNT) FROM ORDER_HISTORY WHERE S_ID = %s AND PAY_STATUS = %s", (i_d,"DUE"))
                pay_amount = cursor.fetchone()
                print('\n'+'\t'*6+"  TOTAL PAYABLE AMOUNT : Rs.", float(pay_amount[0]), '\n')
                print('\t'*5,"   PRESS ENTER TO PAY")
                print('\n'*3+"\t"*4,end='')
                choice = input()               
                if choice =='' :
                    cursor.execute("UPDATE ORDER_HISTORY SET PAY_STATUS = %s WHERE S_ID = %s", ("PAID", i_d))
                    connector.commit()
                    print('\n\n','\t'*6,"!!! DUES CLEARED SUCCESSFULLY !!! \n\n")                    
                    go_back("MAIN MENU")
                else :
                    go_back("MAIN MENU")
            except Exception :
                print('\n\n','\t'*6,"  !!! NO AMOUNT DUE !!! \n\n")
                go_back("MAIN MENU")

############################################################################################################################################################        
                                                    # CHOICE : 6 : EXIT #
############################################################################################################################################################

        elif choice == '6' :        
            break
        
################### INVALID CHOICE ####################################################################################################
        
        else:
            print('\n\n',"\t"*6,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*6,"PLEASE ! ENTER VALID CHOICE\n\n")            
            go_back("MAIN MENU")
            
#######################################################################################################################################            

    print('\n\n','\t'*6,"  !!! CONNECTION LOST !!! \n\n")
    while True :
        d = 1
        print('\n'+'\t'*6+"DO YOU WISH TO CONNECT AGAIN ? \n\n")
        print('\t'*5,1,"-","YES \n")
        print('\t'*5,2,"-","NO")
        print('\n'*3+"\t"*4,end='')
        choice = input("CHOICE : ")
        if choice == '1' :
            break
        elif choice == '2':
            d = 0
            break
        else:
            print('\n\n',"\t"*6,"  !!! INVALID CHOICE !!!"+'\n'+"\t"*6,"PLEASE ! ENTER VALID CHOICE \n\n")
    if d == 0 :
                break
            

                             ########################################################################
                             #+====================================================================+#
                             #| MADE BY :                                                          |#
                             #|                                                                    |#
                             #| NAMES           :  ANUPAM KARAN , BITTU KUMAR & HARSH KUMAR PODDAR |# 
                             #| ROLL NOS.       :        9      ,      16     &        20          |#
                             #| BOARD ROLL NOS. :    22677895   ,   22677902  &     22677906       |#
                             #| CLASS           :                   XII / B                        |#
                             #+====================================================================+#
                             ########################################################################

                                            
