from data.tools_list import tools_list

class Help:
    def __init__(self) -> None:
        pass
    
    def fx_help(self):
        
        help = {
            "list tools": "List all tools",
        "help tool <tool>": "Get tool help",
        "set <var> <value>": "Set a variable",
        "get <var>": "Get a variable",
        "getall vars": "Get all variables",
        "del <var>": "Delete a variable",
        "exec <tool>": "Execute a tool",
         "exit, exit(), XXX": "Exit"
        }
        
        print("Help: \n")
        
        for k in help.keys():
            print("{0:30s}  - {1}".format(k, help[k]))
        
    
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
            print("")
            
        except ValueError:
            print("[-] Tool doesnt exit")
   
    
    
    