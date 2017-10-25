import appex,ui
import time

#v = ui.load_view()
v = ui.View(frame=(0,0,300,110))
v.name='hi'
dateLabel = ui.Label(frame=(6,6,150,20),font=('<System>',18),name='datelabel')
dateText = ui.Label(frame=(7,32,280,20),font=('<System>',18),alignment=ui.ALIGN_CENTER,name='datetext')
datefg = ui.Label(frame=(7,32,280,20),font=('<System>',18),name='datefg', bg_color='#87ffd7')
datebg = ui.Label(frame=(6,31,282,22),font=('<System>',18),name='datebg',border_color='#000000',border_width=1)
v.add_subview(dateLabel)

v.add_subview(datebg)
v.add_subview(datefg)
v.add_subview(dateText)

timeLabel = ui.Label(frame=(6,57,150,20),font=('<System>',18),name='timelabel')
timeText = ui.Label(frame=(7,82,280,20),font=('<System>',18),alignment=ui.ALIGN_CENTER,name='timetext')
timefg = ui.Label(frame=(7,82,280,20),font=('<System>',18),name='timefg',bg_color='#87ffd7')
timebg = ui.Label(frame=(6,81,282,22),font=('<System>',18),name='timebg',border_color='#000000',border_width=1)

v.add_subview(timeLabel)
v.add_subview(timefg)
v.add_subview(timebg)
v.add_subview(timeText)

#v = ui.load_view()
now = time.localtime(time.time())
nowDay = "%4d年%02d月%02d日" % (now.tm_year,now.tm_mon,now.tm_mday)
v['datelabel'].text = nowDay
year = now.tm_year
if ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
	daysOfThisYear = 366
else:
	daysOfThisYear = 365
percentageOfYear = now.tm_yday / daysOfThisYear
#print (percentageOfYear)
#v['datefg'].frame=(7,35,round(percentageOfYear,3) * 280,20)
v['datefg'].width *= round(percentageOfYear,3)
v['datetext'].text = str(round(percentageOfYear,3)*100)+'%'

nowTime = "%02d:%02d:%02d" % (now.tm_hour,now.tm_min,now.tm_sec)
v['timelabel'].text = nowTime
secOfPastDay = now.tm_hour * 60 * 60 + now.tm_min * 60 + now.tm_sec
secOfADay = 24 * 60 * 60
percentageOfDay = secOfPastDay / secOfADay
#v['timefg'].frame = (6,91,round(percentageOfDay,3) * 280,20)
v['timefg'].width *= round(percentageOfDay,3)
v['timetext'].text = str(round(percentageOfDay,3)*100)+'%'
#print(percentageOfDay*100)

appex.set_widget_view(v)
#v.present('sheet')
