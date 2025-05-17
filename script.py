import argparse



def addItem(item):
    '''Function to handle adding new item into the lst'''
    #TODO


def deleteItem(itemID):
    '''Function to delete any item given its id'''
    #TODO


def listAllItems():
    '''lists all existing items along with their ids'''
    #TODO


def nextTask():
    '''Show the next task on the list(usually the first task)
    Maybe use cowsay coz ive waited my entire life to use that library'''
    #TODO


def main():

    #main parser
    parser = argparse.ArgumentParser(description='CLI tool to keep track of your immediate cli tasks')

    subparsers = parser.add_subparsers(dest='command', help='commands to run')

    add_parser = subparsers.add_parser('addItem', help='command to add items to the list')

    add_parser.add_argument('addItem', type=str, help='Use this flag along with a string to add a new task!')


    delete_parser = subparsers.add_parser('deleteItem', help='delete items from list')
    delete_parser.add_argument('deleteItem', type=int, help='enter id of the item to be deleted along with the flag')


    # listAllItems = subparsers.add_parser()
    # add in arguments to list item
    # maybe add in some sorting or grep like thingy
    # like get all items with a string in them etc etc


    # separate functions for each 

    args = parser.parse_args()


    if args.command == 'addItem':
        print('function called here')
        addItem(args.name, args.count)


if __name__ == '__main__':
    main()
