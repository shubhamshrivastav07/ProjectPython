# choice = input("enter your Choice\n1: Add\n2: Update\n3: Delete\n4: List\n5: Profile")
from com.app.DepartmentCtl import DepartmentCtl
from com.app.RoleCtl import RoleCtl
from com.app.UserCtl import UserCtl


class MyApp:

    def __init__(self):

        self.r = RoleCtl()
        self.d= DepartmentCtl()
        self.r = UserCtl()
        try:
            choice=int(input("enter your Choice\n1: User\n2: Department\n3: Role\nEnter Here ....:-"))
            match(choice):
                case 1:self.User()
                case 2:self.Department()
                case 3:self.Role()
        except Exception as e:
            print("Enter Only Number")
            self.__init__()


    def User(self):
        choice = int(input("enter your Choice\n1: Add User\n2: Update User\n3: Delete User\n4: ShowUserList\n5: Profile User"))
        self.r = UserCtl()
        match(choice):
            case 1: self.r.Add()
            case 2:
                self.r.Update()
            case 3:
                self.r.Delete()
            case 4:
                print(self.r.Show())
            case 5:
                self.r.ShowById()
        self.__init__()

    def Role(self):
        choice = int(input("enter your Choice\n1: Add Role\n2: Update Role\n3: Delete Role\n4: ShowRoleList\n5: Role Detail"))
        self.r = RoleCtl()
        match choice:
            case 1:self.r.Add()
            case 2: self.r.Update()
            case 3: self.r.Delete()
            case 4: print(self.r.Show())
            case 5 :print(self.r.ShowById())
        self.__init__()
    def Department(self):
        choice = int(input("enter your Choice\n1: Add Department\n2: Update Department\n3: Delete Department\n4: ShowDepartmentList\n5: Department Detail"))
        self.d = DepartmentCtl()
        match choice:
            case 1:
                self.d.Add()
            case 2:
                self.d.Update()
            case 3:
                self.d.Delete()
            case 4:
                print(self.d.Show())
            case 5:
                print(self.d.ShowById())
        self.__init__()

m= MyApp()


