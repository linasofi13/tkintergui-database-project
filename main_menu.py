from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ast
import form_checker
from PIL import Image, ImageTk

main_menu = Tk()
main_menu.title('Menú Principal')
main_menu.geometry('925x600+300+200')
main_menu.configure(bg='#fff')
main_menu.resizable(False, False)

frame = Frame(main_menu, width=600   , height=1000, bg='#fff')
frame.place(x=300, y=0)

frame2 = Frame(main_menu, width=500   , height=1000, bg='#fff')
frame2.place(x=600, y=0)

""" HEADER """

img = PhotoImage(file='./imgs/dogcat.png')
resized_img = img.subsample(6, 6)
Label(main_menu, image=resized_img, border=0, bg='white').place(x=30, y=20)


heading = Label(main_menu, text='Clinica Veterinaria Huellita', font=('Century Gothic', 25, 'bold'), bg= 'white', fg='#30302e')
heading.place(x=130, y=14)

heading3 = Label(main_menu, text='Cl. 36d Sur # 27 A-105, Envigado, Medellín', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading3.place(x=132, y=52)

heading4 = Label(main_menu, text='Tel. 43310600', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading4.place(x=132, y=70)

heading5 = Label(main_menu, text='NIT. 900460817-6', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading5.place(x=132, y=90)

""""""

def registrar_mascota():
    main_menu.destroy()
    import registrar_mascota
    
def registrar_empleado():
    main_menu.destroy()
    import registrar_empleado
    
def generar_formula():
    main_menu.destroy()
    import generar_formula
    
def registrar_medicamento():
    main_menu.destroy()
    import registrar_medicamento
    
def registrar_empleado():
    main_menu.destroy()
    import registrar_empleado
    
def agendar_cita():
    main_menu.destroy()
    import generar_cita
    
def generar_compra():
    main_menu.destroy()
    import generar_compra
    
def ver_registros():
    main_menu.destroy()
    import ver_registros
    
def regresar_inicio():
    main_menu.destroy()
    import welcome
    
def ver_mascotas():
    main_menu.destroy()
    import ver_mascotas
    
def ver_empleados():
    main_menu.destroy()
    import ver_empleados
    
Button(frame, width=35, pady=7, text='Registrar Mascota', bg='#30302e', fg='white', cursor='hand2', border=0, command=registrar_mascota).place(x=10, y=150)

Button(frame, width=35, pady=7, text='Registrar Empleado', bg='#30302e', fg='white', cursor='hand2', border=0, command=registrar_empleado).place(x=10, y=200)

Button(frame, width=35, pady=7, text='Generar Fórmula Médica', bg='#30302e', fg='white', cursor='hand2', border=0, command=generar_formula).place(x=10, y=250)

Button(frame, width=35, pady=7, text='Registrar Medicamento', bg='#30302e', fg='white', cursor='hand2', border=0, command=registrar_medicamento).place(x=10, y=300)

Button(frame, width=35, pady=7, text='Agendar Cita', bg='#30302e', fg='white', cursor='hand2', border=0, command=agendar_cita).place(x=10, y=350)

Button(frame, width=35, pady=7, text='Generar Compra', bg='#30302e', fg='white', cursor='hand2', border=0, command=generar_compra).place(x=10, y=400)


Button(frame, width=35, pady=7, text='Regresar', bg='#19b2ff', fg='white', cursor='hand2', border=0, command=regresar_inicio).place(x=10, y=500)

# frame 2

Button(frame2, width=35, pady=7, text='Ver Mascotas', bg='#30302e', fg='white', cursor='hand2', border=0, command=ver_mascotas).place(x=10, y=150) # que se pueda buscar por mascota y por dueño

Button(frame2, width=35, pady=7, text='Ver Empleados', bg='#30302e', fg='white', cursor='hand2', border=0, command=ver_empleados).place(x=10, y=200)

main_menu.mainloop()

