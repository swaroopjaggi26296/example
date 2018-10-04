import xlrd
sheet_data=[]
found=[]
rows_to_be_saved=[]
loc=(r"/home/test/Downloads/C2-seat-allocation.xls")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0) 
value=[]
while True:
 team_name=input("Enter the team name:\n1.ODH\n2.EYE-BALL\n3.DEVOPS\n4.others\n5.NA\n")
 try:
  if team_name == "ODH":
   for x in range(sheet.nrows):
    if sheet.cell_value(x,2)=="ODH":
     k=x
     value.append(sheet.cell_value(x,0))
     value.append(sheet.cell_value(x,1))
   print(value)
  elif team_name == "EYE-BALL":
    for x in range(sheet.nrows):
     if sheet.cell_value(x,2)=="EYE-BALL":
      k=x
      value.append(sheet.cell_value(x,0))
      value.append(sheet.cell_value(x,1))
    print(value)
  elif team_name == "DEVOPS":
    for x in range(sheet.nrows):
     if sheet.cell_value(x,2)=="DEVOPS":
      k=x
      value.append(sheet.cell_value(x,0))
      value.append(sheet.cell_value(x,1))
    print(value)
  elif team_name == "others":
    for x in range(sheet.nrows):
     if sheet.cell_value(x,2)=="others":
      k=x
      value.append(sheet.cell_value(x,0))
      value.append(sheet.cell_value(x,1))  
    print(value)
  elif team_name == "NA":
    for x in range(sheet.nrows):
     if sheet.cell_value(x,2)=="NA":
      k=x
      value.append(sheet.cell_value(x,0))
      value.append(sheet.cell_value(x,1))
    print(value)
 finally:
  print("Enter proper team name")
  
  

