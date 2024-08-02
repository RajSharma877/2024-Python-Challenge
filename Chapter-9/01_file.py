f = open("file.txt", "r")  # It opens the file. By default in read mode
data = f.read()  # Reads the content from the file
print(data)
f.close()  # Its very important to close the file. close() is used to close the file
