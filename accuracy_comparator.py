import os

def main():
	current_path = os.getcwd()
	for num_of_eigfaces in range (2,27,2):
		# Path to store the running script
		folder_name = str(num_of_eigfaces) + "_eigenfaces"
		file_name = "out.txt"
		folder_path = current_path + "/" + folder_name
		path = folder_path + "/" + file_name

		# Open out.txt to check for accuracy of each face
		fd = open(path)
		
		# Read the whole text files
		lines = fd.readlines()
		
		# The number of correctly identified face
		num_correct = 0
		num_images = 0
		
		# The faces that wasn't been able to be recognized
		unrecognized = []
		recognized = []
		
		line_index = -1
		for line in lines:
			line_index += 1
			actual_result_line_index = line_index +1
			
			# Index of the word recognized
			index = line.find("recognized")
			if(index != -1):
				num_images += 1
				target_line = line
				actual_line = lines[actual_result_line_index]
				#print actual_line
				# Index of the digit in the target_line
				# eg. if it was 11.tga, these keep track of 11
				index_of_last_digit = index
				index_of_first_digit = 0
				
				# Grab the file to be matched
				# eg. 1.tga -> 1
				while (target_line[index_of_last_digit] != '.'):
					index_of_last_digit-= 1
				
				# Inclusive
				index_of_first_digit = index_of_last_digit
				while (target_line[index_of_first_digit] != '/'):
					index_of_first_digit-= 1
				index_of_first_digit += 1
				
				expected_image = int(target_line[index_of_first_digit:index_of_last_digit])
				
				index_of_last_digit = actual_line.find(";")
				index_of_first_digit = index_of_last_digit
				# Now index_of_last and first digit changes purposes
				# too keep track of the number in actual line
				while (actual_line[index_of_first_digit] != '/'):
					index_of_first_digit -= 1
				index_of_first_digit += 1
				actual_image = int(actual_line[index_of_first_digit:index_of_last_digit])
				
				# Now, try to get the data of the MSE
				keyword = "MSE: "
				index_of_first_digit = actual_line.find(keyword);
				index_of_first_digit += len(keyword)
				index_of_last_digit = len(actual_line)
				
				MSE = float(actual_line[index_of_first_digit:index_of_last_digit])
				
				# Check if the expected is the same as the actual
				if(actual_image == expected_image):
					num_correct +=1
					recognized.append((expected_image, MSE))
				else:
					unrecognized.append((expected_image, MSE))
					
		
		print "With " + str(num_of_eigfaces) + " eigenfaces, " + str(num_correct) + " faces are recognized, accuracy = " + str(float(num_correct) / num_images  * 100) + " %"
		print "Not recognized: " + str(sorted(unrecognized, key=lambda tuple: tuple[1]))
#		print "MSE of unrecognized: " + str(mse_unrecognized)
		print "Recognized: " + str(sorted(recognized, key=lambda tuple: tuple[1])) + "\n"
#		print "MSE of recognized: " + str(mse_recognized) + "\n"

main()