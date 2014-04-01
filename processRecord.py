#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      green_pasture
#
# Created:     28/03/2014
# Copyright:   (c) green_pasture 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from datetime import datetime
import time
import sqlite3

class Employee:
    def __init__(self,name=None,code=None):
        self.name=name
        self.code=code

    def __str__(self):
        return '[%s]->[%s]' % (self.name,self.code)

db=sqlite3.connect('mydb')
cursor = db.cursor()

f1=open('record.txt','r+')
list1=[]
db=sqlite3.connect('mydb')
db.text_factory = str
cursor = db.cursor()
cursor.execute('''delete from employee where 1=1''')
db.commit()

for line1 in f1:
    record = line1.split()
    employee=Employee(record[0],record[1])
    #cursor.execute('''CREATE TABLE employee(name TEXT,code TEXT)''')
    cursor.execute(('''Insert into employee(name,code) values(?,?)'''),(record[0],record[1]))
    db.commit()
    list1.append(employee),
f1.close

cursor.execute('''select name,code from employee''')
all_rows = cursor.fetchall()
for row in all_rows:
    print('{0}:{1}'.format(row[0],row[1]))

class Record:
    def __init__(self,code=None,date=None,time=None,name=None):
        self.code=code
        self.date=date
        self.time=time
        self.name=name
    def __str__(self):
        return '[%s]->[%s]->[%s]->[%s]' % (self.code,self.date,self.time,self.name)

f2=open('r.txt','r+')
list2=[]
cursor.execute('''CREATE TABLE record(code TEXT,name TEXT,date TEXT,time TEXT)''')
db.commit()
cursor.execute('''delete from record where 1=1''')
db.commit()
for line2 in f2:
    a = line2.split()
    name = ""
    for employee in list1:
        if employee.code==a[2]:
            name=employee.name
            break
    if a[5]=="3/31/2014":
        record=Record(a[2],a[5],a[6],name)
        #print record
        cursor.execute('''Insert into record(code,name,date,time) values (?,?,?,?)''',(a[2],name,a[5],a[6]))
        db.commit()
        list2.append(record),
f2.close
list3=[]
cursor.execute('''select name,count(time) from record where
                        time(time)  between "6:59:00" and "8:01:00"
                      or time(time)  between "12:00:00" and "12:30:00"
                      or time(time)  between "13:00:00" and "13:30:00"
                      or time(time)  between "17:30:00" and "18:00:00"
                      group by name
                      having count(time)<3
                      order by name''')
all_rows = cursor.fetchall()
for row in all_rows:
   print row[0]
   list3.append(row[0])
   for record in list2:
       if record.name==row[0]:
           print(record.time)


for record in list2:
    #print record.time
    directory={}
    time0 = time.strptime(record.time,"%H:%M")
    if time0<(time.strptime('7:00',"%H:%M")) or (time0>time.strptime('8:00',"%H:%M") and time0<time.strptime('12:00',"%H:%M")) and record.name not in list3:
        print record
    if time0>time.strptime('13:30',"%H:%M") and time0<time.strptime('17:30',"%H:%M") and record.name not in list3:
        print record

db.close()

