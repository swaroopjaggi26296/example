def construct():
 print("enter how many key's u need")
 while True:
  try:
   x=int(input())
   break
  except:
   print("wrong input, give integer value")
 while x>0:
  key=input("enter the key:")
  item=input("enter the item:")
  x-=1
  dict2[key]=item
 dict2.update()
 print(dict2)

def add():
 key=input("Enter the key:")
 item=input("Enter the value of key:")
 dict2[key]=item
 print(dict2)
def remove():
 key=input("Enter the key to be removed:")
 try:
  del dict2[key]
  print(dict2)
 except Exception:
  remove()
 
def clear():
 dict2.clear()
 print(dict2)
def exit():
 exit()
dict1={
0: construct,
1: add,
2: remove,
3: clear,
4: exit

}
dict2={}
selection=0
while (selection != 4):
 print("0.construct")
 print("1.add")
 print("2.remove")
 print("3.clear")
 print("4.exit")
 selection=int(input("select an option: "))
 if (selection >= 0) and (selection <4):
  dict1[selection]()
 try:
  if (selection < 0) or (selection > 4):
   print("choose correct option")
 except:
  print("choose correct option")


