
#try except lesson
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["test"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Here I am!")
# except KeyError as error_message:
#     # print("That key does not exist")
#     print(f"the key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
# if height > 3: