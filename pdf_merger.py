"""
PDF Merger Tool
A command-line utility to merge multiple PDF files into one.
"""

import os
from PyPDF2 import PdfMerger


def get_directory():
    """
    Ask user for directory path containing PDFs.
    
    Returns:
        str: The directory path (current directory if user presses Enter)
    
    TODO:
    - Prompt user: "Enter directory path (or press Enter for current directory): "
    - If user presses Enter, return current directory using os.getcwd()
    - Otherwise, return the path they entered
    - Strip any extra whitespace from input
    """
    directory = input("Enter directory path (or press Enter for current directory): ").strip()
    if directory == "":
        return os.getcwd()
    else:
        return directory  


def find_pdf_files(directory):
    """
    Find all PDF files in the specified directory.
    
    Args:
        directory (str): Path to directory to search
        
    Returns:
        list: List of PDF filenames (just names, not full paths)
        
    TODO:
    - Use os.listdir() to get all files in directory
    - Filter for files ending with '.pdf' (case-insensitive)
    - Sort the list alphabetically
    - If no PDFs found, print error and return empty list
    """
    pass


def display_and_select_files(pdf_list):
    """
    Display PDFs to user and get their selection order.
    
    Args:
        pdf_list (list): List of PDF filenames
        
    Returns:
        list: List of selected filenames in user's chosen order
        None: If user input is invalid
        
    TODO:
    - Display numbered list: "1. filename.pdf"
    - Ask user to enter numbers in order (e.g., "1 3 2")
    - Parse their input (split by spaces, convert to integers)
    - Validate:
        * All numbers are valid indices
        * No duplicates (optional - or allow duplicates?)
    - Return list of filenames in selected order
    - Handle errors (invalid numbers, non-numeric input)
    """
    pass


def get_output_filename(directory):
    """
    Get output filename from user and handle if file exists.
    
    Args:
        directory (str): Directory where output will be saved
        
    Returns:
        str: Full path to output file
        None: If user cancels
        
    TODO:
    - Ask user for output filename
    - If they don't include .pdf extension, add it
    - Create full path: os.path.join(directory, filename)
    - Check if file exists using os.path.exists()
    - If exists:
        * Ask: "File exists. Overwrite? (y/n): "
        * If no, ask for new filename (loop back)
        * If yes, return the path
    - Return the full output path
    """
    pass


def merge_pdfs(file_paths, output_path):
    """
    Merge PDF files into a single output file.
    
    Args:
        file_paths (list): List of full paths to PDF files to merge
        output_path (str): Full path where merged PDF will be saved
        
    Returns:
        bool: True if successful, False if error occurred
        
    TODO:
    - Create a PdfMerger object
    - Loop through file_paths with enumerate to show progress
        * Print: "Merging file X of Y: filename"
        * Use merger.append(filepath)
        * Wrap in try-except to catch corrupted files
        * If error, print which file failed and why
    - After loop, write merged PDF: merger.write(output_path)
    - Close the merger: merger.close()
    - Print success message
    - Return True if successful, False if any errors
    
    HINTS for PyPDF2:
    - Create merger: merger = PdfMerger()
    - Add file: merger.append(filepath)
    - Save: merger.write(output_path)
    - Clean up: merger.close()
    """
    pass


def main():
    """
    Main function that orchestrates the entire program.
    
    TODO:
    - Print welcome message
    - Call get_directory() to get working directory
    - Call find_pdf_files() to get list of PDFs
    - If no PDFs found, exit
    - Call display_and_select_files() to get user's selection
    - If selection is invalid, exit
    - Build full file paths by joining directory with filenames
    - Call get_output_filename() to get output path
    - If user cancels, exit
    - Call merge_pdfs() to do the actual merging
    - Print final success/failure message
    """
    pass


if __name__ == "__main__":
    test_dir = get_directory()
    print(f"Directory selected: {test_dir}")
