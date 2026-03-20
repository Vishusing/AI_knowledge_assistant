"""
AI Knowledge Assistant
Main controller file

This file provides a simple menu to:
1 Build database
2 Ask questions
"""

from scripts.build_db import build
from scripts.ask import ask


def main():

    while True:

        print("\nAI Knowledge Assistant")

        print("\nSelect option:")

        print("1 -> Build Vector Database")

        print("2 -> Ask Questions")

        print("3 -> Exit")

        choice = input("\nEnter choice: ")


        if choice == "1":

            print("\nBuilding database...\n")

            build()


        elif choice == "2":

            print("\nStarting assistant...\n")

            ask()


        elif choice == "3":

            print("\nExiting...")

            break


        else:

            print("\nInvalid choice")


if __name__ == "__main__":

    main()