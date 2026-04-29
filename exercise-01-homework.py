import csv

with open("session1/movies.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)

    total = 0
    count = 0
    imdbhighrating = 0
    
    for row in reader:
        if row[5] != 0:
            ratingrow = float(row[5])/ len(row[5])
            total += ratingrow
            count += 1
            
            if row[5] >= "8.0" and row[5] != 0:
                imdbhighrating += 1
    print("No of IMDB ratings above 8.0: ",imdbhighrating)

    print("IMDB average score: ",total/count)        
    if row[3] != 0:
            ratingrow2 = float(row[3])/ len(row[3])
            total += ratingrow2
            count += 1
    print("Average runtime_min score: ", total/count)

    for i, row in enumerate(reader, start=1):
            count += 1
            if row[4].find('Action') != -1 :
                     print("MATCH: ", row[1])
                     break
print("Number of rows = ", count)
print(header, row[0],row[1],row[2])
