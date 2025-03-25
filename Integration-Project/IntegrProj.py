"""
introduction to the program with citations.
"""
# ___Author___  "Andrea Safadi"

# -----------------------------------------------------------------------------

# --- INTRODUCTION --- #

# This program is directly inspired by, and is based in the fictional
# universe of the "SCP foundation". The SCP foundation is a website with a
# compilation of user-made creative tales of horror, mystery, and sometimes
# memes. These stories largely take place in a universe where supernatural
# or unexplained phenomena plague the earth. The 'SCP foundation' is
# supposedly a foundation that documents and contains these phenomena to
# protect the public. In the early 2010's the website hosted an SCP
# generator, where the user was able to input words as they so wished within
# a template to create an SCP themselves. It could be as goofy or as serious
# as the user wished it to be. This generator however, at least to my
# knowledge, no longer exists. Part of this program will contain an 'SCP
# generator' somewhat similar to that one. The other part of the program is
# somewhat original, and is meant to indulge the user in a narrative
# experience.

# -----------------------------------------------------------------------------

# -- CITATIONS -- #

# (1) -- scp-wiki.wikidot.com
# (2) -- the-scp.foundation
# (3) -- w3schools.com
# (4) -- includehelp.com/python/asking-the-user-for-integer
# -input-in-python-limit-the-user-to-input-only-integer-value.aspx
# (5) -- stackoverflow.com/questions/51151739/how-to-make-a-game-with-lives-in
# -python
# (6) -- m.youtube.com/watch?v=lm37J2Gyebg
# (7) -- m.youtube.com/watch?v=u0402sx05yl
# (8) -- https://discuss.codeacademy.com/t/print-statement-with-a-timer/607802
# (9) -- https://stackoverflow.com/questions/58775663/python-not-reading-file-
# correctly
# (10) -- https://www.freecodecamp.org/news/python-write-to-file-open-read-
# append-and-other-file-handling-functions-explained/amp/
# (11) -- https://stackoverflow.com/questions/19747371/python-exit-commands-why
# -so-many-and-when-should-each-be-used
# (12) -- https://stackoverflow.com/questions/29811082/how-to-print-out-a
# -numbered-list-in-python-3  ***
# (13) -- https://elearning.wsldp.com/python3/python-open-web-browser/#:~:
# text=Python%20has%20a%20module%20called,The%20webbrowser. ***
# (14) -- https://scp-wiki.wikidot.com/scp-even-number-j
# -----------------------------------------------------------------------------

# --- CITATION REFERENCES --- #

# Lines [604], [702], [736], [758], [799] and [817] of code:
# The try and except statements were taken
# from an example posted on the includehelp.com website listed above (4),
# but with minor changes and obviously pertaining to a completely different
# context.
# These were also inspired by a YouTube video titled: "Input
# Validation in Python"(7).

# In lines [796 to 825]:
# The code structure for login was slightly
# inspired by a YouTube video called "Python Practice: Number Guessing Game
# with While Loops & If Statements"(6).
# Meanwhile, the attempt function was
# inspired by the stack overflow website (5) listed above in citations.

# Lines [177] and [407 to the end of the program]:
# The import time module and the use of the sleep function from the
# time library was taken from the website in citation (8).

# Lines [860] and [870]:
# the use of the seek() function for files was taken from the website
# in citation (9).

# Lines [184], [296]:
# The use of "w+", or just adding a + in general for editing and
# reading files was taken from the website in citation (10).

# Lines [535], [698], [714], [889]:
# raise SystemExit was taken from the website in citation (11).

# Lines [597 to 599]:
# for in range function format was taken directly from citation (12),
# with the only changes being the variables used; in other words, not mine.

# Lines [178], [607 to 692], [875] and [885]:
# the use of import webbrowser, along with its functions were taken from
# citation (13).

# Lines [459 to 507]:
# The mad-libs type generator is directly inspired by citation (14).

# -----------------------------------------------------------------------------

# --- EXPLANATIONS//EXAMPLES FOR GRADING PURPOSES --- #

# Explaining Operators:

# -- (Numeric Operators) -- #

# -- (**) - Exponentiation: It will raise the integer to a power
# - example) print(4**5) == 1024

# -- (*) - Multiplication: Will multiply two integers together
# and output the result
# - example) print(4*5) == 20

# -- (/) - Division: Will divide two integers together and display the
# result as a floating point
# - example) print(20/5) == 4.0

# -- (%) - Modulus: Will divide two integers together and display the remainder
# - example) print(4%5) == 4

# -- (//) - Floor Division: Divides two integers together and rounds the
# result down to the nearest whole number
# - example) print(20//5) == 4

