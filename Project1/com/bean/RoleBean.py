

class RoleBean:

    roleId=None
    roleName= None

    def setRoleId(self,rid):
        self.roleId= rid

    def setRoleName(self,rolename):
        self.roleName = rolename
    def __role__(self):
        return  dict({"roleId":self.roleId,"roleName":self.roleName})

    def __save__(self):
        return   (self.roleName )
    def __update__(self):
        return tuple ([self.roleName , self.roleId])





