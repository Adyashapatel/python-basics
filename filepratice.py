with open("sample.txt", "r") as file:
    line = file.readlines()
    for i in line :
        if "Python" in i:  
          print(i)   
