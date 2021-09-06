def group_anagram(arr):
    anagram = {}
    for i in arr:
        anagram["".join(sorted(i))] = []
    for i in arr:
        anagram[''.join(sorted(i))].append(i)
    return list(anagram.values())


print(group_anagram(["eat","tea","tan","ate","nat","bat"]))