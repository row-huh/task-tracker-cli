import argparse
import csv


FILENAME = 'tasks.csv'

def addItem(arg):
    '''Function to handle adding new item into the lst'''
    item = arg.addItem

    last_id = int(get_last_row_id())
    new_id = last_id + 1

    # read all existing rows (there's no append thing - writer will start writing from line 1)
    with open(FILENAME, 'r') as csv_file:
        reader = csv.reader(csv_file)
        all_rows = list(reader)

    # write all existing rows first, then add the new row
    with open(FILENAME, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(all_rows)
        writer.writerow((new_id,item)) 


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
        addItem(args)


def get_last_row_id():
    file_path = 'tasks.csv'

    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)

            if rows:
                row = rows[-1]
                id = row[0]
                print(id)
                return id
            else:
                return -1
            
    except FileNotFoundError:
        raise Exception("Error: File not found at path")
    except Exception as e:
        raise Exception("An error occurred: {e}")


if __name__ == '__main__':
    main()
