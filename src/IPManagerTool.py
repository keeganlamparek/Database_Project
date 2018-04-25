from InputManager import InputManager

class IPManagerTool():
    
    @classmethod
    def start(cls):
        
        print("Welcome to IP Scope Management Services!")
        print()
        done = False

        while(not done):
            
            print("Select an option below:")
            print("1: Display all IP scopes")
            print("2: Insert new scope")
            print("3: Update scope")
            print("4: Delete a scope")
            print("Type q to quit this program")

            caseToUse = input("Select a number: ")

            if(caseToUse == "q"):
                done = True
                print("Quitting program...")
            else:
                InputManager.handleInput(caseToUse)
            print()