#! python
# Creator-> Aditya Nayak
# This is Bookrek, a record-keeper of the books I read and certain other info about them
version = "1.0"

# Imports
from calendar import isleap
from datetime import date  # For date-related stuff, today's date is needed
import os  # for checking paths and similar stuff
import shelve  # for saving data
from random import choice  # for having some fun
from platform import system

# Fuctions
def yesNoConfirmation(inputQuestion):
    """
    This function will be used in yes/no confirmations that are required quite frequently in this program
    Args:
    inputQuestion- Give the yes/no question you want to ask.
    Returns:
    True/False. True for 'yes' and False for 'no'.
    """

    noOfTimesDumbUserGotItWrong = 0
    while True:
        yesOrNo = input(inputQuestion + " [y/n] ").lower()
        if (
            yesOrNo == "y"
            or yesOrNo == "yes"
            or yesOrNo == "ye"
            or yesOrNo == "yep"
            or yesOrNo == "yeah"
            or yesOrNo == "aye"
            or yesOrNo == "yup"
            or yesOrNo == "continue"
            or yesOrNo == "haan"
            or yesOrNo == "han"
            or yesOrNo == "hn"
        ):
            return True
        elif (
            yesOrNo == "no"
            or yesOrNo == "n"
            or yesOrNo == "nope"
            or yesOrNo == "nay"
            or yesOrNo == "nah"
            or yesOrNo == "back"
            or yesOrNo == "cancel"
            or yesOrNo == "na"
            or yesOrNo == "naa"
        ):
            return False
        else:
            noOfTimesDumbUserGotItWrong += 1
            if (
                noOfTimesDumbUserGotItWrong > 5
            ):  # user is given 5 chances in total. if he still gets it wrong, then he's lesser than an orangutan
                print(
                    "Too many invalid inputs! Assuming user's reply to be 'no' by default..."
                )
                return False
            print("Invalid input. Please enter either 'yes' or 'no'.")


def viewBookList():
    "This function will enable the user to view the book list whenever she/he wants."

    # Variables
    booknameLimit = 36  # technically it is 36 + 4, i.e. the 4 letters of "name"
    authornameLimit = 24  # technically it is 24 + 6, i.e. the 6 letters of "author"
    suitable_gap_bw_headings = (
        4  # a suitable gap between each heading; put it in variable for easier handling
    )
    
    print("\nYOUR BOOK LIST\n")
    print(
        "Sl. No.  "
        + "Name"
        + booknameLimit * " "
        + suitable_gap_bw_headings * " "
        + "Author"
        + authornameLimit * " "
        + suitable_gap_bw_headings * " "
        + "Progress "
        + suitable_gap_bw_headings * " "
        + "Score "
    )  # Score will be out of 10, with decimal up to one place allowed
    # NOTE: remember that there is a space in "Progress ". The space has been added to make it a 9-character string to match dddd/dddd for page numbers
    # limit 9 as in dddd/dddd, considering that a book will have a maximum of 4-digit page numbers
    bookList = shelve.open("booklist")
    bookListLength = len(list(bookList.keys()))  # length of the book list
    if bookListLength == 0:
        print(
            "\n\nLooks like your booklist is empty right now. Add some books right now by typing 'addnew'.\n"
        )
    else:
        for i in range(bookListLength):
            sl_no = str(i + 1).rjust(
                5, "0"
            )  # setting up the string for the serial number. NOTE: it's been given 5 digits in total, expecting the user to read 99,999 books at most
            bookData = bookList["book"+str(sl_no)]  # This will put the required values as a list in the variable bookData
            bookName = bookData[0]
            bookAuthor = bookData[1]
            bookProgress = bookData[2] + "/" + bookData[3]
            if bookData[4] != "0":
                bookScore = bookData[4] + "/10"
            else:
                bookScore = "---"
            if len(bookName) > booknameLimit + 4:
                bookName = (
                    bookName[0 : booknameLimit + 1] + "..."
                )  # if the bookname is too long, then we just shorten it and display it with "..." at the end
            if len(bookAuthor) > authornameLimit + 6:
                bookAuthor = (
                    bookAuthor[0 : authornameLimit + 3] + "..."
                )  # if the author's name is too long, then we shorten it and display it with "..." at the end
            print(
                sl_no.ljust(9)
                + bookName.ljust(booknameLimit + 4 + suitable_gap_bw_headings)
                + bookAuthor.ljust(authornameLimit + 6 + suitable_gap_bw_headings)
                + bookProgress
                + suitable_gap_bw_headings * " "
                + bookScore.center(6)
            )
    bookList.close()  # closing an opened shelf is important
    print("\nIf some data is found missing, please type in 'booklist troubleshoot' or 'bl tb' for short into the main_command.")

    # NOTE: the books' data is to be saved as lists in the bookList shelf.


