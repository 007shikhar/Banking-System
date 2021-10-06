import os

from Banking import clear

def create_acct():

  name=input('\nEnter your name   :  : ')
  f=open(name+'.txt','w')
  f.write(name+'\n')
  c4=0
  while(c4==0):
    age=input('Enter Your Age    :  : ')
    b4=list(age)
    for i in range(0,len(b4)):
      if(b4[i].isalpha()==True):
        print('Invalid age.Re-enter   :  : ')
        break
      if(int(age)<1 or int(age)>110):
        print('Invalid age.Re enter    : : ')
        break
    else:
      c4=1
  f.write(age+'\n') 
  
  mobileno=input('Enter Your 10 digits Mobile number  : : +91')
  while(len(mobileno)!=10):   
    print('Invalid Mobile number, Please re-enter : : ')
    mobileno=input('Enter Your 10 Digits Mobile number : : ')
    continue
  f.write(mobileno+'\n')
  
  print('\nEnter your Date Of Birth')
  mm=int(input('Enter The Month : : '))
  while(mm<=0 or mm>12):
    print('Invalid month, Please re-enter : : ')
    mm=int(input('Enter The Month : : '))
    continue
  dd=int(input('Enter the date : : '))
  while(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    if(dd<1 or dd>31):
      print('Invalid date re-enter : : ')
      dd=int(input('Enter the date : : '))
      continue
    else:
      break
  while(mm==4 or mm==6 or mm==9 or mm==11):
    if(dd<1 or dd>30):
      print('Invalid date re-enter : : ')
      dd=int(input('Enter the date : : '))
      continue
    else:
      break
  while(mm==2):
    if(dd<1 or dd>29):
      print('Invalid date re-enter : : ')
      dd=int(input('Enter the date : : '))
      continue
    else:
      break
  
  yy=int(input('Enter the year : : '))
  while(yy<1900 or yy>2019):
    print('Please enter correct year\n')
    yy=int(input('Enter the year : : '))
  if(yy%4!=0):
    if(mm==2 and dd==29):
      print('You have entered wrong date. Please re-enter all your record ')
      create_acct()
    
  dob=str(dd)+'-'+str(mm)+'-'+str(yy)
  f.write(dob+'\n')
  
  print('Enter your gender\n')
  print('For male press   :1')
  print('For female press :2')
  c1=int(input('Enter your choice :'))
  if(c1==1):
      gender='male'
  elif(c1==2):
      gender='female'
  else:
      gender='others'
      
  f.write(gender+'\n')
  pwd=input('\nenter your password :')
  q=pwd;
  f.write(q+'\n')
  f.write('0');
  clear();
  print('Welcome',name,'Thanks for registring with us.Your entered details are as follows:\n\n')
  print('Your name is :',name)
  print('Date of birth"',dob,'\nAge :',age,'\nMobile Number :',mobileno,'\nGender :',gender,'\npassword :',q)
  
  
  print('\n\nCongratulations!Your account is opened at a minimum balance of 0rs. To deposit some money press 3 \n') 
  f.close()
  return



def delete_acct():
  Name=input('Enter  your name :')
  pwd5=input('Enter your password :')
  f=open(Name+'.txt','r')
  test_lines = f.readlines()
  if(pwd5 == test_lines[5].strip()):
      f.close()
      os.remove(Name+'.txt')
      print("\nRecord deleted successfully\n")
  else:
      print('\nWrong password. Not authorized !!!\n\n')
