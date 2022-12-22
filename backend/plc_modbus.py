from socket import timeout
import time

from pyModbusTCP.client import ModbusClient

# init modbus client



class plc_modbus():

    def __init__(self,ip):
        self.ip=str(ip)

        self.connection()
    
    def connection(self):

        try:
            self.c = ModbusClient(host=self.ip, port=502, auto_open=True, debug=True,timeout=0.001)
            # print(self.c.is_open)
            try:
                self.c._open()
                return True
            except:
                return False
        except:
            return False
    
    def disconnect(self):
        
        self.c.disconnect()


    def get_value(self,register):


        try:
            self.c.read_discrete_inputs(register,1)
            return True
        except:
            return False
    
    def set_value(self,register,value):

        try:
            self.c.write_single_coil(register, value)
            return True
        except:
            return False



if __name__=='__main__':
    # read()
    # write()
    c=plc_modbus('192.168.1.5')
    bit =False
    while True:
        # bit = not bit
        # for i in range(2030,2050):
        #     c.set_value(i,bit)
            
        #     time.sleep(0.1)
        #     print(i)
        c.connection()