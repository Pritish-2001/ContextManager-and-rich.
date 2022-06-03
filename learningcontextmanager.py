class Open_file():
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exec_type,exc_val,traceback):
        self.file.close()
        


with Open_file('sample.txt','w') as f:
    f.write('Testing')
print(f.closed)




from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
    try:
        f=open(file,mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt','w') as f:
    f.write('hi there i am testing context manager f based')
    print(1/0)
    


import os

@contextmanager
def change_dir(destination):
    try:
        cwd=os.getcwd()
        os.chdir(destination)
        yield

    finally:
        os.chdir(cwd)



with change_dir('C:\\numpy_satellite'):
    print(os.listdir())

print(len(os.listdir()))        

with change_dir('C:\\numpy_satellite\\.ipynb_checkpoints'):
    print(os.listdir())
    


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before')
        return original_function()
    return wrapper_function

def display():
    print('display ran')
d=decorator_function(display)
d()

















