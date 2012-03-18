import sys
import wx.lib.newevent
from IntegrationFrame import IntegrationFrame


class ProcessEvent:
    StatusUpdate, EVT_STATUS_UPDATE = wx.lib.newevent.NewEvent()
    OnStepSuccess, EVT_STEP_SUCCESS = wx.lib.newevent.NewEvent()


class ProcessStep(object):
    def __init__(self):
        ##options: ASK, ABORT, CONTINUE
        self.onFailure = "ASK"
        #GUI widget corresponding to the step.
        self.widget = None
        self.panel = None
        self.isCont = False

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

    def setResponse(self, result):
        print "Executed Reply!!", result
        self.isCont = result

    def EntryPointWrapper(self, event):
        self.EntryPoint()

    def EntryPoint(self):
        #TODO: Create an event as this is a GUI code.
        self.widget.SetLabel(self.stepname)

        if self.PreCondition() == 0:
            self.ExecuteStep()

            if self.PostCondition() != 0:
                self.widget.SetBackgroundColour('red')
                self.widget.Update()
                if self.onFailure == "ABORT":
                    self.Abort()
                elif self.onFailure == "ASK":
                    print "Do you want to continue?"
                    msg = "Do you want to continue?"
                    self.isCont = IntegrationFrame.AskOnFailure(msg)
                    print "REPLY: ", self.isCont
                else:
                    print "Continue"
                    self.isCont = True
            else:
                print "SUCCESS", self.stepname
                self.isCont = True
                self.widget.SetBackgroundColour('green')
                self.widget.Update()

            print "Bye from EntryPoint"


class BasicSequencer(object):

    def __init__(self):
        self.steps = []
        self.cleanupfn = None
        self._next = -1

    def add(self, processStep):
        self.steps.append(processStep)

    def execute(self):
        for this_step in self.steps:
            this_step.widget.Disable()
            this_step.widget.SetBackgroundColour(wx.NullColour)
            this_step.widget.SetLabel(this_step.stepname)
            this_step.widget.Refresh()
            this_step.widget.Update()

        for this_step in self.steps:
            print "BasicSequencer", this_step.stepname
            event = ProcessEvent.StatusUpdate(status_msg=this_step.stepname)
            wx.PostEvent(this_step.frame, event)

            # Entry to the ProcessStep functionality
            this_step.EntryPoint()

            if this_step.isCont == False:
                print "BasicSequencer", this_step.stepname, "Failed"
                if self.cleanupfn != None:
                    self.cleanupfn()
                break

    def getNextStep(self):
        for this_step in self.steps:
            yield this_step

    def listSteps(self):
        return [thisstep.stepname for thisstep in self.steps]

    def setCleanUp(self, cleanfn):
        self.cleanupfn = cleanfn
