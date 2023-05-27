from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ast
import form_checker
from PIL import Image, ImageTk
import mysql.connector as mysql
import random

window = Tk()
window.title('Ver Registros Empleado')
window.geometry('925x600+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

db = mysql.connect(host="127.0.0.1", user="root", password="Sofia2013**", database="clinica_veterinaria_")
mycursor = db.cursor()

""" HEADER """

img = PhotoImage(file='./imgs/dogcat.png')

img2 = PhotoImage(file='./imgs/lupa.png')

resized_img = img.subsample(6, 6)
resized_img2 = img2.subsample(12, 12)
Label(window, image=resized_img, border=0, bg='white').place(x=30, y=20)

heading = Label(window, text='Clinica Veterinaria Huellita', font=('Century Gothic', 25, 'bold'), bg= 'white', fg='#30302e')
heading.place(x=130, y=14)

heading3 = Label(window, text='Cl. 36d Sur # 27 A-105, Envigado, Medellín', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading3.place(x=132, y=52)

heading4 = Label(window, text='Tel. 43310600', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading4.place(x=132, y=70)

heading5 = Label(window, text='NIT. 900460817-6', font=('Century Gothic', 8), bg='white', fg='#30302e')
heading5.place(x=132, y=90)


# funcioon en sql para obtener el mayor salario de los empleados

query = """CREATE FUNCTION IF NOT EXISTS `mayor_salario` ()
RETURNS INT
        READS SQL DATA
        BEGIN

        DECLARE mayor_salario_ integer;

        SELECT MAX(salario_empleado) INTO mayor_salario_ FROM empleado;
        RETURN mayor_salario_;

END"""

mycursor.execute(query)


""""""

def clicker(e):
	select_record()

def regresar_menu():
    window.destroy()
    import main_menu
    
def mayor_salario():
    dni_empleado = name_box.get()
    telefono_empleado = id_box.get()
    nombre_empleado = topping_box.get()
    
    mycursor.execute("SELECT mayor_salario() AS salario_mayor")
    result = mycursor.fetchone()
    
    query = "SELECT * FROM empleado WHERE salario_empleado = %s"
    values = (result)
    mycursor.execute(query, values)
    results = mycursor.fetchall()

    my_tree.delete(*my_tree.get_children())

    row_count = 0
    for row in results:
        if row_count % 2 == 0:
            my_tree.insert("", "end", values=row, tags=("evenrow",))
        else:
            my_tree.insert("", "end", values=row, tags=("oddrow",))
        row_count += 1
    
def buscar_empleado():
    dni_empleado = name_box.get()
    telefono_empleado = id_box.get()
    nombre_empleado = topping_box.get()

    query = "SELECT * FROM empleado WHERE dni_empleado = %s OR telefono_empleado = %s OR nombre_empleado = %s"
    values = (dni_empleado, telefono_empleado, nombre_empleado)

    mycursor.execute(query, values)
    results = mycursor.fetchall()

    my_tree.delete(*my_tree.get_children())

    row_count = 0
    for row in results:
        if row_count % 2 == 0:
            my_tree.insert("", "end", values=row, tags=("evenrow",))
        else:
            my_tree.insert("", "end", values=row, tags=("oddrow",))
        row_count += 1
        
def eliminar_empleado():
    selected_items = my_tree.selection()

    if not selected_items:
        messagebox.showinfo("Error", "No ha seleccionado ningún registro.")
        return

    confirm = messagebox.askyesno("Confirmar Borrado", "¿Está seguro que desea eliminar?")
    if not confirm:
        return

    try:
        for item in selected_items:
        
            values = my_tree.item(item, 'values')

            
            record_id = values[0]

            
            query = "DELETE FROM empleado WHERE dni_empleado = %s" 
            mycursor.execute(query, (record_id,))
            db.commit()

            # Delete the selected item from the treeview
            my_tree.delete(item)

        messagebox.showinfo("Éxito", "Se han eliminado los registros.")

    except mysql.Error as error:
        messagebox.showerror("Error", f"Error eliminando los registros: {error}")

def editar_empleado():
    selected = my_tree.focus()

    # Obtener los valores existentes de la fila seleccionada
    values = my_tree.item(selected, 'values')
    dni_empleado = values[0]
    nit_clinica = values[1]
    numero_seguridad_social_empleado = values[2]
    telefono_empleado = values[3]  
    titulo_empleado = values[4]  
    experiencia_laboral_empleado = values[5]  
    salario_empleado = values[6]
    nombre_empleado = values[7]
    apellidos_empleado = values[8]
    direccion_empleado = values[9]

    # Actualizar los valores de las casillas de entrada
    dni_empleado_new = name_box.get()
    telefono_new = id_box.get()
    nombre_empleado_new = topping_box.get()
    numero_ss_new = numero_ss_box.get()
    titulo_new = titulo_box.get()
    experiencia_new = experiencia_box.get()
    salario_new = salario_box.get()

	# Actualizar el Treeview con los nuevos valores
    my_tree.item(selected, values=(dni_empleado_new, nit_clinica, numero_ss_new, telefono_new, titulo_new, experiencia_new, salario_new, nombre_empleado_new, procedimientos_box_new))

    # update en sql
    query = "UPDATE mascota SET codigo_mascota = %s, dni_dueño = %s, nombre_mascota = %s WHERE codigo_mascota = %s"
    values = (codigo_mascota_new, dni_dueno_new, nombre_mascota_new, codigo_mascota)
    
    query2 = "UPDATE enfermedades SET enfermedad_mascota = %s WHERE codigo_mascota = %s"
    values2 = (enfermedades_box_new, codigo_mascota)
    
    query3 = "UPDATE alergias SET alergia_mascota = %s WHERE codigo_mascota = %s"
    values3 = (alergias_box_new, codigo_mascota)
    
    query4 = "UPDATE vacunas SET vacuna_mascota = %s WHERE codigo_mascota = %s"
    values4 = (vacunas_box_new, codigo_mascota)
    
    query5 = "UPDATE procedimientos_quirurgicos SET procedimiento_quirurgico_mascota = %s WHERE codigo_mascota = %s"
    values5 = (proceddimientos_box_new, codigo_mascota)

    try:
        mycursor.execute(query, values)
        mycursor.execute(query2, values2)
        mycursor.execute(query3, values3)
        mycursor.execute(query4, values4)
        mycursor.execute(query5, values5)

        db.commit()

        messagebox.showinfo("Éxito", "Se ha actualizado el registro.")

    except mysql.Error as error:
        messagebox.showerror("Error", f"Error actualizando el registro: {error}")


style = ttk.Style()
style.theme_use("default")
# Configure our treeview colors

style.configure("Treeview", 
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="white",
	font=("Century Gothic", 12)
	)

style.configure("Treeview.Heading",
                font=("Century Gothic", 11, "bold"),
                background="#0f9abd",
                foreground="white")
# Change selected color
style.map('Treeview', 
	background=[('selected', 'gray')])


# Create Treeview Frame
tree_frame = Frame(window, width=800, height=400, bg='#fff')
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)  # Agregar margen con padx y pady


# Create vertical scrollbar
v_scrollbar = Scrollbar(tree_frame, orient="vertical")
v_scrollbar.pack(side="right", fill="y")

# Create horizontal scrollbar
h_scrollbar = Scrollbar(tree_frame, orient="horizontal")
h_scrollbar.pack(side="bottom", fill="x")

my_tree = ttk.Treeview(
    tree_frame,
    yscrollcommand=v_scrollbar.set,
    xscrollcommand=h_scrollbar.set,
    selectmode="extended",
    height=10
)
my_tree.pack()

# Attach scrollbars to the treeview


tree_frame.place(x=50, y=130)




# Retrieve mascota records with aggregated enfermedades
query = """
    SELECT m.dni_empleado, m.direccion_empleado, m.numero_seguridad_social_empleado, m.telefono_empleado, m.titulo_empleado, m.experiencia_laboral_empleado, m.salario_empleado, m.nombre_empleado, m.apellidos_empleado
    FROM empleado m
"""

mycursor.execute(query)
results = mycursor.fetchall()

column_names = ("DNI", "Dirección", "# SS", "Telefono", "Título", "Experiencia Laboral", "Salario Empleado", "Nombre", "Apellidos")
my_tree['columns'] = column_names

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightgray")

# Track the row count
row_count = 0

for row in results:
    # Alternate between oddrow and evenrow tags based on the row count
    if row_count % 2 == 0:
        my_tree.insert('', 'end', values=row, tags=('evenrow',))
    else:
        my_tree.insert('', 'end', values=row, tags=('oddrow',))

    row_count += 1

    
for index, column in enumerate(column_names):
    my_tree.column(column, anchor='center', width=90)  # Adjust the width value as needed
    my_tree.heading(column, text=column)
    my_tree.column("#0", width=0)  # Hide the leftmost column (tree item ID)
    

# Add Data
"""
data = [
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
]
"""


global count
count=0

"""
for record in data:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))

	count += 1
 
"""

# -----------
'''
my_tree.insert(parent='', index='end', iid=0, text="", values=("John", 1, "Peperroni"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Mary", "2", "Cheese"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Tina", "3", "Ham"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Bob", "4", "Supreme"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Erin", "5", "Cheese"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Wes", "6", "Onion"))
'''

# buscar registro de mascota

Button(window, width=15, height=1, pady=7, text='Regresar', bg='#19b2ff', fg='white', cursor='hand2', border=0, command=regresar_menu).place(x=45, y=550)

add_frame = Frame(window)
add_frame.place(x=230, y=1)
add_frame.place(relx=0.5, rely=0.5, anchor='center')  # Adjust the rely value to move it down
add_frame.place(relx=0.25, rely=0.75, anchor='center')  # Adjust the relx value to move it to the right

#Labels
nl = Label(add_frame, text="DNI", font=('Century Gothic', 10))
nl.grid(row=0, column=0)

il = Label(add_frame, text="Direccion", font=('Century Gothic', 10))
il.grid(row=0, column=1)

tl = Label(add_frame, text="Titulo", font=('Century Gothic', 10))
tl.grid(row=0, column=2)

po = Label(add_frame, text="Experiencia", font=('Century Gothic', 10))
po.grid(row=0, column=3)

er = Label(add_frame, text="Salario", font=('Century Gothic', 10))
er.grid(row=0, column=4)

gu = Label(add_frame, text="Nombre", font=('Century Gothic', 10))
gu.grid(row=0, column=5)

la = Label(add_frame, text="Apellidos", font=('Century Gothic', 10))
la.grid(row=0, column=6)


#Entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

numero_ss_box = Entry(add_frame)
numero_ss_box.grid(row=1, column=3)

titulo_box = Entry(add_frame)
titulo_box.grid(row=1, column=4)

experiencia_box = Entry(add_frame)
experiencia_box.grid(row=1, column=5)

salario_box = Entry(add_frame)
salario_box.grid(row=1, column=6)

Button(window, width=15, height=1, pady=7, text='Buscar', bg='#30302e', fg='white', cursor='hand2', border=0, command=buscar_empleado).place(x=27, y=490)
Button(window, width=15, height=1, pady=7, text='Eliminar', bg='#30302e', fg='white', cursor='hand2', border=0, command=eliminar_empleado).place(x=155, y=490)
Button(window, width=15, height=1, pady=7, text='Editar', bg='#30302e', fg='white', cursor='hand2', border=0, command=editar_empleado).place(x=280, y=490)
Button(window, width=25, height=1, pady=7, text='Obtener Mayor Salario', bg='#30302e', fg='white', cursor='hand2', border=0, command=mayor_salario).place(x=410, y=490)
# Select Record
def select_record():
	# Clear entry boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)
    numero_ss_box.delete(0, END)
    titulo_box.delete(0, END)
    experiencia_box.delete(0, END)
    salario_box.delete(0, END)


    # Grab record number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    #temp_label.config(text=values[0])

    # output to entry boxes
    name_box.insert(0, values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[4])
    numero_ss_box.insert(0, values[5])
    titulo_box.insert(0, values[6])
    experiencia_box.insert(0, values[7])
    salario_box.insert(0, values[8])

my_tree.bind("<ButtonRelease-1>", clicker)

# Close the database connection

window.mainloop()