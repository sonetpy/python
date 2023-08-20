# Before Static Method
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
        ShippingContainer.next_serial += 1

c6 = ShippingContainer("YML", ["Coffee"])
print(c6.serial)
c7 = ShippingContainer("YML", ["Coffee"])
print(c7.serial)
c8 = ShippingContainer("YML", ["Coffee"])
print(c8.serial)