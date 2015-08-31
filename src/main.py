#READING IN A FILE AND EXTRACTING THE VALUES

f = open('People.txt', 'r')#opening the file for reading

#Loops over the file line by line and prints it out
for line in f:
    #print(repr(line))    #prints the line out but leaves newline (\n) characters and qoutes.
    line = line.strip()   #this takes each line and strips of the characters that are not needed(\n ')
    #print(line)
    columns = line.split() #We can turn this line into a list with each word now an element in the list(columns)
    firstName = columns[0] #now we exract each value from the list, this is how we extract values from a file 
    lastName = columns[1]
    age = columns[2]
    grade = columns[3]
    print("FIRST NAME:{0}   LAST NAME:{1}   AGE:{2}   GRADE:{3}".format(firstName, lastName, age, grade))

#Simple Prints out the entire file in one long string    
#data = f.read()
#print(data)
f.close() #closes the file

w = open('output.txt', 'w')#Re-opening the file for writing

w.write("Hello, World!\n")#You can easily write string into file with write()

