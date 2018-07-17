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

qty_pat = "Quantity:\s(\d+)"
qty = findall(qty_pat,data)
print(qty)

cp_pat = "CP:\s(\d+)"
cp = findall(cp_pat,data)
print(cp)

sp_pat = "SP:\s(\d+)"
sp = findall(sp_pat,data)
print(sp)

csv_file = open("tables.csv","w",newline = "")
csv_obj = writer(csv_file)
csv_obj.writerow(title)
                
csv_file.close()


