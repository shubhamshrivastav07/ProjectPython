from abc import ABC

from com.base.BaseDao import BaseDao


class UserDao(BaseDao):

    def CreateTable(self):
        super().__init__()
        table="create table user(user_id int primary key auto_increment,user_name varchar(255) not null,user_age int,user_city varchar(255),role_id int,department_id int,create_date datetime,update_date datetime, foreign key(role_id)  references Role(role_id),foreign key(department_id)  references Department(department_id)   ) "
        self.cursor.execute(table)

    def SaveData(self, data):
        print(data)
        insert = "insert into user(user_name ,user_age,user_city,role_id,department_id,create_date,update_date)value(%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(insert,data)
        print("ok")
        self.con.commit()


    def UpdateData(self, data):
        update = "update user set user_name = %s,user_age = %s,user_city = %s,role_id = %s,department_id = %s,update_date = %s where user_id=%s )"
        self.cursor.execute(update,data)
        pass

    def ShowData(self):
        search="select * from user"
        self.cursor.execute(search)
        return  self.cursor.fetchall()

    def DeleteData(self, id):
        delete = "delete from user where user_id=%s"
        self.cursor.execute(delete,id)

        pass

    def SearchById(self, id):
        search = ("select * from user where "
                  "user_id=%s")
        self.cursor.execute(search, id)
        return self.cursor.fetchall()
