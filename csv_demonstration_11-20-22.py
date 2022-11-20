import csv

# Reading a CSV:
csvfile = open("Singles List.csv", newline="")
reader = csv.reader(csvfile, delimiter = ",", quotechar = "|")

data = []
for row in reader:
    data.append(row)

new_data = []
for i in range(len(data)):
    if i > 0: 
        song_name = data[i][1][1:-1]
        year = data[i][2]

        print("(" + year + ") " + song_name)
        new_data.append([year,song_name])

# Writing a CSV:
writefile = open("csv_written.csv", "w")
writer = csv.writer(writefile)

write_list = []
for i in range(2000,2023):
    write_list.append([i,0])

for row in new_data:
    year = int(row[0])
    i = 0
    while not year == write_list[i][0]:
        i+=1
    write_list[i][1]+=1

for row in write_list:
    writer.writerow(row)