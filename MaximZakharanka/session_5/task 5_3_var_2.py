def get_top_performers(file_path, number_of_top_students=5):
    top_names = []
    with open(file_path, 'r') as file:
        for row in file:
            words = row.split(',')
            words[2] = words[2].rstrip('\n')
            top_names.append((words[0], words[1], words[2]))
        top_names.sort(key = lambda i: i[2], reverse = True)
        print([i[0] for i in top_names[1:number_of_top_students+1]])

def top_age_students(file_path):
    top_ages = []
    with open(file_path, 'r') as file:
        for row in file:
            words = row.split(',')
            words[2] = words[2].rstrip('\n')
            top_ages.append((words[0], words[1], words[2]))
        top_ages.sort(key = lambda i: i[1], reverse = True)
    with open('data/students_age_var_2.csv', 'w', newline='') as f:
        for line in top_ages:
            f.write(",".join(line)+'\n')
                        

get_top_performers('data/students.csv')
top_age_students('data/students.csv')
