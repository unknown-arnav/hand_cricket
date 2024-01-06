import random as r
s=0
tr=0
#toss start
print("toss")
ml=[1,2,3,4,5,6]
#toss choice start
tc=r.randint(1,2)
if tc==1 :
  tcc=r.randint(0,1)
  if tcc==0:
    print("my call is even")
    td=0
  elif tcc==2:
    print("my call is odd")
    td=1
elif tc==2:
  print("what's your call")
  td=int(input("press 0 for EVEN and 1 for ODD"))
  if td !=1 and td!=0:
    print('you have entered an invalid input')
    td=int(input("press 0 for EVEN and 1 for ODD"))
#toss choice end
#toss decision
compch=r.randint(1,6)
userch=int(input('your (between 1 to 6):'))
if userch>6 or userch<1:
  print("invalid input")
  userch=int(input('your (between 1 to 6):'))
print("my : ",compch)
s=compch+userch
print("total= ",s)
if s%2==0:
  tr=0
elif s%2==1:
  tr=1
if tc==1 :
  if tr==td :
    print ("i won the toss")
    tosscompch=r.randint(0,1)
    if tosscompch==0:
      print("i choose to bat")
      comp1r=1
      user1r=0
    elif tosscompch==1:
      print("i choose to ball")
      comp1r=0
      user1r=1
  elif tr!=td :
    print("you won the toss")
    user1r=int(input("your choice(1 for batting , 0 for bowling)"))
    if user1r==0:
      comp1r=1
      print("my batting")
    elif user1r==1:
      comp1r=0
      ("my bowling")
    else:
      print("invalid input")
      user1r=int(input("your choice(1 for batting , 0 for bowling)"))
elif tc==2:
  if tr!=td :
    print ("i won the toss")
    tosscompch=r.randint(0,1)
    if tosscompch==0:
      print("i choose to bat")
      comp1r=1
      user1r=0
    elif tosscompch==1:
      print("i choose to ball")
      comp1r=0
      user1r=1
  elif tr==td :
    print("you won the toss")
    user1r=int(input("your choice(1 for batting , 0 for bowling)"))
    if user1r==0:
      comp1r=1
      print("my batting")
    elif user1r==1:
      comp1r=0
      ("my bowling")
    else:
      print("invalid input")
      user1r=int(input("your choice(1 for batting , 0 for bowling)"))
#toss over
#match begins
compsc=0
usersc=0
inn=1
tar=0
while inn<3:
  userch=int(input('your (between 1 to 6):'))
  if userch>6 and userch<1:
    print("invalid input. please enter a number between 1 and 6")
    userch=int(input('your (between 1 to 6):'))
  compch=r.randint(1,6)
  print('my : ',compch)
#out coding
  if userch==compch :
    if comp1r==1 :
      print("i am out now it's your batting")
      user1r=1
      comp1r=0
      inn+=1
      if inn==2:
        print("your target: ",compsc+1)
        tar=compsc+1
      elif inn==3:
        if compsc<tar:
          print('you won the match')
          break
    elif user1r==1:
      print("you are out now it's my batting")
      comp1r=1
      user1r=0
      inn+=1
      if inn==2:
        print("my target: ",compsc+1)
        tar=usersc+1
      elif inn==3:
        if usersc<tar:
          print('you lost the match')
          break
  elif userch!=compch:
    if comp1r==1 :
      compsc+=compch
      print("my total runs= ",compsc)
      if compsc>=tar and inn==2 :
        print('you lost')
        break
      if inn==2:
        print("i need ",tar-compsc," more runs to win")
    elif user1r==1:
      usersc+=userch
      print("your total score =",usersc)
      if usersc>=tar and inn==2:
        print('you won')
        break
      if inn==2:
        print("you need ",tar-usersc," more runs to win")
