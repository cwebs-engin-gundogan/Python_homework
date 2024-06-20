import http.client
import json
import tkinter as tk

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 6sbOiNy7ZGg7tTbmPee76H:30vedEzmfAlfdluFXYJQ6k"
    }

conn.request("GET", "/economy/currencyToAll?int=10&base=USD", headers=headers)

res = conn.getresponse()
data = res.read()
veri = json.loads(data)

print(veri)

pen = tk.Tk()
pen.title("Kişisel Varlık Uygulaması")

lb = tk.Listbox(pen, width=40, height=7)
lb.pack()

for item in veri["result"]["data"]:
    lb.insert(tk.END,item["code"])



pen.mainloop()