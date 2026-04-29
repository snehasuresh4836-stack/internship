import datetime
today=datetime.datetime.now()
from logsystem import *
try:
    print('line1')
    print('line2')
    print('line3')
    raise Exception('WE CREATED AN EXCEPTION IN OUR PROGRAM')
    print('line4')
    print('line5')
    print('line6')
except Exception as e:
   
    data='module login'+'#'+'exception handle file'+'#'+str(today)+'#'+str(e)
    write_log(data)
