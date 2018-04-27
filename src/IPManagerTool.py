from IPAddress import IPAddress
from IPScope import IPScope
from InputManager import InputManager

class IPManagerTool():
    
    addressManager = IPAddress()
    scopeManager = IPScope()

    @classmethod
    def start(cls):

        print("Welcome to IP Scope Management Services!")
        print()
        done = False

        while(not done):
            
            print("Do you want to manage IP addresses or IP scopes?")
            print("Select an option below:")
            print("1: IP Addresses")
            print("2: IP Scope")
            print("Type q to quit this program")

            caseToUse = input("Select a number: ")

            if(caseToUse == "1"):
                InputManager.handleInput(cls.addressManager)

            elif(caseToUse == "2"):
                InputManager.handleInput(cls.scopeManager)

            elif(caseToUse == "q"):
                done = True
                print("Quitting program...")
                
            else:
                print()
                print("Please add valid input!")

            print()