from data.tools_list import tools_list

class Help:
    def __init__(self) -> None:
        pass
    
    def fx_help(self):
        print("Help\n\n" +
            
        "list tools           - List all tools\n"+
        "help <tool>          - Get tool help\n"+
        "set <var> <value>    - set a variable\n"+
        "get <var>            - get a variable\n"+
        "del <var>            - delete a variable\n"+
        "exec <tool>          - execute a tool\n"+

        "exit, exit(), XXX    - Exit.\n")
        
        
    def tool_help(self, tool_name):
        
    
    
    