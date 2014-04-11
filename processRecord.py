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
import sys
db=sqlite3.connect('db')
cursor = db.cursor()
db.text_factory = str

class Employee:
    def __init__(self,name=None,code=None):
        self.name=name
        self.code=code

    def __str__(self):
        return '[%s]->[%s]' % (self.name,self.code)

f1=open('record.txt','r+')
list1=[]
#cursor.execute('''CREATE TABLE employee(name TEXT,code TEXT)''')
cursor.execute('''delete from employee where 1=1''')
db.commit()


for line1 in f1:
    record = line1.split()
    employee=Employee(record[0],record[1])
    cursor.execute(('''Insert into employee(name,code) values(?,?)'''),(record[0],record[1]))
    db.commit()
    list1.append(employee),
f1.close


cursor.execute('''select name,code from employee''')
all_rows = cursor.fetchall()
#for row in all_rows:
    #print('{0}:{1}'.format(row[0],row[1]))

today=sys.argv[1]
try:
    sys.argv[2]
except NameError:
    reg = 'reg.txt'
else:
    reg = sys.argv[2]

class Record:
    def __init__(self,code=None,date=None,time=None,name=None):
        self.code=code
        self.date=date
        self.time=time
        self.name=name
    def __str__(self):
        return '%s\t%s\t%s\n' % (self.name,self.date,self.time)

f2=open('r.txt','r+')
list2=[]
#cursor.execute('''CREATE TABLE record(code TEXT,name TEXT,date TEXT,time TEXT)''')
#db.commit()
cursor.execute('''delete from record where 1=1''')
db.commit()

for line2 in f2:
    name = ""
    for employee in list1:
        a = line2.split()
        if employee.code==a[2]:
            name=str(employee.name)
            break
    if a[5]==today:
        record=Record(a[2],a[5],a[6],name)
        cursor.execute('''Insert into record(code,name,date,time) values (?,?,?,?)''',(a[2],name,a[5],a[6]))
        db.commit()
        list2.append(record),
f2.close

class Regular:
    def __init__(self,code=None,name=None,start_time=None,end_time=None,type=None):
        self.code=code
        self.name=name
        self.start_time=start_time
        self.end_time=end_time
        self.type=type
    def __str__(self):
        return '[%s]->[%s]->[%s]->[%s]->[%s]' % (self.code,self.name,self.start_time,self.end_time,self.type)


"""
cursor.execute('''Drop table regular''')
db.commit()

cursor.execute('''CREATE TABLE regular(code TEXT,name TEXT,start_time TEXT,
  end_time TEXT,type TEXT)''')
db.commit()


cursor.execute('''delete from regular where 1=1''')
db.commit()
for employee in list1:
    cursor.execute('''Insert into regular(code,name,start_time,end_time,type) values (?,?,?,?,?)''',(employee.code,employee.name,'08:00:00','12:00:00','m'))
    db.commit()
    cursor.execute('''Insert into regular(code,name,start_time,end_time,type) values (?,?,?,?,?)''',(employee.code,employee.name,'13:30:00','17:30:00','n'))
    db.commit()
    cursor.execute('''Insert into regular(code,name,start_time,end_time,type) values (?,?,?,?,?)''',(employee.code,employee.name,'21:00:00','06:00:00','s1'))
    db.commit()
    cursor.execute('''Insert into regular(code,name,start_time,end_time,type) values (?,?,?,?,?)''',(employee.code,employee.name,'21:00:00','06:00:00','s2'))
    db.commit()
    cursor.execute('''Insert into regular(code,name,start_time,end_time,type) values (?,?,?,?,?)''',(employee.code,employee.name,'21:00:00','06:00:00','l'))
    db.commit(),
cursor.execute('''select name,code,start_time,end_time,type from regular''')
all_rows = cursor.fetchall()
for row in all_rows:
    print('{0}:{1}:{2}:{3}:{4}'.format(row[0],row[1],row[2],row[3],row[4]))
"""

