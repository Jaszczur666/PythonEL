import dummy
import timer


class ExperimentalLoop:
    def __init__(self):
        self.list_of_devices = []
        self.commands = []

    def loop(self):
        if len(self.commands) > 0:
            self.parse(self.commands[0])
            self.commands.pop(0)
            self.loop()
        return None

    def parse(self, command):
        dictionary = {
            self.list_of_devices[j][0]: self.list_of_devices[j][1]
            for j in range(0, len(self.list_of_devices))
        }
        print(dictionary["timer"].time_elapsed())
        dictionary[command[0]].parse(command[1])
        return None

    def add_device(self, label, device):
        self.list_of_devices.append((label, device))

    def __str__(self):
        string_rep = "Experimental loop \n List of devices: \n"
        string_rep += self.list_of_devices.__str__() + "\n list of commands"
        string_rep += self.commands.__str__()
        return string_rep


if __name__ == "__main__":
    el = ExperimentalLoop()
    el.add_device("dummy", dummy.Dummy())
    el.list_of_devices[0][1].init()
    el.add_device("timer", timer.TimeManager())
    for i in range(10):
        el.commands.append(("timer", "wait 110"))
        el.commands.append(("timer", "wait 110"))
        el.commands.append(("dummy", "echo teststring"))
    # print(el)
    el.loop()
