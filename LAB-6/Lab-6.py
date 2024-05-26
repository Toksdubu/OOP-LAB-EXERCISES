# Module 4 - Introduction to Object oriented programming
# Problem 1

class TV:
    def __init__(self, brand, size, is_on=False, channel=1, volume=50):
        self.brand = brand
        self.size = size
        self.is_on = is_on
        self.channel = self.validate_channel(channel)
        self.volume = self.validate_volume(volume)

    def validate_channel(self, channel):
        return (channel % 120)

    def validate_volume(self, volume):
        if volume <= 7:
            return volume
        else:
            return 7

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, channel):
        if self.is_on:
            self.channel = self.validate_channel(channel)

    def set_volume(self, volume):
        if self.is_on:
            self.volume = self.validate_volume(volume)


class TestTV:
    def __init__(self):
        tv1 = TV("TV 1", 42, channel=180, volume=6)
        tv2 = TV("TV 2", 55, channel=3, volume=2)

        tv1.turn_on()
        tv2.turn_on()

        self.display_tv_info(tv1)
        self.display_tv_info(tv2)

    @staticmethod
    def display_tv_info(tv):
        print(f"{tv.brand}'s channel is {tv.channel} and volume level is {tv.volume}")


# Test
TestTV()
