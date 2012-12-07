import os
import subprocess
import shutil

list_file_path = "/Users/antoniusharijanto/Desktop/UW_FALL_2012/CSE_455/list.txt"
string1 = "./main --eigenfaces [num_of_eigfaces] 25 25 " + list_file_path + " [out_path]/out.face"
string2 = "./main --constructuserbase out.face " + list_file_path + " [out_path]/database"
string3 = "for i in /Users/antoniusharijanto/Desktop/UW_FALL_2012/CSE_455/faceImages/Interesting/*.tga; do ./main --recognizeface $i [out_path]/database [out_path]/out.face 1; done > [out_path]/out.txt"

main_program_path = os.getcwd() + "/main"

def main():
	current_path = os.getcwd()
	for num_of_eigfaces in range (2,27,2):
		# Path to store the running script
		folder_name = str(num_of_eigfaces) + "_eigenfaces"
		file_name = "run.sh"
		folder_path = current_path + "/" + folder_name
		path = folder_path + "/" + file_name
		
		script = "cd " + folder_path
		script += '\n'
		script += string1
		script += '\n'
		script += string2
		script += '\n'
		script += string3
		
		script = script.replace("[num_of_eigfaces]", str(num_of_eigfaces))
		script = script.replace("[out_path]", folder_path)
		
		# Set permission of the script file
		script_file = open(path, "w+")
		# Copy main program to the folder
		#os.system("rm -rf " + main_program_path)
		shutil.copy(main_program_path, folder_path)
		#os.system ("cp " + main_program_path + " " + os.getcwd() + folder_path)
		#os.system("cp " + main_program_path + " " + os.getcwd() + folder_path)
		script_file.write(script)

		os.system("chmod 777 " + path)
		print "Running the script for " + str(num_of_eigfaces) + " eigenfaces"
		#os.system("sh " + path)
		subprocess.call(path, shell=True)

main()