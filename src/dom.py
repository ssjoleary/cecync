class Node(object):
    def __init__(self):
        self.children = []
        self.node_type = ""

    def __str__(self):
        print "Node: \nChildren: " + ', '.join(self.children)
        print self.node_type
        return ''

    @classmethod
    def typeElement(cls, nameIn, attrsIn, childrenIn):
        obj = cls()
        obj.node_type = ElementData(nameIn, attrsIn)
        obj.children = childrenIn
        return obj

    @classmethod
    def typeText(cls, data):
        obj = cls()
        obj.children = []
        obj.node_type = data
        return obj


class ElementData(object):
    def __init__(self, tag_nameIn, attrsIn):
        self.tag_name = tag_nameIn
        self.attrs = attrsIn

    def __str__(self):
        print "Element Data: \nTag Name: " + self.tag_name
        for attr in self.attrs:
            print (attr)
        return  ''
