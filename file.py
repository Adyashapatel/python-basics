'''with open ("sample.txt","w") as file :
    file.write("adyasha\n ruchi \n python \n java \n c++")

f = open("sample.txt","r")
content = f.read()  
print(content)
f.close() '''

'''with open("log.txt","a") as file1:
    file1.write("This is a new log entry.\n")       
with open("log.txt","r") as file2:
    logs = file2.read()
    print(logs)'''

'''l1 = [5,10,15,20,25]
l2 = [i for i in l1 if i >15 ]
print(l2)'''

'''import json

with open("data.json","r") as file:
    py_obj = json.load(file)
    print(py_obj)


with open("data.json","w") as file:
    json.dump(d,file)

city = input("Enter the city name :")
population = int(input("Enter the population :"))
d[city] = population    
with open("data.json","w") as file:
    json.dump(d,file    )
    print("Data added successfully")'''

try:
    file3 = open("nonexistent.txt","r")
    content = file3.read()
    print(content)
    file3.close()
except FileNotFoundError:
    print("Error: The file does not exist.")
else: 
    print("File read successfully.")