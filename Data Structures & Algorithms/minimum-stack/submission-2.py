class MinStack:

    def __init__(self):
        self.MinStack = []
        self.mainstack=[]
        # self.ans =[]
    def push(self, val: int) -> None:
        # self.ans.append('null')
        self.mainstack.append(val)
        if self.MinStack and self.MinStack[-1]>=val:
            self.MinStack.append(val)
        elif not self.MinStack:
            self.MinStack.append(val)
        return 'null'

    def pop(self) -> None:
        # self.ans.append('null')
        a=self.mainstack.pop()
        if a==self.MinStack[-1]:
            self.MinStack.pop()
        return 'null'



    def top(self) -> int:
        # self.ans.append(self.mainstack[-1])
        return self.mainstack[-1]
        

    def getMin(self) -> int:
        # self.ans.append(self.MinStack[-1])
        return self.MinStack[-1]
        