def addNewBook():
    "This function will help to add a new book to the book list of the user."

    bookList = shelve.open("booklist")
    bookslno = len(list(bookList.keys())) + 1  # getting the current length of the booklist
    # bookslno is the book's serial number. it will be used to save it as Book001, Book002, etc. for easy identification
    # this is important to check in every function.
    # If we check it once at first and reuse the values then we can't keep track of the changes made by the user.
    bookList.close()

    print("\n>>> ADD NEW BOOK <<<\n")
    print("[NOTE: This is your last chance to turn back.]")
    randomyesnovariable = yesNoConfirmation(
        "You have chosen to add a new book to your book list. Do you wish to proceed?"
    )
    if not randomyesnovariable:
        # the user doesn't wish to continue
        print(
            "Returning to main command input..."
        )  # this line is not needed, just added it for elegance
    else:
        # this means that the user chose "yes", so continue with the function

        # Book's name:-
        while True:
            bookname = input("Enter the book's NAME.\n>>> ")
            bookname = bookname.strip()
            randomvariablethatiwillprobablyneveruseagainthereforeimadeitsofuckinglong = yesNoConfirmation(
                "You entered the book's name as: "
                + bookname
                + "\nDo you want to proceed?"
            )
            if randomvariablethatiwillprobablyneveruseagainthereforeimadeitsofuckinglong:
                break  # This means the user confirmed that it is correct, so break the while loop
            else:
                # This means that the user got it wrong and wishes to re-enter it. So just print a consolation message
                print("No worries. Try to type the correct one this time.")

        # Author's name:-
        i_just_want_to_know_a_setting = shelve.open("progvar")
        autoTitle = i_just_want_to_know_a_setting["autoTitle"]
        i_just_want_to_know_a_setting.close()
        while True:
            authorname = input("Enter the AUTHOR's name.\n>>> ")
            authorname = authorname.strip()
            if autoTitle: authorname = authorname.title()
            if not authorname.isalpha():
                randomlistofcharactersthatilikedinsomebooksandmovies = [
                    "Sirius Black",
                    "Harry Potter",                 # Special Mention: Really likeable characters from epic novels
                    "Hermione Granger",
                    "Ron Weasley",
                    "Neville Longbottom",
                    "Jack Sparrow",
                    "Napoleon Bonaparte",
                    "Mohandas Karamchand Gandhi",
                    "Albus Percival Wolfric Brian Dumbledore",
                    "Naruto Uzumaki",
                    "Sasuke Uchiha",
                    "Light Yagami",
                    "Kanda Sorata",
                    "Carolus Linnaes",
                    "Harris Sinclair",
                    "Liesel Meminger",              # Special Mention: Really likeable characters from epic novels
                    "Rudy Steiner",                 # Special Mention: Really likeable characters from epic novels
                    "Cadence Sinclair Eastman",     # Special Mention: Really likeable characters from epic novels
                    "Aditya Nayak"  # my name is important after all :P
                ]
                print("Please enter the name of the author using alphabets only. For example: "+choice(randomlistofcharactersthatilikedinsomebooksandmovies))  # No real reason to add it, just for fun
            else:
                anotherrandomvariableiwillneveruseagainsoimadeitlooong = (
                    yesNoConfirmation(
                        "You entered the author's name as: "
                        + authorname
                        + "\nDo you want to proceed?"
                    )
                )
                if anotherrandomvariableiwillneveruseagainsoimadeitlooong:
                    break  # This means that the user confirmed that it is correct, so proceed on to the next item
                else:
                    print("No problem. Do it right this time.")  # User got it wrong so ask again

        # Total no. of pages in the book
        while True:
            totalpagesinbook = input("Enter the TOTAL NUMBER OF PAGES in the book: ")
            # I am not sure if isdecimal() rejects in-string whitespaces or not, so I'll remove them myself just in case
            totalpagesinbook = totalpagesinbook.replace(" ", "")

            if not totalpagesinbook.isdecimal():  # The user entered a non-decimal value, which is obviously not what we are asking for here
                print("Please enter only an integral value for the total number of pages in the book. (Use the digits 0123456789 only)")

            # Actually, the isdecimal() function doesn't accept negative values, so the below block of code wouldn't have been needed
            # but isdecimal() does accept 0, which we don't want. So I'm leaving the below code as it is.
            elif (
                int(totalpagesinbook) <= 0
            ):  # Book's total page number can't be zero or negative
                print("Book's total page number can't be less than 1.")
            else:
                break

        # No. of pages read by user
        while True:
            noOfPagesReadByUser = input("Enter the NUMBER OF PAGES READ BY YOU: ")
            noOfPagesReadByUser = noOfPagesReadByUser.replace(" ", "")  # removing whitespaces just in case

            if not noOfPagesReadByUser.isdecimal():  # The user entered a non-decimal value
                print("Please enter only an integral value for the number of pages read by you. (Use the digits 0123456789 only)")

            # The below lines are commented out because I think they are not needed. isdecimal() probably doesn't take negative values
            # elif (
            #     int(noOfPagesReadByUser) < 0
            # ):  # here we use <0 and not <=0 because it is fine if user has read zero pages
            #     print(
            #         "Number of pages read by you can't be negative. Please enter a positive integral value."
            #     )

            elif int(noOfPagesReadByUser) > int(
                totalpagesinbook
            ):  # Which means that it is invalid
                print(
                    "Number of pages read by you can't exceed the total number of pages in the book. Enter it again."
                )
            else:
                break

        # Status of the book
        if int(noOfPagesReadByUser) == int(totalpagesinbook):
            bookStatus = 0  # 0 = completed
        elif int(noOfPagesReadByUser) == 0:
            bookStatus = 4  # 4 = plan to read
        else:
            bookStatus = 1  # 1 = Currently reading
            # Assume it to be 1 for now, at the end the user has the option to change it before finalization and storage

        # Score of the book (on a scale of 1 to 10)
        while True:
            scoreOfBook = input(
                "On a scale of 1 to 10, what score would you give the book? "
            )
            if not scoreOfBook in [
                "0",
                "1",
                "1.5",
                "2",
                "2.5",
                "3",
                "3.5",
                "4",
                "4.5",
                "5",
                "5.5",
                "6",
                "6.5",
                "7",
                "7.5",
                "8",
                "8.5",
                "9",
                "9.5",
                "10",
            ]:  # This could have been written in a better and more generalised way, but for the scale of 1 to 10, this is the shortest way I know
                print(
                    "Please rate it on a scale of 1 to 10 only. If you don't wish to rate it yet, enter 0."
                )
                print(
                    'NOTE: Decimal numbers like 1.5, 2.5, etc. are allowed, but only the ".5" decimals. Decimals like "1.1", "1.2", etc. are not allowed.'
                )
            else:
                break

        todays_date = date.today()  # Date object of today's date
        # Start date of reading the book
        print("\nSTART DATE ENTRY")
        if yesNoConfirmation("Would you like to enter a start date? (Otherwise would be left as 'none'.)"):
            while True:
                startYear = input("Please enter the year you started reading the book (YYYY) : ")
                if not startYear.isdecimal(): print("Please enter a valid numeric value.")
                elif len(startYear) != 4: print("Please enter the year in the correct format (YYYY).")
                elif int(startYear) < 1900: print("How low a value are you entering? Were you even born then? Enter a realistic value.")
                elif int(startYear) > todays_date.year: print("Who started reading it, your future self? Enter a value within "+str(todays_date.year)+".")
                else: break # All conditions clear, user entered a completely valid & practical input

            veryrandomerrorcountinthemiddleofnowherethatijustinsertedbecauseiwassuperbored = 0
            while True:
                startMonth = input("Please enter the month you started reading the book (MM) : ").lower()
                startMonth = startMonth.strip().lstrip("0")  # first strip whitespace characters then strip the leading zeroes

                # then we convert all the different kinds of valid inputs into a single format: MM
                if startMonth == "1" or startMonth == "jan" or startMonth == "january":
                    startMonth = "01"
                elif startMonth == "2" or startMonth == "feb" or startMonth == "february":
                    startMonth = "02"
                elif startMonth == "3" or startMonth == "mar" or startMonth == "march":
                    startMonth = "03"
                elif startMonth == "4" or startMonth == "apr" or startMonth == "april":
                    startMonth = "04"
                elif startMonth == "5" or startMonth == "may":
                    startMonth = "05"
                elif startMonth == "6" or startMonth == "jun" or startMonth == "june":
                    startMonth = "06"
                elif startMonth == "7" or startMonth == "jul" or startMonth == "july":
                    startMonth = "07"
                elif startMonth == "8" or startMonth == "aug" or startMonth == "august":
                    startMonth = "08"
                elif startMonth == "9" or startMonth == "sep" or startMonth == "september":
                    startMonth = "09"
                elif startMonth == "10" or startMonth == "oct" or startMonth == "october":
                    startMonth = "10"
                elif startMonth == "11" or startMonth == "nov" or startMonth == "november":
                    startMonth = "11"
                elif startMonth == "12" or startMonth == "dec" or startMonth == "december":
                    startMonth = "12"

                else:
                    print("Invalid value. Please enter the month in the MM format.")
                    continue

                # then we compare

                # if the start year is less than the current year
                if int(startYear) < todays_date.year:
                    # then all is fine as it is, no need to judge the value's validity. so we just break the while loop
                    break
                else:  # That means it is the current year and hence we need to judge what month the user enters
                    if int(startMonth) > todays_date.month:
                        veryrandomerrorcountinthemiddleofnowherethatijustinsertedbecauseiwassuperbored += 1
                        if veryrandomerrorcountinthemiddleofnowherethatijustinsertedbecauseiwassuperbored < 5:
                            # then the month entered by the user hasn't even arrived yet, so we "politely" inform him of this, once.
                            print("That month hasn't even arrived this year ○_○ Enter a valid number, please.")
                        else:
                            # well if the user is acting so dumb that calling him/her a human would be a shame to humanity,
                            # then guess we gotta show them that we ain't messing around here
                            print("Now, just pound it already into that thick skull of yours that we don't accept a read start date that hasn't even arrived yet (in this human world, at least).")
                            veryrandomerrorcountinthemiddleofnowherethatijustinsertedbecauseiwassuperbored = 0  # well one insult per 5 mistakes should be enough, no reason to shame him further
                    else: break # the month is all good now, so we can move on to the date

            while True:
                startDate = input("Please enter the date you started reading this book (DD) : ").strip().lstrip("0")
                # with this, all whitespaces and all leading zeroes have been removed

                normalDaysInMonths = (31,28,31,30,31,30,31,31,30,31,30,31)

                leapDaysInMonths = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

                if not startDate.isdecimal(): print("Please enter a decimal value only.")
                elif len(startDate) > 2 or int(startDate) > 31: print("Maximum value of input is 31.")
                elif int(startDate) == 0:
                    print("Well a month starts from its first day. I don't think I've ever seen one start with its zero'th day.")
                    print("Please enter a valid date.")
                elif int(startYear) == todays_date.year and int(startMonth) == todays_date.month:
                    if int(startDate) > todays_date.day:
                        # The user entered a date from the future
                        print("What's up with your future self suddenly deciding to read a book?")
                        print("Enter a date that has not yet passed.")
                    else:
                        # All good
                        # Set it up in a good format
                        startDate = startDate.rjust(2, "0")
                        break
                else:

                    # First we decide if the start year is a leap year.
                    isLeapYear = isleap(int(startYear))

                    # Next, for leap years:-
                    if isLeapYear:
                        if int(startDate) > leapDaysInMonths[int(startMonth) - 1]:
                            # The user has typed an impossible date.
                            print("The said month only has "+str(leapDaysInMonths[int(startMonth) - 1])+" at most. Please enter a valid date.")
                        else:
                            # All good
                            startDate = startDate.rjust(2, "0")  # setting it up in a good format
                            break
                    else:
                        if int(startDate) > normalDaysInMonths[int(startMonth) - 1]:
                            # The user has typed an impossible date.
                            print("The said month only has "+str(normalDaysInMonths[int(startMonth) - 1])+" at most. Please enter a valid date.")
                        else:
                            # All good
                            startDate = startDate.rjust(2, "0")  # setting it up in a good format
                            break
                        # Completion of start date part. Now just compile it to make a start date.
            finalStartDate = startDate + "/" + startMonth + "/" + startYear

        else:
            finalStartDate = ("----------")   # NOTE- DD/MM/YYYY all replaced by "-" character.

        # END DATE
        print("\nEND DATE ENTRY")
        if not yesNoConfirmation("Are you sure you want to proceed with entering the end date? (Note- otherwise will be saved as NONE)"):
            finalEndDate = ("----------")  # NOTE- DD/MM/YYYY all replaced by "-" character.

        else:
            while True:
                endYear = input("Please enter the year you finished reading the book (YYYY) : ")
                if not endYear.isdecimal():
                    print("Please enter a valid numeric value.")
                elif len(endYear) != 4:
                    print("Please enter the year in the correct format (YYYY).")
                elif int(endYear) < 1900:
                    print(
                        "How low a value are you entering? Were you even born then? Enter a realistic value."
                    )
                elif int(endYear) > todays_date.year:
                    print("Who finished reading it, your future self? Enter a value within "+str(todays_date.year)+".")
                else: break   # All conditions clear, user entered a completely valid & practical input

            andherewegowithanothergoddamnlongvariablenamejustforsomeeastereggs = 0  # tbh, i was simply bored
            while True:
                endMonth = input("Please enter the month you ended reading the book (MM) : ").lower()
                endMonth = endMonth.strip().lstrip("0")  # first strip whitespace characters then strip the leading zeroes

                # then we convert all the different kinds of valid inputs into a single format: MM
                if endMonth == "1" or endMonth == "jan" or endMonth == "january":
                    endMonth = "01"
                elif endMonth == "2" or endMonth == "feb" or endMonth == "february":
                    endMonth = "02"
                elif endMonth == "3" or endMonth == "mar" or endMonth == "march":
                    endMonth = "03"
                elif endMonth == "4" or endMonth == "apr" or endMonth == "april":
                    endMonth = "04"
                elif endMonth == "5" or endMonth == "may":
                    endMonth = "05"
                elif endMonth == "6" or endMonth == "jun" or endMonth == "june":
                    endMonth = "06"
                elif endMonth == "7" or endMonth == "jul" or endMonth == "july":
                    endMonth = "07"
                elif endMonth == "8" or endMonth == "aug" or endMonth == "august":
                    endMonth = "08"
                elif endMonth == "9" or endMonth == "sep" or endMonth == "september":
                    endMonth = "09"
                elif endMonth == "10" or endMonth == "oct" or endMonth == "october":
                    endMonth = "10"
                elif endMonth == "11" or endMonth == "nov" or endMonth == "november":
                    endMonth = "11"
                elif endMonth == "12" or endMonth == "dec" or endMonth == "december":
                    endMonth = "12"

                else:
                    print("Invalid value. Please enter the month in the MM format.")
                    continue

                # then we compare

                # if the start year is less than the current year
                if int(endYear) < todays_date.year:
                    # then all is fine as it is, no need to judge the value's validity. so we just break the while loop
                    break

                else:  # if it is the current year, then we need to judge if the month entered is valid or not
                    if int(endMonth) > todays_date.month:
                        andherewegowithanothergoddamnlongvariablenamejustforsomeeastereggs += 1
                        if andherewegowithanothergoddamnlongvariablenamejustforsomeeastereggs < 5:
                            # politely inform the user
                            print("The month you entered is not valid, as it hasn't even arrived yet. Please enter a valid date.")
                        else:
                            # DUMB USER DETECTED. AVAILABLE SOLUTIONS: INSULT
                            print("Ayo dumbass user! When will you learn to enter it right? I told you, THAT MONTH HASN'T ARRIVED YET.")
                            andherewegowithanothergoddamnlongvariablenamejustforsomeeastereggs = 0  # 1-insult-per-5-mistakes-rule
                    else: break # All good. moving on to next stage

            while True:  # end date
                endDate = input("Please enter the date you ended reading this book (DD) : ").strip().lstrip("0")    # with this, all whitespaces and all leading zeroes have been removed

                normalDaysInMonths = (31,28,31,30,31,30,31,31,30,31,30,31)

                leapDaysInMonths = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

                if not endDate.isdecimal(): print("Please enter a decimal value only.")
                elif len(endDate) > 2 or int(endDate) > 31: print("Maximum value of input is 31.")
                elif int(endDate) == 0:
                    print("Well a month starts from its first day. I don't think I've ever seen one start with its zero'th day.")
                    print("Please enter a valid date.")
                elif int(endYear) == todays_date.year and int(endMonth) == todays_date.month:
                    if int(endDate) > todays_date.day:
                        # The user entered a date from the future
                        print("How do you know that you'll be completing the book on that date? You some kind of quack fortune-teller or something?")
                        print("Enter a date that has not yet passed.")
                    else:
                        # All good
                        # Set it up in a good format
                        endDate = endDate.rjust(2, "0")
                        break
                else:

                    # First we decide if the start year is a leap year.
                    isLeapYear = isleap(int(endYear))

                    # Next, for leap years:-
                    if isLeapYear:
                        if int(endDate) > leapDaysInMonths[int(endMonth) - 1]:
                            # The user has typed an impossible date.
                            print("The said month only has "+str(leapDaysInMonths[int(endMonth) - 1])+" at most. Please enter a valid date."
                            )
                        else:
                            # All good
                            endDate = endDate.rjust(2, "0")  # setting it up in a good format
                            break
                    else:
                        if int(endDate) > normalDaysInMonths[int(endMonth) - 1]:
                            # The user has typed an impossible date.
                            print("The said month only has "+str(normalDaysInMonths[int(endMonth) - 1])+" at most. Please enter a valid date.")
                        else:
                            # All good
                            endDate = endDate.rjust(2, "0")  # setting it up in a good format
                            break
                # Completion of end date part

            finalEndDate = endDate + "/" + endMonth + "/" + endYear  # DD/MM/YYYY ftw
            # Finally done with end Date

        # NO. OF TIMES BOOK RE-READ
        while True:
            print("\n(NOTE- The question below does not include the first time you read it.)")
            noOfTimesReRead = input("Enter the number of times you have re-read the book: ")
            if noOfTimesReRead.lower() == "none" or noOfTimesReRead.lower() == "never" or noOfTimesReRead.lower() == "no": noOfTimesReRead = "0"
            elif not noOfTimesReRead.isdecimal(): print("Please enter a valid numerical value")
            else:
                # Just a few tricks
                if int(noOfTimesReRead) > 1729:
                    print("You sure read it more than a couple of times, eh? ")
                elif int(noOfTimesReRead) == "69" or int(noOfTimesReRead) == "420":
                    print("Hmmm... interesting number!")
                break  # Number entered is alright, let's move on

        # GENRE
        print("GENRE")
        print("If you don't wanna enter a genre (leaving the field blank), type 'none' or simply press enter.")
        print("Whatever else you enter will be treated as the name of a genre.")
        genreName = input("Enter genre of the book: ").title()
        if genreName == "None" or genreName == "No" or genreName == "Cancel" or genreName == "":
            genreName = "---"
        # otherwise the name will remain the same, so move on

        # PUBLISHER
        print("PUBLISHER")
        print("If you don't wanna enter the name of the publisher, press enter or type 'none'.")
        print("Anything else you type will be treated as the name of the publisher and will be saved thus.")
        publisherName = input("Enter the name of the publisher: ")
        if publisherName.lower() == "none" or publisherName.lower() == "no" or publisherName.lower() == "cancel" or publisherName.lower() == "":
            publisherName = "---"
        # Otherwise it will remain the same, so all done here

        # PERSONAL REVIEW
        print("PERSONAL REVIEW")
        if yesNoConfirmation("Do you wish to enter a personal review on the book?"):
            print("NOTE: Type it out in one straight paragraph; the moment you press enter the entry will be saved.\n")
            personalReview = input("Enter you personal review here: \n")
        else:
            personalReview = "---"
        
        # Finally, the detail-collection phase is over. Now compile all of them into a single entry to be saved.
        newBook = shelve.open(os.path.join(".", "bookdata", "book"+str(bookslno).rjust(5, "0")))
        newBook["bookName"] = bookname
        newBook["authorName"] = authorname
        newBook["pagesTotal"] = totalpagesinbook
        newBook["pagesRead"] = noOfPagesReadByUser
        newBook["status"] = bookStatus
        newBook["score"] = scoreOfBook
        newBook["startDate"] = finalStartDate
        newBook["endDate"] = finalEndDate
        newBook["rereadTimes"] = noOfTimesReRead
        newBook["genre"] = genreName
        newBook["publisher"] = publisherName
        newBook["personalReview"] = personalReview
        # Added all of the details to the required shelve file
        newBook.close()

        # Now adding a few of the details to the bookList:-
        bookList = shelve.open("booklist")
        bookList["book"+str(bookslno).rjust(5, "0")] = [bookname, authorname, noOfPagesReadByUser, totalpagesinbook, scoreOfBook]
        bookList.close()
        """
        Remember:
        1. bookname
        2. authorname
        3. no of pages read by user
        4. total no of pages
        5. score of the book

        This is the order in which all books are to be saved in booklist so that viewBookList can read it properly.
        """
        # Done with this function, now just display a successfully done message.
        print("\nSUCCESSFULLY SAVED ENTRY\n")
        print("Details of the entry:")
        printBookDetails(str(bookslno))

        # Finally done with addNewBook!!! ^_^


