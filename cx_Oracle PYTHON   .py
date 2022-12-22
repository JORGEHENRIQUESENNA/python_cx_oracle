import cx_Oracle as oc

uid = "USUARIO"    # usuário
pwd = "SENHA"   # senha
db = "IP:PORTA/SERVICES"  # string de conexão do Oracle, configurado no
                                # cliente Oracle, arquivo tnsnames.ora
 
connection = oc.connect(uid+"/"+pwd+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor

cursor.execute("select..... ") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
if result == None: 
        print ('Nenhum Resultado')
        exit
else:
        while result:   
                print (
                    result[0],result[1],result[2],result[3],result[4],result[5]
                )
                result = cursor.fetchone()
cursor.close()
connection.close()