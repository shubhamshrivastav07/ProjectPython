


class User:

    user_id=None
    user_name=None
    user_age=None
    user_city=None
    user_role_id = None
    user_dep_id = None
    create_date=None
    update_date=None

    def setUserId(self,user_id):
        self.user_id= user_id

    def setUserName(self,user_name):
        self.user_name= user_name
    def setUserAge(self,user_age):
        self.user_age= user_age
    def setUserCity(self,user_city):
        self.user_city= user_city

    def setRoleId(self, role_id):
        self.user_role_id = role_id

    def setDepartmentId(self, dep_id):
        self.user_dep_id = dep_id


    def setUserCreateDate(self,create_date):
        self.create_date= create_date
    def setUserUpdateDate(self,update_date):
        self.update_date= update_date

    def __Userdict__(self):
      return dict({"user_id":self.user_id,
                   "user_name":self.user_name,
                   "user_age":self.user_age,
                   "user_city":self.user_city,
                   "role_id": self.user_role_id,
                   "dep_id": self.user_dep_id,
                   "create_date":self.create_date,
                   "update_date": self.update_date
                   })


    def __save__(self):

        return (  self.user_name,
                  self.user_age,
                  self.user_city,
                   self.user_role_id,
                   self.user_dep_id,
                  self.create_date,
                   self.update_date
                )
    def __update__(self):

        return (
                  self.user_name,
                  self.user_age,
                  self.user_city,
                   self.user_role_id,
                   self.user_dep_id,
                   self.update_date,
                    self.user_id
                   )