# -- (+) - Addition: Adds two integers together and displays the result
# - example) print(4+5) == 9

# -- (-) - Subtraction: Subtracts two integers together and displays the result
# - example) print(4-5) == -1
# -----------------------------------------------------------------------------

# -- (String Operators) -- #

# -- *(Have been used in lines 86 and 118)* -- #

# -- (+) - Concatenation: Essentially meshes two strings together to form
# one string, unless commas or spaces are used. Cannot be used with two
# different data types.
# - example) print("Hello"+"World") == HelloWorld

# -- (*) - Repetition: Will concatenate a string a number of instances
# depending on the int it is multiplied by.
# - example) print("Hello!" * 3) == Hello!Hello!Hello!

# *(sep and end arguments are visible in lines 104 - 107, and are used
# thereafter)*

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# --- OTHER PROGRAMS FOR GRADING PURPOSES --- #

# uncomment to test!
# use of boolean (not), !=, and the for in range() function.

# print("[Countdown]")
# for x in range(10, -1, -1):
#     if x != 0:
#         print(x)
#     else:
#         print("blastoff!")
#
# print("\n[Even or Odd?]")
# x = int(input("\ninput a number: "))
# y = int(input("input a second number: "))
#
# subtract = y - x
# if subtract % 2 != 0:
#     subtract = not True
# else:
#     subtract = True
# print(x, "minus", y, "equals an even number; True or False?", subtract)

# ------------------------------------------------------------------------------

# I've never programmed before, so in my humble
# opinion this is probably the coolest thing ever but that's just me.

# ------------------------------------------------------------------------------

import time
import webbrowser

# Files for use in the main menu, where they are called

# --- The Guide File --- #

Guide_File = open("Guide.txt", "w+")
Guide_File.write("------------------------------------------------------------"
                 "------------------------------------\n"
                 "\nSCP's are otherworldly phenomena that inhabit "
                 "the earth and are regulated by the "
                 "SCP foundation. \nThis organization heavily "
                 "reinforces the importance of the acronym which "
                 "represents our name and our purpose. "
                 "\nSecure. Contain. Protect."
                 "\nWhen referring to the containment of unnatural "
                 "phenomena, \nSCP's are arranged into different "
                 "classes depending on their inherent effects and "
                 "danger to society."
                 "\n"
                 "\nThese classes include:"
                 "\n"
                 "\n-- SAFE: anomalies that are easily and safely "
                 "contained. \nThis can be due to either extensive "
                 "research and understanding of the SCP, or due to the "
                 "anomaly only activating in response to "
                 "specific triggers. "
                 "\nThis does NOT, however, mean the SCP "
                 "itself is considered 'safe'."
                 "\n"
                 "\n-- EUCLID: anomalies that require more resources to "
                 "contain completely. \nThis is due to the unpredictable "
                 "nature of the SCP, and minimal understanding. "
                 "\nThese SCP's tend to be "
                 "sentient/autonomous."
                 "\n"
                 "\n-- KETER: anomalies that are exceedingly difficult to "
                 "contain reliably, with containment "
                 "procedures often being extensive. "
                 "\nThis can be due to a "
                 "lack of technology or understanding required for "
                 "containment."
                 "\nThese SCP's are not necessarily dangerous, "
                 "just difficult."
                 "\n"
                 "\n-- THAUMIEL: anomalies that are used to contain other "
                 "SCP's that couldn't be contained otherwise. "
                 "\nThese are classified at the highest levels of the "
                 "SCP foundation."
                 "\n"
                 "\n-- NEUTRALIZED: anomalies that are no longer anomalous, "
                 "due to having been intentionally \nor accidentally "
                 "destroyed/disabled."
                 "\n"
                 "\n-- APOLLYON: anomalies that cannot be contained or are "
                 "expected to breach containment. \nThese are usually "
                 "associated with apocalyptic events, or a K-Class "
                 "scenario of some kind, and require a massive amount of "
                 "effort to deal with. "
                 "\n"
                 "\n{*Note: The term 'K-class scenario' refers to different "
                 "types of apocalyptic events. \nPlease refer to the "
                 "[K-Class Scenarios] page on our site's menu for "
                 " \nfurther information on the different subtypes and their "
                 "descriptions.}"
                 "\n"
                 "\n-- ARCHON: anomalies that could theoretically be "
                 "contained, but are best left uncontained for reasons. "
                 "\nThey may be part of consensus reality that is either "
                 "difficult or may have adverse effects if "
                 "contained. \nThese are specifically chosen not to be "
                 "contained."
                 "\n"
                 "\n"
                 "------------------------------------------------------------"
                 "------------------------------------"
                 "\n[FOR HELP WITH CLASSIFYING AN SCP, PLEASE REFER TO THE"
                 " 'LOCK AND BOX' TEST BELOW]: \n"
                 "-----------------------------------"
                 "--------------------------"
                 "-----------------------------------"
                 "\n"
                 "\n* If you lock it in a box, leave it alone, and nothing "
                 "bad will happen, \nthen it is classified as SAFE."
                 "\n"
                 "\n* If you lock it in a box, leave it alone, and you're "
                 "not entirely sure what will happen, \nthen it is "
                 "classified as EUCLID."
                 "\n"
                 "\n* If you lock it in a box, leave it alone, and it "
                 "easily escapes, \nthen it is classified as KETER. "
                 "\n"
                 "\n* If it is the box, then it is classified as THAUMIEL."
                 "\n"
                 "\n* If you can't fit it in a box, and it contains the"
                 " capacity to induce an apocalyptic event, \nthen it is"
                 " classified as APOLLYON."
                 "\n"
                 "\n* If you could have locked it in a box but chose not to,"
                 " \nthen it is classified as ARCHON."
                 "\n"
                 "\nRemember again that these classes have nothing to do "
                 "with danger, ONLY containment."
                 "\nThe SCP Foundation will hold no responsibility for "
                 "\ncasualties caused by failure to follow these "
                 "procedures."
                 "\n"
                 "\n"
                 "--------------------------------"
                 "----------------------------- "
                 "-----------------------------------"
                 "\n"
                 "\n"
                 "\n(To access main menu once more, input command [menu])"
                 "\n(to leave the system, press [x])")

