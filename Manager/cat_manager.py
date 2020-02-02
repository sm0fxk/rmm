#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cat_client.py
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
from subprocess import Popen, PIPE
import socket
#import hardware

class CatManager:
    def __init__(self, tnc_interface, agent):
        self.tnc_interface = tnc_interface
        if tnc_interface == "network":
            ip, port = agent
            #host = socket.gethostname()  # as both code is running on same pc
            #port = 5000  # socket server port number

            self.client_socket = socket.socket()  # instantiate
            try:
                self.client_socket.connect((ip, port))  # connect to the server
                self.conn_status = True
            except:
                self.conn_status = False
            

        else:
            print(agent)		
            self.process=Popen([agent],stdin=PIPE,stdout=PIPE)
        
    def __del__(self):
        if self.tnc_interface == 'network':
            self.client_socket.close()  # close the connection
        else:
            self.process.kill()

    def tnc_connected(self):
        return self.conn_status

        
    def compose_cat_command(self, cmd, parameters):
        for parameter in parameters:
            cmd = cmd + str(parameter) + ','
        print (cmd)
        return cmd.rstrip(',')
        
        
    def cat_transaction(self, command, parameters = []):
        cmd = self.compose_cat_command(command, parameters)
        if self.tnc_interface == 'network':
            self.client_socket.send(cmd.encode())  # send message
            data = self.client_socket.recv(1024).decode('utf-8')  # receive response
#            print('Received from server: ' + data)  # show in terminal
            return(data.strip("\n"))
        else:
#-------------------------------------------------
            self.process.stdin.write(str.encode(cmd + '\n'))
            self.process.stdin.flush()
            reply = self.process.stdout.readline()
#-------------------------------------------------
        print(reply)
        reply_string = reply.decode('utf-8')
        return(reply_string.strip("\n"))
        
    def radio_model(self):
        command = 'ID'
        chip = self.cat_transaction(command)
        return(chip)
        
        
    def trcvRegisters(self, address = None, value = None):
        command = "RE"
        if address == None and value == None:
            parameters = []
        elif value == None:
            parameters = [address]
        else:
            parameters = [address, value]
            print(parameters)
        reply = self.cat_transaction(command, parameters)

        return(reply)
      
 
   
    def txPower(self, power = []):
        return(self.cat_transaction("PC", power))
        
    def frequency(self,frequency_Hz = []):
        return(self.cat_transaction("FA", frequency_Hz))
              
    def modemConfig(self, index= None):
        if index == None:    # get
            config = eval(self.cat_transaction("MD"))
            return(config)
        else:                 #set
            self.cat_transaction('MD', index)
        
    def setSyncWords( syncWords,  length):
        pass
               
    def rxBandwidth(self, bw = []):
        return(self.cat_transaction("SH", bw))


    def bitrate(self, rate = []):
        return(self.cat_transaction("DR", rate))

    def deviation(self, fdev = []):
        return(self.cat_transaction("FD", fdev))

    def apply_config(self, config = []):
        return(self.cat_transaction("AP", config))

