from a2 import*
import json

records = read_data_from_file(file_path="data.json")

print('------------------------------------------------------------------------')
print(' HELLO USER!')
print('------------------------------------------------------------------------')
print(' ')
print('1. read_data_from_file')
print('2. filter_by_first_name')
print('3. filter_by_last_name')
print('4. filter_by_full_name')
print('5. filter_by_age_range')
print('6. count_by_gender')
print('7. filter_by_address')
print('8. find_alumni')
print('9. find_topper_of_each_institute')
print('10. find_blood_donors')
print('11. get_common_friends')
print('12. is_related')
print('13. delete_by_id')
print('14. add_friend')
print('15. remove_friend')
print('16. add_education')
print(" ")



while True:

    x=int(input("CHOOSE OF THE ABOVE QUERIES LISTED ABOVE TO PERFORM THE FUNCTION (INTEGER): "))

    if x==(-1):
        print("Thank You")
        break

    elif x==1:
        read_data_from_file(file_path="data.json")
                

    elif x==2:
        a=input("First Name (STRING): ")
        print(filter_by_first_name(records, a))
                

    elif x==3:
        a=input("Last Name (STRING): ")
        print(filter_by_last_name(records,a))
                

    elif x==4:
        a=input("Full Name (STRING): ")
        print(filter_by_full_name(records, a))
                

    elif x==5:
        a=input("Minimum age (INTEGER): ")
        b=input("Maximum age (INTEGER): ")
        print(filter_by_age_range(records, a, b))
                

    elif x==6:
        print(count_by_gender(records))
                

    elif x==7:

        add={}
        try:
            a=int(input("House no (INTEGER): "))
            if a!='':
                x1={"house_no":int(a)}
                add.update(x1)
        except:
            pass

        try:
            b=input("Block (STRING): ")
            if b!='':
                x2={"block":b.upper()}
                add.update(x2)
        except:
            pass

        try:
            c=input("Town (STRING): ")
            if c!='':
                x3={"town":c}
                add.update(x3)
        except:
            pass

        try:
            d=input("City (STRING): ")
            if d!='':
                x4={"city":d}
                add.update(x4)
        except:
            pass

        try:
            e=input("State (STRING): ")
            if e!='':
                x5={"state":e}
                add.update(x5)
        except:
            pass

        try:
            f=int(input("Pincode (INTEGER): "))
            if f!='':
                x6={"pincode":f}
                add.update(x6)
        except:
            pass

        print(filter_by_address(records, add))
                
                    
    elif x==8:
        a=input("Institute Name (STRING): ")
        print(find_alumni(records, a))
                

    elif x==9:
        print(find_topper_of_each_institute(records))
                

    elif x==10:
        a=int(input("Receiver person's id (INTEGER): "))
        print(find_blood_donors(records, int(a)))
                

    elif x==11:
        a= list(map(int, input("List of ids (SPACE SEPERATED INTEGERS): ").split()))
        print(get_common_friends(records, a))
                

    elif x==12:
        a=input("Person 1 id (INTEGER): ")
        b=input("Person 2 id (INTEGER): ")
        print(is_related(records, a, b))
                

    elif x==13:
        a=int(input("Person's id (INTEGER): "))
        print(delete_by_id(records, int(a)))
        records=delete_by_id(records, int(a))
                

    elif x==14:
        a=input("Person's id (INTEGER): ")
        b=input("Friend's id (INTEGER): ")
        print(add_friend(records, a, b))
        records=add_friend(records, a, b)
                

    elif x==15:
        a=input("Person's id (INTEGER): ")
        b=input("Friend's id (INTEGER): ")
        print(remove_friend(records, a, b))
        records=remove_friend(records, a, b)
                

    elif x==16:
        a=input("Person's id (INTEGER): ")
        b=input("Institue Name (STRING): ")
        c=input("Ongoing (BOOLEAN): ")
        d=input("Percentage (FLOAT): ")
        print(add_education(records, a, b, c, d))
        records=add_education(records, a, b, c, d)
                

    
    else:
        print("YOU'VE ENTERED AN INVALID CODE. PLEASE TRY AGAIN.")
        





    








