class MobilePhone():
    def __init__(self, number):
        self.number = number
        self.switch = False

    
    def turn_on(self):
        self.switch = True
        return f'Мобильный номер: {self.number} включен'
    

    def turn_off(self):
        self.switch = False
        return f'Мобильный номер: {self.number} выключен'


    def call(self, cally):
        if self.switch:
            return f'Звоню абоненту {cally}'
        else:
            return "Мобильный выключен"


phone1 = MobilePhone('37529000000000')
phone2 = MobilePhone('37533000001000')

print(phone1.turn_on())
print(phone2.turn_on())

print(phone2.call('2882883'))

print(phone1.turn_off())
print(phone2.turn_off())