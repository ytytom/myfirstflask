import time
import datetime
while True:
    time111 = datetime.datetime.now()
    # time222 = time.strftime()
    subject = time.strftime("%H:%M", time111)
    print time111
    print subject

    if subject > '17:23':
        print subject+"time is now "
        break
    else:
        print "17:23 time is big"




