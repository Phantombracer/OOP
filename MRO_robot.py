class Core:
    def boot(self):
        print("Core boot")


class PowerModule(Core):
    def boot(self):
        print("PowerModule boot")
        super().boot()


class SensorsModule(Core):
    def boot(self):
        print("SensorsModule boot")
        super().boot()


class CommsModule(Core):
    def boot(self):
        print("CommsModule boot")
        super().boot()


class LoggerModule(Core):
    def boot(self):
        print("LoggerModule boot")
        Core.boot(self)


class SafetyModule(SensorsModule, LoggerModule):
    def boot(self):
        print("SafetyModule boot")
        super().boot()


class DiagnosticsModule(CommsModule, LoggerModule):
    def boot(self):
        print("DiagnosticsModule boot")
        super().boot()


class Robot(SafetyModule, PowerModule, DiagnosticsModule):
    pass


print("\n=== RUN 3 (інший порядок) ===")
r = Robot()
r.boot()

print("\nMRO:")
print(Robot.__mro__)