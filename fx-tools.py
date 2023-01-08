# CLI MODE  


# Steps 
# 1. Parse arguments from command line
# 2. Process the commands
# 3. Show the result to the user
# Prompt: fx-tools>
import argparse


def fx_help():
    print("""Help
          
list tools           - List all tools
set <var> <value>    - set a variable
get <var>            - get a variable
del <var>            - delete a variable
exec <tool>          - execute a tool
exit, exit(), XXX    - Exit.
          """)

def parse_arguments():
    parser = argparse.ArgumentParser(description ="Tools for trading Deriv's Synthentic Indices. Written in Python")
    parser.add_argument('-i', '--interactive',
                        action ='store_true',
                        help ='Run in interactive mode')
    args = parser.parse_args()
    
    if (args.interactive):
        interactive()
    else:
        parser.print_help()




def get_input():
    user_input = input("fx-tools> ")
    return user_input


def interactive():
    print("""
          
███████╗██╗  ██╗  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝╚██╗██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
█████╗   ╚███╔╝█████╗██║   ██║   ██║██║   ██║██║     ███████╗
██╔══╝   ██╔██╗╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
██║     ██╔╝ ██╗     ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝     ╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                           
       =[ fx-tools v1.0.0                                  ]                                                          
+ -- --=[ 5 tools                                          ]   
    """)
    
    user_input = ""
    exit_list = ["exit", "bye", "XXX", "exit()"]
    
    try:
        while exit_list.count(user_input) == 0:
            user_input = get_input()
            
            if user_input == 'help':
                fx_help()
        
        print("bye bye!")
    except KeyboardInterrupt:
        print("bye bye!")

    
if __name__ == '__main__':
    parse_arguments()
