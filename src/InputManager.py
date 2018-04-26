from IPScope import IPScope

class InputManager():

    @classmethod
    def handleInput(cls, caseToHandle):

        if (caseToHandle == "1"):
            IPScope.displayIPScopeTable()

        elif (caseToHandle == "2"):
            IPScope.insertScope()

        elif (caseToHandle == "3"):
            IPScope.updateScope()

        elif (caseToHandle == "4"):
            IPScope.displayIPScopeTable()

            scopeToDelete = input("Select ScopeID to delete: ")

            ipScope = IPScope(scopeToDelete)
            ipScope.displayIPScopeTable()
            ipScope.deleteScope(scopeToDelete)


        


