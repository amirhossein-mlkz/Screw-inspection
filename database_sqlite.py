import sqlite3


class dataBase:
    def __init__(self,database_name):

        self.data_base_name=database_name
        self.connect()

    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    def connect(self):
            self.conn = sqlite3.connect('{}'.format(self.data_base_name))
            self.cur = self.conn.cursor()

            return self.cur,self.conn     

    #--------------------------------------------------------------------------
    def execute_quary(self,quary,need_data=False, close=False):
    
        # try:
            if need_data:
                self.cur.execute(quary,data)

            else:
                self.cur.execute(quary)

            # connection.commit()
            if close:
                self.cur.close()
            else:
                return self.cur
        # except :
        #     print("Error while Exwcute")
    
    #--------------------------------------------------------------------------
    def search(self,table_name,param_name, value, multi=False,int_type=True):
        # try:

                if int_type:
                    if not multi:
                        sql_select_Query = "SELECT * FROM {} WHERE {} = '{}'".format(table_name,param_name,str(value))
                    else:
                        if len(value) == 1:
                            sql_select_Query = "SELECT * FROM %s WHERE %s=('%s')" % (table_name, param_name, value[0])
                        else:
                            sql_select_Query = "SELECT * FROM %s WHERE %s=%s" % (table_name, param_name, tuple(value))
                    #
                    # print(sql_select_Query)
                else:
                    print('else')
                    sql_select_Query = "SELECT * FROM {} WHERE {} = {}".format(table_name,param_name,"'"+str(value)+"'")


                cursor=self.execute_quary(sql_select_Query)

                records = cursor.fetchall()
                #print("Total number of rows in table: ", cursor.rowcount)
                #print(len(records),records)
                #----------------------------
                
                field_names = [col[0] for col in cursor.description]
                res = []
                for record in records:
                    record_dict = {}
                    for i in range( len(field_names) ):
                        record_dict[ field_names[i] ] = record[i]
                    res.append( record_dict )
                    
              
                return res

                
    def add_record(self,data,table_name,parametrs,len_parameters):

        try:
            s ='%s,'*len_parameters
            s = s[:-1]
            s = '(' + s + ')'

            cursor,connection=self.connect()

            mySql_insert_query = """INSERT INTO {} {}
                                VALUES 
                                {} """.format(table_name,parametrs,data)
            # cursor=self.execute_quary(mySql_insert_query,data)
            self.cur.execute(mySql_insert_query)
            # cursor.execute(mySql_insert_query,data)
            # mySql_insert_query=(mySql_insert_query,data)
            # self.execute_quary(mySql_insert_query, cursor, connection, close=False,need_data=True )
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into images table")
            # cursor.close()
            return True

        except:
            return False




    def update_record(self,table_name,col_name,value,id_name,id_value):
        
        # try:
            cursor,connection=self.connect()
            # mySql_insert_query = """UPDATE {} 
            #                         SET {} = {}
            #                         WHERE [{} ={}] """.format(table_name, col_name, ("'"+value+"'"),id_name,(str(id_value)))
            
            # #print(mySql_insert_query)
            # self.cur.execute(mySql_insert_query)
            sql_update_query = """Update {} set {} = ? where {} = ?""".format(table_name,col_name,id_name)
            data = (value, id_value)
            self.cur.execute(sql_update_query, data)
            connection.commit()
            return True

        # except:
        #     return False


    def get_all_content(self,table_name):


            sql_select_Query = "select * from {} ".format(table_name)
            cursor= self.cur.execute(sql_select_Query)
            records = cursor.fetchall()

            field_names = [col[0] for col in cursor.description]
            res = []
            for record in records:
                    record_dict = {}
                    for i in range( len(field_names) ):
                        record_dict[ field_names[i] ] = record[i]
                    res.append( record_dict )
            # print(res)

            return res



if __name__=='__main__':
    t=  dataBase('screw_sqlite')
    # t.search('camera_settings','serial_number','111')
    # data=('0',1,1)
    # t.add_record(str(data),'PLC_PARMS','(id,name,path)',3)

    # t.update_record('PLC_PARMS','name','2','id',0)

    # t.get_all_content('PLC_PARMS')
    # t.get_all_content('plc_setting')
    # t.update_record('history','all_screw','50','id','0')
    t.update_record('plc_setting', 'path',' str(plc_parms[param])', 'name','run')
    