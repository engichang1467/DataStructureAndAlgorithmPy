'''
Parentheses checker

Desc: Check if those parentheses are balanced
      This time we got {} and []

Ex:
    Balanced
    * {{([][ ] ) } ( ) }
    * [ [ { { ( ( ) ) } } ] ]
    * [][][](){}

    Not Balanced
    * ( [ ) ]
    * ( ( ( ) ] ) )
    * [ { ( ) ] 
'''

from StackADT import Stack

def matches(open, close):
    opens = "({["
    closes= "]})"
    return opens.index(open) == closes.index(close)

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False
    

if __name__ == "__main__":

    # a = '{{([][])}()}'
    a = '[][][](){}'
    print(par_checker(a))

    a = '[{()]'
    print(par_checker(a))
