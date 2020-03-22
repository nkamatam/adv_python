import logging

logging.basicConfig(filename = 'sq.log', level=logging.INFO, format='%(levelname)s:%(asctime)s:%(message)s')

def squ(num):
    return num * num

a=10
result_squ = squ(a)
logging.info('Square : {}  = {}'.format(a,result_squ))
