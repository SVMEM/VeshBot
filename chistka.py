import csv
with open('nicks.csv','r') as f:
    dic = {}
    re = csv.reader(f)
    for row in re:
        dic[row[0]] = row[2]
with open('nicks_cleared.csv', 'w') as f:
    wri = csv.writer(f)
    for k, v in dic.items():
        users = [k, v]
        wri.writerow(users)

