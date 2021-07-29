import serial

class serialCommunication:
    _rate = 9600

    def __init__(self, path):
        self._path = path


    def serial_connect(self):
        return serial.Serial(self._path, self._rate)

class Data:
    def __init__(self):
        pass
        
    

def main():
    pass

if __name__ == '__main__':
    main()
