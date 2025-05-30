
'''
w r a 
'''



# file = open("example.txt",'r')
# content = file.read()
# print(content)

# file = open("example.txt","a")
# file.write("hello world")
# file.close()
file = open("example.txt", "r+")
read = file.read()
print(read)
file.seek(0)  # Move file pointer back to the beginning
file.write("Updated")
print(read)
file.close()



'''
w r a 
'''



# file = open("example.txt",'r')
# content = file.read()
# print(content)

# file = open("example.txt","a")
# file.write("hello world")
# file.close()
file = open("example.txt", "r+")
read = file.read()
print(read)
file.seek(0)  # Move file pointer back to the beginning
file.write("Updated")
print(read)
file.close()



