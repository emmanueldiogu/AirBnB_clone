import cmd

class HBNBCommand(cmd.Cmd):
     prompt = '(hbnb) '

      def do_quit(self, arg):
           """Exit the program"""
           return True

    def do_EOF(self, arg):
         """Exit the program"""
         return True

     def emptyline(self):
         """Display help message for quit command"""
         print("Exit the program")

    def help_EOF(self):
        """Display help message for EOF command"""
        print("Exit the program")

    def help_help(self):
        """Display help message for help command"""
        print("Display available commands")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
