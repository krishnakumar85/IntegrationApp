#import wx
#import IntegrationFrame
from IntegrationFrame import *
#TODO: use import instead of from ... import ...


class IntegrationApp(wx.App):
    def __init__(self, process_steps):
        self.process_steps = process_steps
        wx.App.__init__(self, False)

    def OnInit(self):
        self.frame = IntegrationFrame(parent=None, fid=-1,
                                      title='Integration Assist',
                                      sequencer=self.process_steps)
        image = wx.Image("..\img\splash.bmp", wx.BITMAP_TYPE_BMP)
        wx.SplashScreen(image.ConvertToBitmap(), wx.SPLASH_CENTER_ON_SCREEN |
                        wx.SPLASH_TIMEOUT, 500,
                        None, -1)
        wx.Yield()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
