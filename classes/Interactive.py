from data.tools_list import tools_list
from classes.Help import Help


help = Help()

class Interactive:
    def __init__(self) -> None:
        self.exit_list = ["exit", "bye", "XXX", "exit()"]
        self.user_input = ""
    
    
    
    def process_input(self):
        
        if self.user_input.lower() == "list tools":
            help.list_tools()
        
        if self.user_input.lower() == "help":
            help.fx_help()
            
        if self.user_input.lower().startswith("tool help"):
            try:
                tool_name = self.user_input.lower().split()[-1]
                help.tool_help(tool_name)
            except IndexError:
                print("[-] Please enter tool name")
    
    
    def get_input(self):
        self.user_input = input("fx-tools> ")



    def start(self):
        print("""
            
    ███████╗██╗  ██╗  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██╔════╝╚██╗██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    █████╗   ╚███╔╝█████╗██║   ██║   ██║██║   ██║██║     ███████╗
    ██╔══╝   ██╔██╗╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║     ██╔╝ ██╗     ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝     ╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                            
        =[ fx-tools v1.0.0                                  ]                                                          
    + -- --=[ {0} tools                                          ]   
        """.format(len(tools_list.keys())))
        
        user_input = ""
       
        
        try:
            while self.exit_list.count(user_input) == 0:
                self.get_input()
                
                if self.exit_list.count(self.user_input) > 0:
                    break 
                
                self.process_input()
                
            
            print("bye bye!")
        except KeyboardInterrupt:
            print("bye bye!")
