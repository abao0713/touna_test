from common.configDB import  MyDB

a = MyDB()
a.connectDB()
sql="select * from rb_case_info where id=%s"
b = a.executeSQL(sql,29627)
a.get_all(b)
a.get_field(b)
a.closeDB()