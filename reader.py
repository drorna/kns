import json
import csv
names_roles = []
names = []
cnt = 1
cnt_p = 1
cnt_p_p = 1
cnt_r = 1
compleate_file = open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\compleate_file.csv", 'at',encoding="utf8")
just_name_file = open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\just_name__file.csv", 'at',encoding="utf8")

with open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\‏‏גליון עבודה של Microsoft Excel חדש.csv",encoding="utf8") as my_file:
    my_reader = csv.reader(my_file)
    my_list = list(my_reader)

for row in my_list[1:]:
    invitees = row[1]
    CommitteeSessionID = row[0]
    d = json.loads(invitees)
    for inveeter in d:
        if 'name' in inveeter and 'role' in inveeter:
            name = inveeter['name']
            role = inveeter['role']
            compleate_file.write(f'{CommitteeSessionID}, {cnt}, {name}, {role}\n')
            print(f'{cnt}, {name}, {role}\n')
            cnt += 1
            names_roles.append(inveeter)
        elif 'name' in inveeter:
            name = inveeter['name']
            just_name_file.write(f'{CommitteeSessionID}, {cnt_p}, {name}\n')
            print(f'{cnt_p}, {name}\n')
            cnt_p += 1
            names.append(inveeter)
        else:
            cnt_p_p += 1
            continue
    cnt_r +=1





print(cnt)
print(cnt_p)
print(cnt_p_p)
print(cnt_r)