# --- The K-Scenario File --- #

K_Scenario_File = open("K-ClassScenarios.txt", "w+")
K_Scenario_File.write(
    "------------------------------------------------------------"
    "------------------------------------\n"
    "\nThe term 'K-Class Scenarios' refers to a series of "
    "hypothetical end of the world scenarios. "
    "\nThese are assumed to be caused by anomalies "
    "that possess the capability to either significantly "
    "change reality or induce apocalyptic events."
    "\n"
    "\nAs the Foundation in charge of overseeing these"
    " anomalies, it is our duty to ascertain the "
    "\nlikelihood of these events occurring, and in turn"
    " do whatever possible to prevent them from "
    "happening."
    "\n"
    "\nPlease be sure to keep these in mind when enforcing containment "
    "procedures,"
    "\nas failure to do so will result in immediate termination from the"
    " Foundation."
    "\n"
    "\nThere is never a moment where the fate of the world does not"
    " rest on our shoulders."
    "\n------------------------------------------------------------"
    "------------------------------------\n"
    "\n"
    "\n------------------------------------------------------------\n"
    "\nThe Comprehensive List of K-Class End of the World Scenarios "
    "\n                  are As Follows:\n"
    "\n------------------------------------------------------------"
    "\n"
    "\n-- [FIK]: scenario where the only surviving members"
    " of humanity are those"
    "\nthat reside within the Foundation."
    "\n"
    "\n-- [TPK]: scenario where all of humanity gain thaumaturgic abilities"
    "\n"
    "\n-- [GD]: scenario where the use of memory wiping agents to prevent"
    "\nthe exposure of anomalies, in turn creates it's own anomaly"
    "\n"
    "\n-- [AK]: scenario where all of humanity becomes infected by madness."
    "\n(In other words, unusual behavior spreads memetically, "
    "compromising survival)"
    "\n"
    "\n-- [ADK]: scenario where anomalous beings take over the earth after a "
    "human extinction event."
    "\n"
    "\n-- [CK]: scenario where reality is either significantly altered or is"
    "\nbrought to an end."
    "\n"
    "\n-- [EK]: scenario where all of human consciousness either becomes"
    "\nreplaced or corrupted in some manner."
    "\n"
    "\n-- [FK]: Failure or destruction of the SCP organization."
    "\nThis in turn results in other K-Class scenario occurrences due to"
    "\nunmanaged anomalies"
    "\n"
    "\n-- [GK]: scenario where humans become extinct, but the earth remains"
    " habitable."
    "\n(Also known as the 'Dead Greenhouse Scenario'.)"
    "\n"
    "\n-- [HK]: scenario where a God-like entity takes control of the earth."
    "\n"
    "\n-- [IK]: scenario that encompasses the collapse of human civilization."
    "\n"
    "\n-- [LK]: scenario where humans are altered in some way, whether it be"
    "\nphysically or psychologically"
    "\n"
    "\n-- [NK]: scenario where a self-replicating object replicates"
    " uncontrollably,"
    "\nto the point that it fills or replaces the world with itself."
    "\n"
    "\n-- [PK]: scenario where hyper realities collapse into ours, creating a "
    "\nnew incomprehensible reality. This results in the collapse of "
    "consciousness as we understand it."
    "\n"
    "\n-- [SK]: scenario where another species or civilization surpasses"
    " humanity"
    "\n"
    "\n-- [TK]: scenario where our current timeline becomes broken and then"
    " restructured,"
    "\nwith past events seemingly happening without cause or reason"
    "\n"
    "\n-- [XK]: scenario where a religious-type of apocalypse occurs"
    "\n"
    "\n-- [Lifted Veil]: scenario where the presence of the Foundation or"
    "\nanomalous beings becomes public knowledge, thus resulting in mass "
    "hysteria"
    "\n"
    "\n-- [BI]: scenario where another dimension invades our own"
    "\n"
    "\n-- [CC]: scenario where the laws of physics are significantly altered."
    "\nThus the chemistry relying on the chemical "
    "structure of carbon no longer"
    "\nprovides the conditions suitable for life to exist"
    "\n"
    "\n"
    "------------------------------------------------------------"
    "------------------------------------"
    "\n"
    "\n"
    "\n(To access main menu once more, input command [menu])"
    "\n(to leave the system, press [x])")


