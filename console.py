import cmd

class HBNBCommand(cmd.Cmd):
     prompt = '(hbnb) '

      def do_quit(self, arg):
           return True

    def do_EOF(self, arg):
         return True

     def emptyline(self):
         print("Exit the program")

    def help_EOF(self):
        print("Exit the program")

    def help_help(self):
        print("Display available commands")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
