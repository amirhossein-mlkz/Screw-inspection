from opcua import Client,ua
#pip install cryptography
class management():
    def __init__(self,ip):

        self.ip=ip
        # self.connection()
    
    def connection(self):

        print('Start Connecting to {}'.format(self.ip))
        self.client = Client(self.ip)
        # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
        try:
            self.client.connect()

            print('Connection Successed')
            return True
        except:
            print('Connection Eror')
            return False
    
    def disconnect(self):
        
        self.client.disconnect()

    def get_value(self,path):

        try:

            var = self.client.get_node(path)
            print(var)
            data_value=var.get_data_value() # get value of node as a DataValue object
            value=var.get_value() # get value of node as a python builtin
            # print('x'*5,value)
            return (value,data_value)
        except:
            print('except')
            return "Path Eror"

    def set_value(self,path,value):
        var = self.client.get_node(path)
        if value.isdigit():
            print('number')
            var = self.client.get_node(path)
            var.set_value(ua.Variant(int(value), ua.VariantType.Int64)) #set node value using explicit data type
            var.set_value(int(value)) # set node value using implicit data type

        else:
            print('value:',value)
            if value=='False':
                value_=False
                print(value_)
            else:
                value_=True
            value = ua.DataValue(ua.Variant(value_,ua.VariantType.Boolean))
            var.set_value(value)