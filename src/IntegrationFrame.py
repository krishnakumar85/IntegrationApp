import wx
import Process
import images

ID_PLAY = wx.NewId()
ID_STOP = wx.NewId()


class IntegrationFrame(wx.Frame):
    def __init__(self, parent, fid, title, sequencer):
        self.sequencer = sequencer

        wx.Frame.__init__(self, parent, fid, title=title, size=wx.DefaultSize)
        icon = wx.Icon("..\img\icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        panel = wx.Panel(self, -1)

        self.BuildToolBar()
        self.statusbar = self.CreateStatusBar()

        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        panel.Bind(Process.ProcessEvent.EVT_STEP_SUCCESS, self.StepSuccess)
        self.Bind(Process.ProcessEvent.EVT_STATUS_UPDATE, self.OnStatusUpdate)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.statusbar.SetStatusText("Ready.")

        self.StartWorker()

        # Addition of process buttons
        self.processButtons = []
        for this_step in sequencer.steps:
            print this_step.stepname
            thisbtn = wx.Button(panel, label=this_step.stepname,
                                size=(100, 30))
            this_step.widget = thisbtn
            this_step.panel = panel
            this_step.frame = self
            # Call process specific steps
            self.Bind(wx.EVT_BUTTON, this_step.EntryPointWrapper, thisbtn)
            sizer.Add(thisbtn)

            # See if the objectives of the step are met. It met, show in green.
            if this_step.PostCondition() == 0:
                thisbtn.SetLabel(thisbtn.GetLabel() + " [Done]")
                thisbtn.SetBackgroundColour('yellow')

        self.SetSizerAndFit(sizer)

    def BuildToolBar(self):
        toolbar = self.CreateToolBar()
        toolbar.AddSimpleTool(ID_PLAY, images.GetBitmap_Play_png(), "Start",
                              "Start with integration")
        #toolbar.AddTool(ID_PLAY, images.GetBitmap_Play_png(), isToggle=True)
        wx.EVT_TOOL(self, ID_PLAY, self.OnPlay)
        toolbar.Realize()

    def StartWorker(self):
        import Worker
        self.wthread = Worker.Worker()
        self.wthread.start()

    def OnPlay(self, event):
        print "OnPlay Play Clicked"
        self.wthread.assign_work(self.sequencer)
        #self.statusbar.SetStatusText("Completed.")

    def OnStatusUpdate(self, event):
        print "OnStatusUpdate", event.status_msg
        self.statusbar.SetStatusText(event.status_msg)
        self.statusbar.Refresh()
        self.statusbar.Update()

    @staticmethod
    def AskOnFailure(msg):
        print "AskOnFailure", msg
        dlg = wx.MessageDialog(None, msg, "Failed", wx.YES_NO |
                               wx.ICON_QUESTION)
        retcode = dlg.ShowModal()
        dlg.Destroy()
        if retcode == wx.ID_YES:
            return True
        else:
            return False

    def StepSuccess(self, event):
        event.widget.SetBackgroundColour(event.colour)

    def onCloseWindow(self, event):
        #wx.MessageBox("Thank you!")
        self.Destroy()
