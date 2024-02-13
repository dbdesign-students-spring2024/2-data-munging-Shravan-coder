# Place code below to do the analysis part of the assignment.

import csv

df = open("munged.csv", 'r')
list_of_lines = csv.DictReader(df)

count = 0
total = 0
average = 0
year = 1880

for row in list_of_lines:
    # Access the value of the "J-D" column in the current row
    total += float(row["J-D"])
    count += 1
    
    if count == 10:
        average = total / 10
        print(f"Average temperature for years {year-9}-{year} is {average:.2f}")
        count = 0
        total = 0
        average = 0
    year += 1

df.close()


        


    
        
