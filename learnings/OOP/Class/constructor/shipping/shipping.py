class ShippingContainer:
    next_serial = 1377

    def _generate_serial(self):
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self._generate_serial()
        #ShippingContainer.next_serial += 1

"""
>>> from shipping import *
>>> c1 = ShippingContainer("68YCB", "Abhinav")
>>> print(c1.serial) 
1377
>>> c2 = ShippingContainer("68YCB", "Abhinav") 
>>> print(c2.serial) 
1379
>>> print(c2.owner_code)
68YCB
"""