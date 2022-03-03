# wxtest

import wx;

app = wx.App();

frame = wx.Frame(None, 0, "Test");


p1 = wx.Panel(frame);
frame.Show(True);
bt1 = wx.Button(p1,label = 'button1');
bt2 = wx.Button(p1,label = 'button2');
bt3 = wx.Button(p1,label = 'button3');
ps = wx.BoxSizer(wx.HORIZONTAL);
ps.Add(bt1);
ps.Add(bt2);
ps.Add(bt3);
p1.SetSizer(ps);

p2 = wx.Panel(frame);

text1 = wx.StaticText(p2,label = '           a             ');
text2 = wx.StaticText(p2,label = '           b             ');
text3 = wx.StaticText(p2,label = '           c             ');
ps2 = wx.BoxSizer(wx.VERTICAL);
ps2.Add(text1);
ps2.Add(text2);
ps2.Add(text3);
p2.SetSizer(ps2);

box = wx.BoxSizer(wx.VERTICAL);
frame.SetSizer(box)
box.Add(p1,border=10,flag=wx.DOWN);
box.Add(p2,border=10,flag=wx.UP);


def clickbt1(event):
    text1.SetLabelText('Click button 1');

def clickbt2(event):
    text2.SetLabelText('Click button 2');

def clickbt3(event):
    text3.SetLabelText('Click button 3');

bt1.Bind(wx.EVT_BUTTON, clickbt1)
bt2.Bind(wx.EVT_BUTTON, clickbt2)
bt3.Bind(wx.EVT_BUTTON, clickbt3)
frame.Show(True)
app.MainLoop();#애플리케이션이 무한루프로 계~속 구동
#안드로이드 개발에 이용되는 코드.