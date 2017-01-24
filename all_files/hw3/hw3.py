#---------------------------------------------------------
# Nia Vivekanandan
# niavivek@berkeley.edu
# Homework #3
# September 20, 2016
# hw3.py
# Main
#---------------------------------------------------------

from BST import *
#function to read a file and tokenize it
def read_file(filename):
   #try-except to throw exception if any error in reading the file
    try:
        with open(filename, 'rU') as document:
            text = document.read()
    except:
        print("Error reading file. Try again.")
        return
    #tokenize the words in the file by converting it into lower case and removing punctuations
    filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
    words = [x for x in map(filter_punc, text.split()) if x]
    return words
#function to prompt user to enter word to find in the tree, print stats and to terminate the query
def prompt_user(tree):
    input_word = ""#initialize word to empty string
    #while terminate is not yet typed
    while(input_word != "terminate"):
        #get input from user
        try:
            input_word = input("Query? ")
        except:
            print("Program interrupted.")
            #break out of the program if ctrl-C is typed or other exception during input is encountered
            break
        #if stats is typed - print the height and number of entries in the tree
        if(input_word == "stats"):
            print("Number of entries in the tree: ",tree.size())
            print("Maximum depth of the tree: ",tree.height())
        #if terminate is typed- end program
        elif(input_word == "terminate"):
            break
        #else - find the word in the tree, and print it's count
        else:
            word,count = tree.find(input_word)
            print("The word {} appears {} times in the tree.".format(word,count))


def main():
    #continue prompting for file name, till a valid file with entries is entered
    while(True):
        print("Enter the file name to read:")
        #exception for any interruption
        try:
            #get input file name from user
            filename = input('> ')
        except:
            print("Program interrupted.")
            return
        #exception when reading file
        try:
            words = read_file(filename)
        except IOError:
            print("Unable to find the file {}".format(filename))
        #if no exception - check if file is empty
        else:
            #if file is empty of has no words - prompt for another filename
            if(words == None or len(words) == 0):
                print("File is empty. Enter the name of another file to read.")
                continue
            #initialize a new tree
            try:
                tree = BSTree()
                #add the words to the tree
                for word in words:
                    tree.add(word)
                break
            #exception when adding the words
            except:
                print("Error. Try again.")
                continue
    #after adding words - prompt user for query
    prompt_user(tree)
    ######################
    # Begin Student Code #
    ######################
    #Functions for use
    # tree.add(word)
    #print(tree.find(word))
    # tree.size()
    # tree.height()
    # tree.inOrderPrint()


if __name__ == "__main__":
    main()