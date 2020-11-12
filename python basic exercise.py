"""INSTRUCTIONS:
1.DISPLAY QUESTIONS USING questions.py module 
2.CALL THE FUNCTIONS BY ITS FUNCTIONS NAME IN python basic exercise.py module
"""
import questions
#NEW LINE
def new_line():
    print('\n')
new_line()
#1
def poem():
    print('\nSolution:'),print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!\n")

#2
def version():
    import sys
    print('\nVersion',sys.version)
    print('Version_info',sys.version_info,end='\n\n')

#3
import datetime
def date_time():
    current_time = datetime.datetime.now()
    print("\nCurrent Date and Time: ",current_time), print (current_time.strftime("%Y-%m-%d %H:%M:%S"))

#4
from math import pi
def area_of_circle():
    radius_input = float(input('Radius of the Circle: '));area = round(pi*(radius_input**2),4)
    print("Area of the Circle: ",area),print(f"Calculated area: {area} square units\n")

#5
def lastname_firstname():
    fname,lname= input('First name: '),input('Last name: ')
    print(lname + " " + fname)

#6
def gen_list_and_tup():
    values = (input('Enter some numbers with space: '))
    lis = values.split(' ')
    tup = tuple(lis)
    set1 = set(lis)
    set2 = set(tup) # set from tuple
    #dict1 = dict(lis).update()
    print(f"In List: {lis}\nIn Tuple: {tup}\nIn various data type: {set1}")

#7
def extension_return():
    ext_ip= input('Filename: ')
    ext_dot_check = ext_ip.split('.')
    print(ext_dot_check[-1])

#8
def first_last_clrs():
    clr_list= ['Red','Green','Blue','Black','White']
    print(f'First Color: {clr_list[0]} and Last color: {clr_list[-1]}')

#9
def exam_schedule():
    date= input('Date: ')
    replace_dt = date.replace(',','/',3)
    print(replace_dt)

#10
def n_nn_nnn():    
    n= int(input("Num: "))
    n1,n2,n3=n,(n*11),(n*111) 
    print(n1+n2+n3)

#11
def numsuperpairs(nums):
    dict1 = dict()
    pairs = 0
    for i in nums:
        if i in dict1:
            pairs += dict1[i]
            dict1[i] += 1
        else:
            dict1[i] = 1
    print(pairs)




