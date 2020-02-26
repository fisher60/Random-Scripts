
result = {x: "value " + str(x) for x in range(20)}

reversed_dict = {x: y for x, y in zip(reversed(result.keys()), reversed(result.values()))}

print(reversed_dict)