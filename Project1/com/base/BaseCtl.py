
from abc import  ABC,abstractmethod

from com.base.BaseDao import BaseDao


class BaseCtl(ABC):


    @abstractmethod
    def Add(self):
        pass
    @abstractmethod
    def Update(self):
        pass
    @abstractmethod
    def Delete(self):
        pass
    @abstractmethod
    def Show(self):
        pass
    @abstractmethod
    def ShowById(self):
        pass
