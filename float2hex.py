import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import struct

class FloatToHexConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.inputLabel = QLabel('Enter a double or hex:')
        layout.addWidget(self.inputLabel)

        self.inputField = QLineEdit()
        layout.addWidget(self.inputField)

        self.floatButton = QPushButton('Convert to Float Hex')
        self.floatButton.clicked.connect(self.convert_to_float_hex)
        layout.addWidget(self.floatButton)

        self.doubleButton = QPushButton('Convert to Double Hex')
        self.doubleButton.clicked.connect(self.convert_to_double_hex)
        layout.addWidget(self.doubleButton)

        self.convertHexToFloatButton = QPushButton("Convert Hex to Float/Double", self)
        self.convertHexToFloatButton.clicked.connect(self.convert_hex_to_double)
        layout.addWidget(self.convertHexToFloatButton)

        self.resultLabel = QLabel('Result:')
        layout.addWidget(self.resultLabel)

        self.resultField = QLineEdit()
        self.resultField.setReadOnly(True)
        layout.addWidget(self.resultField)

        self.setLayout(layout)
        self.setWindowTitle('Float/Double and Hex Converter')
        self.show()

    def convert_to_float_hex(self):
        try:
            float_value = float(self.inputField.text())
            packed_value = struct.pack('!f', float_value)
            hex_value = packed_value.hex()
            self.resultField.setText(hex_value)
        except ValueError:
            self.resultField.setText('Invalid input')

    def convert_to_double_hex(self):
        try:
            double_value = float(self.inputField.text())
            packed_value = struct.pack('!d', double_value)
            hex_value = packed_value.hex()
            self.resultField.setText(hex_value)
        except ValueError:
            self.resultField.setText('Invalid input')

    def convert_hex_to_double(self):
        try:
            hex_value = self.inputField.text()
            # Convert hex string to bytes
            byte_value = bytes.fromhex(hex_value)
            # Unpack bytes to double precision float
            float_value = struct.unpack('!d', byte_value)[0]
            self.resultField.setText(str(float_value))
        except ValueError:
            self.resultField.setText('Invalid input')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FloatToHexConverter()
    sys.exit(app.exec_())
    print("finished")
