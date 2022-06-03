from rich.console import Console
import time
from rich.traceback import install
install()
class c:
    def __init__(self):
        self.co=Console()
        self.style="yellow"
    def add(self,x,y):
        return x+y
C=c()

class changestyle:

    def __init__(self,C):
        self.C=C
        self.pre=C.style
        #print(self.pre)

        C.style="red"
    def __enter__(self):
        return self.C


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            ht=Console(record=True)
            ht.log("Execetion",log_locals=True)
            ht.print_exception()
            ht.save_html("{}.html".format(time.time()))

            C.co.print("Exception has been Handled,")




        C.style=self.pre
        return True

#def add(a, b):
 #   return a + b
C.co.print("status Code",100)
C.co.print("hi i am executing normal instructions",style=C.style)



with changestyle(C) as C:

    C.co.print("Hii from critical section",style=C.style)
    #1/0
    C.add(1,3)
    C.add(4,5)
    C.add(1,"awdwa")




C.co.print("Hii again executing normally",style=C.style)
C.co.print("status Code",100)