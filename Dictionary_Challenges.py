#Challenge 1: Frequency Counter

def count_frequencies(arr):
    
    wordFreq = {}

    for word in arr:
        
        if word in wordFreq:
            wordFreq[word] += 1
            
        else:
            wordFreq[word] = 1

    return wordFreq
            

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
#print(count_frequencies(words))

#Challenge 2: Student Grades


def average_grades(dic):

     for name, grades in dic.items():

         print(f"{name} average score is:{(sum(grades)/3)}")
    

student_grades = {
 "Alice": [85, 90, 78],
 "Bob": [92, 88, 84],
 "Charlie": [70, 75, 80]
}
#average_grades(student_grades)


#Challenge 3: Square Values

def square_values(dic):
    
    for key, value in dic.items():
        
        print(f"The value for the key {key} squared is {value**2}")
        

original_dict = {"a": 2, "b": 3, "c": 4}
#square_values(original_dict)


#Challenge 4: Merge Dictionaries

def merge_dicts(dic1, dic2):

    dic3 = {}

    for key in dic1:
        dic3[key] = dic1.get(key, 0) + dic2.get(key, 0)
    
    for key in dict2:
        if key not in dic3:
            dic3[key] = dict2[key]

    return dic3

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
#print(merge_dicts(dict1, dict2))


#Challenge 5: Dictionary of Lists to List of Dictionaries

def transform_data(data):

    result = []
    
    for key, values in data.items():

        for value in values:

            result.append({key: value})
    
    return result

data = {
 "fruit": ["apple", "banana", "orange"],
 "colour": ["red", "yellow", "orange"]
}

#print(transform_data(data))


#Challenge 6: Remove and Return Value

def remove_and_return(dictionary, key):

    return dictionary.pop(key, None)

data = {"a": 1, "b": 2, "c": 3}
#print(remove_and_return(data, "b"))
#print(data)


#Challenge 7: Pop All Values

def pop_all_values(dictionary):

    return [dictionary.pop(key) for key in list(dictionary.keys())]

data = {"x": 10, "y": 20, "z": 30}
#print(pop_all_values(data))
#print(data)


#Challenge 8: Pop and Sum Values

def pop_and_sum(dictionary, keys):

    total_sum = 0
    
    for key in keys:

        total_sum += dictionary.pop(key, 0)
    
    return total_sum

data = {"p": 5, "q": 15, "r": 25}
#print(pop_and_sum(data, ["p", "r"]))
#print(data)


#Challenge 9: Pop with Default

def pop_with_default(dictionary, key, default_value):

    return dictionary.pop(key, default_value)

data = {"m": 7, "n": 14}
#print(pop_with_default(data, "n", 0))
#print(pop_with_default(data, "o", 0))
#print(data)


#Challenge 10: Pop and Create New Dictionary

def pop_and_create_new(dictionary, keys):

    new_dict = {}
    
    for key in keys:

        if key in dictionary:

            new_dict[key] = dictionary.pop(key)
    
    return new_dict

data = {"a": 1, "b": 2, "c": 3, "d": 4}
#print(pop_and_create_new(data, ["b", "d"]))
#print(data)