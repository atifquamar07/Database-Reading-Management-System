import json



def read_data_from_file(file_path="data.json"):

    with open(file_path, 'r') as data:
        records = json.load(data)

    return records




def filter_by_first_name(records, first_name):

    ids = []
    for i in records:
        if i['first_name'].upper() == first_name.upper():
            ids.append(i['id'])
    return (ids)


def filter_by_last_name(records, last_name):

    a = []
    for i in records:
        if i['last_name'].upper() == last_name.upper():
            a.append(i['id'])
    return (a)





def filter_by_full_name(records, full_name):

    b = []
    for i in records:
        c = i['first_name'].upper()+' '+i['last_name'].upper()
        if c == full_name.upper():
            b.append(i['id'])
    return (b)


def filter_by_age_range(records, min_age, max_age):

    d = []
    for i in records:
        if int(min_age) <= i['age'] <= int(max_age):
            d.append(i['id'])
    return d


def count_by_gender(records):

    male = 0
    female = 0
    for i in records:
        if i['gender'] == 'male':
            male += 1
        if i['gender'] == 'female':
            female += 1
    return{"male": male, "female": female}


def filter_by_address(records, address):

    dic={}
    q=[]
    c=[]
    for y in range (0,200):
        c.append(y)
    for j in records:
        a=j['address']
        for i in address:
            if i in a:
                if type(address[i])==(str):
                    if address[i].upper()==a[i].upper():
                        continue
                    else:
                        if j['id'] in c:
                            c.remove(j['id'])
                else:
                    if type(address[i])==(int):
                        if address[i]==a[i]:
                            continue
                        else:
                            if j['id'] in c:
                                c.remove(j['id'])


    for j in records:
        for i in c:
            if i==int(j['id']):
                b={'first_name':j['first_name'], 'last_name':j['last_name']}
                q.append(b)

    return q




def find_alumni(records, institute_name):

    lst = []
    for i in records:
        a=i['education']
        for j in a:
            if (j['institute'].upper() == institute_name.upper()) and (not j['ongoing']):
                if len(j)==3:
                    b = {"first_name": i['first_name'], "last_name": i["last_name"], "percentage": j["percentage"]}            
                    lst.append(b)
    
    return lst



def find_topper_of_each_institute(records):

    dic = {}
    a={}
    insti=[]
    percent=[]
    idd=[]
    for address in records:
        edu=address['education']
        for j in edu:
            if (not j["ongoing"]):                
                insti.append({'institute':j['institute'],'percentage':j['percentage'],'id':address['id']})

    college=[]
    for b in insti:
        if b["institute"] not in college:
            college.append(b["institute"])

    for address in college:
        p={address:[]}
        a.update(p)

    for address in insti:
        for j in a:
            if address['institute']==j:
                a[j].append(address['percentage'])
    
    for address in a:
        a[address]=max(a[address])

    for address in a:
        for j in insti:
            if j['percentage']==a[address]:
                a[address]=j['id']

    return (a)



    
def find_blood_donors(records, receiver_person_id):

    dic = {}
    bgroup=""
    for i in records:

        if i['id']==int(receiver_person_id):
            bgroup=i["blood_group"]

    for i in records:

        if bgroup == "A" and (i["blood_group"] == ("A") or i["blood_group"]==("O")):
            p = {i['id']: i['contacts']}
            dic.update(p)
        if bgroup == "B" and i["blood_group"] == ("B" or "O"):
            p = {i['id']: i['contacts']}
            dic.update(p)
        if bgroup == "AB" and i["blood_group"] == ("AB" or "O"):
            p = {i['id']: i['contacts']}
            dic.update(p)
        if bgroup == "O" and i["blood_group"] == ("O"):
            p = {i['id']: i['contacts']}
            dic.update(p)
    
    
    del dic[int(receiver_person_id)]

    return dic



def get_common_friends(records, list_of_ids):

    b=[]
    for i in (list_of_ids):
        for j in records:
            if i==j['id']:
                b.append(j['friend_ids'])

    if len(b)>0:
        result = set(b[0]) 
        for h in b[1:]: 
            result.intersection_update(h) 
    
        q=list(result) 

        return q

    else:
        return b




def is_related(records, person_id_1, person_id_2):

    friends=[]
    for i in records:
        if i["id"]==person_id_1:
            friends.append(i)
    while True:
        for i in friends:
            if person_id_2 in i['friend_ids']:
                return True
            else:
                friends.remove(i)
                for j in i['friend_ids']:
                    for k in records:
                        if k['id']==j:
                            friends.append(k)



def delete_by_id(records, person_id):

    if (0<=int(person_id)<=199):
        record=records.copy()
        for i in record:
            if i['id']==int(person_id): 
                record.remove(i)

        for i in record:
            b=i["friend_ids"]
            for j in b:
                if j==int(person_id):
                    b.remove(j)
            return record

    else:
        return records





def add_friend(records, person_id, friend_id):

    if (0<=int(person_id)<=199 and 0<=int(friend_id)<=199):
        record=records.copy()
        for i in record:
            if i["id"]==int(person_id):
                a=i["friend_ids"]
                if int(friend_id) not in a:
                    a.append(int(friend_id))
                else:
                    continue
            if i["id"]==int(friend_id):
                a=i["friend_ids"]
                if int(person_id) not in a:
                    a.append(int(person_id))
                else:
                    continue
        return record
    
    else:
        return records
        



def remove_friend(records, person_id, friend_id):

    if (0<=person_id<=199 and 0<=friend_id<=199):
        record=records.copy()
        for i in record:
            if i["id"]==friend_id:
                a=i["friend_ids"]
                if person_id in a:
                    a.remove(person_id)
            
            if i["id"]==person_id:
                a=i["friend_ids"]
                if friend_id in a:
                    a.remove(friend_id)
        return record
    
    else:
        return records


                
def add_education(records, person_id, institute_name, ongoing, percentage):

    for i in records:
        if i['id']==int(person_id):
            record=records.copy()
            q=i['education']
            if ongoing==True:
                a={
                    "institute":institute_name.upper(),
                    "ongoing":ongoing,
                }
                q.append(a)
            elif ongoing==False:
                a={
                    "institute":institute_name.upper(),
                    "ongoing":ongoing,
                    "percentage":percentage
                }
                q.append(a)
    if (0<=int(person_id)<=199):
        return record

    else:
        return records








    

