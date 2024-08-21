#Lists - order is very important
my_list = ["Abel",True, 10,45,"Kevin"]
print(len(my_list))
print(my_list)

#Set - unique elements - order does not matter in sets
my_set = {1,2,3,4,5}
print(len(my_set))

#Tuples - order matters and cannot append elements
my_tuple = (1, 2, 3)
print((1,2,3) == (3,2,1))

#Dictionaries
my_dictionary = {
    "apple":"A red fruit",
    "bear": "A scary animal"
}
print(my_dictionary )
print(my_dictionary["apple"])
print(my_dictionary["bear"])