def printBookDetails(slno: str):
    "This function will simply print the details of a book whose serial number is provided to it."

    slno = slno.rjust(5, "0")
    print("Book #"+slno)
    requiredBook = shelve.open(os.path.join(".", "bookdata", "book"+slno))
    print("Name of book -> "+requiredBook["bookName"])
    print("Name of author -> "+requiredBook["authorName"])
    print("Number of pages read = "+requiredBook["pagesRead"]+"/"+requiredBook["pagesTotal"])
    bookStatus = requiredBook["status"]
    if bookStatus == 0: bookStatus = "completed"
    elif bookStatus == 1: bookStatus = "currently reading"
    elif bookStatus == 2: bookStatus = "on-hold"
    elif bookStatus == 3: bookStatus = "dropped"
    elif bookStatus == 4: bookStatus = "plan to read"
    print("Status of book: "+bookStatus)
    print("Score of the book: "+requiredBook["score"]+"/10")
    print("Date on which started reading -> "+requiredBook["startDate"])
    print("Date on which ended reading -> "+requiredBook["endDate"])
    print("No. of times reread book = "+requiredBook["rereadTimes"])
    print("Genre of book -> "+requiredBook["genre"])
    print("Publisher of book -> "+requiredBook["publisher"])
    print("Personal Review on the book:")
    print(requiredBook["personalReview"])
    print("---------------------------------------------------------\n")
    requiredBook.close()    # That's all there was to print.