def generator_intro():

    """
Introduction to the scp file generator.
    """

    print("\nWELCOME TO [D̸A̷T̤́A̢E̶̥X̦̀PUNGE̩D̟́]̶̀ ̶̧͔̀͋̍"), time.sleep(1)
    print("\nThis program helps us "), time.sleep(0.1)
    print("find the humor in our livelihoods.\n"), time.sleep(3)
    print("enjoy the program! :)"), time.sleep(2)
    print("\n------------------------------------------------------------")
    print("\n-- SCP FILE GENERATOR --\n")
    print("------------------------------------------------------------")
    time.sleep(2)
    print("\n[Note: This is going to take quite a bit, so we hope the results"
          + " are worth it!]\n"), time.sleep(2)


def mad_lib_scp():

    """
Inputs for the scp generator.

Input:
    anything is allowed, the whole nature of this section of code is
    silly nonsense made for weird people like me.

Returns:
     Prints a nonsensical scp file born out of user ignorance

    """

    User_Name = "Dr.Ethan Briar"
    Number_1 = input("\nEnter a number: ")
    SCP_Class = input("\nEnter SCP Class: ")
    Container = input("\nEnter a container: ")
    Measure_1 = input("\nEnter second number: ")
    Measure_2 = input("\nEnter a third number: ")
    Unit_Measurement = input("\nEnter a unit of measurement: ")
    Place_1 = input("\nEnter a place: ")
    Object_1 = input("\nEnter an object (plural): ")
    Noun_1 = input("\nEnter a noun (all caps): ")
    Substance = input("\nEnter a substance: ")
    Verb_1 = input("\nEnter a verb (no suffixes): ")
    Favorite_Movie = input("\nEnter your favorite movie/series: ")
    Adjective_1 = input("\n[Halfway there!]\n \nEnter an adjective: ")
    Adjective_2 = input("\nEnter a second adjective: ")
    Noun_2 = input("\nEnter a second noun: ")
    Ing_Verb = input("\nEnter a '-ing' verb: ")
    Verb_Action = input("\nEnter a verb/action (no suffixes): ")
    Adjective_3 = input("\nEnter a third adjective: ")
    Phrase = input("\nEnter a phrase or spoken words: ")
    Verb_Action_2 = input("\nEnter a second verb/action (no suffixes): ")
    Place_2 = input("\nEnter a second place: ")
    Ing_Verb_2 = input("\nEnter a second '-ing' verb: ")
    Object_2 = input("\nEnter a second object (plural): ")
    Number_2 = input("\n[Last one!]\n \nEnter a fourth number: ")
    print("\n[Item #]:", Number_1,
          "\n"
          "\n[Object Class]:", SCP_Class,
          "\n"
          "\n[Containment Procedures]: SCP-", Number_1,
          "must be kept within a", Container,
          "measuring approximately",
          Measure_1, "by", Measure_2, Unit_Measurement + "." +
          "\nThe location of this",
          Container, "is said to be in",
          Place_1 + ", " +
          "\nwhich is heavily guarded by task forces armed with",
          Object_1 + "."
                     "\nIf SCP-", Number_1,
          "were to escape, Mobile Task Force Alpha",
          "('" + Noun_1 + "')", "will be dispatched to it's"
                                "\nlocation immediately.\n"
                                "\nIn the event that SCP-", Number_1,
          "begins to emit",
          Substance, "and starts to", Verb_1,
          "violently,\n" + User_Name, "will commence procedure",
          "'" + Favorite_Movie + "'",
          "until SCP-", Number_1, "is incapacitated.\n"
                                  "\n[Description]: SCP-", Number_1,
          "appears to be a",
          Adjective_1 + ",", Adjective_2 + ",", Noun_2 + "." +
          "\nIt's anomalous properties include",
          Ing_Verb, "and emitting",
          Substance + "." +
          "\nThis causes all nearby objects in it's immediate " +
          "vicinity to",
          Verb_Action, "uncontrollably due to it's", Adjective_3,
          "fumes."
          "\nIn addition, if SCP-", Number_1,
          "is allowed to continue in this state, it may commence to",
          "screech", Phrase + "," +
          "\nupon which any sentient beings within audio " +
          "distance will " + "begin to retch, and", Verb_Action_2,
          "in mass hysteria."
          "\nFrom this point, a loss of sanity is likely."
          "\n"
          "\n[Recovery Log]: SCP-", Number_1,
          "was first located by Foundation researchers in a", Place_2,
          "\nafter numerous reports " +
          "were received of a", Noun_2, "seen", Ing_Verb_2,
          "throughout the area."
          "\nIt was later apprehended by Task Force",
          "('" + Noun_1 + "')",
          "through the use of", Object_2, "with only", Number_2,
          "resulting casualties.\n")


