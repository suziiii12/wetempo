import vobject 
from datetime import datetime

event = ''


def make_ics(event):
    cal = vobject.iCalendar()
    vevent = cal.add('vevent')
    vevent.add('summary').value = u'event1'
    vevent.add('description').value = u'3명 참석 예정입니다.'
    vevent.add('dtstart').value = datetime(2024, 10, 19, 0, 0)
    vevent.add('dtend').value = datetime(2024, 10, 20, 0, 0)
    #생성시간
    vevent.add('dtstamp').value = datetime(2024, 10, 18, 0, 0)
    vevent.add('location').value = u'회의실'
    o = vevent.add('organizer')
    o.value = u'MAILTO:organizer@gmail.com'
    o.params['CN'] = [u'참석자']
    o = vevent.add('attendee')
    o.value = u'MAILTO:attendee1@gmail.com'
    o.params['CN'] = [u'참석자']
    o.params['ROLE'] = [u'REQ-PARTICIPANT']
    o = vevent.add('attendee')
    o.value = u'MAILTO:attendee1@gmail.com'
    o.params['CN'] = [u'참석자']
    o.params['ROLE'] = [u'OPT-PARTICIPANT']
    with open('example.ics', 'wb') as f:
        f.write(cal.serialize().encode('utf-8'))