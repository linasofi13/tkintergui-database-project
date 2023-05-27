from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ast
import form_checker
from PIL import Image, ImageTk
import mysql.connector as mysql



window = Tk()
window.title('Registro de Empleado')
window.geometry('700x620+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

db = mysql.connect(host="127.0.0.1", user="root", password="Sofia2013**", database="clinica_veterinaria_")
mycursor = db.cursor()

def add_employee():
    
    nombreEmpleado = nombre_empleado.get()
    fechaEmpleado = fecha_empleado.get()
    apellidosEmpleado = apellidos_empleado.get()
    DNIEmpleado = DNI_empleado.get()
    salarioEmpleado = salario_empleado.get()
    experienciaEmpleado = experiencia_empleado.get()
    tituloEmpleado = titulo_empleado.get()
    ssEmpleado = ss_empleado.get()
    telefonoEmpleado = telefono_empleado.get()
    direccionEmpleado = direccion_empleado.get()
    
    sql1 = "SELECT NIT_clinica FROM `clinica veterinaria` LIMIT 1;"
    mycursor.execute(sql1)
    NIT_clinica = mycursor.fetchone()[0]
    
    sql = "INSERT INTO empleado (dni_empleado, numero_seguridad_social_empleado, telefono_empleado, titulo_empleado, experiencia_laboral_empleado, salario_empleado, nombre_empleado, apellidos_empleado, direccion_empleado, NIT_clinitica) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (DNIEmpleado, ssEmpleado, telefonoEmpleado, tituloEmpleado, experienciaEmpleado, int(salarioEmpleado), nombreEmpleado, apellidosEmpleado, direccionEmpleado, NIT_clinica)
    mycursor.execute(sql, value)
    db.commit()
    
trigger_query = """
CREATE TRIGGER IF NOT EXISTS _before_insert_trigger_
BEFORE INSERT ON empleado
FOR EACH ROW
BEGIN
    SET NEW.nombre_empleado = UPPER(NEW.nombre_empleado);
    SET NEW.titulo_empleado = UPPER(NEW.titulo_empleado);
    SET NEW.apellidos_empleado = UPPER(NEW.apellidos_empleado);
END
"""
mycursor.execute(trigger_query)

frame = Frame(window, width=600, height=1000, bg='#fff', relief='solid', highlightthickness=0)
frame.place(x=20, y=0)

frame2 = Frame(window, width=600, height=1000, bg='#fff')
frame2.place(x=335, y=0)

# frame3 = Frame(window, width=600, height=1000, bg='#fff')
# frame3.place(x=565, y=0)
#frame2.pack(side='right', fill='y')
# Image of Pet Shop
img = PhotoImage(file='./imgs/dogcat.png')
resized_img = img.subsample(6, 6)
Label(window, image=resized_img, border=0, bg='white').place(x=30, y=20)

img2 = PhotoImage(file='./imgs/clinichistory.png')
resized_img2 = img2.subsample(8, 8)

Label(window, image=resized_img2, border=0, bg='white').place(x=500, y=80)

img3 = PhotoImage(file='./imgs/greencheck.png')
resized_img3 = img3.subsample(10, 10)


img3 = PhotoImage(file='./imgs/greencheck.png')
resized_img3 = img3.subsample(100, 100)
#Label(window, image=resized_img3, border=0, bg='white').place(x=720, y=7)

img4 = PhotoImage(file='./imgs/redx.png')
resized_img4 = img4.subsample(100, 100)

img5 = PhotoImage(file='./imgs/veterinario.png') # veterinaria
resized_img5 = img5.subsample(3, 3)
Label(window, image=resized_img5, border=0, bg='white').place(x=400, y=170)
# Label(window, image=resized_img4, border=0, bg='white').place(x=720, y=7)



# Main Label with the input frames


# Clinica veterinaria huellita
heading = Label(window, text='Clinica Veterinaria Huellita', font=('Century Gothic', 25, 'bold'), bg= 'white', fg='#30302e')
heading.place(x=130, y=14)

heading7 = Label(window, text='Registro\nEmpleados', font=('Century Gothic', 15, 'bold'), fg='#30302e')
heading7.place(x=570, y=85)

heading2 = Label(window, text='Información del Empleado', font=('Century Gothic', 15, 'bold'), fg='#30302e')
heading2.place(x=45, y=120)

heading3 = Label(window, text='Cl. 36d Sur # 27 A-105, Envigado, Medellín', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading3.place(x=132, y=52)

heading4 = Label(window, text='Tel. 43310600', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading4.place(x=132, y=70)

heading5 = Label(window, text='NIT. 900460817-6', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading5.place(x=132, y=90)

def regresar_inicio():
    window.destroy()
    import main_menu

# Nombre del empleado

def on_leave(e):
    if form_checker.nameChecker(str(nombre_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=185)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=260, y=185)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Nombre del Empleado", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=155)
#title_label.pack(pady=10)
nombre_empleado = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('nombre_empleado', borderwidth=0)
nombre_empleado.place(x=28, y=180)
#nombre_empleado.insert(0, 'Nombre Mascota')
nombre_empleado.bind("<FocusOut>", on_leave)

#nombre_mascota.grid(row=0, column=0, padx=10, pady=5)

#Frame(frame, width=295, height=2, bg='black').place(x=25, y=195)
# Fecha de nacimiento Entry

# Apellidos Empleado

def on_leave(e):
    if form_checker.nameChecker(str(apellidos_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=295)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=260, y=295)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Apellidos", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=265)
#title_label.pack(pady=10)
apellidos_empleado = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('apellidos_empleado', borderwidth=0)
apellidos_empleado.place(x=27, y=290)
#apellidos_empleado.insert(0, 'Nombre Mascota')
apellidos_empleado.bind("<FocusOut>", on_leave)



# Fecha de nacimiento Empleado

def on_leave(e):
    if form_checker.birthDateChecker(str(fecha_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=240)
    else:
        label = Label(window, image=resized_img4, border=0, bg='white')
        label.place(x=260, y=240)


style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Fecha de Nacimiento", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=210)
#title_label.pack(pady=10)
fecha_empleado = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('fecha_empleado', borderwidth=0)
fecha_empleado.place(x=27, y=235)
#fecha_empleado.insert(0, 'Nombre Mascota')
fecha_empleado.bind("<FocusOut>", on_leave)



# TItulo Empleado - Entry

# (x=25, y=362)
def on_leave(e):
    if form_checker.nameChecker(str(titulo_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=350)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=350)


style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Título", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=320)
#title_label.pack(pady=10)
titulo_empleado = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('titulo_empleado', borderwidth=0)
titulo_empleado.place(x=27, y=345)
#alergia.insert(0, 'Nombre Mascota')
titulo_empleado.bind("<FocusOut>", on_leave)

# ---




# idea -> cantidad de salarios, nomina total que se da en la clinica con la cantidad de registros de empleados


# ---------


#(x=25, y=417)
# Numero Seguridad Social Entry

def on_leave(e):
    if form_checker.nameChecker(str(ss_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=405)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=405)


style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="# Seguridad Social", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=375)
#title_label.pack(pady=10)
ss_empleado = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('ss_empleado', borderwidth=0)
ss_empleado.place(x=27, y=400)
#alergia.insert(0, 'Nombre Mascota')
ss_empleado.bind("<FocusOut>", on_leave)

#(x=25, y=472)
# Experiencia Laboral Entry


def on_leave(e):
    if form_checker.nameChecker(str(experiencia_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=460)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=460)


style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Experiencia Laboral", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=430)
#title_label.pack(pady=10)
experiencia_empleado = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('experiencia_empleado', borderwidth=0)
experiencia_empleado.place(x=27, y=455)
#alergia.insert(0, 'Nombre Mascota')
experiencia_empleado.bind("<FocusOut>", on_leave)


# Direccion empleado - Entry

def on_leave(e):
    if form_checker.nameChecker(str(direccion_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=515)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=515)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Dirección", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=485)
#title_label.pack(pady=10)
direccion_empleado = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('direccion_empleado', borderwidth=0)
direccion_empleado.place(x=27, y=510)
#alergia.insert(0, 'Nombre Mascota')
direccion_empleado.bind("<FocusOut>", on_leave)

# Salario Empledo - Entry


def on_leave(e):
    if form_checker.nameChecker(str(salario_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=570)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=570)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame, text="Salario", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=540)
#title_label.pack(pady=10)
salario_empleado = Entry(frame, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('salario_empleado', borderwidth=0)
salario_empleado.place(x=27, y=565)
#alergia.insert(0, 'Nombre Mascota')
salario_empleado.bind("<FocusOut>", on_leave)

# FRAME 2


# Telefono Empleado Entry


def on_leave(e):
    if form_checker.nameChecker(str(telefono_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=435)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=435)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="Teléfono", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=405)
#title_label.pack(pady=10)
telefono_empleado = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('telefono_empleado', borderwidth=0)
telefono_empleado.place(x=27, y=430)
#alergia.insert(0, 'Nombre Mascota')
telefono_empleado.bind("<FocusOut>", on_leave)

# DNI Empleado Entry

def on_leave(e):
    if form_checker.nameChecker(str(DNI_empleado.get())):
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=375)
    else:
        label = Label(window, image=resized_img3, border=0, bg='white')
        label.place(x=260, y=375)

style = ttk.Style()
style.theme_use("default")
style.configure("CustomEntry.TEntry", padding=5, relief="solid")

title_label = Label(frame2, text="DNI", font=('Century Gothic', 11), bg='white')
title_label.place(x=25, y=345)
#title_label.pack(pady=10)
DNI_empleado = Entry(frame2, width=25, border=4, font=('Century Gothic', 11), bg='white', relief="groove")
style.configure('DNI_empleado', borderwidth=0)
DNI_empleado.place(x=27, y=370)
#alergia.insert(0, 'Nombre Mascota')
#DNI_empleado.bind("<FocusIn>", on_enter)
DNI_empleado.bind("<FocusOut>", on_leave)


# ---------

# Registrar Mascota Button and Sign In Button
Button(frame2, width=29, pady=7, text='Registrar Empleado', bg='#30302e', fg='white', cursor='hand2', border=0, command=add_employee).place(x=28, y=470)
Button(frame2, width=29, pady=7, text='Registrar Empleado', bg='#30302e', fg='white', cursor='hand2', border=0, command=add_employee).place(x=28, y=470)
Button(frame2, width=29, pady=7, text='Regresar', bg='#19b2ff', fg='white', cursor='hand2', border=0, command=regresar_inicio).place(x=28, y=515)


# Aqui Button
#signin = Button(frame, text='Aquí', width=6, bg='white', fg='#30302e', border=0, cursor='hand2',
#                command=signin_command)
#signin.place(x=240, y=172)


# Dueñoooooooooooooooooooo



# owner frame ------------------------------------

# Create the original frame


# Call the duplicate_frame function to create a new frame
owner_frame = frame
window.mainloop()

