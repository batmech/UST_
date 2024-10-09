import xlwt

loc = 'C:\\Users\\287936\\UST-Training\\Day5\\Students.xls'
wb = xlwt.Workbook()
ws = wb.add_sheet('StudentDetails')

ws.write(0, 0, 'Name')
ws.write(0, 1, 'Age')
row = 1
while True:
    name = input('Enter name (type "exit" to end): ')
    if name.lower() == 'exit': break
    
    age = int(input("Enter age: "))
    
    ws.write(row, 0, name)
    ws.write(row, 1, age)
    row += 1

wb.save(loc)