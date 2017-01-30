import sys
sys.dont_write_bytecode = True


def find_char(string, char): 
  comment = string[:1]
  if comment is char:
    return -1
  else:
    pass


def string_corr(filename):
  print "Correcting string line breaks in " + filename
  file = open(filename,"r")
  lines = file.readlines()
  file.close()

  file = open(filename,"w")
  
  line_break = 0
  last_line = "last line"
  for line in lines:
    is_comment = find_char(line, '#')

    if is_comment != 0:
        
      if line_break > 0:
        line = last_line + line
      
      line_break = line.find("\\\n")
      
      if line_break > 0:
        last_line = line.replace("\\\n", " \" + \"")
        line_break = 1
      
      for x in range(0, 20):
        line = line.replace("  \" + \"", " \" + \"")
        line = line.replace("\" + \" ", "\" + \"")
      
      line = line.replace("^ \" + \"", "^\" + \"")
      line = line.replace("\" + \"", "\" + \n\"")

    if line_break < 1:
      line = line.strip()
      file.write("%s\n"%line)  
  file.close()

def line_corr(filename):
  print "Correcting lines in " + filename
  file = open(filename,"r")
  lines = file.readlines()
  file.close()

  file = open(filename,"w")

  level = 0
  for line in lines:
    line = line.strip()
    acceptableindex = find_char(line, '#')
    if (acceptableindex == -1):
        acceptableindex = len(line)
    level -= line.count("try_end", 0, acceptableindex)
    level -= line.count("end_try", 0, acceptableindex)
    level -= line.count("else_try", 0, acceptableindex)
    newlevel = level
    level_positive_change = 0
    newlevel += line.count("else_try", 0, acceptableindex)
    newlevel += line.count("(", 0, acceptableindex)
    newlevel += line.count("[", 0, acceptableindex)
    newlevel += line.count("try_begin", 0, acceptableindex)
    newlevel += line.count("(try_for", 0, acceptableindex)
    level_positive_change = newlevel - level
    newlevel -= line.count(")", 0, acceptableindex)
    newlevel -= line.count("]", 0, acceptableindex)
    if (level_positive_change == 0):
      level = newlevel
    for i in xrange(level):
      file.write("  ")
    level = newlevel
    file.write("%s\n"%line)
  file.close()



files_to_process = []




def print_menu():
    print "#####################################################"
    print "A note on syntax:"
    print "a) For files in the same directory, do not add any extra prefixes or the '.py'"
    print "    Example: module_troops"
    print "   Just like that."
    print " "
    print "b) for files in subdirectories, add the subdirectory with a '/' after to the beginning of the file name"
    print "    Example: if I had all move module files in a subdirectory MDL, I would put MDL/module_troops"
    print " "
    print "This applies for files defined inside line_correction.py, as well as for any that you input through this menu."
    print "#####################################################"
    print "1) Process files "
    print "2) Input a file to process"
    print "3) Print list of files "
    print "0) Exit"  


def process():

  legal_choices = set(["0","1","2","3","4"])
  choice =""
  print_menu()
  while choice != "0":
    choice =""
    while not choice in legal_choices:
            choice = raw_input("Make a choice (4 to display menu again) >").lower()

            if choice == '1':
              all_files = len(files_to_process)
              print "processing..."
              for n in range(0, all_files):
                line_corr(files_to_process[n] + ".py")

            elif choice == '2':
              try:
                response = raw_input('Input a file to process: ')
                line_corr(response + ".py")

              except:
                print "you fool"
                pass

            elif choice == '3':
              print "######## Files to be processed ########"
              print ""
              all_files = len(files_to_process)
              for n in range(0, all_files):
                print files_to_process[n]
                print ""


            elif choice == '4':
              print_menu()

if __name__ == '__main__':
  process()













    
