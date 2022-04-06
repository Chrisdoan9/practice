from pam import *
p = PAM(N=250).Build_PAMN()
# PAM.read_PAM1
alphabet=['C','S','T','P','A','G','N','D','E','Q','H','R','K','M','I','L','V','F','Y','W']
# print(alphabet)
# print(p)
def word_score(word):
    first_letter_score = p[word[0], word[0]]
    second_letter_score = p[word[1], word[1]]
    third_letter_score = p[word[2], word[2]]
    score = first_letter_score + second_letter_score + third_letter_score
    return score

def neighbor_word(word,threshold=13):
    list_neighbor_word = []
    first_letter_score = p[word[0],word[0]]
    second_letter_score =p[word[1],word[1]]
    third_letter_score =p[word[2],word[2]]
    score = first_letter_score + second_letter_score + third_letter_score
    for i in range(20):
        score = first_letter_score + second_letter_score + p[word[2], alphabet[i]]
        # print(score)
        if score >= threshold:
            list_neighbor_word.append(word[0] + word[1] + alphabet[i])
            # print(list)
    for i in range(20):
        score = first_letter_score + p[word[1], alphabet[i]] + third_letter_score
        # print(score)
        if score >= threshold:
            list_neighbor_word.append(word[0] + alphabet[i] + word[2])
    for i in range(20):
        score = p[word[0], alphabet[i]] + second_letter_score + third_letter_score
        # print(score)
        if score >= threshold:
            list_neighbor_word.append(alphabet[i] + word[1] + word[2])
    return list(set(list_neighbor_word))
# print(neighbor_word('VVA'))
# print(len(neighbor_word('FIM')))
# print(len(set(neighbor_word('FIM'))))
# print(word_score('FIM'))



