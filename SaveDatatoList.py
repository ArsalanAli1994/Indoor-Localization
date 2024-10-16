import csv
ak_1=[]
Sk_1=[]
with open('D:\Research and Projects\Localization Robot controlling\Kalman Filter testing\DataSet3.csv', 'r') as file:
    csv_reader = csv.reader(file)
    lists_from_csv = []
    for row in csv_reader:
        lists_from_csv.append(row)

    for i in range(1112):
        ak_1.append(float(lists_from_csv[i+1][5]))
        Sk_1.append(float(lists_from_csv[i+1][9]))

        
