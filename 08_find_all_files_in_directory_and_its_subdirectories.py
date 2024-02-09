"""
Finding the second maximum number in the list (taking into account that there may be several maximum numbers if they are equal).
"""

from pathlib import Path
from typing import Iterator, List

def find_all_files_in_directory_and_its_subdirectories(directory_to_search_for: str) -> List[str]:
    # using the '**/*' template allows to perform a full recursive search 
    # of all files and directories in the directory hierarchy, including 
    # all subdirectories and their contents
    file_and_directory_generator = Path(directory_to_search_for).glob('**/*')
    resulting_list_of_file_names = []
    return find_all_files_recursion(file_and_directory_generator, resulting_list_of_file_names)

def find_all_files_recursion(file_and_directory_generator: Iterator[Path], 
                             resulting_list_of_file_names: List[str],
                            ) -> List[str]:
    current_file_or_directory = next(file_and_directory_generator, None)
    if current_file_or_directory == None:
        return resulting_list_of_file_names
    if current_file_or_directory.is_file():
        resulting_list_of_file_names.append(current_file_or_directory.name)
    return find_all_files_recursion(file_and_directory_generator, resulting_list_of_file_names)
