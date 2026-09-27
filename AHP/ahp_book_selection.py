import numpy as np

# Define criteria and alternatives
criteria = ["price", "author", "genre"]
sub_criteria = {"genre": ["criminal", "drama"]}
alternatives = ["Book 1", "Book 2", "Book 3", "Book 4"]

# Pairwise comparison matrices for each criterion
price_matrix = np.array([[1, 3, 2, 7],
                         [1/3, 1, 3, 5],
                         [1/2, 1/3, 1, 3],
                         [1/7, 1/5, 1/3, 1]])

author_matrix = np.array([[1, 3, 5, 7],
                          [1/3, 1, 3, 2],
                          [1/5, 1/3, 1, 3],
                          [1/7, 1/2, 1/3, 1]])

criminal_matrix = np.array([[1, 3, 6, 4],
                           [1/3, 1, 3, 5],
                           [1/6, 1/3, 1, 3],
                           [1/4, 1/5, 1/3, 1]])

drama_matrix = np.array([[1, 3, 5, 2],
                               [1/3, 1, 3, 4],
                               [1/5, 1/3, 1, 3],
                               [1/2, 1/4, 1/3, 1]])

# Weighting each criteria
price_weights = np.sum(price_matrix, axis=1) / np.size(price_matrix, axis=1)
author_weights = np.sum(author_matrix, axis=1) / np.size(author_matrix, axis=1)
criminal_weights = np.sum(criminal_matrix, axis=1) / np.size(criminal_matrix, axis=1)
drama_weights = np.sum(drama_matrix, axis=1) / np.size(drama_matrix, axis=1)

genre_weights = (criminal_weights*0.3) + (drama_weights*0.7)

# Constructing a matrix from the criteria weights
criteria_weights = np.vstack((price_weights, author_weights, genre_weights)).T

# Pairwise comparison matrix for alternatives
alternatives_matrix = np.array([[1, 1/3, 1/6, 1/2],
                                [3, 1, 1/3, 1/5],
                                [6, 3, 1, 1/3],
                                [2, 5, 3, 1]])

# Calculating the weighted matrix of alternatives
weighted_alternatives_matrix = alternatives_matrix.dot(criteria_weights)

# Normalizing the weighted matrix
normalized_matrix = weighted_alternatives_matrix / np.sum(weighted_alternatives_matrix, axis=0)

# Calculating the final weights for each alternative
final_weights = np.sum(normalized_matrix, axis=1) / np.size(normalized_matrix, axis=1)

# Finding the best alternative
best_alternative_index = np.argmax(final_weights)
best_alternative = alternatives[best_alternative_index]

# Printing the result
print(f"Final weights of each book is {final_weights}.")
print(f"The best book to choose is {best_alternative}.")