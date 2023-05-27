from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ast
import form_checker
from PIL import Image, ImageTk
import mysql.connector as mysql

db = mysql.connect(host="127.0.0.1", user="root", password="Sofia2013**", database="clinica_veterinaria_")
mycursor = db.cursor()

# ventana inicial: nombre clinica logo y botón de ingresar

# notes:
# x=400, y =200 is center

# funciones para los botones

def ingresar():  
    value2 = None 
    nitClinica = "900460817-6"
    nombreClinica = "Clinica Veterinaria Huellita"
    direccionClinica = "Cl. 36d Sur # 27 A-105, Envigado, Medellín"
    
    sql = """  INSERT INTO `clinica veterinaria` (NIT_clinica, nombre_clinica, direccion_clinica)
    SELECT %s, %s, %s
    WHERE NOT EXISTS (
        SELECT 1
        FROM `clinica veterinaria`
        WHERE NIT_clinica = %s AND (nombre_clinica IS NOT NULL OR direccion_clinica IS NOT NULL)
    )
    """
    value = (nitClinica, nombreClinica, direccionClinica, nitClinica) # nit clinica -> where not exist nitClinica
    mycursor.execute(sql, value)
    db.commit()
    
    welcome_window.destroy()
    mycursor.close()
    db.close()

    import main_menu

welcome_window = Tk()
welcome_window.title('Clinica Veterinaria Huellita')
welcome_window.geometry('925x600+300+200')
welcome_window.configure(bg='#fff')
welcome_window.resizable(False, False)

frame = Frame(welcome_window, width=600   , height=1000, bg='#fff')
frame.place(x=300, y=0)

img = PhotoImage(file='./imgs/dogcat.png')
resized_img = img.subsample(4, 4)
Label(welcome_window, image=resized_img, border=0, bg='white').place(x=120, y=200)

heading = Label(welcome_window, text='Clinica Veterinaria\nHuellita', font=('Century Gothic', 40, 'bold'), bg= 'white', fg='#30302e')
heading.place(x=260, y=200)

# Ingresar

Button(frame, width=35, pady=7, text='Ingresar', bg='#30302e', fg='white', cursor='hand2', border=0, command=ingresar).place(x=25, y=400)

welcome_window.mainloop()