import wx
import Process


class IntegrationFrame(wx.Frame):
    def __init__(self, parent, fid, title, steps):
        wx.Frame.__init__(self, parent, fid, title=title, size=wx.DefaultSize)
        panel = wx.Panel(self, size=(1000, 50))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        panel.Bind(Process.ProcessEvent.EVT_ASK_ON_FAILURE, self.AskOnFailure)

        self.processButtons = []
        for this_step in steps:
            print this_step.stepname
            thisbtn = wx.Button(panel, label=this_step.stepname,
                                size=(100, 30))
            this_step.widget = thisbtn
            this_step.panel = panel
            self.Bind(wx.EVT_BUTTON, this_step.EntryPoint, thisbtn)
            sizer.Add(thisbtn)
            if this_step.PreCondition() != 0:
                thisbtn.Disable()

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

    def onCloseWindow(self, event):
        #wx.MessageBox("Thank you!")
        self.Destroy()
