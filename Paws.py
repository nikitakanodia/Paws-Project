print("                                                    CONNECTIVITY PROJECT OF PYTHON WITH MYSQL")
print("                                                                      Made by- ")
print("                                                                1. Nikita Kanodia ")
print("                                                            **********PAWS**********")
print("                                                     **********THE PETCARE SALON**********")
print("                                                     *******INTRODUCTION OF PROJECT*******")
string1="This project is very useful for the pet salons to keep a check on the pets coming into their petcare."
string2="It helps in bill generation ,updation, searching and deletion of the details of the pets and hence making the work easy for them."

print(" "*25,string1)
print(" "*12,string2)
print()

from tabulate import tabulate
import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',passwd='root',database='pet')
if mycon.is_connected():
    print("                                                         Mysql is Successfully connected")
mycursor=mycon.cursor()
mycursor.execute("select * from pet_salon")
mydata=mycursor.fetchall()

ch="y"
while ch=="y" or ch=="Y":
    print("MENU :")
    print("1. SHOW DETAILS ")
    print("2. INSERT NEW RECORD")
    print("3. UPDATE THE RECORD")
    print("4. SEARCH THE RECORD")
    print("5. DELETE A RECORD ")
    print("6. BILL GENERATION")
    print("7. EXIT")
    print()

    n=int(input("Enter your choice: "))
    if n==1:
        #SHOW DETAILS
        print("                  ****SHOW DETAILS****")
        print()
        mycursor.execute("select * from pet_salon")
        mydata=mycursor.fetchall()
        print(tabulate(mydata,headers=["Owner Name","Owner Phone Number","Pet Number","Pet Type","Full Makeover","Selective Makeover","Number of Hours"],tablefmt="fancy_grid"))
        
        
            
    elif n==2:
      #INSERT NEW DETAILS
      print("                    ****INSERT DETAIL****")
      inp="y"
      while inp=="y":
        print("WELCOME TO THE PETCARE SALON")
        name=input("Enter the owner name :  ")
        phno=int(input("Enter owner's phone number : "))
        pno=int(input("Enter pet number : "))
        ptype=input("Enter the pet type :  ")
        make=input("Enter 1 for full makeover and 2 for special part treatment:")
        dur=int(input("Enter duration of service (in hours): "))
        if make=="1":
                q="yes"
                query="insert into pet_salon values('{owner_name}',{owner_ph},{pet_no},'{pet_type}','{full_makeover}','{selective_makeover}',{no_of_hours})".format(owner_name=name,owner_ph=phno,pet_no=pno,pet_type=ptype,full_makeover=q,selective_makeover="None",no_of_hours=dur)
        elif make=="2":
            print(" SERVICES PROVIDED HERE ARE : ")
            print(" 1. BATH ")
            print(" 2. NAIL CUTTING AND FILING")
            print(" 3. EAR CLEANING ")
            print(" 4. MEDICATED SOAKS")
            print(" 5- FLEA TREATMENTS")
            print(" 6- SPA PACKAGE") 
            choice=input("Enter the service to avail 1/2/3/4/5/6 : ")
            if choice=="1":
                    q="BATH"
            elif choice=="2":
                    q="NAIL CUTTING AND FILING"
            elif choice=="3":
                    q="EAR CLEANING"
            elif choice=="4":
                    q="MEDICATED SOCKS"
            elif choice=="5":
                    q="FLEA TREATMENTS"
            elif choice=="6":
                    q="SPA PACKAGE"
            else:
                     print(" INVALID INPUT ")
            query="insert into pet_salon values('{owner_name}',{owner_ph},{pet_no},'{pet_type}','{full_makeover}','{selective_makeover}',{no_of_hours})".format(owner_name=name,owner_ph=phno,pet_no=pno,pet_type=ptype,full_makeover="None",selective_makeover=q,no_of_hours=dur)
        mycursor.execute(query)
        mycon.commit()
        print("!!!Record Saved!!!")
        inp=input("Do you want to add more? If yes press y: ")
        print()
    elif n==3:
        #UPDATE DETAILS
        print("                 ****UPDATE DETAILS****")
        pno=int(input("Enter the Pet Number to Update: "))
        mycursor.execute("select * from pet_salon where pet_no={}".format(pno))
        data=mycursor.fetchone()
        if data!= None:
            print("!!!Record Found!!!")
            print("Details Are:")
            print(data)
        if data==None:
            print("No record exist")
        if data[4]==None or data[5]==None:
            print("1.Update full makeover")
            print("2.Update selective makeover")
            print("3.Update duration of makeover(in hours) ")
            print("4.Update ownner's phone number")
            u=int(input("Enter Your Choice to Update 1/2/3: "))
        else:
            print(" YOU HAVE TWO CHOICES ")
            print("3. Update duration of makeover(in hours)")
            print("4. Update ownner's phone number")
            u=int(input("Enter Your Choice to Update 3/4: "))
        con="Y"
        while con=='Y':
            if u==1:
                s="yes"
                mycursor.execute("update pet_salon set full_makeover='{}' where pet_no={}".format(s,pno))
                mycon.commit()
            if u==2:
                s=input("Enter the selective makeover for change: ")
                mycursor.execute("update pet_salon set selective_makeover='{}' where pet_no={}".format(s,pno))
                mycon.commit()
            elif u==3:
                s=int(input("Enter Duration of makeover (in hours): "))
                mycursor.execute("update pet_salon set no_of_hours={} where pet_no={}".format(s,pno))
                mycon.commit()
            elif u==4:
                s=int(input(" Enter owner's new phone number: "))
                mycursor.execute("update pet_salon set owner_ph={} where pet_no={}".format(s,pno))
                mycon.commit()
            else:
                print("INVALID INPUT")
                cont="N"
            print("!!!RECORD UPDATED!!!")
            con=input("Do you Want to Update More?Y/N: ")
            print()
    elif n==4:
       #SEARCH DATA
       print("              ****SEARCH DATA****")
       pno=int(input("Enter Pet Number to Search: "))
       mycursor.execute("select * from pet_salon where pet_no="+str(pno))
       data=mycursor.fetchone()
       if data!=None:
            print(data)
       else:
           print("!!!No such record Exist!!!")
           print()
    elif n==5:
        #DELETE DETAIL
        print("             ****DELETE DETAIL****")
        c=int(input("Enter pet number whose record is to be deleted : "))
        for i in mydata :
            if i[2]==c:
                print("!!!RECORD FOUND!!!")
                query="delete from pet_salon where pet_no={}".format(c)
                mycursor.execute(query)
                mycon.commit()
                print("!!!RECORD DELETED!!!")
                print()
    elif n==6:
       #BILL GENERATION
       print("              ****BILL GENERATION****")
       print()
       data=0
       pno = int(input("Enter Pet Number to generate bill: "))
       mycursor.execute("select * from pet_salon where pet_no={}".format(pno))
       data = mycursor.fetchone()
       print(data)
       print()
       a=data[5]
       if data[4]=="yes":
             table=[["1",data[3],"Full Makeover","10000"],[" "," "," ","Total Bill = Rs.10000/-"]]
             print("                           BILL IS : ")          
             print(tabulate(table,headers=["S.No.","Pet Type","Selective/Full Makeover","Cost(in Rs.)"],tablefmt="fancy_grid"))

       else:
            s=data[5].split(",")
            for i in range (len(s)):
               if s[i]=="BATH":
                  c=s[i]
                  b="Total Bill = Rs.1000/-"
                  table=[["1",data[3],c,"1000"],[" "," "," ",b]]
                  
               elif s[i]=="NAIL CUTTING AND FILING" :
                  c=s[i]
                  b="Total Bill = Rs.2500/-"
                  table=[["1",data[3],c,"2500"],[" "," "," ",b]]
                
               elif s[i]=="EAR CLEANING" :
                    c=s[i]
                    b="Total Bill = Rs.1200/-"
                    table=[["1",data[3],c,"1200"],[" "," "," ",b]]
               elif s[i]=="MEDICATED SOAKS" :
                    c=s[i]
                    b="Total Bill = Rs.1000/-"
                    table=[["1",data[3],c,"1000"],[" "," "," ",b]]
               elif s[i]=="FLEA TREATMENTS":
                    c=s[i]
                    b="Total Bill = Rs.800/-"
                    table=[["1",data[3],c,"800"],[" "," "," ",b]]
               elif s[i]=="SPA PACKAGE" :
                    c=s[i]
                    b="Total Bill = Rs.3000/-"
                    table=[["1",data[3],c,"3000"],[" "," "," ",b]]
            print("                           BILL IS : ")
            print(tabulate(table,headers=["S.No.","Pet Type","Selective/Full Makeover","Cost(in Rs.)"],tablefmt="fancy_grid"))
    print()
    if n==7:
           #EXIT
           import sys
           sys.exit()
    ch=input("DO YOU WANT TO CONTINUE? Y/N  :  ")