def options_generator():

    """
A mini menu for the scp generator.

Input:
    User must input the options given by the print statement.
    If not, it will prompt them to try again.

Returns:
    User will be either redirected to the menu, exited out of the system, or
    they may try the mad-lib again.

    """

    print("\n(To access main menu once more, input command [menu])")
    print("\n(To leave the system, press [x])")
    print("\n(To try the program again, press [y])\n")
    Options_loop = True
    while Options_loop:
        Option = input("\nenter command here: ")
        if Option == "menu" or Option == "Menu":
            plain_menu()
            main()
        elif Option == "x" or Option == "X":
            raise SystemExit
        elif Option == "y" or Option == "Y":
            mad_lib_scp()
            print("\n(To access main menu once more, input command [menu])")
            print("\n(To leave the system, press [x])")
            print("\n(To try the program again, press [y]\n")
        else:
            print("\nInvalid command. Please try again.")


def scp_file_menu():

    """
Another menu for accessing documents on SCP creatures.

Input:
    User must input the file's corresponding number to access it, or the
    extra options given.

Returns:
    If a file is selected, the user will be redirected to the SCP's page on
    SCP-wiki.wikidot.com

    """

# list of scp items for use in the scp directory menu

    scp_list = ["Awaiting De-classification [Blocked]", "The 'Living' Room",
                "Biological Motherboard", "The 12 Rusty Keys and the Door",
                "Fountain of Youth", "Zombie Plague", "Red Ice",
                "Shadow Person", "Game Show of Death", "The Gate Guardian",
                "The Stairwell", "There Was A Crooked Man", "An Empty World",
                "The Body Farm", "RONALD REAGAN [DATA EXPUNGED] WHILE TALKING",
                "The Yule Man", "Antique Chess Computer", "Cabinet Maze",
                "Special Personnel Requirements \n[RESTRICTED FOR AGENTS BELOW"
                " CLEARANCE LEVEL 5]", "MalO ver1.0.0", "A Cowbell", "Red Sea"
                                                                     " Object",
                "Old Man", "Camera Disruption", "Infinite IKEA",
                "Clockwork", "[REDACTED PER PROTOCOL 4000-ESHU]",
                "The Bodies in the Water",
                "2010-2011 NBA Season Opening Recording", "The " +
                "Hanged King's Tragedy",
                "Laugh is Fun", "Book Keeper", "Bobble the Clown",
                "Chinese Soup Bowl", "A Hole to Another Place", "Star Signals",
                "Magic Vending Machine", "835", "Eric's Toy",
                "Bad Composition", "The Counting Station", "Ride Ticket",
                "The Doorman"]
    print("\n-----------------------------"
          "-------------------------------"
          "\n{THE SCP DIRECTORY}\n"
          "-----------------------------"
          "-------------------------------\n"), time.sleep(2),
    print("DOCUMENT ARCHIVES ACCESSIBLE BY DR.BRIAR:\n"), time.sleep(3),
    print("\n(To access main menu once more, input command [menu])")
    print("(to leave the system, press [x])\n"), time.sleep(3)

    # [for i in scp_list] -- prints out numbered list of scp items

    # source: code was taken directly from
    # https://stackoverflow.com/questions/29811082/how-to-print-out-a
    # -numbered-list-in-python-3

    for i in scp_list:
        time.sleep(0.2), print(scp_list.index(i) + 1, end='.) ')
        print("", i)

    scp_webpage = True
    while scp_webpage:
        try:
            scp_number = input("\nAccess File Number: ")
            if scp_number == "1":
                webbrowser.open('https://the-scp.foundation/object/scp-001')
            elif scp_number == "2":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-002')
            elif scp_number == "3":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-003')
            elif scp_number == "4":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-004')
            elif scp_number == "5":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-006')
            elif scp_number == "6":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-008')
            elif scp_number == "7":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-009')
            elif scp_number == "8":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-017')
            elif scp_number == "9":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-024')
            elif scp_number == "10":
                webbrowser.open(
                    'https://scp-wiki.wikidot.com/dr-clef-s-proposal')
            elif scp_number == "11":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-087')
            elif scp_number == "12":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-783')
            elif scp_number == "13":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-201')
            elif scp_number == "14":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-792')
            elif scp_number == "15":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-1981')
            elif scp_number == "16":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-4666')
            elif scp_number == "17":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-1875')
            elif scp_number == "18":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-432')
            elif scp_number == "19":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-231')
            elif scp_number == "20":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-1471')
            elif scp_number == "21":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-513')
            elif scp_number == "22":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-093')
            elif scp_number == "23":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-106')
            elif scp_number == "24":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-895')
            elif scp_number == "25":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-3008')
            elif scp_number == "26":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-914')
            elif scp_number == "27":
                webbrowser.open('https://scp-wiki.wikidot.com/taboo')
            elif scp_number == "28":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-2316')
            elif scp_number == "29":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-1733')
            elif scp_number == "30":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-701')
            elif scp_number == "31":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-2030')
            elif scp_number == "32":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-1230')
            elif scp_number == "33":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-993')
            elif scp_number == "34":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-348')
            elif scp_number == "35":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-1437')
            elif scp_number == "36":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-1425')
            elif scp_number == "37":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-261')
            elif scp_number == "38":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-835')
            elif scp_number == "39":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-066')
            elif scp_number == "40":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-012')
            elif scp_number == "41":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-3034')
            elif scp_number == "42":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-342')
            elif scp_number == "43":
                webbrowser.open('https://scp-wiki.wikidot.com/scp-303')
            elif scp_number == "menu" or scp_number == "Menu":
                scp_webpage = False
                plain_menu()
                main()
            elif scp_number == "x" or scp_number == "X":
                raise SystemExit
            else:
                print("\nInvalid input. Command was not derived from the menu."
                      "\nPlease enter a file number.")
        except ValueError:
            print("\nInvalid input. Please enter a file number.")


