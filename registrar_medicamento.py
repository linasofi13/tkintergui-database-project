from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import tkinter as tk
import random
import form_checker

# start window


window = Tk()
window.title('Registro de Medicamento')
window.geometry('925x600+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

# connect to database

db = mysql.connect(host="127.0.0.1", user="root", password="Sofia2013**", database="clinica_veterinaria_")
mycursor = db.cursor()

# functions

def add():
    codigoMedicamento = valor
    nombreMedicamento = nombre_medicamento.get()
    precioMedicamento = precio_medicamento.get()
    presentacionMedicamento = presentacion_medicamento.get()
    accionTerapeutica = accion_terapeutica.get()
    fechaProduccion = fecha_produccion.get()
    fechaVencimiento = fecha_vencimiento.get()
    laboratorio_add = laboratorio.get()
    query = "INSERT INTO medicamento (codigo_medicamento, nombre_medicamento, precio_medicamento, presentacion_medicamento, accion_terapeutica_medicamento,fecha_produccion_medicamento,fecha_vencimiento_medicamento,laboratorio_medicamento) VALUES(%s, %s, %s, %s, %s,%s,%s,%s)"
    format = (codigoMedicamento,nombreMedicamento,precioMedicamento,presentacionMedicamento,accionTerapeutica,fechaProduccion,fechaVencimiento,laboratorio_add)
    mycursor.execute(query, format)
    db.commit()

def back():
    window.destroy()
    import main_menu

def produccion(e):
    if form_checker.birthDateChecker(str(fecha_produccion.get())):
        label = Label(window, image=resized_img6, border=0, bg='white')
        label.place(x=655, y=240)
    else:
        label = Label(window, image=resized_img7, border=0, bg='white')
        label.place(x=655, y=240)

def vencimiento(e):
    if form_checker.birthDateChecker(str(fecha_vencimiento.get())):
        label = Label(window, image=resized_img6, border=0, bg='white')
        label.place(x=655, y=295)
    else:
        label = Label(window, image=resized_img7, border=0, bg='white')
        label.place(x=655, y=295)

# configurate frames

frame = Frame(window, width=800, height=1000, bg='#fff', relief='solid', highlightthickness=0)
frame.place(x=200, y=0)
frame.pack(side='left')

frame2 = Frame(window, width=600, height=1000, bg='#fff')
frame2.place(x=660, y=0)

# Images

img = PhotoImage(file='./imgs/dogcat.png')
resized_img = img.subsample(6, 6)
Label(window, image=resized_img, border=0, bg='white').place(x=30, y=20)

img2 = PhotoImage(file='./imgs/clinichistory.png')
resized_img2 = img2.subsample(7, 7)
Label(window, image=resized_img2, border=0, bg='white').place(x=640, y=18)

img3 = PhotoImage(file='./imgs/medicamento.png')
Label(window, border=0, bg = 'white').place(x=400, y=200)

img5 = PhotoImage(file='./imgs/medicamento.png')
resized_img5 = img5.subsample(2, 2)
Label(window, image=resized_img5, border=0, bg='white').place(x=370, y=170)

img6 = PhotoImage(file='./imgs/greencheck.png')
resized_img6 = img6.subsample(100, 100)

img7 = PhotoImage(file='./imgs/redx.png')
resized_img7 = img7.subsample(100, 100)

# header and title

heading = Label(window, text='Clinica Veterinaria Huellita', font=('Century Gothic', 25, 'bold'), bg= 'white', fg='#30302e')
heading.place(x=130, y=14)

heading7 = Label(window, text='Registro\n Medicamento', font=('Century Gothic', 20, 'bold'), fg='#30302e')
heading7.place(x=710, y=20)

heading2 = Label(window, text='Información del medicamento', font=('Century Gothic', 15, 'bold'), fg='#30302e')
heading2.place(x=310, y=120)

heading3 = Label(window, text='Cl. 36d Sur # 27 A-105, Envigado, Medellín', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading3.place(x=132, y=52)

heading4 = Label(window, text='Tel. 43310600', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading4.place(x=132, y=70)

heading5 = Label(window, text='NIT. 900460817-6', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading5.place(x=132, y=90)


# Frame right - "accion terapeutica"
style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Acción terapeutica", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=155)
accion_terapeutica = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('accion_terapeutica', borderwidth=0)
accion_terapeutica.place(x=25, y=180)

# Frame right - "Fecha producción"

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Fecha producción", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=210)
fecha_produccion = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('fecha_produccion', borderwidth=0)
fecha_produccion.place(x=25, y=235)
fecha_produccion.bind("<FocusOut>", produccion)

# Frame right - "Fecha vencimiento"

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Fecha vencimiento", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=265)
fecha_vencimiento= Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('fecha_vencimiento', borderwidth=0)
fecha_vencimiento.place(x=25, y=290)
fecha_vencimiento.bind("<FocusOut>", vencimiento)

# Frame right - "Laboratorio"

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Laboratorio", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=320)
laboratorio = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('laboratorio', borderwidth=0)
laboratorio.place(x=25, y=345)


# Frame left - "Nombre medicamento"

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=0, relief="solid")

title_label = Label(frame, text="Nombre medicamento", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=155)
nombre_medicamento = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('nombre_medicamento', borderwidth=0)
nombre_medicamento.place(x=25, y=180)

# Frame left - "Precio medicamento"

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Precio medicamento", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=210)
precio_medicamento = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('date_birth', borderwidth=0)
precio_medicamento.place(x=25, y=235)


# Frame left - "Presentación medicamento"

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Presentacion medicamento", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=265)
presentacion_medicamento = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('presentacion_medicamento', borderwidth=0)
presentacion_medicamento.place(x=25, y=290)

# Frame left - "codigo medicamento"

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Codigo medicamento", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=320)
cuadro_id = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('cuadro_id', borderwidth=0)

# about the id number
query = "SELECT medicamento.codigo_medicamento FROM medicamento"
mycursor.execute(query)
ids = mycursor.fetchall()
while True:
    contador=0
    valor = random.randint(100000000,999999999)
    for id in ids:
        if id[0] != valor:
              contador +=1
    if contador == len(ids):
        break
valor = str(valor)
cuadro_id.place(x=27, y=345)
cuadro_id.insert(0,valor)
cuadro_id.config(state='readonly')
# ---------
# buttom "registrar" and "regresar"
Button(frame, width=35, pady=7, text='Registrar medicamento', bg='#30302e', fg='white', cursor='hand2', border=0, command=add).place(x=20, y=450)
Button(frame2, width=30, pady=7, text='Regresar', bg='#19b2ff', fg='white', cursor='hand2', border=0, command=back).place(x=20, y=448)
#
window.mainloop()