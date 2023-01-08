from data.tools_list import tools_list

class Help:
    def __init__(self) -> None:
        pass
    
    def fx_help(self):
        print("Help\n\n" +
            
        "list tools           - List all tools\n"+
        "help tool <tool>     - Get tool help\n"+
        "set <var> <value>    - set a variable\n"+
        "get <var>            - get a variable\n"+
        "del <var>            - delete a variable\n"+
        "exec <tool>          - execute a tool\n"+

        "exit, exit(), XXX    - Exit.\n")
        
    
    def list_tools(self):
        try:
            print("Available tools:\n")
            for t in tools_list.keys():
                print("- "+t)
        except:
            print("Error: ")
        
        
    def tool_help(self, tool_name):
        try: 
            tool = tools_list[tool_name]
            
            print("Tool Name: ", tool['name'])
            print("")
            print("Description:")
            print(tool['desc'])
            print("")
            print("Requires:")
            for r in tool['requires']:
                print("- " + r)
            
        except ValueError:
            print("[-] Tool doesnt exit")
   
    
    
    