import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    sport_dictionary = {}
    listA = []
    final_list = []
    unique_list = []
    for tuples in all_clubs:
        if tuples.sport not in sport_dictionary:
            sport_dictionary[tuples.sport] = []
        sport_dictionary[tuples.sport].append(tuples)
        listA.append(tuples.sport)
        unique_list = list(set(listA))
    for sports in unique_list:
        for k in sport_dictionary.keys():
            if k == sports:
                final_list.append(sport_dictionary[k])
    return final_list
        


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    sortSport = sorted(sport, key=lambda self: (-self.count, self.name), reverse=False)
    return sortSport


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    # TODO: Complete the function
    A = 0
    with open("survey_database.csv", "w") as csvfile:
        info = csv.writer(csvfile)
        info.writerow(['City','Team Name','Sport','Number of Times Picked'])
        for sports in sorted_sports:
            times = 1
            for sport1 in sports:
                if 1 <= times <= 3:
                    info.writerow([sport1.city,sport1.name,sport1.sport,str(sport1.count)])
                    times += 1
                else:
                    A = 0

                    

