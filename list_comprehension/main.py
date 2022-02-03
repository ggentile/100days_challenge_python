# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [num * num for num in numbers]

# print(squared_numbers)

# result = [num for num in numbers if num % 2 == 0]
# print(result)
""" Exercise 1"""

# with open("file1.txt", "r") as file1:
    # numbers_in_one = file1.readlines()

# with open("file2.txt", "r") as file2:
   # numbers_in_two = file2.readlines()

# numbers1_stripped = [int(i.strip("\n")) for i in numbers_in_one]
# numbers2_stripped = [int(i.strip("\n")) for i in numbers_in_two]

# result = [num for num in numbers1_stripped if num in numbers2_stripped]
# print(result)

""" Exercise 2"""
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {word: len(word) for word in sentence.split()}
# print(result)
"""Exercise 3"""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c*9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
