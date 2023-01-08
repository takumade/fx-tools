from data.tools_list import tools_list
from classes.Help import Help


help = Help()

class Interactive:
    def __init__(self) -> None:
        pass
    
    
    def get_input(self):
        user_input = input("fx-tools> ")
        return user_input


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
        exit_list = ["exit", "bye", "XXX", "exit()"]
        
        try:
            while exit_list.count(user_input) == 0:
                user_input = self.get_input()
                
                if user_input == 'help':
                    help.fx_help()
            
            print("bye bye!")
        except KeyboardInterrupt:
            print("bye bye!")
