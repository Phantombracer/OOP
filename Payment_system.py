from abc import ABC, abstractmethod

# 1. Створюємо абстрактний базовий клас
class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self, amount):
        """Абстрактний метод для здійснення оплати"""
        pass

    @abstractmethod
    def refund(self, amount):
        """Абстрактний метод для повернення коштів"""
        pass

    def log_transaction(self, amount):
        """Звичайний метод, який успадкують всі класи"""
        print(f"[LOG]: Транзакція на суму {amount} грн успішно зареєстрована в системі.")


# 2. Реалізація оплати Кредитною Карткою
class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        # Беремо останні 4 цифри для безпеки
        secure_digits = self.card_number[-4:] if len(self.card_number) >= 4 else self.card_number
        print(f"Оплата {amount} грн з кредитної картки ****{secure_digits}")
        self.log_transaction(amount)

    def refund(self, amount):
        secure_digits = self.card_number[-4:] if len(self.card_number) >= 4 else self.card_number
        print(f"Повернення {amount} грн на кредитну картку ****{secure_digits}")


# 3. Реалізація оплати через PayPal
class PayPalPayment(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Оплата {amount} грн через PayPal (аккаунт: {self.email})")
        self.log_transaction(amount)

    def refund(self, amount):
        print(f"Повернення {amount} грн на аккаунт PayPal: {self.email}")


# 4. Реалізація оплати Криптовалютою
class CryptoPayment(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Оплата {amount} грн у криптовалюті з гаманця {self.wallet_address}")
        self.log_transaction(amount)

    def refund(self, amount):
        # Особливість крипти — незворотність транзакцій
        print(f"Помилка: Повернення {amount} грн на гаманець {self.wallet_address} неможливе (особливість блокчейну).")


# Головна частина програми
if __name__ == "__main__":
    # Створюємо список з різними способами оплати
    payments = [
        CreditCardPayment("4141123456789012"),
        PayPalPayment("user@example.com"),
        CryptoPayment("0x71C...3a9")
    ]
    
    print("--- ОПЛАТА ТОВАРІВ (Демонстрація Поліморфізму) ---")
    # Проходимося циклом і викликаємо pay() для кожного об'єкта
    for payment_method in payments:
        payment_method.pay(150)
        print("-" * 50)  # Розділювач для краси
        
    print("\n--- ТЕСТУВАННЯ ПОВЕРНЕННЯ КОШТІВ ---")
    for payment_method in payments:
        payment_method.refund(150)
        print("-" * 50)