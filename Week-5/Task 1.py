n_lines = 0
n_words = 0
with open("analysis.txt", "w") as rec:
    with open("text.txt", "r") as file:
        text = file.read()
        file.seek(0)
        lines = file.readlines()
        for i in range(len(lines)):
            n_lines += 1
        rec.write(f"Number of lines: {n_lines}\n")
        words = []
        for i in range(len(lines)):
            words += lines[i].split()
        for i in range(len(words)):
            n_words += 1
        rec.write(f"Number of words: {n_words}\n")
        for i in words:
            freq = 0
            rec.write(f"Frequency of {i}: ")
            for j in range(len(words)):
                if i == words[j]:
                    freq += 1
            rec.write(f"{freq}\n")