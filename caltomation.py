from datetime import datetime
import caldav
from caldav.elements import dav, cdav
from icalendar import cal
import os

# Caldav url
url = os.environ['CALURL']

client = caldav.DAVClient(url)
principal = client.principal()
calendars = principal.calendars()

for calendar in calendars:
    print "Calendar : %s"%calendar
    print "Looking for events"
    for rawevt in calendar.events():
        calevent = cal.Calendar.from_ical(rawevt.data)
        event = calevent.walk('VEVENT')[0]
        print "%s - %s"%(event['DTSTART'].dt,event['SUMMARY'])