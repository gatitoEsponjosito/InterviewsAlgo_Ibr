class MinStack:
    def __init__(self):
        self.stack=[];
        self.min=[];
    
    def push(self,val:int):
        self.stack.append(val);
        if self.min==[] or val<=self.min[-1]:
            self.min.append(val);
    
    def pop(self):
        element=self.stack.pop();
        if element==self.min[-1]:
            self.min.pop();
    
    def top(self):
        element=self.stack[-1];
        return element;
    
    def getMin(self)->int:
        return self.min[-1];