def viewBookDetails():
    "This function enables users to view the saved details of the books stored in the bookdata folder as shelf files."
    
    booklistshelf = shelve.open("booklist")
    bookListLength = len(list(booklistshelf.keys()))
    booklistshelf.close()
    if bookListLength == 0 and len(os.listdir("bookdata")) != 0:
        print("Booklist found corrupted. Auto-initiating booklist troubleshooter...")
        troubleshooter(True)    # This will avoid a certain bug
    
    if yesNoConfirmation("Do you want to view the Booklist again?"):
        viewBookList()

    slno = ""

    print("The book that you want to view/edit the details of, how do you want to identify it?")
    print("[slno/bookname/authorname]")
    print("(Choose only one from the aforementioned.)")

    while True:
        wayOfBookIdentification = input(">>> ").lower()
        if not wayOfBookIdentification in ["slno", "bookname", "authorname"]:
            # that means that the input is incorrect
            print("Invalid method entered. Please enter one of the accepted values only: 'slno', 'bookname', or 'authorname'.")
            print("Re-enter a correct input.")
        else:
            if yesNoConfirmation("You have chosen '"+wayOfBookIdentification+"'. Do you wish to proceed?"):
                # proceed
                break
            else:
                # don't proceed. back to start.
                print("No worries there. Enter it again.")
    
    print("VIEWING OF BOOK DETAILS")
    print("Method chosen: "+wayOfBookIdentification+"\n")

    if wayOfBookIdentification == "slno":
        # this means that we gotta display the data of "book"+(slno)'s data

        booklist = shelve.open("booklist")
        bookListLength = len(list(booklist.keys()))
        booklist.close()    # close it. not required anymore.

        while True:
            slno = input("Enter the serial number of the book: ")
            if not slno.isdecimal():
                print("Invalid input. Only decimal values accepted.")
            else:
                if 0 < int(slno) <= bookListLength:
                    break
                else:
                    print("Invalid range. Please enter a value from 1 to "+str(bookListLength)+" only")
                    print("Because there are "+str(bookListLength)+" entries only.")
        
        # now just use the printBookDetails function to get the work done
        printBookDetails(slno)  # and that's it!

    elif wayOfBookIdentification == "bookname":
        # gotta make a kind of search system mini-version
        booklistshelf = shelve.open("booklist")
        bookSlNos = []  # Declaring the empty slno. list
        bookNames = []  # Declaring the corresponding empty bookname list
        for i in list(booklistshelf.keys()):
            bookSlNos.append(i.removeprefix("book"))
            bookNames.append(booklistshelf[i][0])
            # This should prepare the necessary lists properly
        booklistshelf.close()   # No more work for the shelf file. everything further is to be handled by lists
        bookNamesLowercase = []
        for book in bookNames:
            bookNamesLowercase.append(book.lower())    # Creating a lowercase name list
        
        # input
        while True:
            possibleBooks = []
            print("For help regarding using this function, type 'b!help'.")
            reqBookName = input("Enter the name of the book that you wish to read: ").lower()
            
            if reqBookName == "b!help":
                print("""\nHOW TO USE THIS FUNCTION\n
Type in the full book name or a few of the most distinguishing words in the name of the book to identify one book only.
Each of your inputs will be put through our search function and all the possible books you found will be listed.
You need not enter the full name of the book always. In case of unique book names, entering just that particular unique
word usually suffices.
For example, to find a book titled "The Adventures of Harris Moorshlew the Gold-axe Swinger", only typing in unique words
and names like 'Harris Moorshlew' or 'Gold-axe Swinger' will suffice in most cases. On the other hand, keying in common
phrases like 'the adventures' will not work. In such cases, instead of identifying one single book, the program will list
out all the book-names that it could find which contain the entered phrase.
[NOTE: The book used in the above-given example does not exist.]
The search feature is not case-sensitive. Enter the book-name anyway you like.""")  # A help feature
            else:
                for i in bookNamesLowercase:
                    if reqBookName in i:
                        possibleBooks.append(i)
                if len(possibleBooks) == 1:
                    # book found
                    break
                else:
                    print("No. of search results found = "+str(len(possibleBooks)))
                    for i in possibleBooks:
                        print(bookNames[bookNamesLowercase.index(i)])   # This will print it in proper CaSiNg
                    print("Choose which book you'd like to read and enter its name again.")
            
        # Now we are sure that there is only 1 book in the possibleBooks list
        # so just printing its details directly:-
        print("Displaying the details of the requested book...\n")
        slno = bookSlNos[bookNamesLowercase.index(possibleBooks[0])]
        printBookDetails(slno) # That should suffice

    elif wayOfBookIdentification == "authorname":
        booklistshelf = shelve.open("booklist")
        # Empty list declaration
        authorNames = []
        for i in list(booklistshelf.keys()):
            authorNames.append(booklistshelf[i][1])
            # This should be enough to prepare the necessary lists
        authorNamesLowercase = []
        for author in authorNames:
            authorNamesLowercase.append(author.lower()) # Creating a lowercase name list
        
        # input
        while True:
            possibleAuthors = []
            print("For help regarding using this function, type 'b!help'.")
            reqAuthorName = input("Enter the name of the author whose book you wish to read: ").lower()
            
            if reqAuthorName == "b!help":
                print("""\nHOW TO USE THIS FUNCTION\n
Type in the full author name or a few of the most distinguishing words in the name of the author to identify one author only.
Each of your inputs will be put through our search function and all the possible authors you found will be listed.
You need not enter the full name of the author always. In case of unique author names, entering just that particular unique
word usually suffices.
For example, to find an author named "Harry Asdfg Zxcvbn", only typing in unique words like 'Asdfg' or 'Zxcvbn' will suffice
in most cases. On the other hand, keying in common names like 'Harry' will not work. In such cases, instead of identifying a
single author, the program will list out all the author-names that it could find which contain the entered phrase.
[NOTE: The author used in the above-given example is only fictional and hence does not exist.]
The search feature is not case-sensitive. Enter the author-name anyway you like.""")  # A help feature
            else:
                for i in authorNamesLowercase:
                    if reqAuthorName in i:
                        possibleAuthors.append(i)
                if len(possibleAuthors) == 1:
                    # book found
                    break
                else:
                    print("No. of search results found = "+str(len(possibleAuthors)))
                    for i in possibleAuthors:
                        print(authorNames[authorNamesLowercase.index(i)])   # This will print it in proper CaSiNg
                    print("Choose whose book you'd like to read and enter his/her name again.")
        
        # Now we are sure that there is only 1 author's name in possibleAuthors
        bookSlNos = []
        possibleBooks = []
        for i in list(booklistshelf.keys()):
            if booklistshelf[i][1].lower() == possibleAuthors[0]:
                bookSlNos.append(i.removeprefix("book"))
                possibleBooks.append(booklistshelf[i][0])
        booklistshelf.close()

        if len(possibleBooks) == 1:
            # All set!
            print("Found 1 book written by the required author. Printing its details...")
            slno = bookSlNos[0]
            printBookDetails(slno)
        else:
            print("Found "+str(len(possibleBooks))+" written by the required author. They are- ")
            for book in possibleBooks:
                print(book)
            while True:
                searchResults = []
                reqBook = input("Enter the name of the book you want to read: ").lower()
                if reqBook == "b!help":
                    print("""\nHOW TO USE THIS FUNCTION\n
The rules are the same as before.
In addition, you can instead choose to select the book faster by keying in the position it occupies in the list
in the format 'b!<position>'.
For example, if your search results contain 5 books, and look like this-

Why Bookrek Is The Best App Out There
How To Read Books
The Adventures of Harris Moorshlew the Gold-axe Swinger
Normalcy Guide: Common Sense for Those Who Ain't Got It
The Blah Blah Blah Book

And suppose you wish to read 'The Blah Blah Blah Book', then just count what position from the top it occupies in the list.
Here we find that it is 5th in the list so to read its details, we can either type in 'The Blah Blah Blah Book' or simply key
in 'b!5'.""")
                elif reqBook.startswith("b!") and reqBook.removeprefix("b!").isdecimal:
                    reqBook = reqBook.removeprefix("b!")
                    if 0 < int(reqBook) <= (len(possibleBooks)):
                        print("Printing the required book's details...")
                        slno = bookSlNos[int(reqBook)-1]
                        printBookDetails(slno)
                        break
                    else:
                        print("Invalid input.")
                        print("Please enter a non-zero integral input that is not more than "+str(len(possibleBooks))+", which is the total number of books in the list.")
                else:
                    for i in possibleBooks:
                        if reqBook in i.lower():
                            searchResults.append(i)
                    if len(searchResults) == 1:
                        # Book found
                        print("Printing book's details...")
                        slno = bookSlNos[possibleBooks.index(searchResults[0])]
                        printBookDetails(slno)
                        break
                    else:
                        print(str(len(searchResults))+" search results were found for this input.")
                        for wewereliarsisaverygoodbook in searchResults:
                            print(wewereliarsisaverygoodbook)
                        print("Please enter a keyword that will enable us to identify a particular book.")  # That should be enough
    if yesNoConfirmation("Do you wish to edit any details?"):
        editBookDetails(slno)
    else: print("Alright. Redirecting to main_command...")


