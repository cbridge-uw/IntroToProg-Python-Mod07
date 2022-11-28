Corbin Bridge
<br>November 30, 2022
<br>IT FDN 110 A Au 22
<br>Assignment07

# Python Pickling and Error Handling

## Introduction
The following document will introduce the reader to pickling and structured error handling in Python. Both concepts will be explained and then introduced in the script in the form of a learning module.

## Creating the Script
Creating this script presents a unique challenge as compared to prior assignments. This project provides me with the creative freedom to introduce picking and structured error handling however I elect. I have decided to create a program that will teach the user about these concepts and provide some working examples.

### Initial Setup
The initial setup follows the pattern of prior assignments. I created a new sub-folder in the _PythonClass folder and added a new knowledge word document (Figure 1).

Next, I created a new project in PyCharm (Figure 2) and added the Assignment07 Python file (Figure 3).

### Code Organization
The code for Assignment07 is organized into data, processing, I/O and main sections. This follows the format introduced by Professor Root in recent assignments. Personally, I like this format as the code looks more organized and professional.

The script will make use of several functions that are created in the processing and I/O sections. The main part of the script will bring all the functions together to run the program.

The script begins with a welcome message to the user contained in the welcome_user() function (Figure 4).

An options menu is presented at the start of the script and each time a lesson module ends. The user can elect to learn about pickling, error handling, or exit the program. The menu is contained in the main_menu() function (Figure 5).

Finally, the main menu is followed by the user_menu_selection() function that requests an input from the user. If the user enters an option that is not valid, they are provided an error message and are asked to try again (Figure 6).

### Pickling

I elected to first address pickling. I wanted the lesson module to be something fun and interactive for the user.

The pickling lesson begins with a simple print statement describing what pickling is, why it is used, and a warning on storing sensitive data in a pickled file. This introduction makes use of the pickling_lesson() function (Figure 7). Note that I am only providing an image of the function docstring to save room. The balance of the function is simply a print and return statement.

With the text out of the way the pickling lesson becomes interactive. My objective is to ask the user for a piece of data, save it to a pickled list, ask the user to view the list so they see a pickled file, and then to finally return the un-pickled list.

First, I request the name of a hero from the user and append this name to an existing list that is declared in the Data section of the script (Figure 8). This code is contained in the main section of the script and is executed when the user selection is 1 (pickling).

Next, the script will call the pickling_write_example() function passing both the file_name that is found as the pickle_file variable in the Data section and the list of names (Figure 9).

With the data written to the file the program pauses and asks the user to find and open the newly created Heros.txt filen. Upon doing so, the user will see a row of pickled data that they will not be able to fully understand.

I created two functions, pickle_write_prompt() and pickle_read_prompt(), that provide the user with some guidance on what is happening with the data when it is being written to and read from the pickle file (Figure 10).

Finally, the pickling_read_example() function is called that un-pickles the file and returns a human-readable list to the user (Figure 11).

At this point the pickling lesson module ends and the user is presented with the main menu. The full code for the pickling lesson is found in the main script section (Figure 12).

#### Pickling Research
As part of Assignment07 I conducted independent research into pickling. I found three resources that were particularly useful.

First was an article from RealPython https://realpython.com/python-pickle-module/ (External Site accessed 2022.11.25). While a bit lengthy, I really enjoyed how this article examined the pickle module and did not simply describe what pickling does. The code examples were also very helpful.

Next, I found the article at Tutorials Point https://www.tutorialspoint.com/python-pickling (External Site accessed 2022.11.25) to be a quick and easy to understand resource. The examples they provided pickling lists helped as I used this approach in my script.

Finally, a seven-minute YouTube video https://youtu.be/Pl4Hp8qwwes (External Site accessed 2022.11.27) allowed me to hear and see someone else demonstrate pickling. This video helped me to understand some of the benefits of pickling and why it is used.

