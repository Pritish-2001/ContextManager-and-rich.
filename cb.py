from rich import print as r
import logging
logging.basicConfig(filename='employee.log',level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')



class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.val=0

        logging.info('created employee: {}-{}'.format(self.first,self.last))

        @property
        def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)

        @property
        def fname(self):
            return '{} {}'.format(self.first,self.last)

emp_1=Employee('John','Smitch')
emp2=Employee('Corey','Schafer')
emp3=Employee('jane','doo')

r(100)