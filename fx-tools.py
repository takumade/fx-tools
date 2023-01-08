# CLI MODE  


# Steps 
# 1. Parse arguments from command line
# 2. Process the commands
# 3. Show the result to the user
# Prompt: fx-tools>
import argparse
from classes.Interactive import Interactive





def parse_arguments():
    parser = argparse.ArgumentParser(description ="Tools for trading Deriv's Synthentic Indices. Written in Python")
    parser.add_argument('-i', '--interactive',
                        action ='store_true',
                        help ='Run in interactive mode')
    args = parser.parse_args()
    
    if (args.interactive):
        interactive_mode = Interactive()
        interactive_mode.start()
    else:
        parser.print_help()





    
if __name__ == '__main__':
    parse_arguments()
