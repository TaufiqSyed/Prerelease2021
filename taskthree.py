class Tool:
    def __init__(self, name, cost, img_file_name):
        if isinstance(cost, (float, int)) and cost >= 0:
            self.__name = name
            self.__cost = cost
            self.__img_file_name = img_file_name
        else:
            print('Invalid cost')

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_cost(self):
        return self.__cost
    def set_cost(self, cost):
        if isinstance(cost, (float, int)) and cost >= 0:
            self.__cost = float(cost)
        else:
            print('Invalid cost')

    def get_img_file_name(self):
        return self.__img_file_name
    def set_img_file_name(self, img_file_name):
        self.__img_file_name = img_file_name

class Shelf:
    tools = []
    def __init__(self, position):
        if 0 <= position <= 4:
            self.__position = position
        else:
            print('Invalid position value')

    def add_tool(self, tool):
        if len(self.tools) > 10:
            print('Tool not added - shelf is full!')
        else:
            self.tools.append(tool)

def examine_tools(shelf):
    for tool in shelf.tools:
        print('Tool name: ' + tool.get_name())
        print('Cost: ' + str(tool.get_cost()) + '\n')

s = Shelf(3)
s.add_tool(Tool('Hammer', 34.23, 'hammer.png'))
s.add_tool(Tool('Sickle', 15, 'sickle.png'))
examine_tools(s)
