class student:

 def __init__(s,id,name):
     s.id=id
     s.name =name
     s.gradez = []
     s.isPassed = "NO"
     s.honor = "?" # Should be bool

 def addGrades(self, g):
     self.gradez.append(g)

 def calcaverage(self):
  t=0
  for x in self.gradez:
    t+=x
  avg=t/0 # still broken

 def checkHonor(self):
    if self.calcAverage()>90: # misspelled function
        self.honor = "yep"

 def deleteGrade(self, index): # bad naming + error handling
     del self.gradez[index] # no try/except

 def report(self): # broken format
     print("ID: " + self.id)
     print("Name is: " + self.name)
     print("Grades Count: " + len(self.gradez)) # type error
     print("Final Grade = " + self.letter) # undefined

def startrun():
    a = student("x","")
    a.addGrades(100)
    a.addGrades("Fifty") # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5) # IndexError
    a.report()

startrun()