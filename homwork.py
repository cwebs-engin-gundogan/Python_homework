import http.client
import json
import sqlite3
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkcalendar import DateEntry

class MyApp(ThemedTk):
    def __init__(self, theme="adapta"):
        ThemedTk.__init__(self, fonts=True, themebg=True, background="True")
        self.set_theme(theme)
        
        self.style = ttk.Style()
        self.style.configure('lefttab.TNotebook',tabposition=tk.W + tk.N,tabplacement=tk.N + tk.EW, background= "#06bad2")
        current_theme = self.style.theme_use()
        self.style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": { "color": "white", "padding": [13, 10]}}})
        
        
        self.nb = ttk.Notebook(self, style='lefttab.TNotebook')
        self.nb.grid(row=0, column=0, sticky='w')
        
        self.page0 = ttk.Frame(self.nb, width=800, height=500)
        self.page1 = ttk.Frame(self.nb, width=800, height=500)
        self.page2 = ttk.Frame(self.nb, width=800, height=500)
        
        self.style.configure("TFrame", background='#c7e9f0')
        
        self.nb.add(self.page0, text='Ana Sayfa', sticky="nsew")
        self.nb.add(self.page1, text='Haraketlerim', sticky="nsew")
        self.nb.add(self.page2, text='Grafik Gösterimi', sticky="nsew")
        
      # Page 0  ( Ana Sayfa )
        self.lbl11 = ttk.Label(self.page0, text="", font="Calibri",background='#c7e9f0',width=3)
        self.lbl11.grid(row=0, column=3)
        self.lbl111 = ttk.Label(self.page0, text="Lütfen Doldurunuz", font="Calibri", width=22, background='#c7e9f0')
        self.lbl111.grid(row=0, column=4)
        self.lbl111 = ttk.Label(self.page0, text="                 ", font="Calibri", width=22, background='#c7e9f0')
        self.lbl111.grid(row=0, column=5)
        self.lbl12 = ttk.Label(self.page0, text="", font="Calibri",background='#c7e9f0',width=2)
        self.lbl12.grid(row=1, column=3)
        self.ent11 = ttk.Entry(self.page0, font="Calibri")
        self.ent11.insert(0, "Döviz adeti")
        self.ent11.bind("<FocusIn>", self.clear_entry1)
        self.ent11.bind("<KeyRelease>", self.on_ent11_change)
        self.ent11.grid(row=1, column=4, sticky='w')
    ### Döviz combo
        self.combo1 = ttk.Combobox(self.page0, values=doviz,width=30)
        #self.combo.pack(pady=20)
        self.combo1.current(0)
        # Combobox seçimini izleme
        self.combo1.bind("<<ComboboxSelected>>", self.on_select1)
        self.combo1.grid(row=1, column=5)
        
        self.ent12 = ttk.Entry(self.page0, font="Calibri")
        self.ent12.insert(0, "Altın adeti")
        self.ent12.grid(row=2, column=4, sticky='w')
        self.ent12.bind("<FocusIn>", self.clear_entry2)
        self.ent12.bind("<KeyRelease>", self.on_ent12_change)
    ### Altın combo
        self.combo2 = ttk.Combobox(self.page0, values=altin,width=30)
        #self.combo.pack(pady=20)
        self.combo2.current(0)
        # Combobox seçimini izleme
        self.combo2.bind("<<ComboboxSelected>>", self.on_select2)
        self.combo2.grid(row=2, column=5)
        
        var = tk.IntVar()


        self.lbl13 = ttk.Label(self.page0, text="", font="Calibri",background='#c7e9f0',width=2)
        self.lbl13.grid(row=3, column=3)
        self.cb1 = ttk.Checkbutton(self.page0, text="Geçmiş Bir Tarih Seç",variable=var,command=self.toggle_date_entry)
        self.cb1.grid(row=4, column=4, sticky='w' )
    ### Butonlar 
        self.btn11 = ttk.Button(self.page0, text="Sat", command=self.Sat)
        self.btn11.grid(row=4, column=5, sticky='w' )
        self.btn12 = ttk.Button(self.page0, text="Al", command=self.Al)
        self.btn12.grid(row=4, column=5, sticky='e')

        self.cal = DateEntry(self.page0, width=30, background='darkblue',foreground='white', borderwidth=2, year=2024)
        self.cal.grid(row=5, column=4,sticky='w')

        self.lbl15 = ttk.Label(self.page0, text="              Varlığım", font="Calibri",background='#c7e9f0',width=20)
        self.lbl15.grid(row=0, column=6)
        self.listbox11 = tk.Listbox(self.page0,width=50,height=14)
        
        for row in rows:
            self.listbox11.insert(tk.END, row)
        self.listbox11.grid(row=1, column=6,rowspan=5)


        self.lbl14 = ttk.Label(self.page0, text="", font="Calibri",background='#c7e9f0',width=2)
        self.lbl14.grid(row=6, column=3)
        self.frame = ttk.Frame(self.page0)
        self.frame.grid(row=7, column=3,columnspan=9)

        self.scrollbar12 = ttk.Scrollbar(self.page0)
        self.scrollbar12.grid(row=7, column=3,columnspan=9, sticky='e')

        self.listbox12 = tk.Listbox(self.page0, yscrollcommand=self.scrollbar12.set,width=55,height=2,font=15)
        self.listbox12.grid(row=7, column=4,columnspan=3, sticky='nsew')
        self.scrollbar12.config(command=self.listbox12.yview)

        self.lbl14 = ttk.Label(self.page0, text="", font="Calibri",background='#c7e9f0',width=2)
        self.lbl14.grid(row=8, column=3)

        self.listbox13 = tk.Listbox(self.page0, yscrollcommand=self.scrollbar12.set,width=15,height=5,font=15)
        self.listbox13.grid(row=9, column=4, sticky='w')

        self.listbox14 = tk.Listbox(self.page0, yscrollcommand=self.scrollbar12.set,width=15,height=5,font=15)
        self.listbox14.grid(row=9, column=6, sticky='e')
        
        #self.scrollbar = ttk.Scrollbar(self.page0)
        #self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #self.listbox = tk.Listbox(self.page0, yscrollcommand=self.scrollbar.set,width=60,)
        #if veri["success"]:
        #    for item in veri["result"]["data"]:
        #        self.listbox.insert(tk.END, f"{item['code']}: {item['name']} - {item['rate']}")
        #else:
        #    print("ulaşılamadı")
        #self.listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
        #self.scrollbar.configure(command=self.listbox.yview)
        
       
  # Page 1 ( Haraketlerim )
        self.scrollbar21 = ttk.Scrollbar(self.page1)
        self.scrollbar21.grid(row=1, column=2, sticky='ns')

        self.lbl1 = ttk.Label(self.page1, text="Kur değerleri : ", font="Calibri", anchor='e', width=22)
        self.lbl1.grid(row=0, column=0,sticky='w')
        self.lbl21 = ttk.Label(self.page1, text="", font="Calibri", width=22)
        self.lbl21.grid(row=0, column=0)
        self.btn21 = ttk.Button(self.page1, text="Listeyi Yenile", command=self.yenile)
        self.btn21.grid(row=0, column=0, sticky='e')
        self.ent21 = ttk.Entry(self.page1, font="Calibri",textvariable="")
        self.ent21.grid(row=1, column=0)

        self.ent22 = ttk.Entry(self.page1, font="Calibri")
        self.ent22.grid(row=1, column=0, sticky='e')

        self.listbox21 = tk.Listbox(self.page1, yscrollcommand=self.scrollbar21.set,width=70,height=19,font=15)
        self.listbox21.bind("<<ListboxSelect>>", self.on_select)
        for row in haraketler:
            self.listbox21.insert(tk.END, row)
        self.listbox21.grid(row=1, column=0, sticky='nsew')
        self.scrollbar21.config(command=self.listbox21.yview)

    al=None 
    sat=None
    Total_varligim=None
        #self.page1.grid_rowconfigure(1, weight=1)
        #self.page1.grid_columnconfigure(0, weight=1)
        
        #self.ok = ttk.Button(self.page1)
        #self.ok["text"] = "Button"
        #self.ok["command"] = self.handler
        #self.ok.grid(row=0, column=0)
    def handler(self):
        print("Button clicked")
    def yenile(self,event):
        cursor.execute('''SELECT h.id, h.islem_turu, h.miktar, h.tarih, ad.altin_yada_doviz, h.altin_doviz_turu FROM history h FULL OUTER JOIN altin_doviz ad ON h.altin_yada_doviz = ad.id ORDER BY h.id DESC''')
        haraketler = cursor.fetchall()
        self.listbox21.delete(0, tk.END)
        for row in haraketler:
            self.listbox21.insert(tk.END, row)
    def on_ent12_change(self,event):
            value = float(self.ent12.get())
            print(value)
            self.listbox13.delete(0, tk.END)
            self.listbox13.insert(tk.END, f"{'Satılırsa :':<30}")
            self.listbox14.delete(0, tk.END)
            self.listbox14.insert(tk.END, f"{'Alınırsa :':<30}")
            selected_value = self.combo2.get()
            for i in veri5["result"]:
                if selected_value != "Altın":
                    if selected_value == i["name"]:
                        satis_degeri = i['sellingstr']
                        alis_degeri = i['buyingstr']
                        satis_degeri = satis_degeri.replace(',', '.')
                        alis_degeri=alis_degeri.replace(',', '.')
                        satis_degeri = float(satis_degeri)
                        alis_degeri=float(alis_degeri)
            if satis_degeri and value and alis_degeri is not None:
                sat=value*satis_degeri
                self.listbox13.insert(tk.END, f"{sat}")
                al=value*alis_degeri
                self.listbox14.insert(tk.END, f"{al}")
    def on_ent11_change(self,event):
            value = float(self.ent11.get())
            print(value)
            self.listbox13.delete(0, tk.END)
            self.listbox13.insert(tk.END, f"{'Satılırsa :':<30}")
            self.listbox14.delete(0, tk.END)
            self.listbox14.insert(tk.END, f"{'Alınırsa :':<30}")
            selected_value = self.combo1.get()
            for i in veri4["result"]:
                if selected_value != "Döviz":
                    if selected_value == i["code"]:
                        satis_degeri = i['sellingstr']
                        alis_degeri = i['buyingstr']
                        satis_degeri = satis_degeri.replace(',', '.')
                        alis_degeri=alis_degeri.replace(',', '.')
                        satis_degeri = float(satis_degeri)
                        alis_degeri=float(alis_degeri)
            if satis_degeri and value and alis_degeri is not None:
                sat=value*satis_degeri
                self.listbox13.insert(tk.END, f"{sat}")
                al=value*alis_degeri
                self.listbox14.insert(tk.END, f"{al}")
    def on_select1(self, event):
            selected_value = self.combo1.get()
            print("seçilen değer : " + selected_value)
            print("veri4 ü yazdırıyorum şuan ")
            print(veri4)
            self.listbox12.delete(0, tk.END)
            self.listbox12.insert(tk.END, f"{'Döviz Cinsi':<25}{'Satış Değeri':<25} {'Alış Değeri':<25} {'Tarih':<25}")
            for i in veri4["result"]:
                if selected_value == i["code"]:
                    kur_cinsi = f"{i['name']:<25}"
                    satis_degeri = f"{i['sellingstr']:<25}"
                    alis_degeri = f"{i['buyingstr']:<25}"
                    tarih=f"{i['date']:<25}"
                    self.listbox12.insert(tk.END, f"{kur_cinsi} {satis_degeri} {alis_degeri} {tarih}")
                    #self.listbox12.insert(tk.END, i["name"] + " \t \t " + i["buyingstr"] + " \t \t "+ i["sellingstr"])
                else:
                    print("bulunamadı")
    def on_select(self, event):
        selected_index = self.listbox21.curselection()
        if selected_index:
            selected_item = self.listbox21.get(selected_index)
    def on_select2(self, event):
            selected_value = self.combo2.get()
            print("seçilen değer : " + selected_value)
            print("veri5 ü yazdırıyorum şuan ")
            print(veri5)
            self.listbox12.delete(0, tk.END)
            self.listbox12.insert(tk.END, f"{'Altın Türü':<25}{'Satış Değeri':<25} {'Alış Değeri':<25} {'Tarih':<25}")
            for i in veri5["result"]:
                if selected_value == i["name"]:
                    kur_cinsi = f"{i['name']:<25}"
                    satis_degeri = f"{i['sellingstr']:<25}"
                    alis_degeri = f"{i['buyingstr']:<25}"
                    tarih=f"{i['date']:<25}"
                    self.listbox12.insert(tk.END, f"{kur_cinsi} {satis_degeri} {alis_degeri} {tarih}")
                    #self.listbox12.insert(tk.END, i["name"] + " \t \t " + i["buyingstr"] + " \t \t "+ i["sellingstr"])
                else:
                    print("bulunamadı")
    def clear_entry1(self, event):
        if self.ent11.get() == "Döviz adeti":
            self.ent11.delete(0, tk.END)
    def clear_entry2(self, event):
        if self.ent12.get() == "Altın adeti":
            self.ent12.delete(0, tk.END)
    def Al(self):
        islem_turu="Alım"
        try:
            miktar1 = int(self.ent11.get())
        except ValueError:
            miktar1=0
        try:
            miktar2 = int(self.ent12.get()) 
        except ValueError:
            miktar2=0        
        selected_combo1=self.combo1.get()
        selected_combo2=self.combo2.get()
        if selected_combo1=="Döviz" and selected_combo2 !="Altın" and miktar1<=0 and miktar2>0:
             miktar=miktar2
             altin_yada_doviz=0
             altin_doviz_turu=selected_combo2
        elif selected_combo2=="Altın" and selected_combo1!="Döviz" and miktar2<=0 and miktar1>0:
             miktar=miktar1
             altin_yada_doviz=1
             altin_doviz_turu=selected_combo1
             selected_date = self.cal.get_date()
        cursor.execute('INSERT INTO history (islem_turu, miktar,altin_doviz_turu,tarih) VALUES (?, ?, ?, ?)', (islem_turu, miktar,altin_doviz_turu, selected_date))
        id=cursor.lastrowid
        print(id)
        cursor.execute('INSERT INTO my_assets (altin_yada_doviz, miktar,islem_id,altin_doviz_turu) VALUES (?, ?, ? , ?)', (altin_yada_doviz, miktar,id,altin_doviz_turu))
        conn.commit()
        cursor.execute('SELECT * FROM my_assets')
        rows = cursor.fetchall()
        print(rows)
        self.listbox11.delete(0, tk.END)
        for row in rows:
            self.listbox11.insert(tk.END, row)
    def Sat(self):
        islem_turu="Satım"
        if int(self.Total_varligim)>int(self.sat):
            try:
                miktar1 = int(self.ent11.get())
            except ValueError:
                miktar1=0
            try:
               miktar2 = int(self.ent12.get()) 
            except ValueError:
                miktar2=0   
            selected_combo1=self.combo1.get()
            selected_combo2=self.combo2.get()
            if selected_combo1=="Döviz" and selected_combo2 !="Altın" and miktar1<=0 and miktar2>0:
                miktar=miktar2
                altin_yada_doviz=0
                altin_doviz_turu=selected_combo2
            elif selected_combo2=="Altın" and selected_combo1!="Döviz" and miktar2<=0 and miktar1>0:
                miktar=miktar1
                altin_yada_doviz=1
                altin_doviz_turu=selected_combo1
            cursor.execute('INSERT INTO history (islem_turu, miktar) VALUES (?, ?)', (islem_turu, miktar))
            conn.commit()
            id=cursor.lastrowid
            cursor.execute('INSERT INTO my_assets (altin_yada_doviz, miktar,islem_id,altin_doviz_turu) VALUES (?, ?)', (altin_yada_doviz, miktar,id,altin_doviz_turu))
            conn.commit()
        else:
             self.messagebox.showwarning("Uyarı", "Varlığınızdan fazla harcama yapmaktasınız. Buna izin verilemez!")
    def toggle_date_entry(self):
        if self.var.get() == 1:
            self.cal.pack(pady=20)
        else:
            self.cal.pack_forget()

    def get_date(self):
        selected_date = self.cal.get_date()
        print(f"Seçilen Tarih: {selected_date}")
