import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, askyesno

from zona_fit_gui.cliente_dao import ClienteDAO
from zona_fit_gui.cliente import Cliente


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.config_ventana()
        self.config_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self._inicializar_tabla_y_scrollbar()
        self._cargar_datos_en_tabla()
        self.mostrar_botones()

    def config_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit')
        self.configure(background='#1d2d44')
        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')  # indicamos que vamos a preparar los estilos para el modo oscuro
        self.estilos.configure(self, background='#1d2d44',
                               foreground='white',
                               fieldbackground='black')

    def config_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 15),
                             background='#1d2d44',
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, padx=30)

    def mostrar_formulario(self):
        # frame para el formulario
        self.frame_formulario = ttk.Frame(self)
        # nombre--
        # etiqueta
        et_nombre = ttk.Label(self.frame_formulario, text='Nombre')
        et_nombre.grid(row=0, column=0, padx=5, pady=30, sticky=tk.W)
        # entrada  texto
        self.entr_nombre = ttk.Entry(self.frame_formulario, width=30)
        self.entr_nombre.grid(row=0, column=1, padx=5, pady=30, sticky=tk.EW)
        # apellido--
        # etiqueta
        et_apellido = ttk.Label(self.frame_formulario, text='Apellido')
        et_apellido.grid(row=1, column=0, padx=5, pady=30, sticky=tk.W)
        # entrada texto
        self.entr_apellido = ttk.Entry(self.frame_formulario, width=30)
        self.entr_apellido.grid(row=1, column=1, padx=5, pady=30, sticky=tk.EW)
        # membresia--
        # etiqueta
        et_membresia = ttk.Label(self.frame_formulario, text='Membresia')
        et_membresia.grid(row=2, column=0, padx=5, pady=30, sticky=tk.W)
        # entrada texto
        self.entr_membresia = ttk.Entry(self.frame_formulario, width=30)
        self.entr_membresia.grid(row=2, column=1, padx=5, pady=30, sticky=tk.EW)

        # mostramos el frame
        self.frame_formulario.grid(row=1, column=0)

    def _inicializar_tabla_y_scrollbar(self):
        # frame para el componente tabla
        self.frame_tabla = ttk.Frame(self)

        # estilos para la tabla
        self.estilos.configure('Treeview',
                               background='black',
                               foreground='white',
                               filedbackground='black',
                               rowheight=20)

        # definimos los nombres de las columnas
        columnas = ('Id', 'Nombre', 'Apellido', 'Membresia')

        # creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        # agregamos los cabeceros
        self.tabla.heading('Id', text='ID', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='NOMBRE', anchor=tk.E)
        self.tabla.heading('Apellido', text='APELLIDO', anchor=tk.E)
        self.tabla.heading('Membresia', text='MEMBRESIA', anchor=tk.E)

        # configuramos las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.E, width=100)
        self.tabla.column('Apellido', anchor=tk.E, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=80)

        # creacion del scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Asociar el evento select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        # publicamos la tabla
        self.tabla.grid(row=0, column=0)

        # mostramos el frame de la tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def _cargar_datos_en_tabla(self):
        # eliminar todos los datos existentes en la tabla antes de cargar los nuevos
        for item in self.tabla.get_children():  # obtiene los id de las filas
            self.tabla.delete(item)  # borra las filas por id

        # cargar los datos que hay en la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id,
                                      cliente.nombre,
                                      cliente.apellido,
                                      cliente.membresia))

    def mostrar_botones(self):
        # frame para los botones
        self.frame_botones = ttk.Frame(self)
        # guardar
        self.bot_guardar = ttk.Button(self.frame_botones, text='Guardar', command=self.validar_cliente)
        self.bot_guardar.grid(row=0, column=0, padx=15)
        # eliminar
        self.bot_eliminar = ttk.Button(self.frame_botones, text='Eliminar', command=self.eliminar_cliente,
                                       state=tk.DISABLED)
        self.bot_eliminar.grid(row=0, column=1, padx=15)
        # limpiar
        self.bot_limpiar = ttk.Button(self.frame_botones, text='Limpiar', command=self.limpiar_datos, state=tk.DISABLED)
        self.bot_limpiar.grid(row=0, column=2, padx=15)

        # aplicar estilo a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # mostramos el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=3)

    def validar_cliente(self):
        membresia_val = self.entr_membresia.get()  # guardamos el valor ingresado por membresia

        if self.entr_nombre.get() and self.entr_apellido.get() and self.entr_membresia.get():
            if self.validar_membresia(membresia_val):
                self.guardar_cliente()
            else:
                showerror(title='Atencion',
                          message='El valor de membresia No es numerico')
                self.entr_membresia.delete(0, tk.END)
                self.entr_membresia.focus_set()
        else:
            showerror(title='Atencion',
                      message='Debe llenar el formulario')
            self.entr_nombre.focus_set()

    def validar_membresia(self, membresia_str):
        try:
            int(membresia_str)
            return True
        except:
            return False

    def guardar_cliente(self):
        nombre = self.entr_nombre.get()
        apellido = self.entr_apellido.get()
        membresia = self.entr_membresia.get()
        if self.id_cliente is None:  # si no hay un item seleccionado se crea un nuevo cliente
            nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(nuevo_cliente)
            showinfo('Info', f'Cliente registrado con exito! {nombre}, {apellido}, {membresia}')
        else:  # comparamos si se hizo un cambio respecto a valores originales para actializar
            if (nombre == self._nombre_original and
                    apellido == self._apellido_original and
                    membresia == self._membresia_original):
                showinfo(title='Info', message='No se detectaron cambios en el cliente. Actualizacion cancelada')
                self.limpiar_datos()
                return # salimos, no hay cambios

            cliente = Cliente(id=self.id_cliente, nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.actualizar(cliente)
            showinfo('Info', 'Cliente actualizado!')
        self.recargar_datos()

    def cargar_cliente(self, event):
        if not self.tabla.selection():
            return
        id_linea_selecc = self.tabla.selection()[0]  # elegimos la linea, nos da un id
        obj_selecc = self.tabla.item(id_linea_selecc)  # usamos el id para conseguir el objeto de esa linea
        self.id_cliente, nombre, apellido, membresia = obj_selecc[
            'values']  # desempaquetamos la tupla dentro de la llave 'values' en el objeto
        # limpiamos el formulario antes de cargar los valores seleccionados
        self.limpiar_formulario()
        # insertamos los valores en el formulario
        self.entr_nombre.insert(0, nombre)
        self.entr_apellido.insert(0, apellido)
        self.entr_membresia.insert(0, membresia)
        # guardamos los valores originales para detectar cambios
        self._nombre_original = str(nombre)
        self._apellido_original = str(apellido)
        self._membresia_original = str(membresia)  # membresia a string igual que en get()

        # habilitamos los botones eliminar y limpiar al cargar el cliente
        # hassatr chequea que se hayan creado los botones
        if hasattr(self, 'bot_eliminar'):  # chequear 1 solo es suficiente
            self.bot_eliminar.config(state=tk.NORMAL)  # habilitados
            self.bot_limpiar.config(state=tk.NORMAL)
            self.bot_guardar.config(text='Actualizar')

    def recargar_datos(self):
        # volver a cargar los datos de la tabla
        self._cargar_datos_en_tabla()
        # limpiar los datos
        self.limpiar_datos()

    def eliminar_cliente(self):
        # revisamos si se selecciono un cliente para eliminar
        if self.id_cliente is None:
            showerror(title='Atencion', message='No ha seleccionado un registro')
        else:  # pedimos confirmacion
            confirmar_elim = askyesno(title='Confirmar Eliminacion',
                                      message=f'Esta seguro de eliminar el cliente {self.entr_nombre.get()} {self.entr_apellido.get()}?')
            if confirmar_elim:
                elim_cliente = Cliente(id=self.id_cliente)
                ClienteDAO.eliminar(elim_cliente)
                showinfo(title='Info',
                         message=f'Cliente eliminado! {self.entr_nombre.get()} {self.entr_apellido.get()}')
                self.recargar_datos()
            else:
                showinfo(title='Cancelado',
                         message='Eliminacion cancelada')

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None
        # deshabilitamos los botones eliminar y limpiar
        if hasattr(self, 'bot_eliminar'):
            self.bot_limpiar.config(state=tk.DISABLED)
            self.bot_eliminar.config(state=tk.DISABLED)
            # renombramos el boton de actualizar a guardar
            self.bot_guardar.config(text='Guardar')
        # dejamos la tabla sin elemento seleccionado
        for item in self.tabla.selection():
            self.tabla.selection_remove(item)


    def limpiar_formulario(self):
        self.entr_nombre.delete(0, tk.END)
        self.entr_apellido.delete(0, tk.END)
        self.entr_membresia.delete(0, tk.END)
        self.entr_nombre.focus_set()


if __name__ == '__main__':
    app1 = App()
    app1.mainloop()
