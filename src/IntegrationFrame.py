import wx
import Process


class IntegrationFrame(wx.Frame):
    def __init__(self, parent, fid, title, steps):
        wx.Frame.__init__(self, parent, fid, title=title, size=wx.DefaultSize)
        icon = wx.Icon("..\img\icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
        panel = wx.Panel(self, size=(1000, 1000))
        
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        panel.Bind(Process.ProcessEvent.EVT_ASK_ON_FAILURE, self.AskOnFailure)
        panel.Bind(Process.ProcessEvent.EVT_STEP_SUCCESS, self.StepSuccess)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Addition of process buttons
        self.processButtons = []
        for this_step in steps:
            print this_step.stepname
            thisbtn = wx.Button(panel, label=this_step.stepname,
                                size=(100, 30))
            this_step.widget = thisbtn
            this_step.panel = panel
            # Call process specific steps
            self.Bind(wx.EVT_BUTTON, this_step.EntryPoint, thisbtn)
            sizer.Add(thisbtn)
            
            # See if the objectives of the step are met. It met, show in green.
            if this_step.PostCondition() == 0:
                thisbtn.SetLabel(thisbtn.GetLabel()+" [Done]")
                thisbtn.SetBackgroundColour('yellow')

        self.SetSizerAndFit(sizer)

    def AskOnFailure(self, event):
        dlg = wx.MessageDialog(None, event.msg, "Failed", wx.YES_NO |
                               wx.ICON_QUESTION)
        retcode = dlg.ShowModal()
        print "INSIDE Ask Dialog"
        if retcode == wx.ID_YES:
            wx.CallAfter(event.reply, True)
        else:
            wx.CallAfter(event.reply, False)
        dlg.Destroy()

    def StepSuccess(self, event):
        event.widget.SetBackgroundColour(event.colour)

    def onCloseWindow(self, event):
        #wx.MessageBox("Thank you!")
        self.Destroy()
