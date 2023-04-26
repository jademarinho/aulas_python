with open('etapa-4.txt', 'w') as file:
    with open('actors.csv', 'r') as data_file:
        lines = data_file.readlines()
        # Troca o nome do IronMan
        lines = [line.replace('"Robert Downey, Jr."', 'Roberts Downey Jr.') for line in lines]
        headers = lines[0].strip().split(',')
        data = []
        for line in lines[1:]:
            fields = line.strip().split(',')
            row = dict(zip(headers, fields))
            data.append(row)

        count_pop_movie = {}
        for row in data:
            if row['#1 Movie'] in count_pop_movie:
                count_pop_movie[row['#1 Movie']] += 1
            else:
                count_pop_movie[row['#1 Movie']] = 1

        pop_movie = max(count_pop_movie, key=count_pop_movie.get)
        num_pop_movie = count_pop_movie[pop_movie]

        result = f'{pop_movie}: {num_pop_movie}\n'
        file.write(result)
        print(result)
