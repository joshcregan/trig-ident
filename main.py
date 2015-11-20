class Net:
    def __init__(self, inSize, outSize):
        self.inSize = inSize
        self.outSize = outSize
        self.nodes = []
        self.totalsize = (inSize**2+inSize)/2 #this is wrong, I'll fix this later
        for i in range(0,self.size):
            self.nodes.append()
            

class Node(Net):
    def __init__(self, layer, layersize):
        self.layer = layer
        self.value = 0
        self.inMod = []
        self.outMod = []
        self.threshold = random.randint(0,100)


class genome(Net):
    def __init__(self):
        self.value = []
    def populate(self):
        for i in range(0, self.totalsize):
            value.append(random.randint(-100,100))


  
