import sys

class ProcessStep(object):
    def __init__(self):
        self.onFailure = "ASK" #options: ASK, ABORT, CONTINUE
        self.widget = None #GUI widget corresponding to the step.

    def ExecuteStep(self):
        print >>sys.stderr, "Override ExecuteStep method to execute the desired functionality"
    
    def PreCondition(self):
        print >>sys.stderr, "Override PreCondition method to execute the desired functionality"
        
    def PostCondition(self):
        print >>sys.stderr, "Override PostCondition method to execute the desired functionality"
        
    def Abort(self):
        print >>sys.stderr, "Override Abort method to execute the desired functionality"

    def EntryPoint(self, event):
        
        print dir(event.GetClientObject)
        if self.PreCondition() == 0:
            self.widget.SetBackgroundColour('green')
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
