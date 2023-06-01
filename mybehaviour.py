import py_trees
class myFun(py_trees.behaviour.Behaviour):
    
    def update(self):
            tmp=int(input())
            tmp=tmp * 5
            if tmp >= 20:
                self.logger.debug("%s.update()[%s: success]" % (self.__class__.__name__, tmp))
                return py_trees.common.Status.SUCCESS
            else:
                self.logger.debug("%s.update()[%s: failure]" % (self.__class__.__name__, tmp))
                return py_trees.common.Status.FAILURE


class myAct(py_trees.behaviour.Behaviour):
    def update(self):
        tmp=0
        a=int(input())
        b=int(input())
        c=a+b
        if c == 10:
            tmp=1
        else:
            tmp=0
        if tmp:
            self.logger.debug("%s.update()[%s: success]" % (self.__class__.__name__,tmp))
            print("finish")
            return py_trees.common.Status.SUCCESS
        else :
            self.logger.debug("%s.update()[%s: failure]" % (self.__class__.__name__,tmp))
            print("failure")
            return py_trees.common.Status.FAILURE