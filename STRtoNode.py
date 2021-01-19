
class buildNode():
    count = 0
    stack = []
    S_paren = []
    S_bracket = []
    S_brace = []
    r_list = []
    length = 0
    sanyuan = []
    dict_stack = {')': S_paren, ']': S_bracket, '}': S_brace}
    dict_jiedian = {')': 'T3L', ']': 'T2u1', '}': 'T2u2'}
    def __init__(self, tag):
        self.tag = tag
    def pop_stack(self, key):
        if self.dict_stack[key][-1] == ':':
            self.dict_stack[key].pop()
            if (self.dict_stack[key][-1]) != ':':
                self.sanyuan = [self.dict_stack[key][-1], self.count]
                self.dict_stack[key].pop()
                self.count = self.count + 1
                self.length = self.length + 1

            if self.tag[self.count] != key:
                self.sanyuan.append(self.length)
                self.sanyuan.append(self.dict_jiedian[key])
                self.r_list.append(self.sanyuan)
                self.length = 0
        elif ((self.dict_stack[key][-1]) != '(' or (self.dict_stack[key][-1]) != '[' or (self.dict_stack[key][-1]) != '{') and self.tag[self.count+1] != key:
            self.dict_stack[key].pop()
            self.length = self.length + 1
            self.count = self.count + 1
            self.sanyuan.append(self.length)
            self.sanyuan.append(self.dict_jiedian[key])
            self.r_list.append(self.sanyuan)
            self.length = 0
        else:
            self.dict_stack[key].pop()
            self.count = self.count + 1
            self.length = self.length + 1
            if self.dict_stack[key][-1] == ':':
                self.sanyuan.append(self.length)
                self.sanyuan.append(self.dict_jiedian[key])
                self.r_list.append(self.sanyuan)
                self.length = 0
    def generate_node(self):
        while self.count < len(self.tag)-1:
            if self.tag[self.count] == '(':
                self.S_paren.append(self.count)
                self.count = self.count + 1
                if self.tag[self.count] != '(':
                    self.S_paren.append(':')
            elif self.tag[self.count] == '[':
                self.S_bracket.append(self.count)
                self.count = self.count + 1
                if self.tag[self.count] != '[':
                    self.S_bracket.append(':')
            elif self.tag[self.count] == '{':
                self.S_brace.append(self.count)
                self.count = self.count + 1
                if self.tag[self.count] != '{':#左括号的下一个进栈
                    self.S_brace.append(':')
                    '''if self.tag[self.count] == ':':
            if self.tag[self.count-1] == '(' or self.tag[self.count+1] == ')': #左括号的下一个或者右括号的前一个点进栈
                self.S_paren.append(':')
                self.count = self.count + 1
            elif self.tag[self.count-1] == '[' or self.tag[self.count+1] == ']': #左括号的下一个或者右括号的前一个点进栈
                self.S_bracket.append(':')
                self.count = self.count + 1
            elif self.tag[self.count-1] == '{' or self.tag[self.count+1] == '}': #左括号的下一个或者右括号的前一个点进栈
                self.S_brace.append(':')
                self.count = self.count + 1
            else:'''
            if self.tag[self.count] == ':':
                self.count = self.count + 1

            if self.tag[self.count] == ')':
                if self.tag[self.count - 1] != ')':
                    self.S_paren.append(':')
            elif self.tag[self.count] == ']':
                if self.tag[self.count - 1] != ']':
                    self.S_bracket.append(':')
            elif self.tag[self.count] == '}':
                if self.tag[self.count - 1] != '}':
                    self.S_brace.append(':')


            while self.tag[self.count] == ')':
                self.pop_stack(')')
            while self.tag[self.count] == ']':
                self.pop_stack(']')
            while self.tag[self.count] == '}':
                self.pop_stack('}')
        return self.r_list


if __name__ == '__main__':
    tag =':((((((((((((:[[[[[[:::::::::)))))))))))):::::((:(((((:]]]]]]))))):))::::'
    # tag = '............((........))((((((.((.......))..((((((((........................)))))))).................))))))..'
    tag = tag + '\n'
    tg = buildNode(tag)
    print(tg.generate_node())




