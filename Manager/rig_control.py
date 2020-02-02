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
#        self.config = self.get_config()
        self.module = StringVar()
        self.frequency = IntVar()
        self.tuning_step = IntVar()
        self.agent_path = self.get_config('agent_path')
#        self.module.set(self.config['module'])
        self.frequency.set(self.get_config('frequency'))
        self.tuning_step.set(self.get_config('tuning_step'))
        self.radio_modes = ["no radio defined"]
        self.tx_power = ["no radio defined"]
        self.tnc_model= StringVar()
        
        
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
        self.a.frequency([f])
		
#    if x < matchFrame.winfo_width():
#        # Match
#        if direction == 'up':
#            pass
#        else:
#            pass
#        Matchgauge.set(int(match_value))

        
            

    def write_config(self, name, value):
        config = get_config()
        config[name] = value

        with open('radio.json', 'w') as outfile:  
            json.dump(config, outfile)
        outfile.close()



    
    def get_config(self, key):
        try:
            fd = open("radio.json")
            config = json.load(fd)
            fd.close()
        except:
            home = os.environ["HOME"]
            fd = open("radio.json", 'w')
            config = {'module':'', 'frequency':433920000, 'tuning_step':1000,
                      'agent_path':home, 'ip_addr' : "localhost", 'tcp_port' : 5000}
            json.dump(config, fd)
            fd.close()
        return(config[key])
          
    
    def menu(self, parent):
        top = Menu(parent)
        parent.config(menu=top)
    

        file =Menu(top)
        file.add_command(label='Load config', command = self.load_config , underline=0)
        file.add_command(label='Exit', command=self.shutdown, underline=0)
        top.add_cascade(label='File', menu=file, underline=0)
        
        module=Menu(top,tearoff=False)
        module.add_command(label='Network', command = self.conn_network, underline=0)
        module.add_command(label='Local',command=self.conn_local, underline=0)
        top.add_cascade(label='Connect agent', menu=module, underline=0)
        
        debug = Menu(top,tearoff=False)
        debug.add_command(label='Register Inspect', command = self.reg_inspect, underline=0)
        top.add_cascade(label='Debug', menu=debug, underline=0)


    def shutdown(self):
#        self.config['module'] = self.module.get()
#        self.config['frequency'] = self.frequency.get()
#        self.config['tuning_step'] = self.tuning_step.get()
    
#        with open('radio.json', 'w') as outfile:  
#            json.dump(self.config, outfile)
            
        try:
            del(self.a)
        except:
            pass
            
        sys.exit()

    def connect_agent(self):

        port = self.get_config('tcp_port')
        connectWindow = Toplevel()
        connectWindow.title("Connect agent")

        ipLabel = Label(connectWindow, text='IP')
        ipLabel.grid(row=0, column=0)
        self.ipEntry = Entry(connectWindow)
        self.ipEntry.grid(row=0, column=1)

        portLabel = Label(connectWindow, text='Port')
        portLabel.grid(row=1, column=0)
        self.portEntry = Entry(connectWindow)
        self.portEntry.grid(row=1, column=1)
        self.portEntry.insert(0, port)
        connectButton = Button(connectWindow, text = "Connect", command = self.conn_network)
        connectButton.grid(row=2,column=0) 


#        dismissButton = Button(connectWindow, text = "Dissmiss", command = connectWindow.destroy)
#        dismissButton.grid(row=2,column=0)             

    def conn_network(self):
        ip = self.ipEntry.get()
        port = int(self.portEntry.get())
        print(ip)
        print(port)
        self.a = CatManager("network", (ip, port))
#        self.a = CatManager("network", ("manx", 5000))
        if self.a.tnc_connected():
            model = self.a.radio_model()
            print (model)
            self.tnc_model.set(model)
            config = self.config_frame(root)
            config.grid(row=2,column=0, sticky="W")
        else:
            self.tnc_model.set("Connection Failed")

    def conn_local(self):
        agent_default = self.get_config('agent_path')
        agent = filedialog.askopenfile(initialdir = agent_default,title='Select a file')
        if agent:
            self.a = CatManager("local", agent.name)
            model = self.a.radio_model()

            self.radio_modes = self.a.modemConfig()
            self.tx_power = eval(self.a.txPower())
            self.write_config('agent_path', os.path.dirname(agent.name))
            root.title(model + " - Radio module configuration manager")
#            config = self.config_frame(root)
#            config.grid(row=2,column=0, sticky="W")
            
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
        regAddress= int(self.regAddress.get(), 16)
        print(regAddress)
        regValue = self.a.trcvRegisters(regAddress)
        self.regValue.delete(0, END)
        self.regValue.insert(0, regValue)
        
	
    def set_reg(self):
        regAddress= int(self.regAddress.get(),16)
        regValue= int(self.regValue.get(),16)
        if regValue == '':
            print("Enter value")
        else:
            self.a.trcvRegisters(regAddress, regValue)
            
    def save_config(self):
        reply = self.a.trcvRegisters()
        (first_reg, last_reg) = eval(reply)
        reg_addresses = range(first_reg, last_reg)
        registers = [int(self.a.trcvRegisters(reg_address),16) for reg_address in reg_addresses]
        print(registers)
        fd = filedialog.asksaveasfile(mode='w', defaultextension=".json")
 #       fd = open(reg_file, 'w')
        model = self.a.radio_model()
        content = {'model':model, 'configuration_name': 'bla', 'registers':registers}
        json.dump(content, fd)
        fd.close()

      
    def load_config(self):
        fd = filedialog.askopenfile(initialdir = os.environ["HOME"]  + "/repository/rmm"
,title='Select a file', filetypes = [("Modem config files","*.py")])
        print(fd)
        config = eval(fd.read())
        fd.close()
        model = config["model"]
        self.description = config["description"]
        registers = config["registers"]
        reply = self.a.trcvRegisters()
