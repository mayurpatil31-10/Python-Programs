
# coding: utf-8

# # Write a program that uses input to prompt a user for their name & then welcome them.

# In[1]:


inp = input('Enter Your Name:- ')
print("Welcome", inp)


# # Write a program to prompt the user for hours and rate per hour to compute gross pay.

# In[3]:


hours = float(input("Enter the Hours:- "))
rate = float(input("Enter the Rate:- "))

gross_pay = hours * rate

print('The Gross Pay is:- ', gross_pay)


# # Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

# In[4]:


cel = int(input("Enter the temperature in celcius:- "))

fah = (cel * 9/5) + 32

print("The temperature in Fahrenheit is:- ", fah,'degree F')


# In[8]:


w = 17
z = w//2
print(z)

