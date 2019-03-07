#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  rig_control.py
#  
#  Copyright 2019 Ulf Nordstrom <ulf@nord500.se>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from tkinter import *
from tkinter import filedialog
import os
import sys
import json
#import hardware
from cat_manager import CatManager
from subprocess import Popen, PIPE

root = 0
front_panel = 0
class FrontPanel:
    def __init__(self, root):
        self.root = root
        self.config = self.get_config()
        self.module = StringVar()
        self.frequency = IntVar()
        self.tuning_step = IntVar()
        self.agent_path = self.config['agent_path']
        self.module.set(self.config['module'])
        self.frequency.set(self.config['frequency'])
        self.tuning_step.set(self.config['tuning_step'])
        self.radio_modes = ["no radio defined"]
        self.tx_power = ["no radio defined"]
        
        
    def __del__(self):
        print("Destructor called ...")
#        del(self.a)

	
    def step(self, x, y,  direction):
 


        step = self.tuning_step.get()
        f = self.frequency.get()

        if direction == 'up':
            f += step
            if f < 438000000:
                self.frequency.set(f)
        if direction == 'down':
            f -= step
            if f > 432000000:
                self.frequency.set(f)	
		
		
#    if x < matchFrame.winfo_width():
#        # Match
#        if direction == 'up':
#            pass
#        else:
#            pass
#        Matchgauge.set(int(match_value))

        
            







    
    def get_config(self):
        try:
            fd = open("radio.json")
            config = json.load(fd)
            fd.close()
        except:
            home = os.environ["HOME"]
            fd = open("radio.json", 'w')
            config = {'module':'', 'frequency':433920000, 'tuning_step':1000, 'agent_path':home}
            json.dump(config, fd)
            fd.close()
        return(config)
          
    
    def menu(self, parent):
        top = Menu(parent)
        parent.config(menu=top)
    

        file =Menu(top)
        file.add_command(label='Exit', command=self.shutdown, underline=0)
        top.add_cascade(label='File', menu=file, underline=0)
        
        module=Menu(top,tearoff=False)
        module.add_command(label='Serial', command = self.module_cc110x, underline=0)
        module.add_command(label='Local',command=self.module_rfm69, underline=0)
        top.add_cascade(label='Connect agent', menu=module, underline=0)
        
        debug = Menu(top,tearoff=False)
        debug.add_command(label='Register Inspect', command = self.reg_inspect, underline=0)
        top.add_cascade(label='Debug', menu=debug, underline=0)


    def shutdown(self):
        self.config['module'] = self.module.get()
        self.config['frequency'] = self.frequency.get()
        self.config['tuning_step'] = self.tuning_step.get()
    
        with open('radio.json', 'w') as outfile:  
            json.dump(self.config, outfile)
            
        try:
            del(self.a)
        except:
            pass
            
        sys.exit()
    
    
    def module_cc110x(self):
        root.title("Radio module configuration utility, CC110x")
        pass
    
    def module_rfm69(self):

	
        agent_default = self.config['agent_path']
        agent = filedialog.askopenfile(initialdir = agent_default,title='Select a file')
        if agent:
            self.a = CatManager(agent.name)
            model = self.a.radio_model()
            self.radio_modes = self.a.modemConfig()
            self.tx_power = eval(self.a.txPower())
            self.config['agent_path'] = os.path.dirname(agent.name)
            root.title(model + " - Radio module configuration manager")
            config = self.config_frame(root)
            config.grid(row=1,column=0)
            
    def reg_inspect(self):
        self.reg_inspect_window = Toplevel()
        self.reg_inspect_window.title("Register inspect")
        
        regLabel = Label(self.reg_inspect_window, text="Register")
        regLabel.grid(row=0, column=0, sticky='w')
        self.regAddress = Entry(self.reg_inspect_window, width=6)
        self.regAddress.grid(row=0, column=1)

        

        regLabel = Label(self.reg_inspect_window, text="Value")
        regLabel.grid(row=0, column=2, sticky='W')
        self.regValue = Entry(self.reg_inspect_window, width=6)
        self.regValue.grid(row=0, column=3)  
        
        getButton = Button(self.reg_inspect_window, text = "Get", command = self.get_reg)
        getButton.grid(row=0,column=4)
        
        setButton = Button(self.reg_inspect_window, text = "Set", command = self.set_reg)
        setButton.grid(row=0,column=5)
           
    def attach():
        pass
        
    def get_reg(self):
        regAddress= self.regAddress.get()
        print(regAddress)
        regValue = self.a.trcvRegisters(regAddress)
        self.regValue.insert(0, regValue)
        
	
    def set_reg(self):
        regAddress= self.regAddress.get()
        regValue= self.regValue.get()
        if regValue == '':
            print("Enter value")
        else:
            self.a.trcvRegisters(regAddress, regValue)
        		 
    def display_frame(self,parent):
        frame = Frame(parent, background='skyblue')
        freq = Label(frame, textvariable=self.frequency, pady=5, background="skyblue")
        freq.config(font=("Courier", 44))
        freq.grid(row=0, column=0)
        s=PhotoImage("s-l1600.jpg")
        #s.grid(row=0, column=0)
        step = self.tuning_step_frame(frame)
        step.grid(row=1,column=0)
        return frame
    
    
    def tuning_step_frame(self,parent):
        frame = Frame(parent, background='skyblue')
    
        M1 = Radiobutton(frame, text = "1MHz", value = 1000000, variable=self.tuning_step, background='skyblue')
        M1.grid(row=0, column=0)
    
        k100 = Radiobutton(frame, text = "100kHz", value = 100000, variable=self.tuning_step, background='skyblue')
        k100.grid(row=0, column=1)
    
        k25 = Radiobutton(frame, text = "25kHz", value = 25000, variable=self.tuning_step, background='skyblue')
        k25.grid(row=0, column=2)   
    
        tenk = Radiobutton(frame, text = "10kHz", value = 10000, variable=self.tuning_step, background='skyblue')
        tenk.grid(row=0, column=3) 
    
    
    
        onek = Radiobutton(frame, text = "1kHz", value = 1000, variable=self.tuning_step, background='skyblue')
        onek.grid(row=0, column=4)   
    
    
        hundred = Radiobutton(frame, text = "100Hz", value = 100, variable=self.tuning_step, background='skyblue')
        hundred.grid(row=0, column=5)  

    
        
        ten = Radiobutton(frame, text = "10Hz", value = 10, variable=self.tuning_step, background='skyblue')
        ten.grid(row=0, column=6)

      
        return(frame)
    
    def config_frame(self, parent):
        radio_modes = self.radio_modes
        radioMode = StringVar()
        TxPower =StringVar()
        tx_power = self.tx_power
        frame = Frame(parent)
        mode = Label(frame, text="mode")
        mode.grid(row=0, column=0, sticky="W")       
        mode = OptionMenu(frame, radioMode, *radio_modes)
        mode.grid(row=0, column=1, sticky="W")
        powerLabel = Label(frame, text="TX Power")
        powerLabel.grid(row=1, column=0, sticky="W")
        powerScale = OptionMenu(frame, TxPower, *tx_power)
        powerScale.grid(row=1,column=1, sticky="W")        

        return frame


def mouse_wheel(event):
        global root
        global front_panel
        

        x = root.winfo_pointerx()- root.winfo_rootx()
        y = root.winfo_pointery()- root.winfo_rooty()
        #print x


        # respond to Linux or Windows wheel event
        if event.num == 5 or event.delta == -120:
            front_panel.step(x,y,'down')
        if event.num == 4 or event.delta == 120:
            front_panel.step(x,y,'up')


def main(args):
    global root
    global front_panel
    
    root        = Tk()
    front_panel = FrontPanel(root)
    front_panel.menu(root)
    display     = front_panel.display_frame(root)
    display.grid(row=0,column=0)

    config = front_panel.config_frame(root)
    config.grid(row=1,column=0)
    
    

    root.title("Radio Module Configuration manager - no radio module attached")




    







# with Windows OS
#root.bind("<MouseWheel>", mouse_wheel)
# with Linux OS
    root.bind("<Button-4>", mouse_wheel)
    root.bind("<Button-5>", mouse_wheel)

        
    root.mainloop()
	
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