#        print(reply)
        (first_reg, last_reg) = eval(reply)
#        reg_addresses = range(first_reg, last_reg)
        print(model)
        print(self.description)

        reg_address = 0        
        for register in registers:
            reply = self.a.trcvRegisters(reg_address, register)
            reg_address +=1
#            print(reply)
        print(last_reg)
        print(reg_address)
        config = self.config_frame(root)
        config.grid(row=2,column=0, sticky="W")

    def top_frame(self, parent):
        frame = Frame(parent)
        Connect_Button = Button(frame, text="Connect TNC", command=self.connect_agent)
        Connect_Button.grid( row = 0, column = 0, sticky="E")

        tnc_model_label = Label(frame, text="Connected to: ")
        tnc_model_label.grid(row =0, column=1)

        tnc_model = Label(frame, textvariable=self.tnc_model)
        tnc_model.grid(row=0,column=2)

 #       Save_Config_Button = Button(frame, text="Save Config", command=self.save_config)
 #       Save_Config_Button.grid( row = 0, column = 0)
        
 #       Load_Config_Button = Button(frame, text="Load Config", command=self.load_config)
 #       Load_Config_Button.grid( row = 0, column = 1)
        return frame
        
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


    def apply(self):
        datamodul = self.radioMode.get()
        fq = self.frequency.get()
        tx_pwr = self.TxPower.get()
        rx_bw = self.RxBandwidth.get()
        rate = self.bps.get()
        fd  = self.fdev.get()
        self.a.apply_config([datamodul, fq, tx_pwr, rx_bw, rate, fd])


    def config_frame(self, parent):
        radio_modes = self.a.modemConfig()
        tx_power = eval(self.a.txPower())
        rx_bw = eval(self.a.rxBandwidth())
        bpslist = eval(self.a.bitrate())
        fdevlist = eval(self.a.deviation())

        print(radio_modes)
        print(tx_power)
        print(rx_bw)
        print(bpslist)
        print(fdevlist)

        self.radioMode = StringVar()
        self.TxPower = StringVar()
        self.RxBandwidth = StringVar()
        self.fdev = StringVar()
        self.bps = StringVar()

        frame = Frame(parent)
        mode = Label(frame, text="Modulation")
        mode.grid(row=0, column=0, sticky="W")       
        mode = OptionMenu(frame, self.radioMode, *radio_modes)
        mode.grid(row=0, column=1, sticky="W")
        powerLabel = Label(frame, text="TX Power")
        powerLabel.grid(row=0, column=2, sticky="W")
        powerScale = OptionMenu(frame, self.TxPower, *tx_power)
        powerScale.grid(row=0,column=3, sticky="W")

        bpsLabel = Label(frame, text = "Bitrate")
        bpsLabel.grid(row = 1, column = 0, sticky="W")
        bpsMenu= OptionMenu(frame, self.bps, *bpslist)
        bpsMenu.grid(row=1, column=1,sticky="W")




        fdevLabel=  Label(frame, text = "Deviation")
        fdevLabel.grid(row = 1, column = 2, sticky="W")
        fdevMenu = OptionMenu(frame, self.fdev, *fdevlist)
        fdevMenu.grid(row = 1, column = 3, sticky="W")



        bwLabel = Label(frame, text = "RX bandwidth")
        bwLabel.grid(row = 1, column = 4, sticky="W")
        bwMenu = OptionMenu(frame, self.RxBandwidth, *rx_bw)
        bwMenu.grid(row = 1, column = 5, sticky="W")


        applyButton = Button(frame, text ="Apply", command = self.apply)
        applyButton.grid(row= 4, column=0)


        """
        frame = Frame(parent)
        mode_label = Label(frame, text="Modulation:")
        mode_label.grid(row=0, column=0, sticky="W")
        mode_value = Label(frame, text=self.description["modulation"])
        mode_value.grid(row=0, column=1)
        speed_label = Label(frame, text = "Speed:")
        speed_label.grid(row = 1, column=0, sticky="W")
        speed_value = Label(frame, text=self.description["speed"])
        speed_value.grid(row=1, column=1)
        deviation_label = Label(frame, text = "Deviation:")
        deviation_label.grid(row=2,column=0, sticky="W")
        """
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
    top = front_panel.top_frame(root)
    top.grid(row=0,column=0)
    display     = front_panel.display_frame(root)
    display.grid(row=1,column=0)

#    config = front_panel.config_frame(root)
#    config.grid(row=1,column=0, sticky="W")
    
    

    root.title("Radio Module Configuration manager")




    







# with Windows OS
#root.bind("<MouseWheel>", mouse_wheel)
# with Linux OS
    root.bind("<Button-4>", mouse_wheel)
    root.bind("<Button-5>", mouse_wheel)

        
    root.mainloop()
	
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
