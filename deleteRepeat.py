temp_list = ["L: | think I'm going to get", 'back into it. | think in June,', ]
transcript = ["L: I think I'm going to get", 'back into it. | think in June,',]


for i in temp_list:
    c = 0
    for x in i.split():
        print(i.split())
        for j in transcript[-15:]:
            for y in j.split():
                print(j.split())
                if x == y:
                    c += 1
    if c <= 5:
        transcript.append(i)
print(transcript)