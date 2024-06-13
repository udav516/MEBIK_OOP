class Themes:
    def __init__(self, themes):
        self.themes = themes

    def add_theme(self, value):
        self.themes.append(value)

    def shift_one(self):
        self.themes = [self.themes[-1]] + self.themes[:-1]

    def reverse_order(self):
        self.themes = self.themes[::-1]

    def get_themes(self):
        return tuple(self.themes)

    def get_first(self):
        return self.themes[0]


tl = Themes(['weather', 'rain'])
tl.add_theme('warm')
print(tl.get_themes())  # Output: ('weather', 'rain', 'warm')
tl.shift_one()
print(tl.get_first())  # Output: 'warm'

tl = Themes(['sun', 'feeding'])
tl.add_theme('cool')
tl.shift_one()
print(tl.get_first())  # Output: 'cool'
tl.reverse_order()
print(tl.get_themes())  # Output: ('feeding', 'sun', 'cool')
