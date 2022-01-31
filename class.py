class planet:
    def__init__(self):
        self.nam = 'Hort'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'hort system'

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
px=planet()
print(f'Name is:{px.name}')
print(f'Radius is:{px.radius}')
print(f'Gravity is:{px.gravity}')
