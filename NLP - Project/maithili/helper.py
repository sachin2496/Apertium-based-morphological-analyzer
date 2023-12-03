import os

# function to find longest common substring
def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store the lengths of common substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length of the longest common substring and its ending index
    max_len = 0
    end_index = 0

    # Fill the table using bottom-up dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    # Extract the longest common substring
    longest_common_sub = str1[end_index - max_len + 1 : end_index + 1]

    return longest_common_sub


# function to find suffix after lcs
def after(com, word):
    l = len(com)
    index = word.index(com)
    return word[index+l:]

def simplify(s):
    z = ""
    for i in range(len(s)):
        if s[i] == "/":
            break
        z += s[i]
    return z

current_directory = os.getcwd()
files = os.listdir(current_directory)
global x
x = 5
for file_name in files:
    if "Noun" not in file_name and "Adj" not in file_name:
        continue
    file_path = os.path.join(current_directory, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            l = len(content)
            word_forms = content.split("\n")
            number_of_words = len(word_forms)
            if "Noun_m" in file_name:
                count = 1
                while count < number_of_words - 1:
                    word_forms[count+1] = simplify(word_forms[count+1])
                    word_forms[count+2] = simplify(word_forms[count+2])
                    word_forms[count+3] = simplify(word_forms[count+3])
                    word_forms[count+4] = simplify(word_forms[count+4])
                    word_forms[count] = simplify(word_forms[count])

                    base1 = lcs(word_forms[count + 1], word_forms[count + 2])
                    base2 = lcs(word_forms[count + 3], word_forms[count + 4])
                    base = lcs(base1, base2)
                    sentence = "\npardef" + str(x) + " = ET.SubElement(pardefs,\'pardef\',n=\'" + base + "\')\n"
                    start = "func_noun_entry_wleft(pardef" + str(x)
                    next1 = ", \'" + after(base, word_forms[count + 1]) + "\',\'\', \'n\',\'m\',\'sg\',\'p3\',\'d\')\n"
                    next2 = ", \'" + after(base, word_forms[count + 2]) + "\',\'\', \'n\',\'m\',\'pl\',\'p3\',\'d\')\n"
                    next3 = ", \'" + after(base, word_forms[count + 3]) + "\',\'\', \'n\',\'m\',\'sg\',\'p3\',\'o\')\n"
                    next4 = ", \'" + after(base, word_forms[count + 4]) + "\',\'\', \'n\',\'m\',\'pl\',\'p3\',\'o\')\n"
                    s1 = start + next1
                    s2 = start + next2
                    s3 = start + next3
                    s4 = start + next4
                    print(sentence, s1, s2, s3, s4)
                    Lines_to_add = [sentence, s1, s2, s3, s4]
                    dictionary_file = "maithili-dix.py"
                    with open(dictionary_file, 'a') as file:
                        file.writelines(Lines_to_add)
                    ds1 = "<e lm=\"" + base + "\">\n"
                    ds2 = "  <i>" + base + "</i>\n"
                    ds3 = "  <par n=\"" + base + "\"/>\n"
                    ds4 = "</e>\n"
                    Lines_to_add = [ds1, ds2, ds3, ds4]
                    auxiliary_file = "another_help"
                    with open(auxiliary_file, 'a') as file:
                        file.writelines(Lines_to_add)
                    count += 5
                    x += 1

            elif "Noun_f" in file_name:
                count = 1
                while count < number_of_words - 1:
                    word_forms[count + 1] = simplify(word_forms[count + 1])
                    word_forms[count + 2] = simplify(word_forms[count + 2])
                    word_forms[count + 3] = simplify(word_forms[count + 3])
                    word_forms[count + 4] = simplify(word_forms[count + 4])
                    word_forms[count] = simplify(word_forms[count])
                    base1 = lcs(word_forms[count + 1], word_forms[count + 2])
                    base2 = lcs(word_forms[count + 3], word_forms[count + 4])
                    base = lcs(base1, base2)
                    sentence = "\npardef" + str(x) + " = ET.SubElement(pardefs,\'pardef\',n=\'" + base + "\')\n"
                    start = "func_noun_entry_wleft(pardef" + str(x)
                    next1 = ", \'" + after(base, word_forms[count + 1]) + "\',\'\', \'n\',\'f\',\'sg\',\'p3\',\'d\')\n"
                    next2 = ", \'" + after(base, word_forms[count + 2]) + "\',\'\', \'n\',\'f\',\'pl\',\'p3\',\'d\')\n"
                    next3 = ", \'" + after(base, word_forms[count + 3]) + "\',\'\', \'n\',\'f\',\'sg\',\'p3\',\'o\')\n"
                    next4 = ", \'" + after(base, word_forms[count + 4]) + "\',\'\', \'n\',\'f\',\'pl\',\'p3\',\'o\')\n"
                    s1 = start + next1
                    s2 = start + next2
                    s3 = start + next3
                    s4 = start + next4
                    print(sentence, s1, s2, s3, s4)
                    Lines_to_add = [sentence, s1, s2, s3, s4]
                    dictionary_file = "maithili-dix.py"
                    with open(dictionary_file, 'a') as file:
                        file.writelines(Lines_to_add)
                    ds1 = "<e lm=\"" + base + "\">\n"
                    ds2 = "  <i>" + base + "</i>\n"
                    ds3 = "  <par n=\"" + base + "\"/>\n"
                    ds4 = "</e>\n"
                    Lines_to_add = [ds1, ds2, ds3, ds4]
                    auxiliary_file = "another_help"
                    with open(auxiliary_file, 'a') as file:
                        file.writelines(Lines_to_add)
                    count += 5
                    x += 1

            elif "Adj_f" in file_name:
                count = 1
                while count < number_of_words - 1:
                    word_forms[count + 1] = simplify(word_forms[count + 1])
                    word_forms[count + 2] = simplify(word_forms[count + 2])
                    word_forms[count] = simplify(word_forms[count])
                    base = lcs(word_forms[count + 1], word_forms[count + 2])
                    if base == "":
                        count += 3
                        continue
                    start = "func_adj_entry(pardef" + str(x)
                    next1 = ", \'" + after(base, word_forms[count + 1]) + "\',\'\', \'adj\',\'f\',\'sg\',\'p3\',\'d\')\n"
                    next2 = ", \'" + after(base, word_forms[count + 2]) + "\',\'\', \'adj\',\'f\',\'pl\',\'p3\',\'d\')\n"
                    sentence = "\npardef" + str(x) + " = ET.SubElement(pardefs,\'pardef\',n=\'" + base + "\')\n"
                    start = "func_adj_entry(pardef" + str(x)
                    s1 = start + next1
                    s2 = start + next2
                    print(sentence, s1, s2)
                    Lines_to_add = [sentence, s1, s2]
                    dictionary_file = "maithili-dix.py"
                    with open(dictionary_file, 'a') as file:
                        file.writelines(Lines_to_add)
                    ds1 = "<e lm=\"" + base + "\">\n"
                    ds2 = "  <i>" + base + "</i>\n"
                    ds3 = "  <par n=\"" + base + "\"/>\n"
                    ds4 = "</e>\n"
                    Lines_to_add = [ds1, ds2, ds3, ds4]
                    auxiliary_file = "another_help"
                    with open(auxiliary_file, 'a') as file:
                        file.writelines(Lines_to_add)
                    count += 3
                    x += 1

            elif "Adj_m" in file_name:
                count = 1
                while count < number_of_words - 1:
                    word_forms[count + 1] = simplify(word_forms[count + 1])
                    word_forms[count + 2] = simplify(word_forms[count + 2])
                    word_forms[count] = simplify(word_forms[count])
                    base = lcs(word_forms[count + 1], word_forms[count + 2])
                    if base == "":
                        count += 3
                        continue
                    sentence = "\npardef" + str(x) + " = ET.SubElement(pardefs,\'pardef\',n=\'" + base + "\')\n"
                    start = "func_adj_entry(pardef" + str(x)
                    next1 = ", \'" + after(base, word_forms[count + 1]) + "\',\'\', \'adj\',\'m\',\'sg\',\'p3\',\'d\')\n"
                    next2 = ", \'" + after(base, word_forms[count + 2]) + "\',\'\', \'adj\',\'m\',\'pl\',\'p3\',\'d\')\n"
                    s1 = start + next1
                    s2 = start + next2
                    print(sentence, s1, s2)
                    Lines_to_add = [sentence, s1, s2]
                    dictionary_file = "maithili-dix.py"
                    with open(dictionary_file, 'a') as file:
                        file.writelines(Lines_to_add)
                    ds1 = "<e lm=\"" + base + "\">\n"
                    ds2 = "  <i>" + base + "</i>\n"
                    ds3 = "  <par n=\"" + base + "\"/>\n"
                    ds4 = "</e>\n"
                    Lines_to_add = [ds1, ds2, ds3, ds4]
                    auxiliary_file = "another_help"
                    with open(auxiliary_file, 'a') as file:
                        file.writelines(Lines_to_add)
                    count += 3
                    x += 1
