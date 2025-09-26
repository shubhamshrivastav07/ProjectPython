from com.Dao.RoleDao import RoleDao
from com.base.BaseCtl import BaseCtl
from com.bean.RoleBean import RoleBean


class RoleCtl(BaseCtl,RoleDao):

    def __init__(self):
        self.r = RoleBean()
        self.CreateTable()

    def ShowById(self):
        role_id = input("Enter Role id")
        roleData= self.SearchById(role_id)
        self.r = RoleBean()
        self.r.setRoleId(roleData[0])
        self.r.setRoleName(roleData[1])

        return self.r.__role__()
    def Show(self):
        datatp= self.ShowData()
        self.r = RoleBean()
        userData=list()
        for x in datatp:
            self.r.setRoleId(x[0])
            self.r.setRoleName(x[1])
            userData.append(self.r.__role__())
        return userData
    def Delete(self):
        role_id = input("Enter Role id")
        self.DeleteData(role_id)


    def Update(self):
        role_id = input("Enter Role id")
        role_name = input("Enter Role Name")
        r= RoleBean()
        r.setRoleId(role_id)
        r.setRoleName(role_name)
        self.UpdateData(r.__update__())

    def Add(self):
        role_name= input("Enter Role Name")
        self.r = RoleBean()
        self.r.setRoleName(role_name)


        self.SaveData(self.r.__save__())
        return  "data save"