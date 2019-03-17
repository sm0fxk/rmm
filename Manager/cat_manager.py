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
#import hardware

class CatManager:
    def __init__(self, agent):
        print(agent)		
        self.process=Popen([agent],stdin=PIPE,stdout=PIPE)
        
    def __del__(self):
        self.process.kill()
        
    def compose_cat_command(self, cmd, parameters):
        for parameter in parameters:
            cmd = cmd + str(parameter) + ','
#       print cmd
        return cmd.rstrip(',')
        
        
    def cat_transaction(self, command, parameters = []):
        cmd = self.compose_cat_command(command, parameters)
        self.process.stdin.write(str.encode(cmd + '\n'))
        self.process.stdin.flush()
        reply = self.process.stdout.readline()
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
        
    def setFrequency(self,frequency_Hz):
        return(self.cat_transaction("FA", [frequency_Hz]))
              
    def modemConfig(self, index= None):
        if index == None:    # get
            config = eval(self.cat_transaction("MD"))
            return(config)
        else:                 #set
            self.cat_transaction('MD', index)
        
    def setSyncWords( syncWords,  length):
        pass
               
"""       
        
    process.stdin.write("xxx")
    process.stdout.read()
# write 'a line\n' to the process
p=Popen(["./cat_server"],stdin=PIPE,stdout=PIPE)




p=Popen(["./cat_server"],stdin=PIPE,stdout=PIPE)


p.stdout.flush()

# get output from process "Something to print"
one_line_output = p.stdout.readline()

# write 'a line\n' to the process
p.stdin.write(str.encode('QR\n'))
p.stdin.flush()

# get output from process "not time to break"
one_line_output = p.stdout.readline() 

# write "n\n" to that process for if r=='n':
p.stdin.write(str.encode('QH\n'))

# read the last output from the process  "Exiting"
one_line_output = p.stdout.readline()
"""
