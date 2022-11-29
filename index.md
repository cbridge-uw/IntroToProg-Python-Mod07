Corbin Bridge
<br>November 28, 2022
<br>IT FDN 110 A Au 22
<br>Assignment07

# Python Pickling and Error Handling

## Introduction
The following document will introduce the reader to pickling and structured error handling in Python. Both concepts will be explained and then introduced in the script in the form of a learning module.

## Creating the Script
Creating this script presents a unique challenge as compared to prior assignments. This project provides me with the creative freedom to introduce picking and structured error handling however I elect. I have decided to create a program that will teach the user about these concepts and provide some working examples.

### Initial Setup
The initial setup follows the pattern of prior assignments. I created a new sub-folder in the _PythonClass folder and added a new knowledge word document (Figure 1).

![Figure 1](./images/Figure%201.png "Figure 1")

<sub>***Figure 1: Creating the new sub-folder and knowledge document.***</sub>

Next, I created a new project in PyCharm (Figure 2) and added the Assignment07 Python file (Figure 3).

![Figure 2](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%202.png "Figure 2")

<sub>***Figure 2: Creating a PyCharm project.***</sub>

![Figure 3](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%203.png "Figure 3")

<sub>***Figure 3: Adding the Assignment07 Python file.***</sub>

### Code Organization
The code for Assignment07 is organized into data, processing, I/O and main sections. This follows the format introduced by Professor Root in recent assignments. Personally, I like this format as the code looks more organized and professional.

The script will make use of several functions that are created in the processing and I/O sections. The main part of the script will bring all the functions together to run the program.

The script begins with a welcome message to the user contained in the welcome_user() function (Figure 4).
```
def welcome_user():                                 # welcome message. no user interaction expected
    '''
    Welcome user and brief explanation of program.
    :return: (string) message
    '''

    message = print(
        '''
        =======================================================================
        \t\tWelcome to the Pickling and Error Handling Tutorial!\n
        \tIn this module you will be introduced to the concepts of
        \tpickling and error handling in Python.
        \n\t\t\t\t\t\t\t\tEnjoy your adventure!
        =======================================================================
        '''
    )
    return message
```
<sub>***Figure 4: The welcome_user() function.***</sub>

An options menu is presented at the start of the script and each time a lesson module ends. The user can elect to learn about pickling, error handling, or exit the program. The menu is contained in the main_menu() function (Figure 5).

```
def main_menu():            # options menu to navigate the script
    '''
    Display menu options to the user.
    :return: nothing
    '''

    print('''
    Options Menu
    1 - Pickling
    2 - Error Handling
    3 - Exit
    ''')
```
<sub>***Figure 5: The main_menu() function.***</sub>

Finally, the main menu is followed by the user_menu_selection() function that requests an input from the user. If the user enters an option that is not valid, they are provided an error message and are asked to try again (Figure 6).

```
def user_menu_selection():
    '''
    Gets menu selection from user.
    :return: (string) selection
    '''

    while True:
        selection = str(input("What would you like to learn about? ")).strip()      # get user input
        if selection in ("1", "2", "3"):        # check if user input is a valid menu option
            return selection
        else:       # Require user to select a valid option
            print(f"{selection} is not a valid option (use 1-3).\n")
```
<sub>***Figure 6: The user_menu_selection() function.***</sub>

### Pickling

I elected to first address pickling. I wanted the lesson module to be something fun and interactive for the user.

The pickling lesson begins with a simple print statement describing what pickling is, why it is used, and a warning on storing sensitive data in a pickled file. This introduction makes use of the pickling_lesson() function (Figure 7). Note that I am only providing an image of the function docstring to save room. The balance of the function is simply a print and return statement.

```
def pickling_lesson():
    '''
    Describes pickling to the user.
    :return: (string) lesson
    '''
```
<sub>***Figure 7: The pickling_lesson() function.***</sub>

