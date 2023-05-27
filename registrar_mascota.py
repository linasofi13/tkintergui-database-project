from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ast
import form_checker
#from PIL import Image, ImageTk
import mysql.connector as mysql
import random


window = Tk()
window.title('Registro de Mascota')
window.geometry('925x600+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

# connect to database

db = mysql.connect(host="127.0.0.1", user="root", password="Sofia2013**", database="clinica_veterinaria_")
mycursor = db.cursor()

# for button 
def regresar_inicio():
    window.destroy()
    import main_menu


def add_owner():
    
    DNI = DNI_dueno.get()
    nombreDueno = nombre_dueno.get()
    apellidosDueno = apellidos_dueno.get()  
    direccionDueno = direccion_dueno.get()
    emailDueno = email_dueno.get()
    
    sql = "INSERT INTO dueno (dni_dueno, nombre_dueno, apellidos_dueno, direccion_dueno, email_dueno) VALUES(%s, %s, %s, %s, %s)"
    value = (DNI, nombreDueno, apellidosDueno, direccionDueno, emailDueno)
    mycursor.execute(sql, value)
    db.commit()
    
def add_pet():
    id_mascota = ""
    for i in range(6):
        num = str(random.randint(0,10))
        id_mascota += num

    nombreMascota = nombre_mascota.get()
    edadMascota = date_birth.get()
    tipoMascota = tipo_mascota.get()
    vacunasMascota = vacunas_mascota.get()
    procedimientosMascota = procedimientos_mascota.get()
    alergiasMascota = alergias_mascota.get()
    
   # query = "SELECT dni_dueno FROM dueno WHERE owner_name = %s"
    
    DNIDueno = DNI_dueno.get()
    
    sql = "INSERT INTO mascota (codigo_mascota, edad_mascota, tipo_mascota, nombre_mascota, dni_dueño) VALUES(%s, %s, %s, %s, %s)"
    value = (id_mascota, edadMascota, tipoMascota, nombreMascota, DNIDueno)
    mycursor.execute(sql, value)
    
    # atributos multivalorados
    
    enfermedadesMascota = enfermedades_mascota.get() 
    insert_enfermedad_query = "INSERT INTO enfermedades (codigo_mascota, enfermedad_mascota) VALUES (%s, %s)"
    enfermedad_values = (id_mascota, enfermedadesMascota)
    mycursor.execute(insert_enfermedad_query, enfermedad_values)
    
    alergiasMascota = alergias_mascota.get() 
    insert_alergias_query = "INSERT INTO alergias (codigo_mascota, alergia_mascota) VALUES (%s, %s)"
    alergias_values = (id_mascota, alergiasMascota)
    mycursor.execute(insert_alergias_query, alergias_values)
    
    vacunasMascota = vacunas_mascota.get() 
    insert_vacunas_query = "INSERT INTO vacunas (codigo_mascota, vacuna_mascota) VALUES (%s, %s)"
    vacunas_values = (id_mascota, vacunasMascota)
    mycursor.execute(insert_vacunas_query, vacunas_values)
    
    procedimientosMascota = procedimientos_mascota.get() 
    insert_procedimientos_query = "INSERT INTO procedimientos_quirurgicos (codigo_mascota, procedimiento_quirurgico_mascota) VALUES (%s, %s)"
    procedimientos_values = (id_mascota, procedimientosMascota)
    mycursor.execute(insert_procedimientos_query, procedimientos_values)
    
    db.commit()

trigger_query = """
CREATE TRIGGER IF NOT EXISTS before_insert_trigger
BEFORE INSERT ON mascota
FOR EACH ROW
BEGIN
    SET NEW.nombre_mascota = UPPER(NEW.nombre_mascota);
    SET NEW.tipo_mascota = UPPER(NEW.tipo_mascota);
END
"""
mycursor.execute(trigger_query)
    
#add_clinic() # cant be executed as the same time the others are
def add():
    add_owner()
    add_pet()
     
# mysql connection

frame = Frame(window, width=800, height=1000, bg='#fff', relief='solid', highlightthickness=0)
frame.place(x=200, y=0)
frame.pack(side='left', fill='y')

frame2 = Frame(window, width=600   , height=1000, bg='#fff')
frame2.place(x=300, y=0)

#frame2.pack(side='right', fill='y')
# Image of Pet Shop
img = PhotoImage(file='./imgs/dogcat.png')
resized_img = img.subsample(6, 6)
Label(window, image=resized_img, border=0, bg='white').place(x=30, y=20)

img2 = PhotoImage(file='./imgs/clinichistory.png')
resized_img2 = img2.subsample(7, 7)

Label(window, image=resized_img2, border=0, bg='white').place(x=720, y=7)

img3 = PhotoImage(file='./imgs/greencheck.png')
resized_img3 = img3.subsample(10, 10)


img3 = PhotoImage(file='./imgs/greencheck.png')
resized_img3 = img3.subsample(100, 100)
#Label(window, image=resized_img3, border=0, bg='white').place(x=720, y=7)

img4 = PhotoImage(file='./imgs/redx.png')
resized_img4 = img4.subsample(100, 100)

img5 = PhotoImage(file='./imgs/dogowner.png')
resized_img5 = img5.subsample(2, 2)

Label(window, image=resized_img5, border=0, bg='white').place(x=600, y=170)

# Label(window, image=resized_img4, border=0, bg='white').place(x=720, y=7)

# Main Label with the input frames

# Clinica veterinaria huellita
heading = Label(window, text='Clinica Veterinaria Huellita', font=('Century Gothic', 25, 'bold'), bg= 'white', fg='#30302e')
heading.place(x=130, y=14)

heading7 = Label(window, text='Historia\nClínica', font=('Century Gothic', 20, 'bold'), fg='#30302e')
heading7.place(x=800, y=10)

heading2 = Label(window, text='Información de la Mascota', font=('Century Gothic', 15, 'bold'), fg='#30302e')
heading2.place(x=25, y=120)

heading2 = Label(window, text='Información del Dueño', font=('Century Gothic', 15, 'bold'), fg='#30302e')
heading2.place(x=320, y=120)

heading3 = Label(window, text='Cl. 36d Sur # 27 A-105, Envigado, Medellín', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading3.place(x=132, y=52)

heading4 = Label(window, text='Tel. 43310600', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading4.place(x=132, y=70)

heading5 = Label(window, text='NIT. 900460817-6', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading5.place(x=132, y=90)


# Nombre del Dueño

def on_leave(e):
    if form_checker.nameChecker(str(nombre_dueno.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=540, y=185)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=540, y=185)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Nombre del Dueño", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=155)
#title_label.pack(pady=10)
nombre_dueno = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('nombre_dueno', borderwidth=0)
nombre_dueno.place(x=25, y=180)
#nombre_dueno.insert(0, 'Nombre Dueño')
nombre_dueno.bind("<FocusOut>", on_leave)

# Apellidos  dueño

def on_leave(e):
    if form_checker.nameChecker(str(apellidos_dueno.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=540, y=240)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=540, y=240)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Apellidos", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=210)
#title_label.pack(pady=10)
apellidos_dueno = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('apellidos_dueno', borderwidth=0)
apellidos_dueno.place(x=25, y=235)
#apellidos_dueno.insert(0, 'Nombre Dueño')
apellidos_dueno.bind("<FocusOut>", on_leave)


# DNI dueño

def on_leave(e):
    if form_checker.nameChecker(str(DNI_dueno.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=540, y=295)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=540, y=295)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="DNI", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=265)
#title_label.pack(pady=10)
DNI_dueno = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('DNI_dueno', borderwidth=0)
DNI_dueno.place(x=25, y=290)
#DNI_dueno.insert(0, 'Nombre Dueño')
DNI_dueno.bind("<FocusOut>", on_leave)

# Direccion dueño

def on_leave(e):
    if form_checker.nameChecker(str(direccion_dueno.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=540, y=350)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=540, y=350)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Dirección", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=320)
#title_label.pack(pady=10)
direccion_dueno = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('direccion_dueno', borderwidth=0)
direccion_dueno.place(x=25, y=345)
#direccion_dueno.insert(0, 'Nombre Dueño')
direccion_dueno.bind("<FocusOut>", on_leave)

# Direccion dueño
# Verificacion TODO

def on_leave(e):
    if form_checker.checkEmail(str(email_dueno.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=540, y=405)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=540, y=405)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Correo Electrónico", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=375)
#title_label.pack(pady=10)
email_dueno = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('email_dueno', borderwidth=0)
email_dueno.place(x=25, y=400)
#email_dueno.insert(0, 'Nombre Dueño')
email_dueno.bind("<FocusOut>", on_leave)

# Teléfono dueño -- verificacion solo numeros ??? TODO
# Multivalorado TODO

def on_leave(e):
    if form_checker.nameChecker(str(telefonos_dueno.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=540, y=465)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=540, y=465)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Teléfono", font=('Century Gothic', 11), bg='white')
title_label.place(x=23, y=435)
#title_label.pack(pady=10)
telefonos_dueno = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('telefonos_dueno', borderwidth=0)
telefonos_dueno.place(x=25, y=460)
#telefonos_dueno.insert(0, 'Nombre Dueño')
telefonos_dueno.bind("<FocusOut>", on_leave)

# ---------------------------------------------------


# Nombre de la mascota

def on_leave(e):
    if form_checker.nameChecker(str(nombre_mascota.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=240, y=185)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=240, y=185)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=0, relief="solid")

title_label = Label(frame, text="Nombre de la Mascota", font=('Century Gothic', 11), bg='white')
title_label.place(x=28, y=155)
#title_label.pack(pady=10)
nombre_mascota = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('nombre_mascota', borderwidth=0)
nombre_mascota.place(x=28, y=180)
#nombre_mascota.insert(0, 'Nombre Mascota')
nombre_mascota.bind("<FocusOut>", on_leave)

#nombre_mascota.grid(row=0, column=0, padx=10, pady=5)
#Frame(frame, width=295, height=2, bg='black').place(x=25, y=195)
# Fecha de nacimiento Entry

# fecha nacimiento

def on_leave(e):
    if form_checker.birthDateChecker(str(date_birth.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=240, y=240)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=240, y=240)
style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Fecha de Nacimiento", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=210)
#title_label.pack(pady=10)
date_birth = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('date_birth', borderwidth=0)
date_birth.place(x=27, y=235)
#date_birth.insert(0, 'Nombre Mascota')
date_birth.bind("<FocusOut>", on_leave)



# Tipo mascota - Entry


def on_leave(e):
    if form_checker.nameChecker(str(tipo_mascota.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=240, y=295)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=240, y=295)


style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Tipo Mascota", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=265)
#title_label.pack(pady=10)
tipo_mascota = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('tipo_mascota', borderwidth=0)
tipo_mascota.place(x=27, y=290)
#tipo_mascota.insert(0, 'Nombre Mascota')
tipo_mascota.bind("<FocusOut>", on_leave)

# Alergias- Entry

# (x=25, y=362)
def on_leave(e):
    if form_checker.nameChecker(str(alergias_mascota.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=240, y=350)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=240, y=350)


style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Alergias", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=320)
#title_label.pack(pady=10)
alergias_mascota = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('alergias_mascota', borderwidth=0)
alergias_mascota.place(x=27, y=345)
#alergia.insert(0, 'Nombre Mascota')
alergias_mascota.bind("<FocusOut>", on_leave)
# ---------

#(x=25, y=417)
# Enfermedades Entry

def on_leave(e):
    if form_checker.nameChecker(str(enfermedades_mascota.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=240, y=405)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=240, y=405)


style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Enfermedades", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=375)
#title_label.pack(pady=10)
enfermedades_mascota = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('enfermedades_mascota', borderwidth=0)
enfermedades_mascota.place(x=27, y=400)
#alergia.insert(0, 'Nombre Mascota')
enfermedades_mascota.bind("<FocusOut>", on_leave)

#(x=25, y=472)
# Procedimientos Quirurjicos Entry

def on_leave(e):
    if form_checker.nameChecker(str(procedimientos_mascota.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=240, y=460)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=240, y=460)


style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Procedimientos Quirúrjicos", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=430)
#title_label.pack(pady=10)
procedimientos_mascota = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('procedimientos_mascota', borderwidth=0)
procedimientos_mascota.place(x=27, y=455)
#alergia.insert(0, 'Nombre Mascota')
procedimientos_mascota.bind("<FocusOut>", on_leave)


# Vacunas - Entry

def on_leave(e):
    if form_checker.nameChecker(str(vacunas_mascota.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=240, y=515)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=240, y=515)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Vacunas", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=485)
#title_label.pack(pady=10)
vacunas_mascota = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('vacunas_mascota', borderwidth=0)
vacunas_mascota.place(x=27, y=510)
vacunas_mascota.bind("<FocusOut>", on_leave)


# ---------

# Registrar Mascota Button and Sign In Button
Button(frame, width=35, pady=7, text='Registrar Mascota', bg='#30302e', fg='white', cursor='hand2', border=0, command=add).place(x=25, y=550)
Button(frame2, width=30, pady=7, text='Regresar', bg='#19b2ff', fg='white', cursor='hand2', border=0, command=regresar_inicio).place(x=20, y=550)
label = Label(frame, text='Ver registro de Mascotas ', font=('Century Gothic', 9), bg='white', fg='black')
label.place(x=27, y=600)

window.mainloop()
