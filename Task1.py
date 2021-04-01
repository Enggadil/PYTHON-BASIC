#!/usr/bin/env python
# coding: utf-8

# In[3]:


name="Adil Hussain"
rollNo="12084"
dept="Software Engineering"
sub="AI Lab"
course="BSSE 5th morning"
Lab="Lab 2"
university="NUML ISLAMABAD"
message= """
Name= {}
rollNo={}
dept={}
sub={}
course={}
Lab={}
University= {}

""".format(name, rollNo, dept,sub,course,Lab,university)

print(message)


# # Task 1

# ## Write a program that first displays a simple cafe menu (see example below), asks the user to enter the
# number of a choice, and either prints the appropriate action OR prints an error message that their choice
# was not valid.
# Example output:
# 1. Soup and salad
# 2. Pasta with meat sauce
# 3. Chef's special
# Which number would you like to order? 2 One Pasta with meat sauce coming right up!
# Another example output:
# 1. Soup and salad
# 2. Pasta with meat sauce
# 3. Chef's special
# Which number would you like to order? 5
# Sorry, that is not a valid choice.

# In[ ]:



        
 
                


# In[35]:


def mainmenu(): 
    print("..........................................................")    
    print("1. Soup and salad") 
    print("2. Pasta with meat sauce") 
    print("3. Chef's special")    
    print("4. Quit") 
    print("..........................................................")  
    while(True):
         try:
                 selection=int(input("Which number would you like to order?   ")) 
                    if selection==1: 
                        selection1() 
                        break
                    elif selection==2:
                        selection2()
                        break
                    elif selection==3:
                         selection3() 
                            break
                    
                     elif selection==4: 
                            break
                    else:
                        print("Sorry, that is not a valid choice.") 
            except valueError:
                 print("Sorry, that is not a valid choice.") 
                    exit()  
                        
def selection1(): 
    print(" You choose Soup and salad") 
    anykey=input("Enter anything to return to main Menu :  ")  
    mainmenu()
def selection2(): 
    print("You choose Pasta with meat sauce coming right up")   
    anykey=input("Enter anything to return to main Menu :  ") 
    mainmenu() 
def selection3(): 
    print("You choose Chef's special") 
    anykey=input("Enter anything to return to main Menu :  ")    
    mainmenu() 
print("..........................................................") 
mainmenu() 
print("..........................................................") 
 
 


# # Task 2

# # Once upon a time in Apple land, John had three apples, Mary had five apples, and Adam had six apples.
# They were all very happy and lived for a long time. End of story.
# Your task is to:
# • create the variables: john, mary, and adam;
# • assign values to the variables. The values must be equal to the numbers of fruit possessed by John,
# Mary, and Adam respectively;
# • having stored the numbers in the variables, print the variables on one line, and separate each of them
# with a comma;
# • now create a new variable named totalApples equal to addition of the three former variables.
# • print the value stored in totalApples to the console
# • Check if the totalApples is greater, smaller or equal to 10

# In[5]:


Appleland= {'john': 3, 'mary': 5, 'adam': 6}
value=Appleland.values()
totalApples=sum(value)
print("The totalApples is :",totalApples)
print("***************************")
print("Now Check if the totalApples is greater, smaller or equal to 10 ")
print("***************************")
if totalApples==10:
    print("TotalApples is Equal to 10")
elif totalApples>10:
    print("TotalApples is greater to 10")
elif totalApples<10:
    print("TotalApples is Smaller to 10")
else:
    print("not Applicable")
   


# In[ ]:




