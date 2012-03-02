import sys

class ProcessStep(object):
    def __init__(self):
        self.onFailure = "ASK" #options: ASK, ABORT, CONTINUE

    def ExecuteStep(self):
        print >>sys.stderr, "Override ExecuteStep method to execute the desired functionality"
    
    def PreCondition(self):
        print >>sys.stderr, "Override PreCondition method to execute the desired functionality"
        
    def PostCondition(self):
        print >>sys.stderr, "Override PostCondition method to execute the desired functionality"
        
    def EntryPoint(self, event):
        if self.PreCondition() == 0:
            self.ExecuteStep()
            
            if self.PostCondition() != 0:
                if self.onFailure == "ABORT":
                    self.Abort()
                elif self.onFailure == "ASK":
                    print "Do you want to continue?"
                else:
                    print "Continue"
            else:
                print "SUCCESS", self.stepname
                
        
class zeroCleanup(ProcessStep):
    pass

class oneParse(ProcessStep):
    def __init__(self, stepname, filename, version):
        ProcessStep.__init__(self)
        
        self.stepname = stepname
        self.filename = filename
        self.version = version

    def ExecuteStep(self):
        print "Parsing file"
        
    def PreCondition(self):
        print "Check if file is present"
        return 0
        
    def PostCondition(self):
        print "Check if build.bat is created"

class twoFetch(ProcessStep):
    def __init__(self, stepname, fetchname):
        self.stepname = stepname
        self.fetchname = fetchname

    def ExecuteStep(self):
        print "Fetching DLLs"