With the text out of the way the pickling lesson becomes interactive. My objective is to ask the user for a piece of data, save it to a pickled list, ask the user to view the list so they see a pickled file, and then to finally return the un-pickled list.

First, I request the name of a hero from the user and append this name to an existing list that is declared in the Data section of the script (Figure 8). This code is contained in the main section of the script and is executed when the user selection is 1 (pickling).

```
    if str_choice == "1":       # run pickling lesson
        pickling_lesson()       # explain pickling
        strHeroName = str(input("Enter the name of a hero: ")).strip()
        lst_Heros.append(strHeroName.title())
```
<sub>***Figure 8: Getting user input for the pickling lesson.***</sub>

Next, the script will call the pickling_write_example() function passing both the file_name that is found as the pickle_file variable in the Data section and the list of names (Figure 9).

```
def pickling_write_example(file_name, list_of_heros):
    '''
    Provides an example of pickling data.
    :param file_name:
    :param list_of_heros:
    :return: (string) message
    '''

    with open(file_name, "wb") as file:     # opens the file and writes data
        pickle.dump(list_of_heros, file)    # file.close() omitted. WITH() closes file automatically
    message = print("Data written to file!")
    return message
```

<sub>***Figure 9: The pickling_write_example() function.***</sub>

With the data written to the file the program pauses and asks the user to find and open the newly created Heros.txt filen. Upon doing so, the user will see a row of pickled data that they will not be able to fully understand.

I created two functions, pickle_write_prompt() and pickle_read_prompt(), that provide the user with some guidance on what is happening with the data when it is being written to and read from the pickle file (Figure 10).

```
def pickle_write_prompt():
    '''
    Pause lesson so user can view newly created file to view pickling output
    :return:
    '''

    print("\nFind the Heros.txt file that was just created. Open it and see if you can read it.")
    pickle_continue = input("Enter to continue...")
    return pickle_continue


def pickle_read_prompt():
    '''
    Explains unpickling process.
    :return:
    '''

    print("\nI'm guessing that pickled file wasn't too easy to read. Sure, you could make out some of the data but \
not everything.")
    pickle_continue = input("\nLet's get out of this pickle and read the data. Enter to continue...")
    return pickle_continue
```
<sub>***Figure 10: The pickle_write_prompt() and pickle_read_prompt() functions.***</sub>

Finally, the pickling_read_example() function is called that un-pickles the file and returns a human-readable list to the user (Figure 11).

```
def pickling_read_example(file_name):
    '''
    Provides an example of unpickling data.
    :param file_name:
    :return:
    '''

    with open(file_name, "rb") as file:     # opens the file and reads data
        content = pickle.load(file)         # loads data from the file and assigns to content variable
        return content
```
<sub>***Figure 11: The pickling_read_example() function.***</sub>

At this point the pickling lesson module ends and the user is presented with the main menu. The full code for the pickling lesson is found in the main script section (Figure 12).

```
while True:
    main_menu()
    str_choice = user_menu_selection()
    if str_choice == "1":       # run pickling lesson
        pickling_lesson()       # explain pickling
        strHeroName = str(input("Enter the name of a hero: ")).strip()
        lst_Heros.append(strHeroName.title())
        pickling_write_example(file_name=pickle_file, list_of_heros=lst_Heros)      # pickle write example
        pickle_write_prompt()
        pickle_read_prompt()
        pickle_data = pickling_read_example(file_name=pickle_file)      # pickle read example
        print("\nThe unpickled list is: ", str(pickle_data))            # print unpickled list
```
<sub>***Figure 12: The pickling lesson code.***</sub>

#### Pickling Research
As part of Assignment07 I conducted independent research into pickling. I found three resources that were particularly useful.

First was an article from RealPython https://realpython.com/python-pickle-module/ (External Site accessed 2022.11.25). While a bit lengthy, I really enjoyed how this article examined the pickle module and did not simply describe what pickling does. The code examples were also very helpful.