def error_message():

    """
Function for the login error message, because I'm lazy.
    """

    print("ERROR, input was not valid. Please remain seated."
          "\n" * 100)
    raise SystemExit


def failed_attempt():

    """
Function for using up the number of login attempts.

Input:
    User may try once again if they learn to follow directions.

Returns:
    If inputted correctly, it will allow the user one last attempt.
    If not, the program ends.

    """

    print("\nREMAIN SEATED WITH YOUR HANDS IN FULL VIEW. "
          "AN AGENT WILL COME TO RETRIEVE YOU FOR QUESTIONING. "
          "\nYOU HAVE USED UP THE LEGAL NUMBER"
          " OF ATTEMPTS.")

    try:
        override = int(input(
            "\nTo override the system and login again," +
            "\nplease enter the 9 digit administration number: "))
        over_ride = str(override)
        if (len(over_ride) > 9) or (len(over_ride) < 9):
            error_message()
        else:
            print("\nWARNING. THIS IS YOUR LAST LOGIN ATTEMPT. "
                  "FAILURE TO PROVIDE VALID CREDENTIALS WILL RESULT"
                  " IN EMERGENCY SHUTDOWN. "
                  "\nIf you are a staff member and require "
                  "assistance, please refer to your supervisor for"
                  " login.")
        Gov_ID = int(input("\nGovernment ID number: "))
        Pass_word = int(input("\nPIN: "))
        Gov_Num = str(Gov_ID)
        Pass_Num = str(Pass_word)
        if len(Gov_Num) == 9 and len(Pass_Num) == 6:
            menu_success()
        else:
            error_message()
    except ValueError:
        error_message()


