# Test Plan for Stroop Test Project

''' Ways the user can test the functionality of this program:

Test 1: The user will be able to launch the program, and present 5 Stroop trials. 
The GUI should open, the user sees 5 colored words, and their reaction time is recorded in tha data file

Test 2: The use can verify the data is saved correctly in the data file.
The data file should have rows of data with the correct headers and values.

test example:
1. run 'stroop_test.py'
2. respond to 5 trials
3. check that
- response input is accepted,
- reaction times are recorded
- data is saved to a .csv file in the data folder
- the csv file has the correct time and accuracy values