#import pypng
import pyqrcode

def main():
    """ Main entry point of the app """
    Wifi_Name = ''
    Wifi_Protocol = 'WPA/WPA2'
    Wifi_Password = ''
    QRCode = pyqrcode.create(F'WIFI:S:{Wifi_Name};T:{Wifi_Protocol};P:{Wifi_Password};;')
    
    # Generate image
    #QRCode.svg('QRCode.svg', scale=4)
    QRCode.eps('QRCode.eps', scale=6)
    #print(QRCode.terminal(quiet_zone=1))
    #QRCode.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    #QRCode.show()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()