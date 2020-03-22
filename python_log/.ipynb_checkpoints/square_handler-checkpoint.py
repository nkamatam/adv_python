import logging

#create a logger specific for this module, and configure the same
#get a new logger with getlogger(name)
logger = logging.getLogger(__name__)

#set loglevel
logger.setLevel(logging.INFO)

#specify the formatting
formatter = logging.Formatter('%(levelname)s:%(name)s:%(asctime)s:%(message)s')

#specify the log file with a file handler
file_handler = logging.FileHandler('sq_new.log')
#add the formatter to the file_handler
file_handler.setFormatter(formatter)


#add the handlers to the logger
logger.addHandler(file_handler)



#logging.basicConfig(filename = 'sq.log', level=logging.INFO, format='%(levelname)s:%(asctime)s:%(message)s')

def squ(num):
    return num * num

a=10
result_squ = squ(a)
logger.info('Square : {}  = {}'.format(a,result_squ)) #log with the new logger
