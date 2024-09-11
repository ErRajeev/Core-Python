from abc import *
class School(ABC):
    @abstractclassmethod
    def classRoom(self):
        pass

ob = School()
ob.classRoom