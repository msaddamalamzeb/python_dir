if open("file.txt","w"):
	print "file and folder are being created"
	txt_file = open("file.txt","w")
	txt_file.write("Hello you read it\n")
	txt_file.write("You are not genious\n")
	txt_file.write("Hello you read it\n")
	txt_file.write("You are not genious\n")
	txt_file.close()

