# https://www.youtube.com/watch?v=zS0HyfN7Pm4&t=4s
class Portished:
    def __init__(self):
        print('Portishead')

class KanyeWest(Portished):
    def __init__(self):
        print('Kanye West')
        Portished.__init__(self)

kanye_west = KanyeWest()

### super() is alternative of super class


class Portished:
    def __init__(self):
        print('Portishead')


class KanyeWest(Portished):
    def __init__(self):
        print('Kanye West')
        super().__init__()


kanye_west = KanyeWest()

# Diamond/Multiple Inheritance

print("\nMultiple Inheritance\n")
class Portished:
    def __init__(self):
        print('Portishead')


class KanyeWest(Portished):
    def __init__(self):
        print('Kanye West')
        Portished.__init__(self)

class ASAPRocky(Portished):
    def __init__(self):
        print('ASAP Rocky')
        Portished.__init__(self)


class ASAPSebbie(ASAPRocky, Portished):
    def __init__(self):
        print('A$AP Sebbie')
        ASAPRocky.__init__(self)
        KanyeWest.__init__(self)

asap_sebbie = ASAPSebbie()

print("How to use Super() and it's beauty")

print("\nMultiple Inheritance\n")


class Portished:
    def __init__(self):
        print('Portishead')
        #pass


class KanyeWest(Portished):
    def __init__(self):
        print('Kanye West')
        super().__init__()


class ASAPRocky(Portished):
    def __init__(self):
        print('ASAP Rocky')
        super().__init__()


class ASAPSebbie(ASAPRocky, Portished):
    def __init__(self):
        print('A$AP Sebbie')
        super().__init__()


asap_sebbie = ASAPSebbie()
