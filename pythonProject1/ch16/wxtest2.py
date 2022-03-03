# wxtest2

import wx;
import  weather;
import itemDB as itemdb#패키지 밑의 모듈을 쓸땐 이렇게 import.

app = wx.App();

frame = wx.Frame(None, 0, "Test");


p1 = wx.Panel(frame);
frame.Show(True);
bt1 = wx.Button(p1,label = 'button1');
bt2 = wx.Button(p1,label = 'button2');
bt3 = wx.Button(p1,label = 'reset');
ps = wx.BoxSizer(wx.HORIZONTAL);
ps.Add(bt1);
ps.Add(bt2);
ps.Add(bt3);
p1.SetSizer(ps);

p2 = wx.Panel(frame)
names = ['여기에','값이','나타난','다.']
list = wx.ListBox(p2,choices= names)
list.SetSize(wx.Size(300,200))

p3 = wx.Panel(frame);
bt_add = wx.Button(p3,label = 'ADD');
text1 = wx.TextCtrl(p3)
text2 = wx.TextCtrl(p3)
text3 = wx.TextCtrl(p3)
text4 = wx.TextCtrl(p3)
ps3 = wx.BoxSizer(wx.VERTICAL);
ps3.Add(bt_add);
ps3.Add(text1);
ps3.Add(text2);
ps3.Add(text3);
ps3.Add(text4);
p3.SetSizer(ps3);

def clickadd(event):
    id = int(text1.GetValue());
    name = text2.GetValue();
    price = int(text3.GetValue());
    rate = float(text4.GetValue());
    try:
        itemdb.insert(id,name,price,rate);
        text1.SetLabelText('')
        text2.SetLabelText('')
        text3.SetLabelText('')
        text4.SetLabelText('')
    except:
        wx.MessageBox('Insert Error','Allert',wx.OK);
bt_add.Bind(wx.EVT_BUTTON, clickadd);

box = wx.BoxSizer(wx.VERTICAL);
frame.SetSizer(box)
box.Add(p1,border=10,flag=wx.DOWN);
box.Add(p2,border=10,flag=wx.UP);
box.Add(p3,border=10,flag=wx.UP);

def clickbt1(event):
    list.Clear();
    items = weather.getdata();
    list.AppendItems(items);
def clickbt2(event):
    list.Clear();
    items = itemdb.selectui();
    list.AppendItems(items);
def clickbt3(event):
    list.Clear();
    wx.ListBox(p2,choices = names)

 # #------------------임시---------------------
 #    items = weather.getdata();
 #    list.AppendItems(items);
 # #------------------임시---------------------

# def clickbt3(event):
#     list.Clear();
#     items = ['999', '000', '111', '222'];
#     list.AppendItems(items);

bt1.Bind(wx.EVT_BUTTON, clickbt1)
bt2.Bind(wx.EVT_BUTTON, clickbt2)
bt3.Bind(wx.EVT_BUTTON, clickbt3)
frame.Show(True)
app.MainLoop();#애플리케이션이 무한루프로 계~속 구동
#안드로이드 개발에 이용되는 코드.
# if __name__ == '__main__':
#     print(weather.getdata())

# UI 프로그래밍은 매우 힘들고 어려우니 많은 연습이 필요하다.
#이런 프로그램을 처음부터 비슷하게 스스로 만들어 볼 것.(무리하게 외우진 말것.)
#프로그램을 만들면서 전체적인 그림,구조,흐름을 생각해봐야 한다.