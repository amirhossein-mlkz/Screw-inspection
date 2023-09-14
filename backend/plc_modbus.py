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
            print('Erro plc connection')
            return False
    
    def disconnect(self):
        
        self.c.disconnect()


    def get_value(self,register):


        try:
            return self.c.read_discrete_inputs(register,1)[0]
            return True
        except:
            print('Error in get path value')
            return False
    
    def set_value(self,register,value):

        try:
            self.c.write_single_coil(register, value)
            return True
        except:
            print('Error in set value')
            return False



if __name__=='__main__':
    # read()r
    # write()
    #c=plc_modbus('192.168.1.5')
    c=plc_modbus('192.168.200.15')
    # c.set_value(2048, False)
    # print('aaaa',c.get_value(2048))
    # for i in range(1000):
    #     c.set_value(2048,False)
    #     print(c.get_value(2048))
    bit =False
    # # for i in range(3000):
    # #     c.set_value(i,True)
    # while True:
        # bit = not bit
    # for i in range(1280,1283):
    #     c.set_value(i,bit)
        
        # time.sleep(1)
        # print(i)
    #     c.connection()

    # c.set_value(1282,True)
    c.get_value(1282)