# --------------------------------------- #
# Title: Pickling and Error Handling in Python
# Desc: Introduce the user to the concepts of pickling and error handling
# in Python in the form of a learning module.
# ChangeLog (Who, When, What)
# CBridge,2022.11.27,Added pickling code
# CBridge,2022.11.28,Added error handling code
# --------------------------------------- #

# IMPORTS ---------------------------------#
import pickle   # import the pickle module

# DATA ---------------------------------#
# declare variables
pickle_file = "Heros.txt"
lst_Heros = ["Spock", "Kirk"]


# PROCESSING ---------------------------#
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


def pickling_read_example(file_name):
    '''
    Provides an example of unpickling data.
    :param file_name:
    :return:
    '''

    with open(file_name, "rb") as file:     # opens the file and reads data
        content = pickle.load(file)         # loads data from the file and assigns to content variable
        return content


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
        a = print("\nYou cannot divide by zero. Python would tell you the following:\n")
        b = print(e)
        c = print(type(e))
        d = print(e.__doc__)
        e = print(e.__str__())
        return a, b, c, d, e


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
        a = print("\n\'The file does not exist\' is much nicer than Python's error:\n")
        b = print(e)
        c = print(type(e))
        d = print(e.__doc__)
        e = print(e.__str__())
        return a, b, c, d, e


def custom_error(hero_name):
    '''
    Demonstrate creation of a custom error message
    :param hero_name: (string) a name
    :return: (string) A custom error message
    '''

    try:
        if hero_name.lower() in ("nero", "kruge", "khan"):
            raise Exception("Really?! They are not a hero!")
    except Exception as e:
        a = print("A custom error was raised.")
        b = print(e)
        c = print(type(e))
        d = print("\nWhile you may disagree, with a custom error the developer sets the rules.")
        return a, b, c, d


# PRESENTATION (I/O) -------------------#
def welcome_user():
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


def main_menu():
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


def pickling_lesson():
    '''
    Describes pickling to the user.
    :return: (string) lesson
    '''

    lesson = print('''
    Pickling isn't just a fun word to say, it's also a handy Python module used to serialize and de-serialize data.
    Wait? Pickles and serial! Starting to sound like an odd breakfast, so let's take a deeper look.
    
    Serializing data is the process of taking Python objects (lists, dictionaries, etc.) and turning them into 0s and 1s.
    De-serializing is simply the opposite of serializing.
    
    Why Pickle? Pickling allows us to transfer and store data and can be lighter than text files.
    
    WARNING: Pickling makes data mostly unreadable, but it is not 100% anonymous. Don't store your bank details in a pickle file!
    
    Now, time for an example...
    ''')

    return lesson


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


def error_handling_lesson():
    '''
    Describe error handling to the user.
    :return: (string) lesson
    '''

    lesson = input('''
    Errors happen when writing code. Sometimes it's a quick syntax error and a missing colon resolves the issue.\n
    Other times a more frustrating logic error is to blame. Ever mixed up the > and < signs by accident?\n
    When errors occur Python attempts to provide some assistance in the form of error messages.\n
    For developers, these can be very useful.\n
    However, the average user is only going to be confused and frustarted when they see \"ValueError: invalid literal \
for int()\".\n
    In this module we'll review some common errors that a user might generate and how you, the developer, can handle
    these in advance to fail gracefully and preserve a positive user experience.
    
    Enter to continue...''')

    return lesson


def zero_division_error_inputs():
    '''
    Collect user input as int for the zero_division_error function
    :return: (int) number1, number2
    '''

    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number (HINT: it should be 0): "))
    return number1, number2


def file_not_found_error_input():
    '''
    Collect user input as string for the file_not_found_error function
    :return:
    '''

    file_name = str(input("\nEnter a file name (i.e., SomeName.txt): ")).strip()
    return file_name


def custom_error_inputs():
    '''
    Collect user input as string for the custom_error function
    :return: (string) name
    '''

    print("\nHINT: the answer likely consists of Khan, Nero, or Kruge")
    hero_name = str(input("\nEnter the name of a hero: ")).strip().lower()
    return hero_name


# MAIN ---------------------------------#
welcome_user()

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
    elif str_choice == "3":     # exit program
        print("Thanks for learning about pickling and error handling. Happy Python-ing!")
        break
