import numpy as np
from tabulate import tabulate
np.set_printoptions(precision=4, suppress=True)

# Defining the decision problem, criterias, alternatives
criterias = ['Performance', 'Runtime', 'Resource Consumption', 'Scalability']
alternatives = ['K-means','Infomap', 'Clauset', 'PICS', 'BAGC', 'NEC', 'CANM']

# Defining the decision matrix
decision_matrix = np.array([[5, 2, 2, 5], 
                              [8, 5, 5, 8], 
                              [8, 8, 8, 5],
                              [8, 5, 5, 5],
                              [8, 8, 8, 8],
                              [8, 8, 5, 5],
                              [8, 8, 9, 8]])

# Normalizing the decision matrix
norm_matrix = np.zeros(decision_matrix.shape)
for j in range(decision_matrix.shape[1]):
    sum_squared = np.sqrt(np.sum(decision_matrix[:, j] ** 2))
    for i in range(decision_matrix.shape[0]):
        norm_matrix[i][j] = decision_matrix[i][j] / sum_squared

# Printing the normalized decision matrix
print('\nNormalized Decision Matrix:')
for i in range(norm_matrix.shape[0]):
    for j in range(norm_matrix.shape[1]):
        print(f"{norm_matrix[i][j]:.4f}", end=' ')
    print()
print("\n")

# Weighting the criterias
weights = np.array([])
for i in range(len(criterias)):
    weight = float(input(f"Weight of Criteria '{criterias[i]}': "))
    weights = np.append(weights, weight)
weights /= np.sum(weights)
print("\nNormalized weights of criterias:", weights)

# Calculating the weighted normalized decision matrix
weighted_norm_matrix = norm_matrix * weights[np.newaxis, :]
print('\nWeighted Normalized Decision Matrix:')
print(weighted_norm_matrix, "\n")

# Calculating the positive ideal and negative ideal solutions
P_ideal_solution = np.zeros(weighted_norm_matrix.shape[1])
N_ideal_solution = np.zeros(weighted_norm_matrix.shape[1])
for j in range(weighted_norm_matrix.shape[1]):
    if j in [1, 2]:
        P_ideal_solution[j] = np.min(weighted_norm_matrix[:, j])
        N_ideal_solution[j] = np.max(weighted_norm_matrix[:, j])
    else:
        P_ideal_solution[j] = np.max(weighted_norm_matrix[:, j])
        N_ideal_solution[j] = np.min(weighted_norm_matrix[:, j])
print("Positive Ideal Solutions: ", P_ideal_solution)
print("Negative Ideal Solutions: ", N_ideal_solution)

# Calculating the distance to positive ideal and negative ideal solutions
dist_to_P_ideal = np.sqrt(np.sum((weighted_norm_matrix - P_ideal_solution) ** 2, axis=1))
dist_to_N_ideal = np.sqrt(np.sum((weighted_norm_matrix - N_ideal_solution) ** 2, axis=1))

table_data = []
for i in range(len(alternatives)):
    table_data.append([alternatives[i], f"{dist_to_P_ideal[i]:.4f}", f"{dist_to_N_ideal[i]:.4f}"])
table_headers = ['alternatives', 'dist_to_P_ideal', 'dist_to_N_ideal']
print('\nDistances to positive ideal and negative ideal solutions:')
print(tabulate(table_data, headers=table_headers, tablefmt='grid', floatfmt=".4f"))

# Calculating the scores (Closeness)
scores = dist_to_N_ideal / (dist_to_P_ideal + dist_to_N_ideal)

# Sort the scores in descending order
sorted_scores_indices = np.argsort(scores)[::-1]
sorted_scores = scores[sorted_scores_indices]

# Print the ranked alternatives and their scores
print('\nRanking Results:')
for i, option in enumerate(sorted_scores_indices):
    print(f"{i+1}. {alternatives[option]}: {sorted_scores[i]:.4f}")

# Print the best alternative
best_alternative = sorted_scores_indices[0]
print(f"\nThe best song is \"{alternatives[best_alternative]}\" with a score of {sorted_scores[0]:.4f}")