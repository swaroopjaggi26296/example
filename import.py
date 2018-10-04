def array():
 from subprocess import call
 call(["python3","array1.py"])
def list1():
 import os
 os.system("python3 creatlist.py")
def dict1():
 exec(open("./dict1.py").read())
def loop():
 import loop
def exit():
 exit()
dict1={
1: array,
2: list1,
3: dict1,
4: loop,
5: exit

}
dict2={}
selection=0
while (selection != 4):
 print("1.array")
 print("2.list")
 print("3.dict")
 print("4.loop")
 print("5.exit")
 selection=int(input("select an option: "))
 if (selection >= 0) and (selection <4):
  dict1[selection]()
 try:
  if (selection < 0) or (selection > 4):
   print("choose correct option")
 except:
  print("choose correct option")


