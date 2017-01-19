class company():
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__datelast = None

    def getname(self):
        return self.__name

    def getemail(self):
        return self.__email

    def getdatelast(self):
        return self.__datelast

    def setdatelast(self,d):
        self.__datelast = d
    
class prao(company):
    def __init__(self, name, email):
        super().__init__(name, email)

