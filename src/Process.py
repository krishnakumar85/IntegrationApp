import sys
import wx.lib.newevent


class ProcessEvent:
    AskOnFailure, EVT_ASK_ON_FAILURE = wx.lib.newevent.NewEvent()
    OnStepSuccess, EVT_STEP_SUCCESS = wx.lib.newevent.NewEvent()


class ProcessStep(object):
    def __init__(self):
        ##options: ASK, ABORT, CONTINUE
        self.onFailure = "ASK"
        #GUI widget corresponding to the step.
        self.widget = None
        self.frame = None
        self.isCont = []

    def ExecuteStep(self):
        print >>sys.stderr, \
        "Override ExecuteStep method to execute the desired functionality"

    def PreCondition(self):
        print >>sys.stderr, \
        "Override PreCondition method to execute the desired functionality"

    def PostCondition(self):
        print >>sys.stderr, \
        "Override PostCondition method to execute the desired functionality"

    def Abort(self):
        print >>sys.stderr, \
        "Override Abort method to execute the desired functionality"

    def Reply(self, result):
        print "Executed Reply!!", result

    def EntryPoint(self, event):
        #TODO: Create an event as this is a GUI code.
        self.widget.SetLabel(self.stepname)
        
        if self.PreCondition() == 0:
            self.ExecuteStep()

            if self.PostCondition() != 0:
                self.widget.SetBackgroundColour('red')
                if self.onFailure == "ABORT":
                    self.Abort()
                elif self.onFailure == "ASK":
                    print "Do you want to continue?"
                    event = ProcessEvent.AskOnFailure(msg="Do you want to continue?", reply=self.Reply)
                    wx.PostEvent(self.panel, event)
                    print "REPLY: ", self.isCont
                else:
                    print "Continue"
            else:
                print "SUCCESS", self.stepname
                event = ProcessEvent.OnStepSuccess(colour="green", widget=self.widget)
                wx.PostEvent(self.panel, event)

            print "Bye from EntryPoint"
