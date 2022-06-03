import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
    return x+y

def sub(x,y):
    return x-y
num1=10
num2=5
addres=add(num1,num2)

logging.debug('Add {}+ {}={}'.format(num1,num2,addres))

subress=sub(num1,num2)
logging.warning('Sub {}-{}={}'.format(num1,num2,subress))

