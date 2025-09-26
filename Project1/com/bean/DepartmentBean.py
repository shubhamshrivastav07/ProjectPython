

class DepartmentBean():


    departmentId=None
    departmentName=None
    departmentCode=None

    def setDepartmentId(self, departmentId):
        self.departmentId = departmentId

    def setDepartmentName(self, departmentName):
        self.departmentName = departmentName

    def setDepartmentCode(self, departmentCode):
        self.departmentCode = departmentCode

    def __save__(self):
        return (self.departmentName,self.departmentCode)

    def __update__(self):
        return tuple([self.departmentName,self.departmentCode, self.departmentId])

    def __dep__(self):
        return dict({"departmentId": self.departmentId,
                     "departmentName": self.departmentName,
                     "departmentCode": self.departmentCode})


