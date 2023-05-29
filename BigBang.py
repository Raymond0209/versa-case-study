import json

#Initialize the result list
result = []

#Loop through the numbers 1 to 100
for num in range(1, 101):

    #Check if the number is divisible by 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        result.append("BIGBANG")

    #Check if the number is divisible by 3
    elif num % 3 == 0:
        result.append("BIG")

    #Check if the number is divisible by 5
    elif num % 5 == 0:
        result.append("BANG")

    else:
        result.append(str(num))

#Write the result to the file output.json
with open('output.json', 'w') as outfile:
    json.dump(result, outfile)