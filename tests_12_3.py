import unittest



def frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_method(self, *args, **kwargs)

    return wrapper