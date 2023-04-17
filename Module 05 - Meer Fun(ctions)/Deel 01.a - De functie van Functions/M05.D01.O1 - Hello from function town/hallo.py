def function (aantal: int):
    antwoord = ''
    for x in range(1,aantal + 1):
        antwoord += f'Hello from function town {x} \n'
    return antwoord

print(function(3))
print(function(7))