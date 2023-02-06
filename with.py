import json
import csv
import collections
name_list = []
dubble = []
compleate_file = open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\compleate_file.csv", 'at')
just_name_file = open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\just_name__file.csv", 'at')
def reader():
    with open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\‏‏גליון עבודה של Microsoft Excel חדש.csv",encoding="utf8") as my_file:
        my_reader = csv.reader(my_file)
        my_list = list(my_reader)
        return my_list
def orgenize(inveeter, CommitteeSessionID):
    cnt = 1
    cnt_p = 1
    cnt_p_p = 1
    cnt_r = 1


    if 'name' in inveeter and 'role' in inveeter:
        name = inveeter['name']
        role = inveeter['role']
        compleate_file.write(f'{CommitteeSessionID}, {cnt}, {name}, {role}\n')
        #print(f'{cnt}, {name}, {role}\n')
        cnt += 1
        name_list.append({name: CommitteeSessionID})
        return CommitteeSessionID, name, role
    elif 'name' in inveeter:
        name = inveeter['name']
        just_name_file.write(f'{CommitteeSessionID}, {name}\n')
            #print(f'{cnt_p}, {name}\n')
        cnt_p += 1
        name_list.append({name: CommitteeSessionID})
        return CommitteeSessionID, name
    else:
        cnt_p_p += 1
        return
def check(inveeter, CommitteeSessionID):
    for dict in name_list:
        if inveeter['name'] == dict['name'] and inveeter['role'] != dict['role']:
            dubble.append(inveeter, CommitteeSessionID)
        else:
            if 'name' in inveeter and 'role' in inveeter:
                name_list.append(inveeter)
            else:
                name_list.append({'name':inveeter['name'], 'role':'none'})









def main():
    my_list = reader()
    row_f = my_list[1]
    invitees = row_f[1]
    CommitteeSessionID = row_f[0]
    invitees_dictionery = json.loads(invitees)
    for inveeter in invitees_dictionery:
        details = orgenize(inveeter, CommitteeSessionID)
        print(details)
        if 'name' in inveeter and 'role' in inveeter:
            name_list.append(inveeter)
        else:
            name_list.append({'name': inveeter['name'], 'role': 'none'})
    for row in my_list[2:]:
        invitees = row[1]
        CommitteeSessionID = row[0]
        invitees_dictionery = json.loads(invitees)
        for inveeter in invitees_dictionery:
            details = orgenize(inveeter, CommitteeSessionID)
            print(details)

            check(inveeter, CommitteeSessionID)
main()

print(dubble)





'''print(cnt)
print(cnt_p)
print(cnt_p_p)
print(cnt_r)'''




