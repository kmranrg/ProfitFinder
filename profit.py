from csv import reader,writer
from re import findall
from collections import OrderedDict

print("\t\t\t***** SUPER MARKET *****\n")

file = open("records.txt")
data = file.read()
file.close()

title_pat = "(\S+):\s"
title = findall(title_pat,data)
# for removing the duplicate entries from list with order maintained
title = list(OrderedDict.fromkeys(title))
title.append("Profit")
print(title)

pro_pat = "Product:\s(\w+)"
pro = findall(pro_pat,data)
print(pro)

qty_pat = "QuantitySold:\s(\d+)"
qty = findall(qty_pat,data)
print(qty)

cp_pat = "CP:\s(\d+)"
cp = findall(cp_pat,data)
print(cp)

sp_pat = "SP:\s(\d+)"
sp = findall(sp_pat,data)
print(sp)

# profit calculation
profit = []
for i in range(len(pro)):
    value = (int(sp[i])-int(cp[i]))*int(qty[i])
    profit.append(value)

print(profit)

csv_file = open("tables.csv","w",newline = "")
csv_obj = writer(csv_file)
csv_obj.writerow(title)

# creating the rows

for i in range(len(pro)):
    row = []
    row.append(pro[i])
    row.append(qty[i])
    row.append(cp[i])
    row.append(sp[i])
    row.append(profit[i])
    csv_obj.writerow(row)
    del row
              
csv_file.close()


