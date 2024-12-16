"""
question: What is a nested dictionary, and give an example of its use case?
Answer: Nested dictionary is that contains other dictionaries as its values. In other words,
        the values in a dictionary can themselves be dictionaries.
        dictionary is a collection of key-value pairs. When a dictionary is nested, the value
        associated with a key can be another dictionary, which can in turn have its own key-value
        pairs.

"""
# Nested dictionary
student = {
    "name":   "karan",
    "subject":  {
        "physics": 97,
        "chemistry": 98,
        "maths":    95
    }
}
print(student) 

