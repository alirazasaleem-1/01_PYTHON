scores = [45, 88, 12, 99, 75]
scores.append(100)
scores.sort(reverse=True)
scores.pop()
print(scores[0:3])

search = int(input("Search for a score: "))
if search in scores:
    print(f"Score foundt at position {scores.index(search)+1}")
else: 
    print("Score not found in top rankings. ")