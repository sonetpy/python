class ShippingContainer:
    next_serial = 1377

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial = ShippingContainer.next_serial + 1
        return result

    def __init__(self,owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

c6 = ShippingContainer("YML", ["Coffee"])
print(c6.serial)
c7 = ShippingContainer("GBR", ["Coffee"])
print(c7.serial)
print(ShippingContainer.next_serial)

# Same code without Static Method
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