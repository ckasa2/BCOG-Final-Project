# BCOG-Final-Project

1.  This project will be based on the Stroop Task. The stroop task is a psychological test used to measure attention and processing speed. Users will be shown color words like "red" or "blue" which will be displayed in matching or mismatched font colors. The user must identify the color of the text, not the word itself. This code should measure the user's response times and accuracy across multiple trials to analyze their cognitive interference and automatic responses.
2.
  - This would require using a random module to generate trials with randomized color and word pairings. This would allow pairs like the word red in blue font or the word pink in green font.
  -  It would also require the code to measure how long the user took to respond by measuring the tiime before the user presses a button. 
  - Finally, it would need to take this data and calculate a summary with statistics like average reaction time(for congruent vs. incongruent trials), and their overall accuracy to display their performance. 

Introduction and Purpose: 
This program simulates the stroop task, which is an experiment that can be used to measure cognitive and executive function by measuring the effects of conflicting signals on reaction time. When the meaning of the word shown and its color are congruent, it is easy to recognize the color of the word. However, when the word and color are incongruent, it creates a conflict in word- recognition and color-recognition. This conflict causes extra processing time for the brain.
This task can help researchers, teachers, and students explore attention, processing speed, and cognitive control. This can be used in research to study cognitive processes. It can also be used in clinical settings to evaluate cognitive functions in individuals who may have ADHD, anxiety, dementia, or brain injury.  

Example use case: 
The stroop effect can be used to indicate attention fatigue or the decreased ability to process conflicting information, which is associated with ADHD. In a clinical setting, a psychiatrist or therapist could use this test to measure these symptoms of ADHD.

Functions:
run_stroop_test()
- launches the gui

show_stimuli()
- creates list of words with their assigned colors

show_stimulus(word,color)
- displays one stimulus on the screen

log_data()
- records the reaction time

save_to_csv()
- saves the test data to a csv file


Data format for results:

trial_number 
- number of trial
- integer

word
- text shown
- string

font_color
- color of the text
- string

correct_response
- expected key pressed
- string

user_response
- actual key pressed
- string

reaction_time
- time before key pressed(in seconds)
- float




Progress Report #3



Concept:The concept is an interactive desktop Stroop‑test that logs reaction time and accuracy to CSV. It follows the prompt and is not simple. (1/1)


File Structure: have src/, results/, readme, and stroop_test files. They all have reasonable names, and the repository conforms to kebab case. (1/1)

Project Description: There is a description of the project in the readme file. (2/2)

Approach: The program uses modules like tkinter for gui, csv, os, time, and a random trial fenerator.(2/4)

Project Code: The code has approopriate variable types, and is organized into functions and classes. It includes 3 original functions(log_trial, save_csv, run_stroop-test). However, I ran into an error uploading data to results file(2/6)

Code style: I used descriptive names, followed naming conventions, used blank lines to seperate elements and logic. (2/2)

Code tests: I included code tests in the test folder that can be used to test if the code executes and that expected outputs are returned. (1/2_)












