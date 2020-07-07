class Calculator:  # 首字母推荐大写，冒号不能缺
    name = 'Good Calculator'  # 该行为class的属性
    price = 18  # 该行为class的属性

    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)

    def minus(self, x, y):
        result = x - y
        print(result)

    def times(self, x, y):
        print(x * y)

    def divide(self, x, y):
        print(x / y)


cal = Calculator()
print(cal.name)
print(cal.price)
cal.add(10, 20)
cal.minus(10, 20)
cal.times(10, 20)
cal.divide(10, 20)


# __init__
class Test:
    name = 'Test'
    price = 100

    def __init__(self, name, price, height=5, width=10, weight=20):
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.weight = weight

    def __str__(self):  # 覆写 __str__ 类似 toString()
        return 'name: ' + self.name \
               + '\nprice: ' + str(self.price) \
               + '\nheight: ' + str(self.height) \
               + '\nwidth: ' + str(self.width) \
               + '\nweight: ' + str(self.weight)


test = Test('test', 50, 25, 55)
print(test.name, test.price, test.height, test.width, test.weight)
test.weight = 25
print(test.name, test.price, test.height, test.width, test.weight)
print(test)
