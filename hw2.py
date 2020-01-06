import Techniovision


def inside_contest(faculty, file_name):
    f = open(file_name, 'r')
    voted_ids = []
    scores = {}
    for line in f:
        split_line = line.split()
        if split_line[0] != 'staff':
            continue
        if split_line[len(split_line)-1] != faculty:
            continue
        scores[split_line[2]] = 20
        for program_index in range(3, len(split_line)-2):
            scores[split_line[program_index]] = 0
    for line in f:
        split_line = line.split()
        if split_line[0] != 'inside' \
                or split_line[4] != faculty \
                or split_line[2] in voted_ids:
            continue

        voted_ids.append(split_line[2])
        current_program = split_line[3]
        if current_program in scores:
            scores[current_program] += 1
    current_max_key = list(scores.keys())[0]
    current_max_value = scores[current_max_key]
    for key, value in scores.items():
        if value > current_max_value:
            current_max_key = key
            current_max_value = value
    f.close()
    return current_max_key


techniovision = Techniovision.TechniovisionCreate()
f = open('input.txt', 'r')
print(inside_contest('CS', 'input.txt'))
contesting_programs = {}
for line in f:
    split_line = line.split()
    if split_line[0] != 'staff':
        continue
    current_faculty = split_line[len(split_line)-1]
    winning_program = inside_contest(current_faculty, 'input.txt')
    contesting_programs[winning_program] = current_faculty

for line in f:
    split_line = line.split()
    #if split_line[0] != 'techniovision':
    #    continue
    current_id = int(split_line[1])
    print(split_line + "\n")
    #Techniovision.TechniovisionStudentVotes(techniovision, )
f.close
Techniovision.TechniovisionDestroy(techniovision)








