class Cookie:
    def __init__(self, color):
        self.color = color

    def __int__(self, color):
        self.color=color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color=color

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is ', cookie_one.get_color())
print('Cookie tow is ',cookie_two.get_color())