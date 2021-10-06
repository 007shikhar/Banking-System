import os


def trxn_dep():
  Name=input('Enter your name : : ')
  f=open(Name+'.txt','r')
  test_lines = f.readlines()
  pwd2=input('Enter your passsword : : ')
  
  if(pwd2 == test_lines[5].strip()):
    deposit=int(input('Enter the amount you want to deposit : : '))
    lineList = [line.rstrip('\n') for line in open(Name+'.txt')]
    lineList[6]=str(int(lineList[6])+deposit)
    f1=open(Name+'.txt','w')
    f1.writelines("%s\n" %place for place in lineList)
    print('\nAmount updated successfully!!')
    f1.close()
  else:
    print('\nIncorrect password, please try again!!')
  f.close()

def trxn_wid():
  Name=input('Enter your name :')
  f=open(Name+'.txt','r')
  test_lines = f.readlines()
  pwd2=input('Enter your passsword :')   
  if(pwd2 == test_lines[5].strip())   :
    wcash=int(input('Enter the amount to withdraw :'))
    if(int(test_lines[6])<wcash): 
      print('Insufficient Balance.Can not withraw')
    else :
      lineList = [line.rstrip('\n') for line in open(Name+'.txt')]
      lineList[6]=str(int(lineList[6])-wcash)
      f1=open(Name+'.txt','w')
      f1.writelines("%s\n" %place for place in lineList)
      
      print('\nAmount updated successfully\n')
      f1.close()
  else:
    print('incorrect password, please try again')
  f.close()
