# find the shortest unique substring among an array of strings

from collections import defaultdict


def generate_char_ngrams(input_str, n):
    ngrams = []
    for i in range(len(input_str) - n + 1):
        ngrams.append(input_str[i:i + n])
    return ngrams


# Example usage:
s1 = "cat"
s2 = "cow"
n = 3  # Change this to the desired n-gram size
res = defaultdict(list)
for i in range(1, len(s1) + 1):
    res[s1].extend(generate_char_ngrams(s1, i))
for i in range(1, len(s2) + 1):
    res[s2].extend(generate_char_ngrams(s2, i))

n_grams_s1 = res[s1]
n_grams_s2 = res[s2]

diff = sorted(set(n_grams_s1) - set(n_grams_s2), key=n_grams_s1.index)
print(diff[0])

