name_roll = {
    "sand": 3,
    "mark": 4,
    "john": 5
}

result = map(lambda x: x[0] +"-->"+ str(x[1]), name_roll.items())

print result

result1 = reduce(lambda x, y: x+y, name_roll.items())

print result1