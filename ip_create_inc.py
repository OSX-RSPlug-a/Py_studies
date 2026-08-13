
class Ip_inc:
    def __init__(self):
        self._value = "192.168.1.1"


    def __add__(self, value):
        inic, final = self._value.rsplit(".", 1)

        final = int(final) + value
        final %= 256

        self._value = inic + "." + str(final)

        return self


    def __str__(self):
        return self._value



ip = Ip_inc()
print(ip)

for _ in range(20):
    ip += 1

    print(ip)
