import pymysql
class Database:
    def getConnection(self):
        try:
            conexion = pymysql.connect(host='localhost',
                             user='dbUser',
                             password='dbPassword',
                             db='pythondb')
            print("Connection Success!")
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	        print("Connection Failed: ", e)

    