def menu_success():

    """
Function for when you successfully log in. Displays the menu.
    """

    User_Name = "Dr. Ethan Briar"
    print("\n" + "\n....." + "\n"), time.sleep(1)
    print("\nCREDENTIALS ACCEPTED", end="_"), time.sleep(2)
    print("\n" + "\n-", "Welcome to the SCP Foundation", "-",
          sep="-------", end=""), time.sleep(2)
    print("\n" + "\nYou are now logged in as", User_Name, "\n" +
          "Clearance Level: 4"),
    time.sleep(3),
    print("\n", "Menu", "", sep="_"), time.sleep(1)
    print("\n[Guide]", "\n[SCP Directory]", "\n[K-Class Scenarios]",
          "\n[Files]", "\n[D̸A̷T̤́A̢E̶̥X̦̀PUNGE̩D̟́]̶̀ ̶̧͔̀͋̍",
          "\n[O-5 Directory]")
    time.sleep(1),
    print("\nFor our new staff members: It is highly recommended to " +
          "read our foundation's Guide before commencing operations." +
          "\nTo enter commands, write them exactly as you see them on the "
          + "menu,\nor with all undercase letters."), time.sleep(3),
    print("\n(To access main menu once more, input command [menu])")
    print("(to leave the system, press [x])")


def login_attempt():

    """
Function for logging in. User has three tries to enter correct input.
[login variable = 3]
    """

    continue_looping = True
    login = 3
    while continue_looping:
        try:
            Gov_ID = int(input("\nGovernment ID number: "))
            Pass_word = int(input("\nPIN: "))
            Gov_Num = str(Gov_ID)
            Pass_Num = str(Pass_word)
            if len(Gov_Num) == 9 and len(Pass_Num) == 6:
                menu_success()
                continue_looping = False
            else:
                login -= 1
                if login > 0:
                    print("\nINVALID CHARACTER LENGTH. PLEASE TRY AGAIN.\n"
                          "\nID should be 9 digits in length."
                          "\nPIN should be 6 digits in length.\n"
                          "\nyou have", login, "attempts left.")
            if login < 1:
                continue_looping = False
                failed_attempt()
        except ValueError:
            login -= 1
            if login < 1:
                continue_looping = False
                failed_attempt()
            else:
                print("\nINVALID CREDENTIALS. PLEASE TRY AGAIN. ONLY THE "
                      "CHARACTERS 0-9 ARE ALLOWED.", "\nyou have",
                      login, "attempts left.")


def plain_menu():

    """
Function for the main menu display.
    """

    print("\n", "Menu", "", sep="_"), time.sleep(1)
    print("\n[Guide]", "\n[SCP Directory]", "\n[K-Class Scenarios]",
          "\n[Files]", "\n[D̸A̷T̤́A̢E̶̥X̦PUNGE̩D̟́]̶̀ ̶̧͔̀͋̍",
          "\n[O-5 Directory]"),
    time.sleep(1),
    print("\nFor our new staff members: It is highly recommended to " +
          "read our foundation's Guide before commencing operations." +
          "\nTo enter commands, write them exactly as you see them on the " +
          "menu,\nor with all undercase letters.")
    time.sleep(3),
    print("\n(To access main menu once more, input command [menu])")
    print("(to leave the system, press [x])")


def main():

    """
Function for the main menu, with options.
    """

    menu_options = ["Guide", "SCP Directory", "K-Class Scenarios", "Files",
                    "DATA EXPUNGED", "0-5 Directory", "Menu"]
    loop_menu = True
    while loop_menu:
        command = input("\nPlease enter a command from the menu: ")
        if (command == menu_options[0]) or (command == "guide"):
            Guide_File.seek(0)
            print("\n."), time.sleep(1), print("\n."), time.sleep(1),
            print("\n."), time.sleep(2)
            print(Guide_File.read())
        elif (command == menu_options[1]) or (command == "scp directory"):
            loop_menu = False
            print("\n."), time.sleep(1), print("\n."), time.sleep(1),
            print("\n."), time.sleep(2)
            scp_file_menu()
        elif (command == menu_options[2]) or (command == "k-class scenarios"):
            K_Scenario_File.seek(0)
            print("\n."), time.sleep(1), print("\n."), time.sleep(1),
            print("\n."), time.sleep(2)
            print(K_Scenario_File.read())
        elif (command == menu_options[3]) or (command == "files"):
            webbrowser.open('https://scp-wiki.wikidot.com/incident-reports'
                            '-eye-witness-interviews-and-personal-logs')
        elif (command == menu_options[4]) or (command == "data expunged"):
            loop_menu = False
            print("\n."), time.sleep(1), print("\n."), time.sleep(1),
            print("\n."), time.sleep(2)
            generator_intro()
            mad_lib_scp()
            options_generator()
        elif (command == menu_options[5]) or (command == "O-5 directory"):
            webbrowser.open('https://scp-wiki.wikidot.com/o5-command-dossier')
        elif command == menu_options[6] or command == "menu":
            plain_menu()
        elif command == "x" or command == "X":
            raise SystemExit
        else:
            print("Invalid input. Command was not derived from the menu.")


