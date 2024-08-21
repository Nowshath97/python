class pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class eclipse:

    def execute(self):
        print("Spell check")
        print("Formatting")
        print("Compiling")
        print("Running")

class laptop:

    def code(self,ide):
        ide.execute()

ide = pycharm()
ide=eclipse()
lap1 = laptop()
lap1.code(ide)
