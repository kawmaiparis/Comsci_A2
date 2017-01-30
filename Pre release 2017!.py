import datetime

class Test:
    def __init__(self, testid):
        self.__testid = testid
        self.__questions = []
        self.__noofq = 0
        self.__maxmarks = 0
        self.__level = None
        self.__date = datetime.datetime.now()

    def DesignTest(self):
        testid = input("Test id: ")
        self.__testid = testid
        
        while True:
            level = input("Level?(A,S,G) :")
            if level.upper() in ['A','S','G']:
                self.__level = level
                break
            else: 
                print("error input")

        
        qno = 0
        totalmarks = 0
        print("set question to 'x' to stop adding questions")
        while qno < 10:
            text = input("question: ")
            if text == 'x':
                break
            answer = input("answer: ")
            topic = input("topic: ")
            marks = input("marks: ")
            
            totalmarks += int(marks)
            self.__maxmarks = totalmarks

            qid = self.__testid + str(qno)
            newQ = Question()
            newQ.SetQuestion(qid, text, answer, marks, topic)
            self.__questions.append(newQ)
            
            qno += 1

    def PrintTest(self):
        for question in self.__questions:
            print(question.GetQuestion())

    def PrintAnswers(self):
        for question in self.__questions:
            print(question.GetAnswer())
        

class Question:
    def __init__(self):
        self.__questionid = None
        self.__questiontext = None
        self.__answer = None
        self.__marks = None
        self.__topic = None

    def SetQuestion(self, ID, text, answer, marks, topic):
        self.__questionid = ID
        self.__questiontext = text
        self.__answer = answer
        self.__marks = marks
        self.__topic = topic

    def GetQuestion(self):
        return self.__questiontext

    def GetMarks(self):
        return self.__marks

    def GetTopic(self):
        return self.__topic

    def GetAnswer(self):
        return self.__answer

newtest = Test("OOP")
newtest.DesignTest()
newtest.PrintTest()
newtest.PrintAnswers()
    
