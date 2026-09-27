import numpy as np

# Define the decision problem and criteria
criteria = ['Popularity', 'Lyrics', 'Artist', 'Genre']
alternatives = ['Slow Down by Selena Gomez',
            'Boome Naghashi by Wantons', 
            'Salvatore by Lana Del Ray']

# Weighting the criterias
weights = np.array([[1, 3, 7, 4],
                    [1/3, 1, 3, 5],
                    [1/7, 1/3, 1, 3],
                    [1/4, 1/5, 1/3, 1]]) 

weights = np.sum(weights, axis=1) / np.size(weights, axis=1)

# Define the evaluation matrix
evaluation_matrix = np.array([[5, 3, 7, 6], [7, 4, 9, 7], [4, 7, 5, 8]])

# Normalize the evaluation matrix
norm_matrix = evaluation_matrix / np.sqrt(np.sum(evaluation_matrix ** 2, axis=0))

# Calculate the weighted normalized decision matrix
weighted_norm_matrix = norm_matrix * weights

# Calculate the positive ideal and negative ideal solutions
P_ideal_solution = np.max(weighted_norm_matrix, axis=0)
N_ideal_solution = np.min(weighted_norm_matrix, axis=0)

# Calculate the distance to positive ideal and negative ideal solutions
dist_to_P_ideal = np.sqrt(np.sum((weighted_norm_matrix - P_ideal_solution) ** 2, axis=1))
dist_to_N_ideal = np.sqrt(np.sum((weighted_norm_matrix - N_ideal_solution) ** 2, axis=1))

# Calculate the scores
scores = dist_to_N_ideal / (dist_to_P_ideal + dist_to_N_ideal)

# Sort the scores in descending order
sorted_scores_indices = np.argsort(scores)[::-1]
sorted_scores = scores[sorted_scores_indices]

# Print the ranked alternatives and their scores
print('Final Results:')
for i, option in enumerate(sorted_scores_indices):
    print(f"{i+1}. {alternatives[option]}: {sorted_scores[i]:.4f}")

# Print the best alternative
best_alternative = sorted_scores_indices[0]
print(f"\nThe best song is \"{alternatives[best_alternative]}\" with a score of {sorted_scores[0]:.4f}")