
def calculate_love_score(name1, name2):
    name = name1 + name2
    count = 0
    for letter in name:
        if letter in "trueloveTRUELOVE":
            count += 1
    return count


print(calculate_love_score("Kanye West", "Kim Kardashian"))
