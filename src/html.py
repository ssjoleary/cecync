def parse(source):
    root_node = Parser(0, source).parse_nodes()
    return root_node


class Parser(object):
    def __init__(self, pos=0, input):
        self.pos = pos
        self.input = input

