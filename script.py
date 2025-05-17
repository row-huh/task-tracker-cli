import argparse


def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool")

    parser.add_argument('--addTask', type=str, help='Use this flag along with a string to add a new task!')
    parser.add_argument('--deleteTask', type=int, help='Enter an existing id of a task to delete it')

    parser.add_argument('--listAll', type="None", help='Lists all existing items in the task list')

    # separate functions 