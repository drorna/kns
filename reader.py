"""
>>> import reader
>>> data = reader.load_data(
"""

import json
import csv

def load_data(fname):
    names_roles = []
    names = []
    unparsed = []

    with open(fname, encoding="utf-8") as my_file:
        my_reader = csv.reader(my_file)
        my_list = list(my_reader)

    for row in my_list[1:]:
        invitees = json.loads(row[1])
        CommitteeSessionID = json.loads(row[0])
        if isinstance(CommitteeSessionID, list):
            # Must be backwards, reverse the order
            invitees, CommitteeSessionID = CommitteeSessionID, invitees
        for inveeter in invitees:
            if 'name' in inveeter and 'role' in inveeter:
                names_roles.append(inveeter)
            elif 'name' in inveeter:
                rawname = inveeter["name"]
                # Try to split it on various known separators
                for s in (",", "הכנסת", "העוצר", "הבריאות", "החברתי"):
                    if len(rawname.split(s) == 2:
                        if s == ",":
                            name, role = rawname.split(s)
                        else:
                            role, name = rawname.split(s)
                        names_roles.append({"name": name, "role": role})
                        break
                else:
                    names.append(inveeter)
            else:
                unparsed.append(inveeter)
    return names_roles, names, unparsed


def write_parsed_data(complete_data, name_only_data, unparsed):
    compleate_file = open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\compleate_file.csv", 'at',encoding="utf8")
    just_name_file = open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\just_name__file.csv", 'at',encoding="utf8")
    cnt = 1
    cnt_p = 1
    cnt_p_p = 1
    for inveeter in complete_data:
        name = inveeter['name']
        role = inveeter['role']
        compleate_file.write(f'{CommitteeSessionID}, {cnt}, {name}, {role}\n')
        print(f'{cnt}, {name}, {role}\n')
        cnt += 1
    for inveeter in name_only_data:
        name = inveeter['name']
        just_name_file.write(f'{CommitteeSessionID}, {cnt_p}, {name}\n')
        print(f'{cnt_p}, {name}\n')
        cnt_p += 1
    print(cnt)
    print(cnt_p)
    print(cnt_p_p)
    print(cnt_r)


if __name__ == "__main__":
    fname = r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\‏‏גליון עבודה של Microsoft Excel חדש.csv"
    name_roles, names, unparsed = load_data(fname)
    # Here is the place to try to deal with splitting names into name_roles, and parsing the unparsed data
    write_parsed_data(name_roles, names, unparsed)


