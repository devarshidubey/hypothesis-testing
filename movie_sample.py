import csv
import random

def select_random_movies1(csv_file, num_movies): #return the list of random movies
    selected_ids = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader:
                if int(row[1]) < 2000:
                    selected_ids.append(int(row[0]))

    except StopIteration:
        pass
    
    random_selected_ids = random.sample(selected_ids, num_movies)

    
    
    return random_selected_ids

def select_random_movies2(csv_file, num_movies): #return the list of random movies
    selected_ids = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader:
                if int(row[1]) >= 2000:
                    selected_ids.append(int(row[0]))

    except StopIteration:
        pass
    
    random_selected_ids = random.sample(selected_ids, num_movies)
    
    return random_selected_ids
