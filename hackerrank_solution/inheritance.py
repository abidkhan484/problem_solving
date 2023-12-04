class myclass:
    greeting = ''
    def __init__(self, name='there'):
        self.greeting = name + '!'
    def sayhello(self):
        print ("hello {0}".format(self.greeting))

myInstance = myclass()
myInstance.sayhello()

myInstance = myclass("AbId")
myInstance.sayhello()
