import csv
dubbel = open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\dubbel.csv", 'at', encoding="utf8")
with open(r"C:\Users\nadel\OneDrive\שולחן העבודה\לובי - 99\kns\קובץ מסודר\compleate_file.csv",encoding="utf8") as complete_file:
    my_reader = csv.reader(complete_file)
    my_list = list(my_reader)
    my_list_2 = my_list
for row in my_list:
    name = row[2]
    CommitteeSessionID = row[0]
    for row in my_list_2:
        names = row[2]
        CommitteeSessionID_s = row[0]
        if names == name:
            if CommitteeSessionID_s != CommitteeSessionID:
                dubbel.write(f'{name},')
                dubbel.write(f'{CommitteeSessionID}, {CommitteeSessionID_s}\n')
            else:
                continue
