#encoding=utf-8
#!/usr/bin/python3

class GStack:
    """ this is a stack"""
    items = []

    def isEmpty(self):
        return (self.items.count == 0)        

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[items.count -1]
        else:
            return None
    def size(self):
        print("gstack size ->",len(self.items))
        return len(self.items)