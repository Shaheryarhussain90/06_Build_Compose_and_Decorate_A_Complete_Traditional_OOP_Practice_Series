

class logger:
    def __init__(self):
        print("loggerobject created")
    
    def __del__(self):
        print("logger object delet")

log = logger()
del log
