import sys
sys.path.insert(1, 'dsp-modulo') #sirve para llamar un archivo dentro de una carpeta el uno es la cantidad de archivos

from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

#módulo para mostrar gráficas
import matplotlib.pyplot as plt

#crear señal senoidal 
seno = SinSignal(freq=400, amp=0.7, offset=0)
coseno = CosSignal(freq=800, amp=1.1, offset=0)

#crear gráfica en memoria
seno.plot()
coseno.plot()
decorate(xlabel='Tiempo (s)')
decorate(ylabel='Amplitud')



plt.show()