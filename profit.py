from csv import reader,writer
from re import findall
from collections import OrderedDict

print("\t\t\t***** ADVANCED PROFIT CALCULATOR *****\n")

def readData():
    file = open("records.txt")
    data = file.read()
    file.close()
    print("\n\tData read successfully from file\n\n")
    return data

def fetchDet(data):
    title_pat = "(\S+):\s"
    title = findall(title_pat,data)
    
    # for removing the duplicate entries from list with order maintained
    title = list(OrderedDict.fromkeys(title))
    title.append("Profit")

    pro_pat = "Product:\s(\w+)"
    pro = findall(pro_pat,data)

    qty_pat = "QuantitySold:\s(\d+)"
    qty = findall(qty_pat,data)

    cp_pat = "CP:\s(\d+)"
    cp = findall(cp_pat,data)

    sp_pat = "SP:\s(\d+)"
    sp = findall(sp_pat,data)

    # profit calculation
    profit = []
    for i in range(len(pro)):
        value = (int(sp[i])-int(cp[i]))*int(qty[i])
        profit.append(value)
    print("\n\tDetails fetched successfully from the data\n\n")
    return title,pro,qty,cp,sp,profit

def storeDet(title,pro,qty,cp,sp,profit):
    csv_file = open("tables.csv","w",newline = "")
    csv_obj = writer(csv_file)
    csv_obj.writerow(title)

    # creating the rows for CSV file
    total_profit = 0
    for i in range(len(pro)):
        row = []
        row.append(pro[i])
        row.append(qty[i])
        row.append(cp[i])
        row.append(sp[i])
        row.append(profit[i])
        total_profit = total_profit + profit[i]
        csv_obj.writerow(row)
        del row              
    csv_file.close()
    print("\n\tDetails stored successfully in a CSV file\n\n")
    return total_profit

def showProfit(total_profit):
    print("\nTotal Profit:",total_profit)
    return

while True:
    ch = int(input("""\t\t --> Main Menu

1. Read data from file
2. Fetch all the details from the data
3. Store the details in a CSV file
4. Show Total Profit
5. Exit

Enter choice:"""))

    if ch == 1:
        data = readData()
    elif ch == 2:
        title,pro,qty,cp,sp,profit = fetchDet(data)
    elif ch == 3:
        total_profit = storeDet(title,pro,qty,cp,sp,profit)
    elif ch == 4:
        showProfit(total_profit)
    elif ch == 5:
        print("\t\t\t *** Thank You ***")
        break
    else:
        print("Invalid Choice!")
