import random

hard_words = ["caramel", "spring", "programmer", "autumn", "greenhouse", "ergonomic", "doughnut"]

short_words = ["cat", "dog", "mom", "dad", "cow", "bee", "fox", "box"]

selection = hard_words #change the value on the right to fit the list of words you'd like to use. Example: change "hard_words" to "short_words"

secret_word = random.choice(selection)