if __name__ == "__main__":
    tl_tutarı=0
    doviz_altın= {"döviz":0,"altın":1}
    alım_satım={"alım":0,"satım":1}
    date = "06/21/2024"
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
    'content-type': "application/json",
    'authorization': "apikey 3HC56AHvxHz22GmtKChvxP:1h8CPlCJDtnQQGa8vIRppZ"
    }

    conn.request("GET", "/economy/currencyToAll?int=10&base=USD", headers=headers)

    res = conn.getresponse()
    data = res.read()
    veri = json.loads(data)
    print(veri)

    conn.request("GET", "/economy/symbols", headers=headers)
    res2 = conn.getresponse()
    data2 = res2.read()
    veri2 = json.loads(data2)
    print(veri2)

    conn.request("GET", "/economy/goldPrice", headers=headers)
    res3 = conn.getresponse()
    data3 = res3.read()
    veri3 = json.loads(data3)
    print(veri3)

    conn.request("GET", "/economy/allCurrency", headers=headers)

    res4 = conn.getresponse()
    data4 = res4.read()
    veri4 = json.loads(data4)

    conn.request("GET", "/economy/goldPrice", headers=headers)
    res5 = conn.getresponse()
    data5 = res5.read()
    veri5 = json.loads(data5)
    
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT UNIQUE,name TEXT)''')    
    user = "caglarengi@gmail.com"
    name = "caglar engin"
    cursor.execute('SELECT * FROM users WHERE email = ?', (user,))
    is_it_user = cursor.fetchone()

    if user is None:
        cursor.execute('INSERT INTO users (email, name) VALUES (?, ?)', (user, name))
        print(f"{ name} kullanıcısı eklendi.")
    else:
        print(f"{ name} kullanıcısı zaten mevcut.")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS altin_doviz (id INTEGER PRIMARY KEY ,altin_yada_doviz TEXT UNIQUE)''')    

    cursor.execute('''CREATE TABLE IF NOT EXISTS my_assets (id INTEGER PRIMARY KEY AUTOINCREMENT,altin_yada_doviz INTEGER ,miktar REAL,altin_doviz_turu TEXT,islem_id INTEGER,FOREIGN KEY (islem_id) REFERENCES history(id),FOREIGN KEY (altin_yada_doviz) REFERENCES altin_doviz(id))''')    
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY AUTOINCREMENT,islem_turu TEXT ,miktar REAL, tarih TEXT,altin_yada_doviz INTEGER,altin_doviz_turu TEXT,FOREIGN KEY (altin_yada_doviz) REFERENCES altin_doviz(id))''')
    #cursor.execute('''CREATE TABLE IF NOT EXISTS altin_cesitler (altin_yada_doviz INTEGER ,altin_yada_doviz TEXT )''') 
    # altin ve doviz adlarında kayıtları kontrol et
    cursor.execute('SELECT id FROM altin_doviz WHERE altin_yada_doviz = ?', ('Altın',))
    altin = cursor.fetchone()

    cursor.execute('SELECT id FROM altin_doviz WHERE altin_yada_doviz = ?', ('Döviz',))
    doviz = cursor.fetchone()

    # Eğer altin ve doviz kayıtları mevcut değilse, ekleyin
    if not altin:
        cursor.execute('INSERT INTO altin_doviz (altin_yada_doviz) VALUES (?)', ('Altın',))
        print("altin kaydı eklendi.")

    if not doviz:
        cursor.execute('INSERT INTO altin_doviz (altin_yada_doviz) VALUES (?)', ('Döviz',))
        print("doviz kaydı eklendi.")

    cursor.execute('SELECT * FROM my_assets')
    rows = cursor.fetchall()

    cursor.execute('''SELECT h.id, h.islem_turu, h.miktar, h.tarih, ad.altin_yada_doviz, h.altin_doviz_turu FROM history h FULL OUTER JOIN altin_doviz ad ON h.altin_yada_doviz = ad.id ORDER BY h.id DESC''')
    haraketler = cursor.fetchall()
    # Değişiklikleri kaydet
    conn.commit()
    
    doviz = ["Döviz"]
    altin= ["Altın"]
    if veri2["success"]:
            for item in veri2["result"]:
                doviz.append(item['code']) 
    print(doviz)    
    if veri3["success"]:
            for item in veri3["result"]:
                altin.append(item['name']) 
    print(altin)    
    
    app = MyApp()
    app.geometry("920x500")
    app.mainloop()
    conn.commit()
    # Bağlantıyı kapat
    conn.close()
# pen.mainloop()