Next, I found the article at Tutorials Point https://www.tutorialspoint.com/python-pickling (External Site accessed 2022.11.25) to be a quick and easy to understand resource. The examples they provided pickling lists helped as I used this approach in my script.

Finally, a seven-minute YouTube video https://youtu.be/Pl4Hp8qwwes (External Site accessed 2022.11.27) allowed me to hear and see someone else demonstrate pickling. This video helped me to understand some of the benefits of pickling and why it is used.

### Error Handling
The error handling lesson module was designed to introduce the user to a few common errors, how to handle them using try/except, and how to create a custom error. Like pickling, several functions were created for this lesson.

The full code in the main section for error handling is shown below (Figure 13).

```
    elif str_choice == "2":     # run error handling lesson
        error_handling_lesson()     # run error handling lesson
        print("\nThe Zero Division Error\n")        # Zero Division Error example
        number1, number2 = zero_division_error_inputs()
        zero_division_error(number1=number1, number2=number2)
        input("\nPress enter to see what happens when you attempt to open a file that does not exist...")
        print("\nThe File Not Found Error")             # File not Found example
        file_name = file_not_found_error_input()
        file_not_found_error(file_name=file_name)
        input("\nHow about creating your very own, custom error? Press enter to see it in action...")
        print("\nThe Custom Error")
        hero_name = custom_error_inputs()           # Custom Error example
        custom_error(hero_name=hero_name)
```
<sub>***Figure 13: The error handling lesson code.***</sub>

The user is first presented with some text on error handling in Python, why errors occur, and why it is helpful to provide users with custom messages. This is packaged in the error_handling_lesson() function (Figure 14).

```
def error_handling_lesson():
    '''
    Describe error handling to the user.
    :return: (string) lesson
    '''
```
<sub>***Figure 14: The error_handling_lesson() function.***</sub>

#### Zero Division Error
The first error examined is the zero-division error. This example requires two integer inputs from the user where the second is a 0 (Figure 15). These inputs are requested via the zero_division_error_inputs() function.

```
def zero_division_error_inputs():
    '''
    Collect user input as int for the zero_division_error function
    :return: (int) number1, number2
    '''

    number1 = int(input("Enter a number: "))                            # request number from user and make int
    number2 = int(input("Enter a number (HINT: it should be 0): "))     # request number from user and make int
    return number1, number2
```
<sub>***Figure 15: The zero_division_error_inputs() function.***</sub>

The results from the zero_division_error_inputs() function are then passed to the zero_division_error() function (Figure 16).

```
number1, number2 = zero_division_error_inputs()
zero_division_error(number1=number1, number2=number2)
```
<sub>***Figure 16: Passing values to the zero_division_error() function.***</sub>

When the zero_division_error function runs it takes in the two user provided integers. Using try/except, the function will fail when the user provides 0 as the second number. This is where the except block will prevent Python from returning a system error. Instead, a custom message is returned along with the code that Python would have presented. This allows the user to quickly see the benefit of a custom message as opposed to the system error code (Figure 17).

```
def zero_division_error(number1, number2):
    '''
    Demonstrates error handling when attempting to divide by zero.
    :param number1: (int) a number
    :param number2: (int) a second number
    :return: (string) A custom and the standard Python error message
    '''

    try:
        quotient = number1 / number2
        return quotient
    except Exception as e:
        a = print("\nYou cannot divide by zero. Python would tell you the following:\n")    # provide custom message
        b = print(e)
        c = print(type(e))
        d = print(e.__doc__)
        e = print(e.__str__())
        return a, b, c, d, e
```
<sub>***Figure 17: The zero_division_error() function.***</sub>

#### File Not Found Error
The next error examined is the file not found error.

First, I collect the name of a file from the user using the file_not_found_error_input() function (Figure 18).

