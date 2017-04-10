from decimal import Decimal


class Fees(object):
    def __init__(self):
        self._fee = None

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value


if __name__ == "__main__":
    f = Fees()
    print(f.fee)
    f.fee = "1.5"
    print(f.fee)
    f.fee = Decimal("2.33")
    print(f.fee)
