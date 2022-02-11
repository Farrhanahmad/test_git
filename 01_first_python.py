#variables
# fruit_basket=input("fav frout")
# print (fruit_basket)
# #input_and_print
# name = input("What is your name")
# age = input ("What is your age")
# greetings =  "Hello"
# print (greetings, name, age)
# -----------------------------------------------------
# 02_operators
# 03_strings
# 04_comments 
# 05_variables
# 06_input variables
# 07_conditional_logics
# 08_type conversion 
# 09_if_else & elif 
# 10_functions 
    # define print_condanics(text):
    # define school_calc(age):
# 11_loops (while, for) for x in range(4,11): print(x)
    # continue skips d
# 12_import_libraries
# 13_trouble_shooting
        # sytax error, runtime error, semantic_error
# ---------------------------------------------------------
# 03- Save python codes in digital notebook (Day-3)
# ---------------------------------------------------------
#Step 1 - import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#Step 2 - set a theme
sns.set_theme(style="ticks", color_codes=True)

#import dataset
kashti = sns.load_dataset("titanic")

#plot graph
p = sns.countplot(x="who", data=kashti, hue="class")
p.set_title("Titanic data - count plot")
plt.show()

p = sns.countplot(x="sex", data=kashti, hue="class")
p.set_title("Titanic data - count plot")
plt.show()
