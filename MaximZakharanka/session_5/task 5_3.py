import csv
def get_top_performers(file_path, number_of_top_students=5):
    top_names = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            top_names.append(row)
        top_names.sort(key = lambda i: i[2], reverse = True)
        print([i[0] for i in top_names[1:number_of_top_students+1]])

def top_age_students(file_path):
    top_ages = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            top_ages.append(row)
        top_ages.sort(key = lambda i: i[1], reverse = True)
    with open('data/students_age.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter = ',')
        for line in top_ages:
            writer.writerow(line)
                        
get_top_performers('data/students.csv')
top_age_students('data/students.csv')
