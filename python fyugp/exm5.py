try:
    file = open("text.txt", "r")  
    data = file.read()             
    print(data)                    
    file.close()   

except:
    print("Error occurred")