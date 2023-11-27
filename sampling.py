import csv
import random
import math
import movie_sample as movies
import pandas as pd


def read_csv_file_dataset(filename, random_cluster):
    data = []
    current_group = None    
    with open(filename, 'r') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')
        
        for row in csvreader:
            if row[0][-1]==':' and int(row[0][:-1]) in random_cluster:
                current_group = int(row[0][:-1])
                continue
            if row[0][-1]==':' and int(row[0][:-1]) not in random_cluster:
                current_group = None

            if current_group is not None:
                name = row[0].strip()
                rating = int(row[1])
                date = str(row[2])
                data.append({
                    "Group": current_group,
                    "Name": name,
                    "Rating": rating,
                    "Date": date
                })

    return data

def get_sample(filename, random_cluster, sample_size): #returns a list of user ratings under the given cluster of movies
    data = []
    current_group = None    
    with open(filename, 'r') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')
        
        for row in csvreader:
            if row[0][-1]==':' and int(row[0][:-1]) in random_cluster:
                current_group = int(row[0][:-1])
                continue
            if row[0][-1]==':' and int(row[0][:-1]) not in random_cluster:
                current_group = None

            if current_group is not None:
                rating = int(row[1])
                data.append(rating)

        random_data = random.sample(data, sample_size)
    return random_data

def population_mean1(): #average ratings for movies before year 2000
    random_movies = movies.select_random_movies1('movie_titles.csv', 100) #choose 100 random movies
    dataset = read_csv_file_dataset(filename = 'combined_data_1.csv', random_cluster= random_movies) #return a list of dictionaries containing the ratings, group
    sample_distribution = []
    current_group = dataset[0]['Group']
    mean = 0
    count = 0
    for data in dataset:
        if data['Group'] == current_group:
            mean+=data['Rating']
            count+=1
        else:
            sample_distribution.append(mean/count)
            mean = 0
            count = 0
            current_group = data['Group']
    return sum(sample_distribution)/len(sample_distribution)

def population_mean2(): #average ratings for movies before year 2000
    random_movies = movies.select_random_movies2('movie_titles.csv', 100) #choose 100 random movies
    dataset = read_csv_file_dataset(filename = 'combined_data_1.csv', random_cluster= random_movies) #return a list of dictionaries containing the ratings, group
    sample_distribution = []
    current_group = dataset[0]['Group']
    mean = 0
    count = 0
    for data in dataset:
        if data['Group'] == current_group:
            mean+=data['Rating']
            count+=1
        else:
            sample_distribution.append(mean/count)
            mean = 0
            count = 0
            current_group = data['Group']
    return sum(sample_distribution)/len(sample_distribution)

def population_variance1(pop_mean):
    random_movies = movies.select_random_movies1('movie_titles.csv', 100) #choose 100 random movies
    dataset = read_csv_file_dataset(filename = 'combined_data_1.csv', random_cluster= random_movies)
    sample_distribution = []
    current_group = dataset[0]['Group']
    variance_estimator = 0
    count = 0
    for data in dataset:
        if data['Group'] == current_group:
            variance_estimator+=math.pow(data['Rating']-pop_mean, 2)
            count+=1
        else:
            sample_distribution.append(variance_estimator/count)
            variance_estimator = 0
            count = 0
            current_group = data['Group']

    return sum(sample_distribution)/len(sample_distribution)

def population_variance2(pop_mean):
    random_movies = movies.select_random_movies2('movie_titles.csv', 100) #choose 100 random movies
    dataset = read_csv_file_dataset(filename = 'combined_data_1.csv', random_cluster= random_movies)
    sample_distribution = []
    current_group = dataset[0]['Group']
    variance_estimator = 0
    count = 0
    for data in dataset:
        if data['Group'] == current_group:
            variance_estimator+=math.pow(data['Rating']-pop_mean, 2)
            count+=1
        else:
            sample_distribution.append(variance_estimator/count)
            variance_estimator = 0
            count = 0
            current_group = data['Group']
            
    return sum(sample_distribution)/len(sample_distribution)

def create_dataframe(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.endswith(':'):
                # Extract the movie_id from the line (assuming it's followed by a colon)
                movie_id = int(line.split(':')[0])
                
                # Extract lines until the next colon is encountered
                columns_lines = []
                for next_line in file:
                    next_line = next_line.strip()
                    if next_line.endswith(':'):
                        # If the next line starts with a new movie_id, break the loop
                        break
                    else:
                        # Split the line into a list, append the movie_id to each element, and join them back to a string
                        columns_lines.append(','.join([str(movie_id)] + next_line.split(',')))

                # Append the columns_lines to the data list
                data.extend([line.split(',') for line in columns_lines])

    df = pd.DataFrame(data, columns=['movieid', 'userid', 'rating', 'date'])
    df['rating'] = df['rating'].astype(int)

    return df