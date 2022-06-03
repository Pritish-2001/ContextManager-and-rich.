class cont:
    def __init__(self,filename,mode):
        self.f=filename
        self.m=mode

    def __enter__(self):
        f=open(self.f,self.   m)
        f.seek(10,2)
        return f
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        f.close()
        return True

with cont("f.txt",'a') as f:
    f.write("hi there bro")

print("hello")



