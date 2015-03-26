import os.path


if os.path.isfile('file.txt'):

	txt_file = open("file.txt","r")	
	line_1 = txt_file.readline()
	line_w = txt_file.readlines()
	txt_file.close()
	
	txt_file = open("file_1.txt","w")
	txt_file.write(line_1)
	txt_file.close # close File_1
	
	txt_file = open("file_2.txt","w")
	txt_file.writelines(line_w)
	txt_file.close() # close file_2
	
	#txt_file.close() #close open file
else:
	print "Something Went wrong"
	
	


	
	
	