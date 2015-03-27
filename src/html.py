from dom import Node


def parse(source):
    root_node = Parser(0, source).parse_nodes()
    return root_node


class Parser(object):
    def __init__(self, stringInput='', pos=0):
        self.pos = int(pos)
        self.stringInput = stringInput

        ' Read the next character without consuming it '
    def next_char(self):
        return self.stringInput[self.pos]

        ' Do the next characters start with the given string?'
    def starts_with(self, s):
        return self.stringInput[self.pos:len(s)] == s

        ' Return true if all input is consumed '
    def eof(self):
        return self.pos >= len(self.stringInput)

        ' Return the current character, and advance to the next character'
    def consume_char(self):
        nextChar = self.stringInput[self.pos]
        self.pos += 1
        return nextChar

        ' Consume characters until false'
    def consume_while(self, test):
        result = ''
        while not (self.eof()) and test(self.nextChar()):
            result += self.consume_char()
        return result

        ' Consume and discard zero or more whitespace characters'
    def consume_whitespace(self):
        self.consume_while('whitespace')

        ' Parse a tag or attribute name'
    def parse_tag_name(self):
        return self.consume_while('alphanumeric')

        ' Parse a single node'
    def parse_node(self):
        if (self.next_char() == '<'):
            return self.parse_element()
        else:
            return self.parse_text()

        ' Parse a text node'
    def parse_text(self):
        return Node.typeText(self.consume_while('need to make anonymous function'))