def scp_introduction():

    """
Introduction that displays when the program is first opened.
    """

    print("\nWARNING"), time.sleep(1)
    print("\nTHE PAGE YOU ARE ABOUT TO ACCESS CONTAINS CLASSIFIED " +
          "GOVERNMENT INFORMATION"), time.sleep(4), print(
        "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣴⣤⣤⣤⣤⣤⡄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⣿⠟⢋⣵⣿⣿⣿⡿⠛⣩⣤⣿⣿⣿⣿⣿⣿⣿⣬⣙⠻⣿⣿⣿⣷⡍⠛⢿⣿⣿⣿⣿⣿⣿"
        "\n⣿⣿⣿⣿⠟⢹⠃⣠⣾⣿⣿⡿⢋⣴⣿⣿⣿⣿⠿⠿⠈⠿⢿⣿⣿⣿⣷⣤⡙⣿⣿⣿⢦⡀⢣⠙⣿⣿⣿⣿"
        "\n⣿⣿⡿⡿⠀⡯⠊⣡⣿⣿⠏⣴⣿⣿⣿⠟⠁⣀⣤⣤⠀⣤⣤⡀⠙⠻⣿⣿⣿⣌⢻⣿⣧⡉⠺⡄⢸⠹⣿⣿"
        "\n⣿⣿⠃⢷⠀⡠⢺⣿⣿⡏⣰⣿⣿⡟⠁⣠⣾⣿⣿⠿⠀⠿⣿⣿⣷⡄⠘⣿⣿⣿⡄⣿⣿⣯⠢⡀⢸⠀⢹⣿"
        "\n⣿⣿⠀⢸⠊⣠⣿⣿⣿⢀⣿⣿⣿⠁⣰⣿⣿⣿⣿⣆⢀⣼⣿⣿⣿⣿⡄⢸⣿⣿⣿⣹⣿⣿⣦⠈⢺⠀⢸⣿"
        "\n⣿⠹⡆⠀⣴⢻⣿⣿⣿⢸⣿⣿⣿⠀⣿⣿⡿⠿⠿⢿⣿⠿⠿⠿⣿⣿⡇⢈⣿⣿⣿⠀⣿⣿⣿⠳⡀⢀⡇⢸"
        "\n⣿⡀⠹⣸⠉⣿⣿⡿⢋⣠⣿⣿⣿⡀⠸⠟⢋⣀⢠⣾⣿⣷⡀⣀⡙⠻⠁⢸⣿⣿⣿⣈⠻⣿⣿⡄⠹⡜⠀⣸"
        "\n⣿⢧⠀⠇⢠⣿⣿⣷⡘⣿⣿⣿⣟⣁⡀⠘⢿⣿⣿⣿⣿⣿⣿⣿⠿⠀⣠⣉⣿⣿⣿⡿⢠⣿⡿⢧⠀⠁⣰⢿"
        "\n⣿⡌⢷⡄⣾⠀⣿⣿⣷⡜⢿⣿⣿⣿⣿⣦⣄⠈⠉⠛⠛⠛⠉⢁⣠⣾⣿⣿⣿⣿⡟⣰⣿⣿⡇⢸⢀⡴⠃⣼"
        "\n⣿⣷⣄⠙⢿⠀⣿⢿⣿⣿⣌⠿⠟⡻⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⡿⠛⠿⠟⣼⣿⡿⢫⠃⢸⠋⢀⣼⣿"
        "\n⣿⣿⣟⣶⣄⡀⢸⡀⢻⣿⣿⣾⣿⣿⣶⣍⣙⠛⠿⠿⠿⠿⠿⠛⣋⣥⣶⣿⣿⣾⣿⣿⠁⣸⢀⣴⣶⣯⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⠾⣧⠀⢯⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⠃⢠⢷⣛⣉⣽⣿⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⣿⣄⣁⡈⢧⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⢋⣀⣠⣴⣾⣿⣿⣿⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⣿⣯⣉⠉⠉⠉⣀⣀⡭⠟⠛⢛⣛⠛⠛⠛⣛⠛⠛⠩⣥⣀⣈⢁⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⡛⢉⣁⣀⣤⠖⣫⣴⣿⣿⣷⣬⡙⣦⣤⣀⡈⣉⣩⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
        "\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    time.sleep(1)
    print("\nANY ACCESS BY UNAUTHORIZED PERSONNEL IS STRICTLY "
          "PROHIBITED"), time.sleep(3)
    print("\nFAILURE TO COMPLY WILL RESULT IN CRIMINAL " +
          "PENALTIES, INCLUDING BUT NOT LIMITED TO LIFE-LONG" +
          " DETAINMENT AND/OR EXECUTION"), time.sleep(5)
    print("\nYOU HAVE BEEN WARNED\n"), time.sleep(5)


if __name__ == "__main__":
    scp_introduction()
    login_attempt()
    main()
