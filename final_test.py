"""
This program will use the grades that are contained within the 'Final.txt'
to display the answer for each of the three criterias
number of grades, the average grade, and the percentaeg of grades that are above the average grade.

to do this we write a main function that will start the application
and also tell it where the location of the grades are(Final.txt)
along with the calculate above average function that we will need later in the code.

Then we define the calculate above average function with the file, and
open the file to read and list the integars within the text file, and
finally close the text file.

After receiving the information the program will now list the grades by its length to find how many grades there are in the file,
then print out the 'Number of grades:',
it will use a function to get the sum of the grades to later use in the average function
by dividing the sum by the length and print out the 'Average grade:'

after it will then use the counter function with greater than formula to get the percent above average,
then it will print 'Percent of grades above average:' answer
"""

"""
main
	set file = "Final.txt"
	set calculate_percent_above_average(file)

define calculate_percent_above_average(file)
	open the infile and set to read only
	create the listGrades = each line of integars from the file 
	close the infile
	create the length = len(listGrades)
	create gradesum = sum(listGrades)
	create average = gradesum / length
	print "Number of grades:", using length)
	print "Average grade:", using average)
	count function starting 0
	for item in listGrades
		if item less than average
			counter += 1
	create aboveAverage = counter divided by length
	print"Percent of grades above average:" using aboveAverage

main
"""