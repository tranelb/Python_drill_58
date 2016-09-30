#Tech Academy python drill
#item 58 of 63

import shutil
import datetime
import pytz
import os
import os.path
import sys
from datetime import datetime
from datetime import date 

#check the contents of the local_I-O folder

tday = datetime.today()
t01_Year = int(str(tday)[:4])
#print "t01_Year is {}".format(t01_Year)
t01_Month = int(str(tday)[5:7])
#print "t01_Month is {}".format(t01_Month)
t01_Day = int(str(tday)[8:10])
#print "t01_Day is {}".format(t01_Day)
t01_date = date(t01_Year, t01_Month, t01_Day)


print "*-"*30
print "--ATTENTIION!!!!  THIS PROGRAM COPIES FILES AND IS BETA--"
print "--Feel free to click and drag the folders into this window--"
print "*-"*30

strtPath = raw_input('Enter start path\\folder: ')

#rawPath = r(strtPath)

dirs = os.listdir(strtPath)

dstPath = raw_input('Enter destination path\\folder: ')

#assign contents of folder to a list

# iterate through the list and check the created, modified, and accessed times of each file
#var = os.path.getctime('C:/Users/Tranel/Desktop/Folder_A/randomFile_04.txt')
#bar = os.path.getmtime('C:/Users/Tranel/Desktop/Folder_A/randomFile_04.txt')
for var in dirs:
    #for i in list:
    varN = strtPath + '\\' + var
    #varFLT = float(varN)
    #print varN
        
#for var in os.walk(dirs):
    #total_path = dirs + var
    print "#"*20
    ##print tb_test
    #print var
    #print dirs
    #print type(dirs)
    fileCTime = os.path.getctime(varN)
    whats_fileCTime = type(fileCTime)
    #print "The fileCTime var is a {} and looks like {}".format(whats_fileCTime,fileCTime)
    #print "The fileCTime var is {}".format(fileCTime)
    standardCtime = datetime.fromtimestamp(fileCTime).strftime('%Y-%m-%d %H:%M:%S')
    print "The created time of {} is {}".format(var, standardCtime)
    fileMTime = os.path.getmtime(varN)
    standardMtime = datetime.fromtimestamp(fileCTime).strftime('%Y-%m-%d %H:%M:%S')
    print "The modified time of {} is {}".format(var, standardMtime)
    dataList = [var,standardCtime,standardMtime,varN]
    cYear = int(dataList[1][:4])
    #print 'cYear = {}'.format(cYear)
    cMonth = int(dataList[1][5:7])
    #print 'cMonth = {}'.format(cMonth)
    cDay = int(dataList[1][8:10])
    #print 'cDay = {}'.format(cDay)
    f_date = date(cYear, cMonth,cDay)
    mYear = int(dataList[2][:4])
    mMonth = int(dataList[2][5:7])
    mDay = int(dataList[2][8:10])
    m_date = date(mYear, mMonth,mDay)
    
    #print "f_date looks like this -> {} and is {}".format(f_date, type(f_date))
    if f_date >= t01_date and m_date >= t01_date:
        print "====>>>Copied {} to {}<<<=====".format(var,dstPath)
        shutil.copy(varN, dstPath)
    elif f_date <= t01_date:
        print "====>>>The f_date of {} is older than today's date<<<=====".format(dataList[0])
    elif m_date <= t01_date:
        print "====>>>The m_date of {} is older than today's date<<<=====".format(dataList[0])
    else:
        print "<<<=====  huh? Moving on... =====>>>"
        pass

    
    
    
    
    #l_date = date(2014, 7, 11)
    #delta = l_date - f_date
    #print(delta.days)
    #shutil.move(varN, dstPath)

    

    







#print "tday = {} and is {}".format(tday, type(tday))


#print dataList
#n = 0
#for d in dataList:
#    n +=1
#    print "Item {} of dataList is {}".format(n, d)
    
    

#print f_date < t01_date

#print f_date > t01_date


#guess = f_date - t01_date

#print t01_date

#print "guess = {} and is  {}".format(guess, type(guess))

#print "t01_date = {} and is {}".format(guess, type(guess))



#testdelta = tday - fileCTime

# convert the times to standard times
#tb_test = datetime.fromtimestamp(bar).strftime('%Y-%m-%d %H:%M:%S') - creates a string


# if the times meet criteria, copy them to the destination folder
#if the created and/or time deltas are within a 24 hr period, copy them to the destination folder.
#if time delta of file is < 24hrs from current work date , copy file to dest folder
#if the modifed time and/or created time is !> 24hrs  
#check the date and the hours



#for i in dirs:
#    if i in varN:
#        shutil.move(varN, dstPath)

