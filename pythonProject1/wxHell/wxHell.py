import wx
import WeatherHell
# import ch143
import bs4

def clickButton1(event):
    list.Clear()
    items = WeatherHell.getData()
    list.AppendItems(items)
def clickButton2(event):
    list.Clear()
    # items = ch143.itemDB.selectui()
    # list.AppendItems(items)
def clickButton3(event):
    list.Clear()
    wx.ListBox(p2,choices = names)
app = wx.App()
frame = wx.Frame(None,0,"Test")
p1 = wx.Panel(frame)
bt1 = wx.Button(p1,label = 'button 1')
bt2 = wx.Button(p1,label = 'button 2')
bt3 = wx.Button(p1,label = 'button 3')
ps1 = wx.BoxSizer(wx.HORIZONTAL)
ps1.Add(bt1)
ps1.Add(bt2)
ps1.Add(bt3)
p1.SetSizer(ps1)

p2 = wx.Panel(frame)
names = ['여기에','뭔가가','쓰여진','다.','메롱~']
list = wx.ListBox(p2,choices = names)
list.SetSize(wx.Size(300,200))

p3 = wx.Panel(frame)
bt_add = wx.Button(p3,label = 'Add')
text1 = wx.TextCtrl(p3)
text2 = wx.TextCtrl(p3)
text3 = wx.TextCtrl(p3)
text4 = wx.TextCtrl(p3)
ps3 = wx.BoxSizer(wx.VERTICAL)
ps3.Add(bt_add)
ps3.Add(text1)
ps3.Add(text2)
ps3.Add(text3)
ps3.Add(text4)
p3.SetSizer(ps3)
box = wx.BoxSizer(wx.VERTICAL);
frame.SetSizer(box)
box.Add(p1,border=10,flag=wx.DOWN);
box.Add(p2,border=10,flag=wx.UP);
box.Add(p3,border=10,flag=wx.UP);

bt1.Bind(wx.EVT_BUTTON,clickButton1)
bt2.Bind(wx.EVT_BUTTON,clickButton2)
bt3.Bind(wx.EVT_BUTTON,clickButton3)
frame.Show(True)
app.MainLoop()