def editBookDetails(slno : str):
    "This function will be used to edit the details of a book."
    
    slno = slno.rjust(5, "0")
    print("\nEDIT BOOK DETAILS\n")
    print("Editing Book#"+slno)
    print("Details available to edit:-")
    print("Details"+" "*8+" "*4+"Keyword")  # Details limit = 7+8=15, Space = 4
    available_details = ["Book's name", "Author's name", "Pages read", "Total pages", "Status", "Score", "Start Date", "End Date", "Reread toll", "Genre", "Publisher", "Personal Review"]
    available_commands = ["bookname/bn", "authorname/an", "pagesread/prd", "pagestotal/pt", "status/sts", "score", "start", "end", "reread", "genre", "publisher/pb", "review/rv"]
    for i in range(len(available_details)):
        if len(available_details[i])>15: print(available_details[i][:11]+"..."+" "*4+available_commands[i])
        else: print(available_details[i]+" "*(15-len(available_details[i]))+" "*4+available_commands[i])

    # now to make the input
    while True:
        print("Key in 'b!back' to go cancel.")
        detailToChange = input("Enter the detail you wish to change: ").lower()
        if (
            detailToChange in ["b!back", "b!cancel"]
            or (detailToChange in ["bookname", "bn", "authorname", "an", "pagesread", "prd", "pagestotal", "pt", "status", "sts", "start", "end", "reread", "genre", "publisher", "pb", "review", "rv"])
            or (("b!" in detailToChange) and detailToChange.removeprefix("b!").isdecimal() and 0<int(detailToChange.removeprefix("b!"))<=len(available_details))
        ): break
        else: print("Please enter a valid input according to the command list shown above.")
    newInput = ""
    bookShelf = shelve.open(os.path.join(".", "bookdata", "book"+slno))
    if detailToChange == "bookname" or detailToChange == "bn" or detailToChange == "b!"+str(available_details.index("Book's name")+1):
        detailToChange = "bookname" # Req for the booklist updater
        print("Current bookname = "+bookShelf["bookName"])
        print("Caution: Anything you enter right now will be considered to be the new name of the book.")
        while True:
            newInput = input("Enter new bookname: ")
            if yesNoConfirmation("You have entered the bookname as "+newInput+"\nDo you wish to continue?"):
                bookShelf["bookName"] = newInput
                print("Book name updated successfully.")
                break
            else: print("No worries. Enter it again.")
    elif detailToChange == "authorname" or detailToChange == "an" or detailToChange == "b!"+str(available_details.index("Author's name")+1):
        detailToChange = "authorname"
        print("Current authorname = "+bookShelf["authorName"])
        print("Caution: Anything you enter right now will be considered to be the new name of the author.")
        while True:
            newInput = input("Enter new authorname: ")
            if yesNoConfirmation("You have entered the authorname as "+newInput+"\nDo you wish to continue?"):
                bookShelf["authorName"] = newInput
                print("Author's name updated successfully.")
                break
            else: print("No worries. Enter it again.")
    elif detailToChange == "pagesread" or detailToChange == "prd" or detailToChange == "b!"+str(available_details.index("Pages read")+1):
        detailToChange = "pagesread"
        print("Currently number of pages read = "+bookShelf["pagesRead"])
        print("Caution: Anything you enter right now will be considered to be the new number of pages read.")
        while True:
            newInput = input("Enter new number of pages read: ")
            if not (newInput.isdecimal() and 0<=int(newInput)<=int(bookShelf["pagesTotal"])):
                print("Input invalid. Please enter an integral value in range "+bookShelf["pagesTotal"]+" which is the total number of pages in the book.")
            else:
                if yesNoConfirmation("You have entered the no. of pages read as "+newInput+"\nDo you wish to continue?"):
                    bookShelf["pagesRead"] = newInput
                    print("No. of pages read updated successfully.")
                    if int(newInput) == int(bookShelf["pagesTotal"]): bookShelf["status"] = 0   # Set the status to "completed"
                    break
                else: print("No worries. Enter it again.")
    elif detailToChange == "pagestotal" or detailToChange == "pt" or detailToChange == "b!"+str(available_details.index("Total pages")+1):
        detailToChange = "pagestotal"
        print("Currently total number of pages in the book = "+bookShelf["pagesTotal"])
        print("Caution: Anything you enter right now will be considered to be the new total number of pages in the book.")
        while True:
            newInput = input("Enter new total number of pages in the book: ")
            if not (newInput.isdecimal() and 0<int(newInput) and int(newInput)>=bookShelf["pagesRead"]):
                print("Input invalid. Please enter an integral value not less than the number of pages read.")
            else:
                if yesNoConfirmation("You have entered the total number of pages in the book as "+newInput+"\nDo you wish to continue?"):
                    bookShelf["pagesTotal"] = newInput
                    print("Total number of pages in the book updated successfully.")
                    break
                else: print("No worries. Enter it again.")
    elif detailToChange == "status" or detailToChange == "sts" or detailToChange == "b!"+str(available_details.index("Status")+1):
        bookStatus = bookShelf["status"]
        if bookStatus == 0: bookStatus = "completed"
        elif bookStatus == 1: bookStatus = "currently reading"
        elif bookStatus == 2: bookStatus = "on-hold"
        elif bookStatus == 3: bookStatus = "dropped"
        elif bookStatus == 4: bookStatus = "plan to read"
        print("Current status = "+bookStatus)
        print("Caution: Anything you enter right now will be considered to be the new status of reading of the book.")
        print("List of available inputs:")
        for _ in ["completed (cmpl)", "currently reading (cr)", "on-hold (onh)", "dropped (drop)", "plan to read (ptr)"]:
            print(_)    # just printing a list in vertical format
        while True:
            newInput = input("Enter the new status of reading of the book: ").lower()
            if newInput == "completed" or newInput == "cmpl":
                if yesNoConfirmation("Change book status to completed?"):
                    bookShelf["status"] = 0
                    break
                else: print("No worries. Enter it again.")
            elif newInput == "currently reading" or newInput == "cr":
                if yesNoConfirmation("Change book status to currently watching?"):
                    bookShelf["status"] = 1
                    break
                else: print("No worries. Enter it again.")
            elif newInput == "on-hold" or newInput == "on hold" or newInput == "onhold" or newInput == "onh":
                if yesNoConfirmation("Change book status to on-hold?"):
                    bookShelf["status"] = 2
                    break
                else: print("No worries. Enter it again.")
            elif newInput == "dropped" or newInput == "drop":
                if yesNoConfirmation("Change book status to dropped?"):
                    bookShelf["status"] = 3
                    break
                else: print("No worries. Enter it again.")
            elif newInput == "plan to read" or newInput == "ptr":
                if yesNoConfirmation("Change book status to plan to read?"):
                    bookShelf["status"] = 4
                    break
                else: print("No worries. Enter it again.")
            else: print("Invalid input. Please enter only a valid input from the list displayed above.")
        print("Book status successfully updated.")
    elif detailToChange == "score" or detailToChange == "b!"+str(available_details.index("Score")+1):
        detailToChange = "score"
        print("Current score: "+bookShelf["score"]+"/10")
        print("Please enter a value from 1 to 10 as the new score of the book.")
        print("You can only enter decimal values that are multiples of 0.5, such as 3.5, 6.5, etc. (excluding 0.5)")
        print("Other decimals such as 4.2, 6.9, etc. won't be accepted.")
        while True:
            newInput = input("Enter the new score of the book: ")
            if newInput in ['0', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10']:
                if yesNoConfirmation("You entered the new score of the book as "+newInput+"\nDo you wish to continue?"):
                    bookShelf["score"] = newInput
                    print("Book score successfully updated.")
                    break
                else: print("No worries. Enter it again.")
            else: print("Invalid input. Please enter a decimal value from 1 to 10 that is a multiple of 0.5 only.")
    elif detailToChange == "start" or detailToChange == "b!"+str(available_details.index("Start Date")+1):
        print("Current start date = "+bookShelf["startDate"])
        print("Initiating start_date_change function...")
        todays_date = date.today()  # Date object of today's date
        print("\nSTART DATE RE-ENTRY")
        if yesNoConfirmation("Would you like to enter a start date? (Otherwise would be left as 'none'.)"):
            while True:
                startYear = input("Please enter the year you started reading the book (YYYY) : ")
                if not startYear.isdecimal(): print("Please enter a valid numeric value.")
                elif len(startYear) != 4: print("Please enter the year in the correct format (YYYY).")
                elif int(startYear) < 1900: print("How low a value are you entering? Were you even born then? Enter a realistic value.")
                elif int(startYear) > todays_date.year: print("Who started reading it, your future self? Enter a value within "+str(todays_date.year)+".")
                else: break # All conditions clear, user entered a completely valid & practical input

            veryrandomerrorcountinthemiddleofnowherethatijustinsertedbecauseiwassuperbored = 0
            while True:
                startMonth = input("Please enter the month you started reading the book (MM) : ").lower()
                startMonth = startMonth.strip().lstrip("0")  # first strip whitespace characters then strip the leading zeroes

                # then we convert all the different kinds of valid inputs into a single format: MM
                if startMonth == "1" or startMonth == "jan" or startMonth == "january":
                    startMonth = "01"
                elif startMonth == "2" or startMonth == "feb" or startMonth == "february":
                    startMonth = "02"
                elif startMonth == "3" or startMonth == "mar" or startMonth == "march":
                    startMonth = "03"
                elif startMonth == "4" or startMonth == "apr" or startMonth == "april":
                    startMonth = "04"
                elif startMonth == "5" or startMonth == "may":
                    startMonth = "05"
                elif startMonth == "6" or startMonth == "jun" or startMonth == "june":
                    startMonth = "06"
                elif startMonth == "7" or startMonth == "jul" or startMonth == "july":
                    startMonth = "07"
                elif startMonth == "8" or startMonth == "aug" or startMonth == "august":
                    startMonth = "08"
                elif startMonth == "9" or startMonth == "sep" or startMonth == "september":
                    startMonth = "09"
                elif startMonth == "10" or startMonth == "oct" or startMonth == "october":
                    startMonth = "10"
                elif startMonth == "11" or startMonth == "nov" or startMonth == "november":
                    startMonth = "11"
                elif startMonth == "12" or startMonth == "dec" or startMonth == "december":
                    startMonth = "12"

                else:
                    print("Invalid value. Please enter the month in the MM format.")
                    continue

                # then we compare

                # if the start year is less than the current year
                if int(startYear) < todays_date.year:
                    # then all is fine as it is, no need to judge the value's validity. so we just break the while loop
                    break
                else:  # That means it is the current year and hence we need to judge what month the user enters
                    if int(startMonth) > todays_date.month:
                        veryrandomerrorcountinthemiddleofnowherethatijustinsertedbecauseiwassuperbored += 1
                        if veryrandomerrorcountinthemiddleofnowherethatijustinsertedbecauseiwassuperbored < 5:
                            # then the month entered by the user hasn't even arrived yet, so we "politely" inform him of this, once.
                            print("That month hasn't even arrived this year ○_○ Enter a valid number, please.")
                        else:
                            # well if the user is acting so dumb that calling him/her a human would be a shame to humanity,
                            # then guess we gotta show them that we ain't messing around here
                            print("Now, just pound it already into that thick skull of yours that we don't accept a read start date that hasn't even arrived yet (in this human world, at least).")
                            veryrandomerrorcountinthemiddleofnowherethatijustinsertedbecauseiwassuperbored = 0  # well one insult per 5 mistakes should be enough, no reason to shame him further
                    else: break # the month is all good now, so we can move on to the date

            while True:
                startDate = input("Please enter the date you started reading this book (DD) : ").strip().lstrip("0")
                # with this, all whitespaces and all leading zeroes have been removed

                normalDaysInMonths = (31,28,31,30,31,30,31,31,30,31,30,31)

                leapDaysInMonths = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

                if not startDate.isdecimal(): print("Please enter a decimal value only.")
                elif len(startDate) > 2 or int(startDate) > 31: print("Maximum value of input is 31.")
                elif int(startDate) == 0:
                    print("Well a month starts from its first day. I don't think I've ever seen one start with its zero'th day.")
                    print("Please enter a valid date.")
                elif int(startYear) == todays_date.year and int(startMonth) == todays_date.month:
                    if int(startDate) > todays_date.day:
                        # The user entered a date from the future
                        print("What's up with your future self suddenly deciding to read a book?")
                        print("Enter a date that has not yet passed.")
                    else:
                        # All good
                        # Set it up in a good format
                        startDate = startDate.rjust(2, "0")
                        break
                else:

                    # First we decide if the start year is a leap year.
                    isLeapYear = isleap(int(startYear))

                    # Next, for leap years:-
                    if isLeapYear:
                        if int(startDate) > leapDaysInMonths[int(startMonth) - 1]:
                            # The user has typed an impossible date.
                            print("The said month only has "+str(leapDaysInMonths[int(startMonth) - 1])+" at most. Please enter a valid date.")
                        else:
                            # All good
                            startDate = startDate.rjust(2, "0")  # setting it up in a good format
                            break
                    else:
                        if int(startDate) > normalDaysInMonths[int(startMonth) - 1]:
                            # The user has typed an impossible date.
                            print("The said month only has "+str(normalDaysInMonths[int(startMonth) - 1])+" at most. Please enter a valid date.")
                        else:
                            # All good
                            startDate = startDate.rjust(2, "0")  # setting it up in a good format
                            break
                        # Completion of start date part. Now just compile it to make a start date.
            finalStartDate = startDate + "/" + startMonth + "/" + startYear

        else:
            finalStartDate = ("----------")   # NOTE- DD/MM/YYYY all replaced by "-" character.
        
        newInput = finalStartDate
        bookShelf["startDate"] = newInput
    elif detailToChange == "end" or detailToChange == "b!"+str(available_details.index("End Date")+1):
        print("Current end date= "+bookShelf["endDate"])
        print("Initiating end_date_change function...")
        
        todays_date = date.today()  # Date object of today
        print("\nEND DATE RE-ENTRY")
        if not yesNoConfirmation("Are you sure you want to proceed with entering the end date? (Note- otherwise will be saved as NONE)"):
            finalEndDate = ("----------")  # NOTE- DD/MM/YYYY all replaced by "-" character.

        else:
            while True:
                endYear = input("Please enter the year you finished reading the book (YYYY) : ")
                if not endYear.isdecimal():
                    print("Please enter a valid numeric value.")
                elif len(endYear) != 4:
                    print("Please enter the year in the correct format (YYYY).")
                elif int(endYear) < 1900:
                    print(
                        "How low a value are you entering? Were you even born then? Enter a realistic value."
                    )
                elif int(endYear) > todays_date.year:
                    print("Who finished reading it, your future self? Enter a value within "+str(todays_date.year)+".")
                else: break   # All conditions clear, user entered a completely valid & practical input

            andherewegowithanothergoddamnlongvariablenamejustforsomeeastereggs = 0  # tbh, i was simply bored
            while True:
                endMonth = input("Please enter the month you ended reading the book (MM) : ").lower()
                endMonth = endMonth.strip().lstrip("0")  # first strip whitespace characters then strip the leading zeroes

                # then we convert all the different kinds of valid inputs into a single format: MM
                if endMonth == "1" or endMonth == "jan" or endMonth == "january":
                    endMonth = "01"
                elif endMonth == "2" or endMonth == "feb" or endMonth == "february":
                    endMonth = "02"
                elif endMonth == "3" or endMonth == "mar" or endMonth == "march":
                    endMonth = "03"
                elif endMonth == "4" or endMonth == "apr" or endMonth == "april":
                    endMonth = "04"
                elif endMonth == "5" or endMonth == "may":
                    endMonth = "05"
                elif endMonth == "6" or endMonth == "jun" or endMonth == "june":
                    endMonth = "06"
                elif endMonth == "7" or endMonth == "jul" or endMonth == "july":
                    endMonth = "07"
                elif endMonth == "8" or endMonth == "aug" or endMonth == "august":
                    endMonth = "08"
                elif endMonth == "9" or endMonth == "sep" or endMonth == "september":
                    endMonth = "09"
                elif endMonth == "10" or endMonth == "oct" or endMonth == "october":
                    endMonth = "10"
                elif endMonth == "11" or endMonth == "nov" or endMonth == "november":
                    endMonth = "11"
                elif endMonth == "12" or endMonth == "dec" or endMonth == "december":
                    endMonth = "12"

                else:
                    print("Invalid value. Please enter the month in the MM format.")
                    continue

                # then we compare

                # if the start year is less than the current year
                if int(endYear) < todays_date.year:
                    # then all is fine as it is, no need to judge the value's validity. so we just break the while loop
                    break

                else:  # if it is the current year, then we need to judge if the month entered is valid or not
                    if int(endMonth) > todays_date.month:
                        andherewegowithanothergoddamnlongvariablenamejustforsomeeastereggs += 1
                        if andherewegowithanothergoddamnlongvariablenamejustforsomeeastereggs < 5:
                            # politely inform the user
                            print("The month you entered is not valid, as it hasn't even arrived yet. Please enter a valid date.")
                        else:
                            # DUMB USER DETECTED. AVAILABLE SOLUTIONS: INSULT
                            print("Ayo dumbass user! When will you learn to enter it right? I told you, THAT MONTH HASN'T ARRIVED YET.")
                            andherewegowithanothergoddamnlongvariablenamejustforsomeeastereggs = 0  # 1-insult-per-5-mistakes-rule
                    else: break # All good. moving on to next stage

            while True:  # end date
                endDate = input("Please enter the date you ended reading this book (DD) : ").strip().lstrip("0")    # with this, all whitespaces and all leading zeroes have been removed

                normalDaysInMonths = (31,28,31,30,31,30,31,31,30,31,30,31)

                leapDaysInMonths = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

                if not endDate.isdecimal(): print("Please enter a decimal value only.")
                elif len(endDate) > 2 or int(endDate) > 31: print("Maximum value of input is 31.")
                elif int(endDate) == 0:
                    print("Well a month starts from its first day. I don't think I've ever seen one start with its zero'th day.")
                    print("Please enter a valid date.")
                elif int(endYear) == todays_date.year and int(endMonth) == todays_date.month:
                    if int(endDate) > todays_date.day:
                        # The user entered a date from the future
                        print("How do you know that you'll be completing the book on that date? You some kind of quack fortune-teller or something?")
                        print("Enter a date that has not yet passed.")
                    else:
                        # All good
                        # Set it up in a good format
                        endDate = endDate.rjust(2, "0")
                        break
                else:

                    # First we decide if the start year is a leap year.
                    isLeapYear = isleap(int(endYear))

                    # Next, for leap years:-
                    if isLeapYear:
                        if int(endDate) > leapDaysInMonths[int(endMonth) - 1]:
                            # The user has typed an impossible date.
                            print("The said month only has "+str(leapDaysInMonths[int(endMonth) - 1])+" at most. Please enter a valid date."
                            )
                        else:
                            # All good
                            endDate = endDate.rjust(2, "0")  # setting it up in a good format
                            break
                    else:
                        if int(endDate) > normalDaysInMonths[int(endMonth) - 1]:
                            # The user has typed an impossible date.
                            print("The said month only has "+str(normalDaysInMonths[int(endMonth) - 1])+" at most. Please enter a valid date.")
                        else:
                            # All good
                            endDate = endDate.rjust(2, "0")  # setting it up in a good format
                            break
                # Completion of end date part

            finalEndDate = endDate + "/" + endMonth + "/" + endYear  # DD/MM/YYYY ftw
        
        newInput = finalEndDate
        bookShelf["endDate"] = newInput
    elif detailToChange == "reread" or detailToChange == "b!"+str(available_details.index("Reread toll")+1):
        print("Saved data: No. of times reread = "+bookShelf["rereadTimes"])
        print("Caution: Anything you enter right now will be considered to be the new number of times the book has been reread.")
        while True:
            newInput = input("Enter new number of times reread: ")
            if newInput.isdecimal():
                if yesNoConfirmation("You have entered "+newInput+"\nDo you wish to continue?"):
                    bookShelf["rereadTimes"] = newInput
                    print("No. of times reread tally updated successfully.")
                    break
                else:
                    print("No worries. Enter it again.")
            else: print("Invalid input. Please enter an integral value not less than 0.")
    elif detailToChange == "genre" or detailToChange == "b!"+str(available_details.index("Genre")+1):
        print("Saved data: Genre = "+bookShelf["genre"])
        print("Caution: Anything you enter right now will be considered to be the new genre of the book.")
        while True:
            newInput = input("Enter new genre: ").title()
            if yesNoConfirmation("You have entered the genre as "+newInput+"\nDo you wish to continue?"):
                bookShelf["genre"] = newInput
                print("Genre updated successfully.")
                break
            else:
                print("No worries. Enter it again.")
    elif detailToChange == "publisher" or detailToChange == "pb" or detailToChange == "b!"+str(available_details.index("Publisher")+1):
        print("Saved data: Publisher = "+bookShelf["publisher"])
        print("Caution: Anything you enter right now will be considered to be the new publisher of the book.")
        while True:
            newInput = input("Enter new publisher's name: ")
            if yesNoConfirmation("You have entered the publisher's name as "+newInput+"\nDo you wish to continue?"):
                bookShelf["publisher"] = newInput
                print("Publisher updated successfully.")
                break
            else:
                print("No worries. Enter it again.")
    elif detailToChange == "review" or detailToChange == "rv" or detailToChange == "b!"+str(available_details.index("Personal Review")+1):
        print("Saved data: Personal review:-\n"+bookShelf["personalReview"])
        print("Caution: Anything you enter right now will be considered to be the new review for the book.")
        while True:
            newInput = input("Enter new personal review: ")
            if yesNoConfirmation("You have entered the review as-\n"+newInput+"\nDo you wish to continue?"):
                bookShelf["personalReview"] = newInput
                print("Book review updated successfully.")
                break
            else:
                print("No worries. Enter it again.")
    elif detailToChange == "b!back" or detailToChange == "b!cancel":
        print("Cancelling edit book and redirecting to main_Command...")
    bookShelf.close()
    if detailToChange in ["bookname", "authorname", "pagesread", "pagestotal", "score"]:
        booklist = shelve.open("booklist")
        if detailToChange == "bookname": booklist["book"+slno][0] = newInput
        elif detailToChange == "authorname": booklist["book"+slno][1] = newInput
        elif detailToChange == "pagesread": booklist["book"+slno][2] = newInput
        elif detailToChange == "pagestotal": booklist["book"+slno][3] = newInput
        elif detailToChange == "score": booklist["book"+slno][4] = newInput
        booklist.close()
    # All done now


def booklistRefresher(osName, listOfFilesInBookdata):
    "This function refreshes the 'booklist' shelf file, drawing its data from the 'bookdata' folder."
    booksSalvaged = 0
    if osName == "Windows": # for windows
        # This means that there will be 3 files for each shelf file, so simply no of shelf files = len(listoffiles)/3
        try:
            for i in range(len(listOfFilesInBookdata)//3): # HACK: Improve it later when you learn regex in python
                slno = str(i+1).rjust(5, "0")
                if "book"+slno+".bak" and "book"+slno+".dat" and "book"+slno+".dir" in listOfFilesInBookdata:
                    # book found
                    backupBook = shelve.open(os.path.join(".", "bookdata", "book"+slno))
                    bookName = backupBook["bookName"]
                    authorName = backupBook["authorName"]
                    pagesRead = backupBook["pagesRead"]
                    pagesTotal = backupBook["pagesTotal"]
                    scoreOfBook = backupBook["score"]
                    backupBook.close()

                    bookList = shelve.open("booklist")
                    bookList["book"+slno] = [bookName, authorName, pagesRead, pagesTotal, scoreOfBook]
                    bookList.close()
                    booksSalvaged+=1
            exceptionFound = None
        except Exception as e:
            exceptionFound = e

    elif osName == "Darwin":    # for Mac
        # Then there will be one file for each shelf file with extension "db"
        try:
            for i in range(len(listOfFilesInBookdata)): # HACK: Can be improved later with regex knowledge
                slNo = str(i+1).rjust(5, "0")
                if "book"+slNo+".db" in listOfFilesInBookdata:
                    # book found
                    backupbookonMac = shelve.open(os.path.join(".", "bookdata", "book"+slNo))
                    bookname = backupbookonMac["bookName"]
                    authorname = backupbookonMac["authorName"]
                    pagesread = backupbookonMac["pagesRead"]
                    pagestotal = backupbookonMac["pagesTotal"]
                    scoreofbook = backupbookonMac["score"]
                    backupbookonMac.close()

                    booklist = shelve.open("booklist")
                    booklist["book"+slNo] = [bookname, authorname, pagesread, pagestotal, scoreofbook]
                    booklist.close()
                    booksSalvaged+=1
            exceptionFound = None
        except Exception as e:
            exceptionFound = e
    else:
        exceptionFound = "Program not supported for operating systems other than Windows and Mac OS."
        # I know this skips possibilities of other OS, but this is the only way to take care of "variable is possibly unbound" issue
    # Due to unavailability of adequate information and knowledge on linux, I am currently not adding any form of linux support.
    return booksSalvaged, exceptionFound


def troubleshooter(bltb_mode : bool = False):
    "This function is a quite basic troubleshooter that helps the user fix errors."

    print("BOOKREK TROUBLESHOOTER\nChecking your program for errors... (Please wait patiently)")
    # Checking if all files/folders are okay, so that no errors arise later in the program
    errorFound = False
    osName = system()

    if bltb_mode:
        if osName == "Windows":
            os.remove(".\\booklist.bak")
            os.remove(".\\booklist.dat")
            os.remove(".\\booklist.dir")
        elif osName == "Darwin":
            os.remove("./booklist.db")

    if not os.path.isdir("bookdata"):
        os.mkdir(
            "bookdata"
        )  # if the folder doesn't yet exist or got deleted by the user, then we make the folder ourselves.
        # Unfortunately though, if the user accidentally deleted it, the data lost can't be recovered.
        print('Corruption detected: the folder "bookdata" was found to be deleted.')
        print(
            "The directory has been remade by me, but the data lost is lost forever in case you did not backup :("
        )  # Informing the user about it is important
        errorFound = True
    
    listOfFilesInBookdata = os.listdir("bookdata")

    martinlutherwroteninetyfivetheses = False
    for i in listOfFilesInBookdata:
        if not (i.endswith(".bak") or i.endswith(".dat") or i.endswith(".dir") or i.endswith(".db")):
            martinlutherwroteninetyfivetheses = True
            break
    if martinlutherwroteninetyfivetheses:
        print("Turns out there are some unwanted files in the folder 'bookdata'.")
        print("These files were not created by us(Bookrek), and hence must've been created by you(user).")
        print("Please refrain from putting anything in that folder as it hampers our smooth functioning.")
        print("\nFor now, move to another folder anything important you have in there and then press enter.")
        while True:
            input("Press enter when you are ready.")
            expectropatronum = yesNoConfirmation("Are you sure you want to proceed? [any unnecessary files will be deleted permanently]")
            if expectropatronum:
                break
            else:
                print("Okay, okay, here's another chance for you...")
        listOfFilesInBookdata = os.listdir("bookdata")  # refreshing the variable
        for z in listOfFilesInBookdata:
            if not (z.endswith(".bak") or z.endswith(".dat") or z.endswith(".dir") or z.endswith(".db")):
                os.remove(os.path.join(".", "bookdata", z))    # This should do it

    listOfFilesInBookdata = os.listdir("bookdata")  # refreshing the variable again
    fileskipped = False
    if osName == "Windows":
        for a in range(len(listOfFilesInBookdata)//3):
            bookNo = str(a+1).rjust(5, "0")
            if not (os.path.isfile(".\\bookdata\\book"+bookNo+".bak") and os.path.isfile(".\\bookdata\\book"+bookNo+".dat") and os.path.isfile(".\\bookdata\\book"+bookNo+".dir")):
                fileskipped = True
                break
        if fileskipped:
            # gotta rename stuff then
            print("Files found disordered. Rearranging and renaming...")
            print("[Please wait, this might take a while.]")
            try:    # using a try & except block because i'm not entirely sure that this will work. might run into some peculiar issues
                for i in range(len(listOfFilesInBookdata)//3):
                    bookNo = str(i+1).rjust(5, "0")
                    if bookNo not in listOfFilesInBookdata[3*i]:    # 3*i because windows creates 3 files for each shelf file
                        # only then shall we rename it.
                        os.rename(".\\bookdata\\"+listOfFilesInBookdata[3*i], ".\\bookdata\\book"+bookNo+".bak")
                        os.rename(".\\bookdata\\"+listOfFilesInBookdata[(3*i)+1], ".\\bookdata\\book"+bookNo+".dat")
                        os.rename(".\\bookdata\\"+listOfFilesInBookdata[(3*i)+2], ".\\bookdata\\book"+bookNo+".dir")
                        # NOTE: not using os.path.join here as we are sure that this block of code will only work on windows, so saving memory
                        # this should take care of the renaming of the file at least
                listOfFilesInBookdata = os.listdir("bookdata")  # refresh the variable again
                nainomesapna_sapnomesajna_sajnapedilaagaya, exceptionsEncountered = booklistRefresher(osName, listOfFilesInBookdata)
                print(str(nainomesapna_sapnomesajna_sajnapedilaagaya)+" data entries were successfully modified.")
                if exceptionsEncountered != None:
                    print("An error occurred in the program:")
                    print(exceptionsEncountered)
            except Exception.with_traceback as e:   # keeping the traceback for developer use
                print("File renaming failed.")
                print("Just in case you need it, the exception encountered was-")
                print(e)
    
    elif osName == "Darwin":    # Mac support
        for a in range(len(listOfFilesInBookdata)):
            bookNo = str(a+1).rjust(5, "0")
            if not os.path.isfile("./bookdata/book"+bookNo+".db"):
                fileskipped = True
                break
        if fileskipped:
            # rename stuff here now
            print("Files found to be disordered. Rearranging and renaming...")
            print("[Please wait, this might take a while.]")
            try:    # this may or may not work, so I used a try & except block
                for i in range(len(listOfFilesInBookdata)):
                    bookNo = str(i+1).rjust(5, "0")
                    if bookNo not in listOfFilesInBookdata[i]:
                        # then this needs to be renamed
                        os.rename("./bookdata/"+listOfFilesInBookdata[i], "./bookdata/book"+bookNo+".db")   # only one renaming required
                listOfFilesInBookdata = os.listdir("bookdata")  # refresh the variable
                korakagazthayemanmeralikhdiyanaamuspetera, exceptionsEncountered = booklistRefresher(osName, listOfFilesInBookdata)
                print(str(korakagazthayemanmeralikhdiyanaamuspetera)+" data entries were successfully modified.")
                if exceptionsEncountered != None:
                    print("An error has occurred in the program:")
                    print(exceptionsEncountered)
            except Exception.with_traceback as e:
                print("File renaming failed.")
                print("Just in case you need it, the exception encountered was-")
                print(e)

    if not ((os.path.isfile("booklist.bak") and os.path.isfile("booklist.dat") and os.path.isfile("booklist.dir")) or os.path.isfile("booklist.db")):
        errorFound = True
        # Accommodating both Windows and Mac
        if not bltb_mode:
            print("PROBLEM FOUND: booklist file(s) found deleted.")
            print("Creating new file...")
        else: print("Deleting old data and recreating the file...")
        terimittimeinmiljaawangulbankemainkhiljaawa = shelve.open("booklist")
        terimittimeinmiljaawangulbankemainkhiljaawa.close()
        # Just creating the shelf file
        print("New booklist file created.")
        if listOfFilesInBookdata != []:    # i.e. the folder bookdata is not blank
            print("Files found in 'bookdata' folder. Recovering data from them...\n")
            booksSalvaged, exceptionFound = booklistRefresher(osName=osName, listOfFilesInBookdata=listOfFilesInBookdata)
            if exceptionFound != None:
                print("Sorry, the data recovery from the bookdata folder failed :(")
                print("The files might be corrupt, or there might be some other reason.")
                print("In case you need it, the error message is:")
                print(exceptionFound)
            print("Data recovery finished. Number of items successfully recovered: "+str(booksSalvaged))
        else:
            print("No data found in folder 'booklist' to be retrieved from.")
    print("Troubleshooting completed.")
    if errorFound:
        print("All troubles found were fixed to the best of my ability.")
        print("If the problem persists, please consider a reset.")
    else: print("No errors found.")


def factoryReset():
    "This function is used to format the program when necessary or on user's demand."

    if yesNoConfirmation("The program will be reformatted and all your data will be lost. Are you sure you wish to proceed?"):
        osName = system()

        if os.path.isdir("bookdata"):
            for i in os.listdir("bookdata"):
                os.remove(os.path.join(".", "bookdata", i))
        else: os.mkdir("bookdata")

        with shelve.open("booklist"): pass  # Ensuring that the required shelf file exists
        if osName == "Windows":
            os.remove(".\\booklist.bak")
            os.remove(".\\booklist.dat")
            os.remove(".\\booklist.dir")
        elif osName == "Darwin": os.remove("./booklist.db")
        # No linux support cuz idk
        with shelve.open("booklist"): pass    # Just creating a file and nothing else

        progvar = shelve.open("progvar")    # reset the program variables
        progvar["progFormat"] = False
        progvar["autoTitle"] = True
        progvar.close()

        # Since idk how to restart a program, let's just pretend that the program was restarted
        print("BOOKREK - Your Bookreading Mate!\nVersion "+version+"\n")
        print("Type 'b!help' for the list of commands.")

    else: print("Reverting to main_command...")


def settings():
    "Just a tiny settings function."

    with shelve.open("progvar") as progvar:
        print("\nSETTINGS\n")
        print("Automatically change authors' names to title format (Auto-Title):".ljust(80, " ")+str(progvar["autoTitle"]))
        # That's it for now; add on more later
    
    if yesNoConfirmation("Would you like to change any setting(s)?"):
        available_settings = ["Auto-Title"]
        print("Settings available to be changed:")
        for i in available_settings: print(i)
        while True:
            print("Key in 'b!back' or 'b!done' to revert to the main_command.")
            settingInput = input("Enter the setting you wish to change: ").lower().replace(" ", "")
            if settingInput in ["auto-title", "autotitle", "b!1"]:
                if progvar["autoTitle"]: progvar["autoTitle"] = False
                else: progvar["autoTitle"] = True
                print("Changed Auto-Tile to "+str(progvar["autoTitle"]))
            elif settingInput in ["b!back", "b!exit", "b!cancel", "b!done"]: break
            else:
                print("Invalid input. Please only enter one of the following inputs:")
                for _ in available_settings: print(_)
    else: print("Reverting to main_command...\n")


# ----------------------------------------------Main Code--------------------------------------------
print("BOOKREK - Your Bookreading Mate!\nVersion "+version+"\n")  # Welcome message
print("Type 'b!help' for the list of commands.")

# Initially the value is set to True, so that the program gets formatted the first time it is run
with shelve.open("progvar") as progvar:
    if progvar["progFormat"]: factoryReset()

while True:
    mainCommand = input("\n(main_command) >>> ").lower().replace(" ", "")
    if mainCommand == "b!help":
        print("""MAIN_COMMAND ACCEPTED INPUT LIST
> To view the book list:
    view list
    view book list
    vbl
> To add a new book's data:
    add new book
    add book
    anb
    addnew
> To view/edit a book's data in details:
    view book
    view book details
    vbd
    edit book
    edit book details
    ebd
> To view/edit the settings:
    settings
    b!settings
> To troubleshoot any issues:
    troubleshooter
    tb
> To troubleshoot the booklist particularly in bltb mode:
    booklist troubleshooter
    bltb
> To factory reset the program:
    reset
    factory reset
    format
    reformat
> To quit the program:
    quit
    close
    exit""")
    elif mainCommand == "viewlist" or mainCommand == "viewbooklist" or mainCommand == "vbl":
        viewBookList()
    elif mainCommand == "addnewbook" or mainCommand == "addbook" or mainCommand == "anb" or mainCommand == "addnew":
        addNewBook()
    elif mainCommand in ["viewbook", "viewbookdetails", "vbd", "editbook", "editbookdetails", "ebd"]:
        viewBookDetails()
    elif mainCommand == "troubleshooter" or mainCommand == "tb":
        troubleshooter()
    elif mainCommand == "booklisttroubleshooter" or mainCommand == "bltb":
        troubleshooter(True)
    elif mainCommand == "quit" or mainCommand == "close" or mainCommand == "exit":
        print("Thank you for using BOOKREK. Wish you a nice day ahead!")
        quit("Program terminated successfully.")
    elif mainCommand in ["reset", "factoryreset", "format", "reformat"]: factoryReset()
    elif mainCommand in ["settings", "b!settings"]: settings()
    else:
        print("Invalid input. Please enter one of the allowed commands only.")
        print("Type 'b!help' for the list of commands.")

"""
PROTOCOL FOR SAVING BOOKDATA IN BOOKLIST
• each book's primary data is to be saved as a list, because lists are easier to work with than saving it in 4 different keys for each book
• for each book, there will be 1 list saved in 1 key. The list will have 5 elements—
    1. book's name
    2. author's name
    3. number of pages read
    4. total number of pages
    5. Score of the book (out of 10)
• number of pages read and total number of pages are to be saved as 4-digit numbers (dddd format).
• Score of the book is to be saved as 3 characters, i.e. \\d.\\d for example, 9.2, 5.6, 3.0, etc.
• if any information is not available, then replace it with the appropriate number of "---" type characters.
"""

"""
WHAT DATA TO SAVE ABOUT A BOOK?
• Book's name
• Author's name
• Status (Currently Reading/Completed/Dropped/On-hold/Plan to Read)
• Number of pages read
• Total number of pages
• Score of the book (out of 10)
• Start date of reading the book (DD/MM/YYYY)
• End date of reading the book (DD/MM/YYYY)
• No. of times book re-read
• A personal review on the book
• Genre of the book (let the user enter all these details)
• Publisher

This much should be enough for now
"""

"""
BRAINSTORMING AREA
• After figuring out the "status" feature mentioned in the above column of comments, use colorama to color books of each status differently
    - maybe a bad idea. using colorama on top of everything might make this code too heavy and cause lag
• Sort books by status by default, provide the option of changing sorting basis to alphabetical
• Create a troubleshooter. Troubles- -> done
    - 'bookdata' folder not found
    - 'booklist' shelf file not found
• Create a way to format/reset the app on demand -> done
    - by default run this formatter once at the first launch of the program to ensure that all required files & folders were installed properly
"""

"""
BOOK STATUS LEGEND
• 0 = Completed
• 1 = Currently Reading
• 2 = On-hold
• 3 = Dropped
• 4 = Plan to Read
"""

"""
FEATURES TO BUILD
• view book list
• view details of a book
• add new book
• edit book
• settings
• troubleshooter
• factory reset

Planning in future:
    - option to change all dates to MM/DD/YYYY for americans
    - learn regex, and implement it in multiple places. this can help avoid potential errors.
"""

# NOTE: To anyone other than me viewing this code, please excuse the variable names. For those that never get used again, I just assign utterly random
# names, so it might come off as weird or offensive to some people, but it's just all light-hearted and nothing serious.