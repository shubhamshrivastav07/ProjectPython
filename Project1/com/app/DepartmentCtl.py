from com.Dao.DepartmentDao import DepartmentDao
from com.base.BaseCtl import BaseCtl
from com.bean.DepartmentBean import DepartmentBean


class DepartmentCtl(BaseCtl,DepartmentDao):

    def __init__(self):
        self.d = DepartmentBean()
        self.CreateTable()

    def Add(self):
        dep_name = input("Enter Department Name")
        dep_code = input("Enter Department Code")
        self.depDto = DepartmentBean()
        self.depDto.setDepartmentName(dep_name)
        self.depDto.setDepartmentCode(dep_code)

        self.SaveData(self.depDto.__save__())

    def Update(self):
        dep_id = input("Enter Department id")
        dep_name = input("Enter Department Name")
        dep_code = input("Enter Department Code")
        self.depDto = DepartmentBean()
        self.depDto.setDepartmentId(dep_id)
        self.depDto.setDepartmentName(dep_name)
        self.depDto.setDepartmentCode(dep_code)
        self.UpdateData(self.depDto.__update__())
    def Delete(self):
        dep_id = input("Enter Department id")
        self.DeleteData(dep_id)


    def Show(self):
        datatp = self.ShowData()
        self.d = DepartmentBean()
        depData = list()
        for x in datatp:
            self.d.setDepartmentId(x[0])
            self.d.setDepartmentName(x[1])
            self.d.setDepartmentCode(x[2])
            depData.append(self.d.__dep__())

        return depData


    def ShowById(self):
        dep_id = input("Enter Department id")
        datatp = self.SearchById(dep_id)
        self.depDto = DepartmentBean()
        self.depDto.setDepartmentId(datatp[0])
        self.depDto.setDepartmentName(datatp[1])
        self.depDto.setDepartmentCode(datatp[2])
        return self.depDto.__dep__()


