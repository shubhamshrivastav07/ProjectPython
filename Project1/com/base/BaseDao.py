
from  abc import  ABC, abstractmethod

import  pymysql as db


class BaseDao(ABC):

    save_op="save"
    delete_op="delete"
    update_op="update"
    show_op="show"

    def __init__(self):
        self.con = db.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    port=3306,
                    database="bhawesh"
                            )
        self.cursor=self.con.cursor()
        self.con.autocommit(True)
    @abstractmethod
    def CreateTable(self):
        pass

    @abstractmethod
    def SaveData(self,data):
        pass

    @abstractmethod
    def UpdateData(self,data):
        pass

    @abstractmethod
    def ShowData(self):
        pass

    @abstractmethod
    def DeleteData(self,id):
        pass

    @abstractmethod
    def SearchById(self,id):
        pass







