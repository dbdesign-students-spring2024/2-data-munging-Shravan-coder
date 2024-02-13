# Place code below to do the munging part of this assignment.


# munge.py

filenasa = open("GLB.Ts+dSST.txt", 'r')  #file variabe for the nasa file
listoflines= filenasa.readlines()    # a list of strings with each line of the nasa file
mungefile= open('munged.csv', 'w')   # new csv file


def farenheit_conversion(celsius):
    try:
        temp = int(celsius)*1.8 /100
        return temp
    except:
        print('something is wrong')

def process(line):
    list =[]
    str = ""
    new_line = ""

    split_str = line.split()    # convert string into a list
    
    count_com = 0
    for i in split_str:     # iterating through new list to convert them into a csv format

        # add column headings and years without alteration
        if len(i) == 4 and i.isnumeric() or i.isalpha() or i in ['J-D','D-N']:
            new_line += i 
        
        # convert temp and handle missing data "***"
        else:
            neg = False
            num_str = ""
            for char in i:  # iterate each character in line
                
                if char == "*":
                    new_line += ""  # replaces * with an empty line
                elif char.isnumeric():
                    num_str += char
                elif char == "-":   # dealing with negative numbers
                    new_line += "-"
                    neg = True
                elif neg == True and char.isnumeric():
                    num_str += char
            print(num_str)
            if len(num_str)>0:
                new_line += '{:.1f}'.format(farenheit_conversion(int(num_str)))
      

        if count_com < len(split_str)-1:    # ensure we're adding the correct number of commas 
            new_line += ","
            count_com+=1

    # convert temperature and handle missing data "***"
    print(split_str)
    print(new_line)        
    
    return new_line +"\n"

count = 0 

for line in listoflines:
    a = line[0]
    striped_line = line.strip()
    if a .isnumeric():
        mungefile.write(process(striped_line))
       
    elif a == "Y" and count ==0 :
        mungefile.write(process(striped_line))
        count += 1 

mungefile.close()
