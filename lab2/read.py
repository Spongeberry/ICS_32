from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    # TODO: Complete the function
    with open (file, 'r') as csvfile1:
        filedata = []
        csvread = csv.reader(csvfile1)
        for row_num, row in enumerate(csvread):
            if row_num == 0 and (row[0] != "City" or row[1] != "Team Name" or row[2] != "Sport"):
                raise ValueError
            if len(row) != 3:
                raise ValueError
            if row[0] == "" or row[1] == "" or row[2] == "": 
                raise ValueError
            if row_num > 0:
                filedata.append(tuple(row))
    return filedata  # erase this


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    # TODO: Complete the function
    p = Path(".").glob("*.csv")
    filecount = 0
    linecount = 0
    unique_list = []
    errorfile = []
    for file in p:
        filecount += 1
        try:
            for row in readFile(file):
                linecount += 1
                club = SportClub(row[0], row[1], row[2], 0)
                if club not in unique_list:
                    unique_list.append(club)
                for clubs in unique_list:
                    if club == clubs:
                        clubs.count += 1
        except ValueError:
            errorfile.append(file.name)
            filecount -= 1
            
    with open('error_log.txt', 'w') as errorlog:
        for file in errorfile:
            errorlog.write(f'{str(file)}\n')

    with open('report.txt', 'w') as reports:
        reports.write(f'Number of files read: {filecount}\n')
        reports.write(f'Number of lines read: {linecount}\n')
    return unique_list  # erase this
