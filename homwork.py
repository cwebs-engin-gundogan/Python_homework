import http.client
import json
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

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
        
        self.padding = ttk.Label(self.page0, text="", background="#c7e9f0")
        self.padding.pack()

        self.combo = ttk.Combobox(self.page0, values=datam)
        self.combo.pack(pady=20)

    
        # Combobox seçimini izleme
        self.combo.bind("<<ComboboxSelected>>", self.on_select)
        
    


        self.scrollbar = ttk.Scrollbar(self.page0)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.page0, yscrollcommand=self.scrollbar.set,width=60,)
        if veri["success"]:
            for item in veri["result"]["data"]:
                self.listbox.insert(tk.END, f"{item['code']}: {item['name']} - {item['rate']}")

        else:
            print("ulaşılamadı")
        self.listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
        self.scrollbar.configure(command=self.listbox.yview)
        
       
  # Page 1 ( Haraketlerim )
        self.scrollbar2 = ttk.Scrollbar(self.page1)
        self.scrollbar2.grid(row=1, column=2, sticky='ns')

        self.lbl1 = ttk.Label(self.page1, text="Kur değerleri : ", font="Calibri", anchor='e', width=22)
        self.lbl1.grid(row=0, column=0,sticky='w')
        
        self.ent1 = ttk.Entry(self.page1, font="Calibri",textvariable="")
        self.ent1.grid(row=1, column=0)

        self.ent2 = ttk.Entry(self.page1, font="Calibri")
        self.ent2.grid(row=1, column=0, sticky='e')

        self.listbox2 = tk.Listbox(self.page1, yscrollcommand=self.scrollbar2.set,width=60,)
        for i in range(1000):
            self.listbox2.insert(tk.END, str(i))
        self.listbox2.grid(row=1, column=0, sticky='nsew')
        self.scrollbar2.config(command=self.listbox2.yview)

        self.page1.grid_rowconfigure(1, weight=1)
        self.page1.grid_columnconfigure(0, weight=1)
        #self.ok = ttk.Button(self.page1)
        #self.ok["text"] = "Button"
        #self.ok["command"] = self.handler
        #self.ok.grid(row=0, column=0)
    def handler(self):
        print("Button clicked")
    
    def on_select(self, event):
            selected_value = self.combo.get()
            print("seçilen değer : " + selected_value)


if __name__ == "__main__":
    
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
    'content-type': "application/json",
    'authorization': "apikey 6CyxdGYXewGZ0f4HpI2bFN:5jAv7AARSTX9qu6LDIqDge"
    }

    conn.request("GET", "/economy/currencyToAll?int=10&base=USD", headers=headers)

    res = conn.getresponse()
    data = res.read()
    veri = json.loads(data)

    conn.request("GET", "/economy/symbols", headers=headers)

    res2 = conn.getresponse()
    data2 = res2.read()
    veri2 = json.loads(data2)

    print(veri)
    print(veri2)
    #pen = tk.Tk()
    #pen.title("Kişisel Varlık Uygulaması")

    datam = []
    if veri2["success"]:
            for item in veri2["result"]:
                datam.append(item['code']) 
    print(datam)    

    app = MyApp()
    app.geometry("920x500")
    app.mainloop()

# pen.mainloop()