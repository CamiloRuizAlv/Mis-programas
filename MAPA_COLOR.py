import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Circle

def Tv(NDVI):
    return ((51.82062/(1+(0.00059593713/0.01438)*np.log(0.004*NDVI*NDVI)))+119)

def Tu(IU):
    return (5.2746+1.2203*IU)

def DTc(PC):
    pc = PC/100
    if PC>0:
        return (1.42*np.log(1+pc)+pc)
    elif PC<0:
        return (1.42*np.log(1+pc)-pc)
    else:
        return 0

def Ts(tr, v):
    return (12.12 + 0.615*tr - 11.37*(v**0.16)+0.3965*tr*(0.278*v)**(0.16))

def Tr(pc, iu, ndvi):
    return (-0.041563*Tv(ndvi) + 5.229933*Tu(iu) + DTc(pc))

r = 0.5
b = 0.5

fig, ax = plt.subplots()
img = plt.imread("Mapa_Medellin.jpg")
plt.subplots_adjust(bottom=0.13)
C0 = 0
delta_f = 0.01

ax.margins(x=0)
ax.imshow(img)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

circ = Circle((137,342),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ2 = Circle((143,303),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ3 = Circle((129,299),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ4 = Circle((132,289),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ5 = Circle((156,275),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ6 = Circle((172,285),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ7 = Circle((185,264),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ8 = Circle((194,280),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ9 = Circle((231,237),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ10 = Circle((120,260),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ11 = Circle((119,243),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ12 = Circle((158,222),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ13 = Circle((190,229),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ14 = Circle((182,194),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ15 = Circle((114,197),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ16 = Circle((179,166),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ17 = Circle((221,161),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ18 = Circle((264,136),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ19 = Circle((352,98),8,color = (r,0,b,0.8),ec = (0,0,0,0.8))
circ20 = Circle((420,445),20,color = (r,0,b,0.8),ec = (0,0,0,1))
ax.add_patch(circ)
ax.add_patch(circ2)
ax.add_patch(circ3)
ax.add_patch(circ4)
ax.add_patch(circ5)
ax.add_patch(circ6)
ax.add_patch(circ7)
ax.add_patch(circ8)
ax.add_patch(circ9)
ax.add_patch(circ10)
ax.add_patch(circ11)
ax.add_patch(circ12)
ax.add_patch(circ13)
ax.add_patch(circ14)
ax.add_patch(circ15)
ax.add_patch(circ16)
ax.add_patch(circ17)
ax.add_patch(circ18)
ax.add_patch(circ19)
ax.add_patch(circ20)

axcolor = 'lightgoldenrodyellow'
cont = plt.axes([0.35, 0.05, 0.38, 0.03], facecolor=axcolor)
urb = plt.axes([0.35, 0.01, 0.38, 0.03], facecolor=(0,0,0,0.8))
viento = plt.axes([0.35,0.09, 0.38, 0.03], facecolor=axcolor)

scont = Slider(cont, '% Contaminacion', -99.8, 400, valinit=C0, valstep=delta_f)
surb = Slider(urb, '% Vegetacion', 10,100, valinit = 50, valstep=delta_f, color = 'green')
sviento = Slider(viento, 'Velocidad Viento', 0,10, valinit = 5, valstep=0.001)

ax.text(330,450, "Sensación Termica", fontsize=5)

def update(val):

    pc = scont.val
    NDVI = surb.val/100
    IU = 1-NDVI
    V = sviento.val

    T = Tr(pc, IU, NDVI)
    ST = Ts(T, V)

    circ.set_color((T/31,0,1-T/31,1))
    circ2.set_color((T/31,0,1-T/31,1))
    circ3.set_color((T/31,0,1-T/31,1))
    circ4.set_color((T/31,0,1-T/31,1))
    circ5.set_color((T/31,0,1-T/31,1))
    circ6.set_color((T/31,0,1-T/31,1))
    circ7.set_color((T/31,0,1-T/31,1))
    circ8.set_color((T/31,0,1-T/31,1))
    circ9.set_color((T/31,0,1-T/31,1))
    circ10.set_color((T/31,0,1-T/31,1))
    circ11.set_color((T/31,0,1-T/31,1))
    circ12.set_color((T/31,0,1-T/31,1))
    circ13.set_color((T/31,0,1-T/31,1))
    circ14.set_color((T/31,0,1-T/31,1))
    circ15.set_color((T/31,0,1-T/31,1))
    circ16.set_color((T/31,0,1-T/31,1))
    circ17.set_color((T/31,0,1-T/31,1))
    circ18.set_color((T/31,0,1-T/31,1))
    circ19.set_color((T/31,0,1-T/31,1))
    circ20.set_color((ST/31,0,1-ST/31,1))


    circ.set_edgecolor((0,0,0,0.8))
    circ2.set_edgecolor((0,0,0,0.8))
    circ3.set_edgecolor((0,0,0,0.8))
    circ4.set_edgecolor((0,0,0,0.8))
    circ5.set_edgecolor((0,0,0,0.8))
    circ6.set_edgecolor((0,0,0,0.8))
    circ7.set_edgecolor((0,0,0,0.8))
    circ8.set_edgecolor((0,0,0,0.8))
    circ9.set_edgecolor((0,0,0,0.8))
    circ10.set_edgecolor((0,0,0,0.8))
    circ11.set_edgecolor((0,0,0,0.8))
    circ12.set_edgecolor((0,0,0,0.8))
    circ13.set_edgecolor((0,0,0,0.8))
    circ14.set_edgecolor((0,0,0,0.8))
    circ15.set_edgecolor((0,0,0,0.8))
    circ16.set_edgecolor((0,0,0,0.8))
    circ17.set_edgecolor((0,0,0,0.8))
    circ18.set_edgecolor((0,0,0,0.8))
    circ19.set_edgecolor((0,0,0,0.8))
    circ20.set_edgecolor((0,0,0,0.8))

    fig.canvas.draw_idle()


scont.on_changed(update)
surb.on_changed(update)
sviento.on_changed(update)


resetax = plt.axes([0.8, 0.055, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    scont.reset()
    surb.reset()
    sviento.reset()

button.on_clicked(reset)

plt.show()
