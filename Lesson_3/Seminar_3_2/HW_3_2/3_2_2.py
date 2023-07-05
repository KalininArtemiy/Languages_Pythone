bushes = int(input())
berries_on_bushes = list()
for i in range (bushes):
    berries = int (input(f'''Enter berries on {i+1} bush '''))
    berries_on_bushes.append(berries)
berries_count = list()
for i in range(len(berries_on_bushes) - 1):
    berries_count.append(berries_on_bushes[i-1]+berries_on_bushes[i]+ berries_on_bushes[i + 1])
berries_count.append(berries_on_bushes[-2] + berries_on_bushes[-1] + berries_on_bushes[0])
print(max(berries_count))