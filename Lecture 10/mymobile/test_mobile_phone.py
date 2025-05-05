from mobile_phone_class import MobilePhone

def test_1():
    phone = MobilePhone('375445678902')
    assert phone.number == '375445678902'
    assert phone.switch == False


def test_2():
    phone = MobilePhone("375445678902")
    test_turn_on = phone.turn_on()
    assert test_turn_on == "Мобильный номер: 375445678902 включен"
    assert phone.switch == True


def test_3():
    phone = MobilePhone("375445678902")
    test_turn_off = phone.turn_off()
    assert test_turn_off == "Мобильный номер: 375445678902 выключен"
    assert phone.switch == False


def test_4():
    phone = MobilePhone("375445678902")
    phone.turn_on()
    test_call_on = phone.call('2882883')
    assert test_call_on == "Звоню абоненту 2882883"


def test_5():
    phone = MobilePhone("375445678902")
    test_call_off = phone.call('2882883')
    assert test_call_off == "Мобильный выключен"