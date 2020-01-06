def inside_contest(faculty, file_name):
    f = open(file_name, 'r')
    voted_ids = []
    scores = {}
    for line in f:
        split_line = line.split()
        if split_line[0] != "staff":
            continue
        if split_line[len(split_line)-1] != faculty:
            continue
        scores[split_line[2]] = 20
        for program_index in range(3, len(split_line)-2):
            scores[split_line[program_index]] = 0
    for line in f:
        split_line = line.split()
        if split_line[0] != "inside" \
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
    return current_max_key


print(inside_contest("CS", "input.txt"))








