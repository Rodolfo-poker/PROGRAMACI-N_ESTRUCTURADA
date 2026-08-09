import funciones

def insertar(peli,conexionBD):
    try:
        if conexionBD!=None:
          cursor=conexionBD.cursor()
          cursor.execute("insert into peliculas values (null,%s)",(peli,))
          conexionBD.commit()
          return True
        else:
          return False   
    except Exception as e:
        return False
    
def consultar(conexionBD):
    try:
       if conexionBD!=None:
           cursor=conexionBD.cursor()
           cursor.execute("select * from peliculas")
           return cursor.fetchall()
       else:
           return []
    except:
        return []

def vaciar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("truncate peliculas")
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False

def buscar(peli,conexionBD):
    try:
       if conexionBD!=None:
           cursor=conexionBD.cursor()
           cursor.execute("select * from peliculas where nombre = %s",(peli,))
           return cursor.fetchall()
       else:
           return []
    except:
        return []

def borrar(peli,conexionBD):
    try:
        if conexionBD!=None:
          cursor=conexionBD.cursor()
          cursor.execute("delete from peliculas where nombre=%s",(peli,))
          conexionBD.commit()
          return True
        else:
          return False   
    except Exception as e:
        return False

def actualizar(peli,peli2,conexionBD):
    try:
        if conexionBD!=None:
          cursor=conexionBD.cursor()
          cursor.execute("update peliculas set nombre=%s where peliculas nombre=%s",(peli2,peli))
          conexionBD.commit()
          return True
        else:
          return False   
    except Exception as e:
        return False