from tkinter import *
import  datetime
def kontrol_et():
    dosya=open("usom.txt","r")
    icerik=dosya.read( )
    dosya.close()
    ip=entry1.get()
    bugun=datetime.datetime.now()
    if str(ip) in icerik:
        dosya=open("log.txt","a")
        yazi=str(ip)+" zararlı\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        v.set("IP ZARARLIDIR!")
        dosya.close()
        
    else:
        dosya=open("log.txt","a")
        yazi=str(ip)+" zararlı değil\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        v.set("IP ZARARSIZDIR")
        dosya.close()
        


top=Tk()
top.title("USOM İP KONTROL By Brave")
B=Button(top,text="Kontrol Et",command=kontrol_et)
B.place(x=50,y=50)
B.pack()
label3=Label(top,text="USOM IP KONTROL BY BRAVE")
label3.place(x=50,y=40)
label3.pack()
label1=Label(top,text="Kontrol edilecek IP adresini giriniz:")
label1.place(x=50,y=80)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=90)
entry1.pack()
v=StringVar()
label2=Label(top,text="IP Kontrol Sonucu:")
label2.place(x=50,y=100)
label2.pack()





entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=110)
entry2.pack()
label4=Label(top,text="TAM IP GİRİN ÖRN:https://www.turkiye.gov.tr,http//www.google.com")
label4.place(x=50,y=120)
label4.pack()
top.mainloop()