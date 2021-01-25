################################################################
###           Generateur de courbes paramétrées              ###
################################################################

# Ce programme ouvre une fenetre (figure) contenant un espace graphique, les champs pour les expressions de X et Y, et les champs pour définir l'intervale de la fonction t (t min, t max, et delta t)


# Importation des modules
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox,Button
from matplotlib.animation import *

# Paramètres de la fenetre de base
fig, ax = plt.subplots()
fig.title='titre'
plt.subplots_adjust(bottom=0.4)

t = arange(0.0, 200.0, 0.1)
x=t
s = t ** 2
initial_text = "t"
l, = plt.plot(x, s, lw=0.5)
la, =plt.plot([],[],'gx',markersize=30)
plt.axis('equal')
plt.grid()
fig_mng=plt.get_current_fig_manager()
#fig_mng.full_screen_toggle()
fig_mng.set_window_title("Oi !")
xdata=x
ydata=s
# Definition des fonctions d'animation
n_frames=3000
rapport=len(x)/n_frames

def init():
    la.set_data([],[])
def pt_a(i,x,y):
    la.set_data([x[int(i*rapport)%len(x)]],[y[int(i*rapport)%len(y)]])
    return la,


# Definition des fonctions d'edition
def submit_x(text):
    global xdata
    xdata = eval(text)
    l.set_xdata(xdata)
    ax.set_xlim(min(xdata)*(1-0.05*sign(min(xdata))), max(xdata)*(1+0.05*sign(max(xdata))))
    #ani=FuncAnimation(fig,pt_a,init_func=init,frames=n_frames,interval=10,repeat=True,fargs=(xdata,ydata))
    return(xdata)
def submit_y(text):
    global ydata
    ydata = eval(text)
    l.set_ydata(ydata)
    ax.set_ylim(min(ydata)*(1-0.05*sign(min(ydata))), max(ydata)*(1+0.05*sign(max(ydata))))
    #plt.draw()
    #ani=FuncAnimation(fig,pt_a,init_func=init,frames=n_frames,interval=10,repeat=True,fargs=(xdata,ydata))
    #plt.show()
    return(ydata)
def submit_t(texte):
    global xdata
    global ydata
    global t
    t=eval("arange("+text_box_t_min.text+","+text_box_t_max.text+","+text_box_dt.text+")")
    xdata=eval(text_box_x.text)
    ydata=eval(text_box_y.text)
    l.set_ydata(ydata)
    # ax.set_ylim(min(ydata)*(1-0.05*sign(min(ydata))), max(ydata)*(1+0.05*sign(max(ydata))))
    l.set_xdata(xdata)
    # ax.set_xlim(min(xdata)*(1-0.05*sign(min(xdata))), max(xdata)*(1+0.05*sign(max(xdata))))
    ax.axis('equal')
    ax.axes.relim()
    global rapport
    rapport =len(xdata)/n_frames
    plt.draw()
    #ani=FuncAnimation(fig,pt_a,init_func=init,frames=n_frames,interval=10,repeat=True,fargs=(xdata,ydata))
    #plt.show()

def refresh(event):
    #submit_x(text_box_x.text)
    #submit_y(text_box_y.text)
    submit_t(event)
    plt.draw()
    plt.show()
# Organisation de la fenetre
axbox = plt.axes([0.1, 0.25, 0.35, 0.075])
aybox = plt.axes([0.55, 0.25, 0.35, 0.075])
at_min = plt.axes([0.1, 0.15,0.15,0.075])
at_max = plt.axes([0.4, 0.15,0.15,0.075])
at_dt =  plt.axes([0.7, 0.15,0.15,0.075])
text_box_x = TextBox(axbox, 'X(t) = ', initial="cos(t)*(1-exp(-t/50))")
text_box_y = TextBox(aybox, 'Y(t) = ', initial="sin(t)*(1-exp(-t/50))")
text_box_t_min= TextBox(at_min, 't min = ',initial= str(t[0]))
text_box_t_max= TextBox(at_max, 't max = ',initial= str(t[-1]))
text_box_dt= TextBox(at_dt, 'Delta t = ',initial= str(t[1]-t[0]))

abutton_refresh=plt.axes([0.1,0.05,0.35,0.075])

Refresh=Button(abutton_refresh,label="Rafraichir")
Refresh.on_clicked(refresh)
# Activation de la detection de changements dans les champs
#text_box_x.on_submit(submit_x)
#text_box_y.on_submit(submit_y)

#text_box_t_max.on_submit(submit_t)
#text_box_t_min.on_submit(submit_t)
#text_box_dt.on_submit(submit_t)

# Animation init
#ani=FuncAnimation(fig,pt_a,init_func=init,frames=n_frames,interval=10,repeat=True,fargs=(xdata,ydata))

# Affichage
plt.show()

