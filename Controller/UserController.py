from Database import Database
import pymysql
class UserController:
    def createUser(self):
        try:
            connection=pymysql.connect(host='localhost',
                             user='dbUser',
                             password='dbPassword',
                             db='pythondb')
            cursor=connection.cursor()
            query="INSERT INTO users(cdUser,name,password) VALUES(%s,%s,%s)"
            data=("2","admin2","admin2")
            cursor.execute(query,data)
            connection.commit()
            
            print("Creation User Successfull!")
        except:
            print("Creation User Failed! :(")

        finally:
            connection.close()


    def getAll(self):
        try:
            connection=pymysql.connect(host='localhost',
                             user='dbUser',
                             password='dbPassword',
                             db='pythondb')
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM users")
            connection.commit()
            results = cursor.fetchall()
            for row in results:
                print row[0:]
 
        except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Get All Failed! :(",e)

        finally:
            connection.close()

