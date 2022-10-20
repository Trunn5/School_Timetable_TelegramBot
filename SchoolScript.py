from datetime import datetime
import time
import codecs

def Calls():
    CallsTimeFile = open('callstime.txt','r')
    text = CallsTimeFile.read()
    return text

def TimeTable(n):
    day = (datetime.today().weekday() + n) % 7
    if day == 5 or day == 6:
        if n == 0:
            return 'Сегодня уроки не идут😴🥱'
        return 'Завтра уроки не идут😴🥱'
    TimeTableFile = codecs.open('timetable.txt','r','utf-8')
    text = TimeTableFile.readlines()[day*8:(day+1)*8]
    responce = ''
    for i in text:
        responce += i
    return responce

def WhenCall():
    CallsTimeFile = open('callstime.txt','r')
    text = CallsTimeFile.readlines()
    TIME = int(time.strftime("%H")) * 60 + int(time.strftime("%M"))
    m = []
    for lesson in text:
        lesson = lesson[3:].replace('\n', '').split('-')
        m.append(lesson[0])
        m.append(lesson[1])
    for i in range(len(m)-1):
        time1 = int(m[i].split(':')[0]) * 60 + int(m[i].split(':')[1])
        time2 = int(m[i+1].split(':')[0]) * 60 + int(m[i+1].split(':')[1])
        if TIME >= time1 and TIME <= time2:
            return f"Звонок через {(60+time2%60-TIME%60)%60} минут!"
    return "Уроки не идут😴🥱"
        
