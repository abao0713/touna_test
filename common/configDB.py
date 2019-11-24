import pymysql
from common import readConfig
from logs.Log import MyLog

localReadConfig = readConfig.ReadConfig()


class MyDB:
    global host, username, password, port, database, config
    host = localReadConfig.get_db('host')
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    code = localReadConfig.get_db("code")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database,
        'charset': code
    }


    def __init__(self):
        self.log = MyLog.get_log(logger="MyDB")
        self.Logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            self.Logger.error(str(ex))

    def executeSQL(self, sql, params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # accept the field names
        col = self.cursor.description
        # executing by committing to DB
        self.db.commit()
        return self.cursor
    def get_field(self, cursor):
        # accept the field names
        list = []
        col = cursor.description
        for i in range(len(col)):
            list.append(col[i][0])
        print(list)
        self.Logger.info("the field name is %s" % list)
        return list

    def get_all(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        self.Logger.info("the data is %s"%value)
        return value

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        self.Logger.info("the data is %s" % value)
        return value

    def closeDB(self):
        """
        close database
        :return:
        """
        self.db.close()
        print("Database closed!")

