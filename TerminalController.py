"""
File: TerminalController.py
Author: J. McPolin
Date: Oct. 6 2024
Description: This file contains method stubs to create a project
that replicated the behaviour of a computer terminal in a
choose your own adventure style game.
"""

# built-in library with functions to interact with the operating system
import os

# built-in library with functions for using JSON files
import json

# Set the initial directory
initialDirectory = "GameStart"

# Add your function header here (this explains what your func does)
def LoadJsonMessage(fileName):
    """
    This function should:
    - Take the path of the JSON as a parameter called fileName
    - Open the file
    - Read the file and display the message to the user
    """
    return #placeholder, you will need to change this

# Add your function header here
def ListFiles():
    """
    This function should:
    - Get all the files in the current directory
    - JSON files should not be listed (to keep the story a mystery), only the folders
    - Print the list of files to the user for selection
    - Handle any potential errors if the directory cannot be accessed
    """
    return #placeholder, you will need to change this

# Add your function header here
def ChangeDirectory(directoryName):
    """
    This function should:
    - Take a directory name as a parameter called directoryName
    - Check if the specified directory exists in the current path
    - If the directoryName is "..", change the current working directory to the parent directory
    - Otherwise, change to the specified directory if it exists
    - Handle any potential errors if the directory cannot be accessed
    """
    return #placeholder, you will need to change this

# Add your function header here
def main():
    """
    This function should:
    - Initialize the game by setting the current directory to initialDirectory
    - Continuously prompt the user for commands until they choose to exit
    - Parse user input
    - Call the appropriate functions based on user input (e.g., ListFiles, ChangeDirectory, LoadJsonMessage)
    - Handle invalid commands and provide feedback to the user
    - Users must be able to exit / reset the game
    """
    return #placeholder, you will need to change this

main()