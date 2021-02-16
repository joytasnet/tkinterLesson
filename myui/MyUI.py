import tkinter as tk

root=tk.Tk()
root.title('UI Test')
root.geometry('800x600')
root['bg']='#333'

#基本のフレームを5種配置
main=tk.Canvas(root,width=600,height=400,bd=0,highlightthickness=0)
main.grid(row=0,column=0,sticky=tk.NW)
canvas=tk.Canvas(root,width=200,height=200,bd=0,highlightthickness=0)
canvas.grid(row=0,column=1,sticky=tk.NE)
player=tk.Frame(root,width=200,height=200,bd=3,relief='raised',bg='#555')
player.grid(row=0,column=1,sticky=tk.SE)
inventry=tk.Frame(root,width=200,height=200,bd=3,relief='raised',bg='tan')
inventry.grid(row=1,column=1,sticky=tk.SE)
textbox=tk.Frame(root,width=600,height=200,bd=3,relief='raised',bg='#4682b4')
textbox.grid(row=1,column=0,sticky=tk.SW)

mainphoto=tk.PhotoImage(file='back.png')
main.create_image(300,200,image=mainphoto)
#キャラクター情報を載せる
photo1=tk.PhotoImage(file='yoroi.png')
canvas.create_image(100,100,image=photo1)
#ステータスのラベルを作り、placeで配置
player_name=tk.Label(player,text='さむらい:Lv8',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_name.place(x=4,y=2)
player_health=tk.Label(player,text='たいりょく:255',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_health.place(x=4,y=35)
player_weapon=tk.Label(player,text='ぶき:きくいちもんじ',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_weapon.place(x=4,y=70)
player_armor=tk.Label(player,text='ぼうぐ:おおよろい',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_armor.place(x=4,y=105)
player_condition=tk.Label(player,text='じょうたい:けんこう',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_condition.place(x=4,y=140)

attack=tk.Button(inventry,text='こうげき',width=9,height=2)
attack.place(x=8,y=6)
defense=tk.Button(inventry,text='ぼうぎょ',width=9,height=2)
defense.place(x=100,y=6)
nanori=tk.Button(inventry,text='なのる',width=9,height=2)
nanori.place(x=8,y=53)
item=tk.Button(inventry,text='どうぐ',width=9,height=2)
item.place(x=100,y=53)
intimidation=tk.Button(inventry,text='どうかつ',width=9,height=2)
intimidation.place(x=8,y=101)
apologize=tk.Button(inventry,text='あやまる',width=9,height=2)
apologize.place(x=100,y=101)
death_poem=tk.Button(inventry,text='じせいのく',width=9,height=2)
death_poem.place(x=8,y=148)
harakiri=tk.Button(inventry,text='せっぷく',width=9,height=2)
harakiri.place(x=100,y=148)

main_text=tk.Label(textbox,text='さむらいは洞窟を探索している・・・\nものかげに千両箱を発見した！',width=30,height=5,font=('HackGen35',30),fg='white',bg='#4682b4')
main_text.place(x=8,y=8)

root.mainloop()
