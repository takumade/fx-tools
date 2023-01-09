from data.tools_list import tools_list
from classes.Help import Help
from classes.Calculations import Calculations


help = Help()

class Interactive:
    def __init__(self) -> None:
        self.exit_list = ["exit", "bye", "XXX", "exit()"]
        self.user_input = ""
        self.fx_calcs = Calculations()
    
    
    
    def process_input(self):
        
        if self.user_input.lower() == "list tools":
            help.list_tools()
        
        if self.user_input.lower() == "getall vars":
            self.fx_calcs.get_all_vars()
        
        if self.user_input.lower() == "help":
            help.fx_help()
            
        if self.user_input.lower().startswith("help tool"):
            try:
                tool_name = self.user_input.lower().split()[-1]
                help.tool_help(tool_name)
            except IndexError:
                print("[-] Please enter tool name e.g tool help fly")
                
        if self.user_input.lower().startswith("set "):
            try:
                key = self.user_input.lower().split()[1]
                value = self.user_input.lower().split()[2]
                self.fx_calcs.set_variable(key, value)
                print("[i] {0}: {1}".format(key, self.fx_calcs.get_variable(key)))
            except (IndexError, ValueError):
                print("[-] Please enter variable name e.g set cats 3")
        
        if self.user_input.lower().startswith("get "):
            try:
                key = self.user_input.lower().split()[1]
                value = self.fx_calcs.get_variable(key)
                print("[i] {0}: {1}".format(key, value))
            except (IndexError, ValueError):
                print("[-] Please enter variable name e.g set cats 3")
            except KeyError:
                print("[i] Variable not set!")
        
        if self.user_input.lower().startswith("run "):
            try:
                tool_name = self.user_input.lower().split()[1]
                self.run_tool(tool_name)
            except IndexError:
                print("[-] Please enter tool name e.g run kill_mouse")  
            
            
    def run_tool(self, tool_name):
        print("RUNNING ", tool_name)
        if tool_name == "loss":
            pips,loss = self.fx_calcs.calculate_loss()
            print("PIPS: ",pips)
            print("LOSS: ${0}".format(loss))
        elif tool_name == "profit":
            pips,profit = self.fx_calcs.calculate_profit()
            print("PIPS: ",pips)
            print("PROFIT: ${0}".format(profit))
            
        print("")
        
        
    
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
       """)
        print("       =[ fx-tools v1.0.0                                  ]")                                                          
        print("+ -- --=[ {0} tools                                          ]".format(len(tools_list.keys())))   

        
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
