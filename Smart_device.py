# Базовий клас для всіх пристроїв
class Device:
    def __init__(self):
        print("Device initialized")
        
    def __del__(self):
        print("Device destroyed")

# Перший рівень спадкування: окремі компоненти
class Camera(Device):
    def __init__(self):
        print("Camera initialized")
        super().__init__()
        
    def __del__(self):
        print("Camera destroyed")
        super().__del__()

class Microphone(Device):
    def __init__(self):
        print("Microphone initialized")
        # Замість super().__init__() пишемо:
        Device.__init__(self)
        
    def __del__(self):
        print("Microphone destroyed")
        # Замість super().__del__() пишемо:
        Device.__del__(self)

class Speaker(Device):
    def __init__(self):
        print("Speaker initialized")
        super().__init__()
        
    def __del__(self):
        print("Speaker destroyed")
        super().__del__()

# Другий рівень спадкування: об'єднання мікрофона та динаміка
class VoiceModule(Microphone, Speaker):
    def __init__(self):
        print("VoiceModule initialized")
        super().__init__()
        
    def __del__(self):
        print("VoiceModule destroyed")
        super().__del__()

# Фінальний клас: Розумний помічник, що має камеру та голосовий модуль
class SmartAssistant(Camera, VoiceModule):
    def __init__(self):
        print("SmartAssistant initialized")
        super().__init__()
        
    def __del__(self):
        print("SmartAssistant destroyed")
        super().__del__()

# Головна частина, яка запускає код
if __name__ == "__main__":
    print("--- 1. Створення об'єкта ---")
    assistant = SmartAssistant()
    
    print("\n--- 2. Порядок MRO для класу SmartAssistant ---")
    print(SmartAssistant.__mro__)
    
    print("\n--- 3. Видалення об'єкта ---")
    del assistant