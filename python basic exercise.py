#1
'''Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are'''
def poem():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")
#poem()
#2
def version():
    import sys
    print('Version')
    print(sys.version)
    print('Version_info')
    print(sys.version_info)
#version()

#3
import datetime
def date_time():
    current_time = datetime.datetime.now()
    print("\nCurrent Date and Time: ",current_time)
    print (current_time.strftime("%Y-%m-%d %H:%M:%S"))
#date_time()
#4
from math import pi
def area_of_circle():
    print('\n')
    radius_input = float(input('Radius of the Circle: '))
    area = round(pi*(radius_input**2),4)
    print("Area of the Circle: ",area)
    print(f"Calculated area: {area} square units")
#area_of_circle()
#5
def lastname_firstname():
    print('\n')
    fname,lname= input('First name: '),input('Last name: ') 
    print(lname + " " + fname)
#lastname_firstname()
#6
def gen_list_and_tup():
    print('\n')
    lis= []
    a = input('Number to add: ')
    if a.isnumeric() :
        for a not in lis:
            lis.append(a)
            return gen_list_and_tup()
        print(lis)
    
    else:
        print('Please enter a valid number!!')
        return gen_list_and_tup()
    #print('Nums in list: ',lis)#print('Nums in tuple: ',tup)
gen_list_and_tup()






















