f3=open(reg,'r+')

for line3 in f3:
    a = line3.split()
    #print line3
    name = ""
    for employee in list1:
        if employee.name==a[0]:
            code=employee.code
            cursor.execute('''delete from regular where code=? and type=?''',(code,a[3]))
            db.commit()
            cursor.execute('''Insert into regular(code,name,start_time,end_time,type) values (?,?,?,?,?)''',(code,a[0],a[1],a[2],a[3]))
            db.commit(),
            break
    regular=Regular(code,a[0],a[1],a[2],a[3])

    #print regular


f3.close

list3=[]
out=open('out.txt','w')
for employee in list1:
    name= employee.name
    code= employee.code
    query =cursor.execute('''select start_time,end_time from regular where name=? and type='m' ''',(name,))
    mtime = query.fetchone()
    m_start = mtime[0]
    m_end = mtime[1]
    #print m_start
    #print "\n",
    query =cursor.execute('''select start_time,end_time from regular where name=? and type='n' ''',(name,))
    ntime = query.fetchone()
    n_start = ntime[0]
    n_end = ntime[1]
    #print n_start
    #print "\n",
    query =cursor.execute('''select start_time,end_time from regular where name=? and type='s1' ''',(name,))
    s1time = query.fetchone()
    if s1time is  None:
        s1_start="20:00:00"
        s1_end="06:00:00"
        #print "no class\n",
    else:
        s1_start = s1time[0]
        s1_end = s1time[1]
        #print s1_start
        #print "\n",
    query =cursor.execute('''select start_time,end_time from regular where name=? and type='s2' ''',(name,))
    s2time = query.fetchone()
    if s2time is  None:
        s2_start="20:00:00"
        s2_end="06:00:00"
        #print "no class2\n",
    else:
        s2_start=s2time[0]
        s2_end = s2time[1]
        #print s2_start
        #print "\n",

    query =cursor.execute('''select start_time,end_time from regular where name=? and type='l' ''',(name,))
    ltime = query.fetchone()
    if ltime is  None:
        l_start="20:00:00"
        l_end="06:00:00"
        #print "no leave\n",
    else:
        l_start = ltime[0]
        l_end = ltime[1]
        #print l_start
        #print "\n",
 
    if time.strptime(m_start,"%H:%M:%S")>time.strptime(s1_start,"%H:%M:%S") or time.strptime(m_start,"%H:%M:%S")>time.strptime(l_start,"%H:%M:%S"):
        print "\n",
    else:
        all_rows =cursor.execute('''select rec.name from record rec,regular reg where rec.code=reg.code
                        and (time(time) between time(reg.start_time,'-30 Minute') and  time(reg.start_time))
                        and reg.type='m' and rec.name=? ''',(name,))
        if cursor.fetchone() is None:
            if employee  in list3:
                print(",  no record on "+today+" in 30 minutes before morning starts\n")
                #out.write(",  no record on "+today+" in 30 minutes before morning starts\n"),
            else:
                print(employee.name+", you have no record on "+today+" in 30 minutes before morning starts\n")
                #out.write(employee.name+",you have  no record on "+today+" in 30 minutes before morning starts\n")
                list3.append(employee),
    if (time.strptime(m_end,"%H:%M:%S")>time.strptime(s1_start,"%H:%M:%S") and time.strptime(m_end,"%H:%M:%S")<time.strptime(s1_end,"%H:%M:%S")) or (time.strptime(m_end,"%H:%M:%S")>time.strptime(s2_start,"%H:%M:%S") and time.strptime(m_end,"%H:%M:%S")<time.strptime(s2_end,"%H:%M:%S")) or (time.strptime(m_end,"%H:%M:%S")>time.strptime(l_start,"%H:%M:%S") and time.strptime(m_end,"%H:%M:%S")<time.strptime(l_end,"%H:%M:%S")):
        print "\n",
    else:
        all_rows =cursor.execute('''select rec.name from record rec,regular reg where rec.code=reg.code
                        and (time(time) between time(reg.end_time) and  time(reg.end_time,'+30 Minute'))
                        and reg.type='m' and rec.name=? ''',(name,))
        if cursor.fetchone() is None:
            if employee  in list3:
                 print(",  no record on "+today+" in 30 minutes after morning ends\n")
                 #out.write(", no record on "+today+" in 30 minutes after morning ends\n"),
            else:
                print(employee.name+", you have no record on "+today+" in 30 minutes after morning ends\n")
                #out.write(employee.name+", you have no record on "+today+" in 30 minutes after morning ends\n")
                list3.append(employee),

    if (time.strptime(n_start,"%H:%M:%S")>time.strptime(s1_start,"%H:%M:%S") and time.strptime(n_start,"%H:%M:%S")<time.strptime(s1_end,"%H:%M:%S")) or (time.strptime(n_start,"%H:%M:%S")>time.strptime(s2_start,"%H:%M:%S") and time.strptime(n_start,"%H:%M:%S")<time.strptime(s2_end,"%H:%M:%S")) or (time.strptime(n_start,"%H:%M:%S")>time.strptime(l_start,"%H:%M:%S") and time.strptime(n_start,"%H:%M:%S")<time.strptime(l_end,"%H:%M:%S")):
        print "\n",
    else:
        all_rows =cursor.execute('''select rec.name from record rec,regular reg where rec.code=reg.code
                        and (time(time) between time(reg.start_time,'-30 Minute') and  time(reg.start_time))
                        and reg.type='n' and rec.name=? ''',(name,))
        if cursor.fetchone() is None:
            if employee in list3:
                 print(", no record on "+today+" in 30 minutes before afternoon starts\n")
                 #out.write(", no record on "+today+" in 30 minutes before afternoon starts\n"),
            else:
                print(employee.name+", you have no record on "+today+" in 30 minutes before afternoon starts\n")
                #out.write(employee.name+", you have no record on "+today+" in 30 minutes before afternoon starts\n")
                list3.append(employee),


    if (time.strptime(n_end,"%H:%M:%S")<time.strptime(s1_end,"%H:%M:%S")) or (time.strptime(n_end,"%H:%M:%S")<time.strptime(s2_end,"%H:%M:%S")) or (time.strptime(n_end,"%H:%M:%S")<time.strptime(l_end,"%H:%M:%S")):
        print "\n",
    else:
        all_rows =cursor.execute('''select rec.name from record rec,regular reg where rec.code=reg.code
                        and (time(time) between time(reg.end_time) and  time(reg.end_time,'+30 Minute'))
                        and reg.type='n' and rec.name=? ''',(name,))
        if cursor.fetchone() is None:
            if employee in list3:
                 print(", no record on "+today+" in 30 minutes after afternoon ends\n")
                 #out.write(", no record on "+today+" in 30 minutes after afternoon ends\n"),
            else:
                print(employee.name+", you have no record on "+today+" in 30 minutes after afternoon ends\n")
                #out.write(employee.name+", you have no record on "+today+" in 30 minutes after afternoon ends\n")
                list3.append(employee),

    if employee in list3:
        count=0
        for record in list2:
            if record.name==employee.name:
                name= employee.name
                code= employee.code
                query =cursor.execute('''select start_time,end_time from regular where name=? and type='m' ''',(name,))
                mtime = query.fetchone()
                m_start = mtime[0]
                m_end = mtime[1]
                #print m_start
                #print "\n",
                query =cursor.execute('''select start_time,end_time from regular where name=? and type='n' ''',(name,))
                ntime = query.fetchone()
                n_start = ntime[0]
                n_end = ntime[1]
                #print n_start
                #print "\n",
                query =cursor.execute('''select start_time,end_time from regular where name=? and type='s1' ''',(name,))
                s1time = query.fetchone()
                if s1time is  None:
                    s1_start="20:00:00"
                    s1_end="06:00:00"
                    #print "no class\n",
                else:
                    s1_start = s1time[0]
                    s1_end = s1time[1]
                    #print s1_start
                    #print "\n",
                query =cursor.execute('''select start_time,end_time from regular where name=? and type='s2' ''',(name,))
                s2time = query.fetchone()
                if s2time is  None:
                    s2_start="20:00:00"
                    s2_end="06:00:00"
                    #print "no class2\n",
                else:
                    s2_start = s2time[0]
                    s2_end = s2time[1]
                    #print s2_start
                    #print "\n",

                query =cursor.execute('''select start_time,end_time from regular where name=? and type='l' ''',(name,))
                ltime = query.fetchone()
                if ltime is  None:
                    l_start="20:00:00"
                    l_end="06:00:00"
                    #print "no leave\n",
                else:
                    l_start = ltime[0]
                    l_end = ltime[1]
                    #print l_start
                    #print "\n",
                
                if  ( (time.strptime(record.time,"%H:%M:%S")>time.strptime(m_start,"%H:%M:%S") ) and ( time.strptime(record.time,"%H:%M:%S") < time.strptime(m_end,"%H:%M:%S") ) ):
                    if ( (time.strptime(record.time,"%H:%M:%S")<time.strptime(s1_start,"%H:%M:%S") ) or ( time.strptime(record.time,"%H:%M:%S") > time.strptime(s1_end,"%H:%M:%S") ) ):
                        if  ( (time.strptime(record.time,"%H:%M:%S")<time.strptime(s2_start,"%H:%M:%S") ) or ( time.strptime(record.time,"%H:%M:%S") > time.strptime(s2_end,"%H:%M:%S") ) ):
                           if ( (time.strptime(record.time,"%H:%M:%S")<time.strptime(l_start,"%H:%M:%S") ) or ( time.strptime(record.time,"%H:%M:%S") > time.strptime(l_end,"%H:%M:%S") ) ):
                                #out.write(" have record in the morning during working time\n")
                                print " have record in the morning during working time\n",
                if  ( (time.strptime(record.time,"%H:%M:%S")>time.strptime(n_start,"%H:%M:%S") ) and ( time.strptime(record.time,"%H:%M:%S") < time.strptime(n_end,"%H:%M:%S") ) ):
                    if ( (time.strptime(record.time,"%H:%M:%S")<time.strptime(s1_start,"%H:%M:%S") ) or ( time.strptime(record.time,"%H:%M:%S") > time.strptime(s1_end,"%H:%M:%S") ) ):
                        if ( (time.strptime(record.time,"%H:%M:%S")<time.strptime(s2_start,"%H:%M:%S") ) or ( time.strptime(record.time,"%H:%M:%S") > time.strptime(s2_end,"%H:%M:%S") ) ):
                            if ( (time.strptime(record.time,"%H:%M:%S")<time.strptime(l_start,"%H:%M:%S") ) or ( time.strptime(record.time,"%H:%M:%S") > time.strptime(l_end,"%H:%M:%S") ) ):
                                #out.write(" have record in the afternoon during working time\n")
                                print " have record in the afternoon during working time\n",
                print record 
                out.write(str(record))
                """   
                if ( (time.strptime(record.time,"%H:%M:%S")>time.strptime("07:30:00","%H:%M:%S") ) and ( time.strptime(record.time,"%H:%M:%S") < time.strptime("12:30:00","%H:%M:%S") ) ):
                    count=count+1
                    out.write(str(record)),
                if  ( (time.strptime(record.time,"%H:%M:%S")>time.strptime("13:00:00","%H:%M:%S") ) and ( time.strptime(record.time,"%H:%M:%S") < time.strptime("18:00:00","%H:%M:%S") ) ):
                    count=count+1
                    out.write(str(record)),
        if count==0:       
            out.write(employee.name+"\n")
            """
out.close()
db.close()


