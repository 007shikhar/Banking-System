import os
from os import system, name
from time import sleep

import DML
import DDL

def clear():
  if name == 'nt':
    _ = system('cls')

def getBalance():
  Name=input('Enter your name :')
  f=open(Name+'.txt','r')
  test_lines = f.readlines()
  pwd2=input('Enter your passsword :')
  clear();
  if(pwd2 == test_lines[5].strip()):
      print('your current balance is',test_lines[6])
  else:
      print('Incorrect user id or password')

def getDetails():
  Name=input('Enter your name :')
  f=open(Name+'.txt','r')
  test_lines = f.readlines()
  pwd2=input('Enter your passsword :')
  clear();
  if(pwd2 == test_lines[5].strip())   :
      print("Your account details :-\n")
      print("NAME : "+test_lines[0]+'\n')
      print("AGE : "+test_lines[1]+'\n')
      print("Contact : "+test_lines[2]+'\n')
      print("DOB : "+test_lines[3]+'\n')
      print("GENDER : "+test_lines[4]+'\n\n')
  else:
      print('Incorrect user id or password')

if __name__ == '__main__': 
 print("\n")
 print("             WELCOME TO THE BANK     \n")    
 choice=1   
 while(choice<=6 and choice>=1):    

  print('-> To Insert Record Press : 1')
  print('-> To Deposit Cash INR press : 2')
  print('-> To Withdraw Cash Press : 3')
  print('-> For Balance Enquiry Press : 4')
  print('-> To Get Details of an Account Press : 5')
  print('-> To Delete Record Press : 6')
  print('- To exit press : 0')
  choice=int(input('\nPlease Enter Your Choice : : '))
  clear()
 
  if(choice==1):
    print('Your request has been made...... wait for 2 sec');
    sleep(2)
    clear()
    DDL.create_acct()
   
  elif(choice==2):
    print('Your request has been made...... wait for 2 sec');    sleep(2)
    clear()
    DML.trxn_dep()
 
  elif(choice==3):
    print('Your request has been made...... wait for 2 sec');
    sleep(2)
    clear()
    DML.trxn_wid()
        
  elif(choice==4):
    print('Your request has been made...... wait for 2 sec');
    sleep(2)
    clear()
    getBalance()

  elif(choice==5):
    print('Your request has been mad...... wait for 2 sec');
    sleep(2)
    clear()
    getDetails()

  elif(choice==6):
    print('Your requestion is processing...... wait for 2 sec');
    sleep(2)
    DDL.delete_acct()

  else:
    print("Thank you..... This terminal will get terminate in 3 seconds")
    sleep(3)
