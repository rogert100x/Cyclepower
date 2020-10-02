# Bicycle power calculator

#from tkinter import *

# this to prevent VSC from identifying 100 warning because of the import *
import tkinter as tk 


window=tk.Tk()# create a window object

#create programs below

def click():
    try:        #check for non numeric entries
        g=float(9.81)#gravity
        K1=float('0.0053') #Aero factor
        K2=float(Cd.get()) #Cd factor
        m=float(Rider_mass.get())+float(Bike_mass.get())
        Vr=float(Road_speed.get())/float(3.6)
        Va=(float(Road_speed.get())+float(Headwind.get()))/float(3.6)
        s=float(Gradient.get())/100
    except ValueError: #check input validity
        power_box.delete(0.0,tk.END)
        power_box.insert(tk.END,'Non numeric entered',1)
    else:
        Drag=(g*m*Vr*(K1+s))+(K2*pow(Va,2)*Vr)
        power_box.delete(0.0,tk.END)
        power_box.insert(tk.END,str(round(Drag,1)) + " W " +str(round(Drag/m,0)) + ' w/kg')
        #prepare to create list
        tg=0
        ta=float(Headwind.get())/3.6
        ob.delete(0.0,tk.END)#cleaout window
        for i in range(1,6):
            tg=(i*10)/3.6
            tair=(ta+tg)
            Drag=(g*m*tg*(K1+s))+(K2*pow(tair,2)*tg)
            #ob.insert(tk.END,'At '+str(i*10)+' kph - ' +str(round(Drag,1)) + ' Watts - \n')
            ob.insert(tk.END,'At '+str(i*10)+' kph - ' +str(round(Drag,1)) + ' Watts - ' + str(round(Drag/m,1)) + '-watts/kg \n')



def close_window():
    window.destroy()
    exit()                 
    
#create layouts below
#define a window

    
#window=Tk()
window.geometry("450x550")
window.title('Cycling Power calculator')
window.configure(background='light green')

#Create labels for constants
tk.Label(window,text='\nThis App will calculate the power required to \n cycle at a specified speed, gradient and headwind.\n\n',bg='light green',font='bold').grid(row=1,columnspan=3,sticky=tk.W)
tk.Label(window,text='Assumed constants;',bg='light green', font='bold').grid(row=2,column=0,sticky=tk.W)
tk.Label(window,text='Gravity',bg='light green').grid(row=3,column=0,sticky=tk.W)
tk.Label(window,text='9.81 m/s/s',bg='light green').grid(row=3,column=2,sticky=tk.W)
tk.Label(window,text='Friction constant',bg='light green').grid(row=4,column=0,sticky=tk.W)
tk.Label(window,text='0.0053',bg='light green').grid(row=4,column=2,sticky=tk.W)
tk.Label(window,text='Aero drag coefficient Cd 0.185',bg='light green').grid(row=5,column=0,sticky=tk.W)
#tk.Label (window,text='0.185',bg='light green').grid(row=5,column=2,sticky=tk.W)

#Create tk.Labels and entry boxes +prepopulate
Cd=tk.Entry(window,width=5,bg='light grey',relief='sunken')
Cd.grid(row=5,column=2,sticky=tk.W)
Cd.insert(tk.END,float('0.185'))#prepopulate

tk.Label (window,text='Bike mass in Kg ',bg='light green').grid(row=6,column=0,sticky=tk.W)
Bike_mass=tk.Entry(window,width=5,bg='light grey',relief='sunken')
Bike_mass.grid(row=6,column=2,sticky=tk.W)
Bike_mass.insert(tk.END,float(10))#prepopulate

tk.Label (window,text='Rider mass in Kg ',bg='light green').grid(row=7,column=0,sticky=tk.W)
Rider_mass=tk.Entry(window,width=5,bg='light grey',relief='sunken')
Rider_mass.grid(row=7,column=2,sticky=tk.W)
Rider_mass.insert(tk.END,float(85))

tk.Label (window,text='Gradient %age ',bg='light green').grid(row=8,column=0,sticky=tk.W)
Gradient=tk.Entry(window,width=5,bg='light grey',relief='sunken')
Gradient.grid(row=8,column=2,sticky=tk.W)
Gradient.insert(tk.END,float(0))#prepopulate

tk.Label (window,text='Road speed Kph',bg='light green').grid(row=9,column=0,sticky=tk.W)
Road_speed=tk.Entry(window,width=5,bg='light grey',relief='sunken')
Road_speed.grid(row=9,column=2,sticky=tk.W)
Road_speed.insert(tk.END,float(25))#prepopulate

tk.Label (window,text='Headwind Kph',bg='light green').grid(row=10,column=0,sticky=tk.W)
Headwind=tk.Entry(window,width=5,bg='light grey',relief='sunken')
Headwind.grid(row=10,column=2,sticky=tk.W)
Headwind.insert(tk.END,float(0))#prepopulate

#result tk.Label and output box
tk.Label(window,text='\nPower required is :-',bg='light green', font ='bold').grid(row=15,column=0,sticky=tk.W)
power_box=tk.Text(window,width=20,height=1,wrap=tk.WORD,background="white")
power_box.grid(row=17,columnspan=2,sticky=tk.W)

#create a submit button
tk.Button(window, text="Submit",bg="grey",  width=6, command=click).grid(row=17,column=2,sticky=tk.E)

#create a quit button
tk.Button(window, text="Exit", bg="light blue", width=6, command=close_window).grid(row=20,column=2,sticky=tk.E)

#create a large display window
ob=tk.Text(window,width=40,height=5,wrap=tk.WORD,background="white",relief='sunken')
ob.grid(row=22,column=0,sticky=tk.W)