```
def file_not_found_error_input():
    '''
    Collect user input as string for the file_not_found_error function
    :return:
    '''

    file_name = str(input("\nEnter a file name (i.e., SomeName.txt): ")).strip()  # request file name and make string
    return file_name
```
<sub>***Figure 18: The file_not_found_error_input() function.***</sub>

The result, file_name, is then passed to the file_not_found_error() function. This function attempts to open a file and return any data within the file. Unfortunately, this file does not yet exist. Rather then returning a system error, the code demonstrates how a custom message can be returned. The elements of the Python error message are also returned so the user can see how Python addresses the error (Figure 19).

```
def file_not_found_error(file_name):
    '''
    Demonstrate error handling when attempting to open a non-existing file.
    :return: (string) A custom and the standard Python error message
    '''

    try:
        file = open(file_name, "r")
        for i in file:
            return i
    except Exception as e:
        a = print("\n\'The file does not exist\' is much nicer than Python's error:\n")     # provide custom message
        b = print(e)
        c = print(type(e))
        d = print(e.__doc__)
        e = print(e.__str__())
        return a, b, c, d, e
```
<sub>***Figure 19: The file_not_found_error() function.***</sub>

#### Custom Error
Finally, I wanted to show the user how they could create their own custom error.

Sticking with the hero theme from the pickling lesson, a hero name is requested using the custom_error_inputs() function (Figure 20) and is passed to the custom_error() function.

```
def custom_error_inputs():
    '''
    Collect user input as string for the custom_error function
    :return: (string) name
    '''

    print("\nHINT: the answer likely consists of Khan, Nero, or Kruge")
    hero_name = str(input("\nEnter the name of a hero: ")).strip().lower()  # request user input and make string
    return hero_name
```
<sub>***Figure 20: The custom_error_inputs() function.***</sub>

The hero name is passed to the custom_error() function where a custom error is raised if the user entered an incorrect response (Figure 21).

```
def custom_error(hero_name):
    '''
    Demonstrate creation of a custom error message
    :param hero_name: (string) a name
    :return: (string) A custom error message
    '''

    try:
        if hero_name.lower() in ("nero", "kruge", "khan"):      # test for custom error condition
            raise Exception("Really?! They are not a hero!")    # raise Exception if error found
    except Exception as e:
        a = print("A custom error was raised.")
        b = print(e)
        c = print(type(e))
        d = print("\nWhile you may disagree, with a custom error the developer sets the rules.")
```
<sub>***Figure 21: The custom_error() function.***</sub>

As I have done with the other error handling examples, the Python system error message is also presented so the user is able to compare the custom versus system language.

The final section of the main script allows the user to exit the program when they enter option 3 (Figure 22).

```
    elif str_choice == "3":     # exit program
        print("Thanks for learning about pickling and error handling. Happy Python-ing!")
        break
```
<sub>***Figure 22: Exiting the program.***</sub>

#### Error Handling Research
While researching error handling I came across a few helpful resources.

The first was an article by GeeksforGeeks https://www.geeksforgeeks.org/python-exception-handling/ (External Site accessed 2022.11.25). What was most helpful was the numerous code examples in the article showing both the code and output.

I also found an article on GUI Commits https://guicommits.com/how-to-structure-exception-in-python-like-a-pro/ (External Site accessed 2022.11.26). The code examples were helpful and I particularly liked the flowchart at the start of the article.

Finally, I found a YouTube video by Microsoft Developer https://youtu.be/HQqqNBZosn8 (External site accessed 2022.11.26) that provided an informative introduction to error handling. The video was easy to understand and did a good job explaining syntax, logic, and runtime errors.

### Testing the Code
With both the pickling and error handling lesson modules completed I tested in PyCharm and the command prompt.

#### PyCharm
First, I started the program (Figure 23).

![Figure 23](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2023.png "Figure 23")

<sub>***Figure 23: Starting the program.***</sub>

I selected 1 to learn about pickling first and enter a name when prompted to do so (Figure 24).

![Figure 24](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2024.png "Figure 24")

