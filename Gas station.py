class FuelDispenser:
    def __init__(self, max_volume, fuel_balance, fuel_price):
        """
        Конструктор
        :param max_volume: максимальний обʼєм колонки
        :param fuel_balance: поточний баланс пального
        :param fuel_price: вартість 1 літра пального
        """
        self.max_volume = max_volume
        self.fuel_balance = fuel_balance
        self.fuel_price = fuel_price
        self.cars_fueled = 0
        self.fuel_sold = 0.0
        self.money_earned = 0.0


    @classmethod
    def copy(cls, other):
        new_obj = cls(
            other.max_volume,
            other.fuel_balance,
            other.fuel_price
        )
        new_obj.cars_fueled = other.cars_fueled
        new_obj.fuel_sold = other.fuel_sold
        new_obj.money_earned = other.money_earned
        return new_obj

    def refuel_car(self, liters):
        """
        Заправити авто
        :param liters: кількість літрів
        """
        if liters <= 0:
            print("Кількість пального повинна бути більшою за 0.")
            return

        if liters > self.fuel_balance:
            print("Недостатньо пального в колонці.")
            return

        self.fuel_balance -= liters
        self.fuel_sold += liters
        self.money_earned += liters * self.fuel_price
        self.cars_fueled += 1

        print(f"Авто заправлено на {liters} л.")

    def refill_fuel(self, liters):
        """
        Поповнити запас пального
        :param liters: кількість літрів
        """
        if liters <= 0:
            print("Кількість пального повинна бути більшою за 0.")
            return

        if self.fuel_balance + liters > self.max_volume:
            print("Перевищення максимального обʼєму колонки.")
            return

        self.fuel_balance += liters
        print(f"Колонку поповнено на {liters} л.")

    def get_statistics(self):
        """
        Видати дані по заробітку, реалізованому пальному і кількості авто
        """
        return {
            "Зароблені кошти": self.money_earned,
            "Реалізоване пальне (л)": self.fuel_sold,
            "Кількість заправлених авто": self.cars_fueled
        }