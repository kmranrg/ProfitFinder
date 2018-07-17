from csv import reader,writer
from re import findall

print("\t\t\t***** SUPER MARKET *****\n")

data = open("records.txt").read()

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



