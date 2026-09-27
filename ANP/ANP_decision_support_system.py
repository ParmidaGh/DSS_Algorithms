import numpy as np
import PySimpleGUI as sg

# Step 1: Get the main criteria from the user
layout = [
    [sg.Text('Enter the number of main criteria:'), sg.Input(key='num_main_criteria')],
    [sg.Button('Next')]
]

window = sg.Window('ANP Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Next':
        num_main_criteria = int(values['num_main_criteria'])
        break

window.close()

main_criteria = []
for i in range(num_main_criteria):
    layout = [
        [sg.Text(f'Enter the main criterion {i+1}:'), sg.Input(key=f'main_criterion{i+1}')],
        [sg.Button('Next')]
    ]

    window = sg.Window('ANP Calculator', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Next':
            criterion = values[f'main_criterion{i+1}']
            main_criteria.append(criterion)
            break

    window.close()

# Step 2: Get the sub-criteria for each main criterion from the user
sub_criteria = {}
for criterion in main_criteria:
    layout = [
        [sg.Text(f'Enter the number of sub-criteria for {criterion}:'), sg.Input(key=f'num_sub_criteria_{criterion}')],
        [sg.Button('Next')]
    ]

    window = sg.Window('ANP Calculator', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Next':
            num_sub_criteria = int(values[f'num_sub_criteria_{criterion}'])
            sub_criteria[criterion] = []
            break

    window.close()

    for i in range(num_sub_criteria):
        layout = [
            [sg.Text(f'Enter the sub-criterion {i+1} for {criterion}:'), sg.Input(key=f'sub_criterion_{criterion}_{i+1}')],
            [sg.Button('Next')]
        ]

        window = sg.Window('ANP Calculator', layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Next':
                sub_criterion = values[f'sub_criterion_{criterion}_{i+1}']
                sub_criteria[criterion].append(sub_criterion)
                break

        window.close()

# Step 3: Get the options from the user
layout = [
    [sg.Text('Enter the number of options:'), sg.Input(key='num_options')],
    [sg.Button('Next')]
]

window = sg.Window('ANP Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Next':
        num_options = int(values['num_options'])
        break

window.close()

options = []
for i in range(num_options):
    layout = [
        [sg.Text(f'Enter option {i+1}:'), sg.Input(key=f'option{i+1}')],
        [sg.Button('Next')]
    ]

    window = sg.Window('ANP Calculator', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Next':
            option = values[f'option{i+1}']
            options.append(option)
            break

    window.close()

# Step 4: Get the importances of main criteria compared to each other from the user
main_criteria_matrix = np.zeros((num_main_criteria, num_main_criteria))
for i in range(num_main_criteria):
    for j in range(num_main_criteria):
        if i == j:
            main_criteria_matrix[i, j] = 1
        elif i < j:
            layout = [
                [sg.Text(f'Enter the importance of {main_criteria[i]} compared to {main_criteria[j]}:'), sg.Input(key=f'importance_{i+1}_{j+1}')],
                [sg.Button('Next')]
            ]

            window = sg.Window('ANP Calculator', layout)

            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                if event == 'Next':
                    importance = float(values[f'importance_{i+1}_{j+1}'])
                    main_criteria_matrix[i, j] = importance
                    main_criteria_matrix[j, i] = 1 / importance
                    break

            window.close()

# Step 5: Get the importances of sub-criteria compared to each other from the user
sub_criteria_matrices = {}
for criterion in main_criteria:
    num_sub_criteria = len(sub_criteria[criterion])
    sub_criteria_matrices[criterion] = np.zeros((num_sub_criteria, num_sub_criteria))

    for i in range(num_sub_criteria):
        for j in range(num_sub_criteria):
            if i == j:
                sub_criteria_matrices[criterion][i, j] = 1
            elif i < j:
                layout = [
                    [sg.Text(f'Enter the importance of {sub_criteria[criterion][i]} compared to {sub_criteria[criterion][j]} for {criterion}:'),
                     sg.Input(key=f'importance_{criterion}_{i+1}_{j+1}')],
                    [sg.Button('Next')]
                ]

                window = sg.Window('ANP Calculator', layout)

                while True:
                    event, values = window.read()
                    if event == sg.WINDOW_CLOSED:
                        break
                    if event == 'Next':
                        importance = float(values[f'importance_{criterion}_{i+1}_{j+1}'])
                        sub_criteria_matrices[criterion][i, j] = importance
                        sub_criteria_matrices[criterion][j, i] = 1 / importance
                        break

                window.close()

# Step 6: Get the pairwise comparisons of the dependencies of the sub-criteria from the user
dependency_matrices = {}
for criterion in main_criteria:
    num_sub_criteria = len(sub_criteria[criterion])
    dependency_matrices[criterion] = np.zeros((num_sub_criteria, num_sub_criteria))

    for i in range(num_sub_criteria):
        for j in range(num_sub_criteria):
            if i == j:
                dependency_matrices[criterion][i, j] = 1
            elif i < j:
                layout = [
                    [sg.Text(f'Enter the dependency of {sub_criteria[criterion][i]} compared to {sub_criteria[criterion][j]} for {criterion}:'),
                     sg.Input(key=f'dependency_{criterion}_{i+1}_{j+1}')],
                    [sg.Button('Next')]
                ]

                window = sg.Window('ANP Calculator', layout)

                while True:
                    event, values = window.read()
                    if event == sg.WINDOW_CLOSED:
                        break
                    if event == 'Next':
                        dependency = float(values[f'dependency_{criterion}_{i+1}_{j+1}'])
                        dependency_matrices[criterion][i, j] = dependency
                        dependency_matrices[criterion][j, i] = 1 / dependency
                        break

                window.close()

# Step 7: Get the pairwise comparisons of the superiority of options for each sub-criteria from the user
superiority_matrices = {}
for criterion in main_criteria:
    num_sub_criteria = len(sub_criteria[criterion])
    superiority_matrices[criterion] = np.zeros((num_options, num_options))

    for i in range(num_options):
        for j in range(num_options):
            if i == j:
                superiority_matrices[criterion][i, j] = 1
            elif i < j:
                layout = [
                    [sg.Text(f'Enter the superiority of option {options[i]} compared to option {options[j]} for {criterion}:'),
                     sg.Input(key=f'superiority_{criterion}_{i+1}_{j+1}')],
                    [sg.Button('Next')]
                ]

                window = sg.Window('ANP Calculator', layout)

                while True:
                    event, values = window.read()
                    if event == sg.WINDOW_CLOSED:
                        break
                    if event == 'Next':
                        superiority = float(values[f'superiority_{criterion}_{i+1}_{j+1}'])
                        superiority_matrices[criterion][i, j] = superiority
                        superiority_matrices[criterion][j, i] = 1 / superiority
                        break

                window.close()

# Step 8: Calculate the unweighted supermatrix
unweighted_supermatrix = np.zeros((num_options, num_options))
for i in range(num_options):
    for j in range(num_options):
        for criterion in main_criteria:
            num_sub_criteria = len(sub_criteria[criterion])
            sub_criteria_matrix = sub_criteria_matrices[criterion]
            dependency_matrix = dependency_matrices[criterion]
            superiority_matrix = superiority_matrices[criterion]
            unweighted_supermatrix[i, j] += main_criteria_matrix[main_criteria.index(criterion), main_criteria.index(criterion)] * \
                                           sub_criteria_matrix[i % num_sub_criteria, j % num_sub_criteria] * \
                                           dependency_matrix[i % num_sub_criteria, j % num_sub_criteria] * \
                                           superiority_matrix[i, j]

# Step 9: Calculate the weighted supermatrix
weighted_supermatrix = unweighted_supermatrix / np.sum(unweighted_supermatrix, axis=0)

# Step 10: Calculate the limit supermatrix
limit_supermatrix = weighted_supermatrix.copy()
while not np.allclose(np.sum(limit_supermatrix, axis=0), np.sum(limit_supermatrix, axis=1)):
    limit_supermatrix = np.matmul(limit_supermatrix, limit_supermatrix)

# Step 11: Find the best option
column_sums = np.sum(limit_supermatrix, axis=0)
best_option_index = np.argmax(column_sums)
best_option = options[best_option_index]

sg.popup('Best Option:', best_option)