### Error Handling
The error handling lesson module was designed to introduce the user to a few common errors, how to handle them using try/except, and how to create a custom error. Like pickling, several functions were created for this lesson.

The full code in the main section for error handling is shown below (Figure 13).

The user is first presented with some text on error handling in Python, why errors occur, and why it is helpful to provide users with custom messages. This is packaged in the error_handling_lesson() function (Figure 14).

#### Zero Division Error
The first error examined is the zero-division error. This example requires two integer inputs from the user where the second is a 0 (Figure 15). These inputs are requested via the zero_division_error_inputs() function.

The results from the zero_division_error_inputs() function are then passed to the zero_division_error() function (Figure 16).

When the zero_division_error function runs it takes in the two user provided integers. Using try/except, the function will fail when the user provides 0 as the second number. This is where the except block will prevent Python from returning a system error. Instead, a custom message is returned along with the code that Python would have presented. This allows the user to quickly see the benefit of a custom message as opposed to the system error code (Figure 17).

#### File Not Found Error
The next error examined is the file not found error.

First, I collect the name of a file from the user using the file_not_found_error_input() function (Figure 18).

The result, file_name, is then passed to the file_not_found_error() function. This function attempts to open a file and return any data within the file. Unfortunately, this file does not yet exist. Rather then returning a system error, the code demonstrates how a custom message can be returned. The elements of the Python error message are also returned so the user can see how Python addresses the error (Figure 19).

#### Custom Error
Finally, I wanted to show the user how they could create their own custom error.

Sticking with the hero theme from the pickling lesson, a hero name is requested using the custom_error_inputs() function (Figure 20) and is passed to the custom_error() function.

The hero name is passed to the custom_error() function where a custom error is raised if the user entered an incorrect response (Figure 21).

As I have done with the other error handling examples, the Python system error message is also presented so the user is able to compare the custom versus system language.

The final section of the main script allows the user to exit the program when they enter option 3 (Figure 22).

#### Error Handling Research
While researching error handling I came across a few helpful resources.

The first was an article by GeeksforGeeks https://www.geeksforgeeks.org/python-exception-handling/ (External Site accessed 2022.11.25). What was most helpful was the numerous code examples in the article showing both the code and output.

I also found an article on GUI Commits https://guicommits.com/how-to-structure-exception-in-python-like-a-pro/ (External Site accessed 2022.11.26). The code examples were helpful and I particularly liked the flowchart at the start of the article.

Finally, I found a YouTube video by Microsoft Developer https://youtu.be/HQqqNBZosn8 (External site accessed 2022.11.26) that provided an informative introduction to error handling. The video was easy to understand and did a good job explaining syntax, logic, and runtime errors.

### Testing the Code
With both the pickling and error handling lesson modules completed I tested in PyCharm and the command prompt.

#### PyCharm
First, I started the program (Figure 23).

I selected 1 to learn about pickling first and enter a name when prompted to do so (Figure 24).

As instructed, I find and open the newly created and pickled Heros.txt file (Figure 25).

I continue with the program and finally see the full, un-pickled list (Figure 26).

Next, I ran the error handling module (Figure 27).

The zero-division error is addressed first and works as expected (Figure 28).

Next up is the file not found error (Figure 29).

Finally, the custom error is demonstrated (Figure 30).

Once the custom error completes, I am returned to the main menu and exit the program (Figure 31).

#### OS Command Prompt
I next tested the script in the OS Command Prompt. The welcome message and pickling modules ran first (Figure 32).

Next, the error handling lesson runs. I navigate through the zero division error and file not found error (Figure 33).

I conclude the test with the custom error and exiting the program (Figure 34).

## Summary
Assignment07 provided an opportunity to research pickling and error handling in Python. The coding task was presented as open-ended, so several options existed. The approach of teaching someone else about these topics was helpful for me. Making the lessons interactive for the user will hopefully provide a fun and educational experience.
