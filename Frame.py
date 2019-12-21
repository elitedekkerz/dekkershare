import wx
import os
import webbrowser

class MyForm(wx.Frame):
    def __init__(self):
        self.Dir="none"
        wx.Frame.__init__(self,None,wx.ID_ANY,"Dekkerz SFSOL")
        panel=wx.Panel(self,wx.ID_ANY)
        self.CurrentDir=os.getcwd()
        
        button=wx.Button(panel,wx.ID_ANY,"Select share folder",(10,10))
        button.Bind(wx.EVT_BUTTON,self.OnButton)

        button2=wx.Button(panel,wx.ID_ANY,"Open browser",(10,40))
        button2.Bind(wx.EVT_BUTTON,self.OpenBrowser)

    def OnButton(self,event):
        dlg=wx.DirDialog(self,"Choose a directory",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal()==wx.ID_OK:
            print("you chose %s"%dlg.GetPath())
            self.Dir=dlg.GetPath()
            self.WriteFile()

    def WriteFile(self):
        with open("Settings.txt","w")as file:
            file.write(self.Dir)
        print("file written")

    def OpenBrowser(self,event):
        webbrowser.open("localhost/",new=2)


if __name__ == "__main__":
    app=wx.App(False)
    frame=MyForm()
    frame.Show()
    app.MainLoop()

#frame.Show(True)
#app.MainLoop()