<sub>***Figure 24: Running the pickling lesson.***</sub>

As instructed, I find and open the newly created and pickled Heros.txt file (Figure 25).

![Figure 25](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2025.png "Figure 25")

<sub>***Figure 25: The pickled Heros.txt file.***</sub>

I continue with the program and finally see the full, un-pickled list (Figure 26).

![Figure 26](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2026.png "Figure 26")

<sub>***Figure 26: The un-pickled Heros.txt file.***</sub>

Next, I ran the error handling module (Figure 27).

![Figure 27](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2027.png "Figure 27")

<sub>***Figure 27: Starting the error handling lesson.***</sub>

The zero-division error is addressed first and works as expected (Figure 28).

![Figure 28](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2028.png "Figure 28")

<sub>***Figure 28: The Zero Division Error.***</sub>

Next up is the file not found error (Figure 29).

![Figure 29](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2029.png "Figure 29")

<sub>***Figure 29: The File Not Found Error.***</sub>

Finally, the custom error is demonstrated (Figure 30).

![Figure 30](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2030.png "Figure 30")

<sub>***Figure 30: The Custom Error.***</sub>

Once the custom error completes, I am returned to the main menu and exit the program (Figure 31).

![Figure 31](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2031.png "Figure 31")

<sub>***Figure 31: Exiting the program.***</sub>

#### OS Command Prompt
I next tested the script in the OS Command Prompt. The welcome message and pickling modules ran first (Figure 32).

![Figure 32](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2032.png "Figure 32")

<sub>***Figure 32: Welcome and Pickling lesson in the command prompt.***</sub>

Next, the error handling lesson runs. I navigate through the zero division error and file not found error (Figure 33).

![Figure 33](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2033.png "Figure 33")

<sub>***Figure 33: Zero Division Error and File Not Found Error.***</sub>

I conclude the test with the custom error and exiting the program (Figure 34).

![Figure 34](https://github.com/cbridge-uw/IntroToProg-Python-Mod07/blob/main/images/Figure%2034.png "Figure 34")

<sub>***Figure 34: Custom Error and exiting the program.***</sub>

## GitHub
We continue to use GitHub to save our Python scripts for this assignment. As was done in prior assignments, I created a new repository and initialized with a README file (Figure 35).

<sub>***Figure 35: Creating a new GitHub repository.***</sub>

With the repository created I added my Python script file as well as the pickled text file (Figure 36).

<sub>***Figure 36: Committing Assignment07.py and Heros.txt.***</sub>

### GitHub Webpage
I added a GitHub webpage once the new Assignment07 repository was created. This was accomplished by navigating to Settings > Pages and selecting the branch to build from (Figure 37).

<sub>***Figure 37: Adding a GitHub webpage.***</sub>

With the webpage created I added an index.md file to the repository. To this file I added all the text from this knowledge document (Figure 38).

<sub>***Figure 38: Index.md in GitHub.***</sub>

In the main section of the repository, I created a folder called images. To add the images from the knowledge document to the GitHub webpage I will need to save the images somewhere. This folder will be my central location for all Assignment07 images (Figure 39).

<sub>***Figure 39: Creating the images folder on GitHub.***</sub>

Finally, I added the images to the GitHub webpage. In the index.md file I added the necessary code with syntax ![Alt Text](image URL “tool tip text”) that would render all the necessary images (Figure 40).

<sub>***Figure 40: Adding images to a GitHub webpage.***</sub>

Where I elected to enter code and not an image I needed to surround the code with three tick marks (``` ```) so that it would show properly (Figure 41).

<sub>***Figure 41: Adding code snippets to a GitHub webpage.***</sub>

## Summary
Assignment07 provided an opportunity to research pickling and error handling in Python. The coding task was presented as open-ended, so several options existed. The approach of teaching someone else about these topics was helpful for me. Making the lessons interactive for the user will hopefully provide a fun and educational experience.
