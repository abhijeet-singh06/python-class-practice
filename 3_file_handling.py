# with open(r"C:\Users\viraj\Downloads\file.txt", "r") as file1:
#     content = file1.read()
#     print(content)


# with open(r"C:\Users\viraj\Downloads\file.txt" , "r") as file1:
#     content = file1.readlines()
#     print(content)
    
    
    
# with open(r"C:\Users\viraj\Downloads\file.txt", "r") as file1:
#     for line in file1:
#         print(line.strip())
    
    
    
# with open(r"C:\Users\viraj\Downloads\file.txt" , "r") as file1:
#     content = file1.readlines()
#     print(len(content))


# OR
# count = 0
# with open(r"C:\Users\viraj\Downloads\file.txt" , "r") as file1:
#     for line in file1:
#         count+=1
# print(count)



# with open(r"C:\Users\viraj\Downloads\file.txt" , "w") as file1:
#     file1.write("Abhi,50,Bareilly\n")
#     file1.write("Abhinav,30,Sitapur\n")
#     file1.write("Abhishek,40,GKP\n")
# with open(r"C:\Users\viraj\Downloads\file.txt" , "r") as file1:
#     content= file1.read()
#     print(content)
    
    
# with open(r"C:\Users\viraj\Downloads\file.txt" , "a") as file1:
#     file1.write("Karan,20,Samodha\n")
# with open(r"C:\Users\viraj\Downloads\file.txt" , "r") as file1:
#     content = file1.read()
#     print(content)
    
    
with open(r"C:\Users\viraj\Downloads\file.txt" , "r+") as file1:
    lines = file1.readlines()
    lines[0] = "Rohit,25,Lucknow\n"

    file1.seek(0)                         # Go back to start
    file1.writelines(lines)               # Write updated lines
    file1.truncate()                      # Remove leftover old data

with open(r"C:\Users\viraj\Downloads\file.txt", "r") as file1:
    print(file1.read())

    

