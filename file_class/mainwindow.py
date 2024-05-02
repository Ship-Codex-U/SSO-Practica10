from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6.QtCore import Signal, Slot, QObject
from file_class.window01_ui import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt

from file_class.cola import Cola

import threading
import time
import random
import copy


# Crear variables globales para los threads y las frecuencias
entry_frequency = random.choice((0.5, 1, 2))  # Frecuencia inicial de entrada
exit_frequency = random.choice((0.5, 1, 2))  # Frecuencia inicial de salida
entry_thread = None  # Thread de entrada
exit_thread = None  # Thread de salida
stop_threads = False  # Variable para detener los threads

# Lock para sincronizar el acceso a las funciones de entrada y salida
queue_lock = threading.Lock()



class Worker(QObject):
    # Define una señal que puedes emitir desde el hilo secundario
    update_gui = Signal()

    def run(self):
        # ...
        # Cuando quieras actualizar la GUI, emite la señal
        self.update_gui.emit()
        # ...


class MainWindow(QMainWindow):
    update_gui = Signal(list) 
    
    def __init__(self) -> None:
        super().__init__()
        
        self.update_gui.connect(self.showGrafic)
        
        #Cola
        self.estacionamiento = Cola(12)
        #Colores
        self.colores = ['indigo', 'rebeccapurple', 'darkviolet', 'darkorchid', 'mediumpurple', 'fuchsia', 'violet', 'plum', 'thistle', 'lightpink', 'pink', 'lavenderblush']
        self.useColors = ['indigo', 'rebeccapurple', 'darkviolet', 'darkorchid', 'mediumpurple', 'fuchsia', 'violet', 'plum', 'thistle', 'lightpink', 'pink', 'lavenderblush']
        
        # Configurar la interfaz de usuario
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #layout
        self.layout = QVBoxLayout(self.ui.w_queue)
        self.fig, self.ax = plt.subplots()
        
        self.ui.b_openParkingLot.clicked.connect(self.action_openParkingLot)
        self.ui.b_closeParkingLot.clicked.connect(self.action_closeParkingLot)
        self.ui.b_updateEntry.clicked.connect(self.action_updateEntry)
        self.ui.b_updateExit.clicked.connect(self.action_updateExit)
        
        
        
    def showGrafic(self, colors):
        # Lista de valores según el tamaño del arreglo de colores
        valores = [20] * len(colors)  # Inicializamos con valores de altura
        print(colors)
        
        if hasattr(self, "canvas"):
            # Limpia el Axes antes de redibujar
            self.ax.clear()
            
            # Actualiza las barras con los nuevos valores y colores
            self.bars = self.ax.bar(range(len(valores)), valores, color=colors)
            
            # Refresca la gráfica
            self.canvas.draw_idle()
        else:
            # Si no existen barras, las creamos
            self.bars = self.ax.bar(range(len(valores)), valores, color=colors)
            self.canvas = FigureCanvas(self.fig)
            self.layout.addWidget(self.canvas)
    
    def getNextColor(self):
        if len(self.useColors) == 0:
            self.useColors = copy.deepcopy(self.colores)
            
        return self.useColors.pop(0)      
    
    def action_enqueueCar(self):
        if(self.estacionamiento.lleno()):
            print("Estacionamiento lleno")
        else:    
            self.estacionamiento.encolar(self.getNextColor())
    
    def action_dequeueCar(self):
        if(self.estacionamiento.vacio()):
            print("Estacionamiento Vacio")
        else:    
            color = self.estacionamiento.desencolar()
    
    # Función que simula la entrada de autos al estacionamiento
    def entry_thread_function(self):
        global stop_threads
        while not stop_threads:
            time.sleep(entry_frequency)
            with queue_lock:
                if not self.estacionamiento.lleno():  # Solo añadir autos si el estacionamiento no está lleno
                    self.action_enqueueCar()
                    self.update_gui.emit(self.estacionamiento.obtenerDatos())
        
    # Función que simula la salida de autos del estacionamiento
    def exit_thread_function(self):
        global stop_threads
        while not stop_threads:
            time.sleep(exit_frequency)
            with queue_lock:
                if not self.estacionamiento.vacio():  # Solo retirar autos si el estacionamiento no está vacío
                    self.action_dequeueCar()
                    self.update_gui.emit(self.estacionamiento.obtenerDatos())
    
    
    def convertir_texto(self, texto):
        try:
            # Intenta convertir a entero
            numero_entero = int(texto)
            return numero_entero
        except ValueError:
            # Si no se puede convertir a entero, intenta convertir a float
            try:
                numero_decimal = float(texto)
                return numero_decimal
            except ValueError:
                print("El texto no es un número válido.")
            
            
    @Slot( )
    def action_openParkingLot(self):
        global entry_thread, exit_thread, stop_threads, entry_frequency, exit_frequency
        stop_threads = False  # Asegúrate de que los threads no se detengan inmediatamente
        
        entry_frequency = random.choice((0.5, 1, 2))  # Frecuencia inicial de entrada
        exit_frequency = random.choice((0.5, 1, 2))  # Frecuencia inicial de salida
        
        # Inicia los threads para la entrada y salida de autos
        entry_thread = threading.Thread(target=self.entry_thread_function)
        exit_thread = threading.Thread(target=self.exit_thread_function)
        
        self.ui.l_showEntryFrecuency.setText(str(entry_frequency) + ' segundos')
        self.ui.l_showExitFrecuency.setText(str(exit_frequency) + ' segundos')
        
        entry_thread.start()
        exit_thread.start()
    
    @Slot( )
    def action_closeParkingLot(self):
        global stop_threads
        
        stop_threads = True
        
        self.ui.l_showEntryFrecuency.setText('xxxx segundos')
        self.ui.l_showExitFrecuency.setText('xxxx segundos')
        
        # Detener los threads de entrada y salida
        if entry_thread:
            entry_thread.join()
        if exit_thread:
            exit_thread.join()
        
    
    @Slot( )
    def action_updateEntry(self):
        global entry_frequency
        
        new_frequency = self.convertir_texto(self.ui.i_inputEntryFrecuency.text())
        self.ui.i_inputEntryFrecuency.setText('')
        self.ui.l_showEntryFrecuency.setText(str(new_frequency) + ' segundos')
        
        entry_frequency = new_frequency
        
            
    @Slot( )
    def action_updateExit(self):
        global exit_frequency
        
        new_frequency = self.convertir_texto(self.ui.i_inputExitFrecuency.text())
        self.ui.i_inputEntryFrecuency.setText('')
        self.ui.l_showExitFrecuency.setText(str(new_frequency) + ' segundos')
        
        exit_frequency = new_frequency
        
        
    
        
         

        
