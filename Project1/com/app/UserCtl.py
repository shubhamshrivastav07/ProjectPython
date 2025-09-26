from com.Dao.DepartmentDao import DepartmentDao
from com.Dao.RoleDao import RoleDao
from com.Dao.UserDao import UserDao
from com.app.DepartmentCtl import DepartmentCtl
from com.app.RoleCtl import RoleCtl
from com.base.BaseCtl import BaseCtl
from datetime import  datetime as d

from com.bean import UserBean
from com.bean.UserBean import  User


class UserCtl(BaseCtl,UserDao):

    def Add(self):
        user_name = input("Enter User Name")
        user_age = input("Enter User Age")
        user_city = input("Enter User City")
        r= RoleCtl()
        for x in r.Show():
            print(f"Role : {x}",end="\n" )

        role_id = input("Enter Role id")
        dep= DepartmentCtl()
        for depData in dep.Show():
            print(f"Department : {depData}",end="\n" )

        dep_id = input("Enter Dep_id")
        u = User()
        u.setUserName(user_name)
        u.setUserAge(user_age)
        u.setUserCity(user_city)
        u.setRoleId(role_id)
        u.setDepartmentId(dep_id)
        u.setUserCreateDate(d.strftime(d.now(),"%Y-%m-%d %H:%M:%S"))
        u.setUserUpdateDate(d.strftime(d.now(),"%Y-%m-%d %H:%M:%S"))
        print(u.__Userdict__())
        self.SaveData(u.__save__())



    def Update(self):
        user_id = input("Enter User Id")
        user_name = input("Enter User Name")
        user_age = input("Enter User Age")
        user_city = input("Enter User City")
        r= RoleCtl()
        for x in r.Show():
            print(f"Role : {x}",end="\n" )

        role_id = input("Enter Role id")
        dep= DepartmentCtl()
        for depData in dep.Show():
            print(f"Department : {depData}",end="\n" )

        dep_id = input("Enter Dep_id")
        u = User()
        u.setUserId(user_id)
        u.setUserName(user_name)
        u.setUserAge(user_age)
        u.setUserCity(user_city)
        u.setRoleId(role_id)
        u.setDepartmentId(dep_id)
        u.setUserCreateDate(d.strftime(d.now(),"%Y-%m-%d %H:%M:%S"))
        u.setUserUpdateDate(d.strftime(d.now(),"%Y-%m-%d %H:%M:%S"))
        self.UpdateData(u.__update__())



    def Delete(self):
        user_id = input("Enter User Id")
        self.DeleteData(user_id)

    def Show(self):

        userDataList =  self.ShowData()
        newUserList= list()
        for userdata in userDataList:
            user= User()
            user.setUserId(userdata[0])
            user.setUserName(userdata[1])
            user.setUserAge(userdata[2])
            user.setUserCity(userdata[3])
            user.setRoleId(userdata[4])
            user.setDepartmentId(userdata[5])
            user.setUserCreateDate(userdata[6])
            user.setUserUpdateDate(userdata[7])
            newUserList.append(user.__Userdict__())
        return newUserList

    def ShowById(self):
        pass

