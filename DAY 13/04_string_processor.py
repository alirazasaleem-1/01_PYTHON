def clean_names(list_of_names):
    names = []
    for name in list_of_names:
        fixed_names = name.capitalize()
        names.append(fixed_names)
    return names

friends = ["ali", "junaid", "jamshaid"]
processed_names = clean_names(friends)
print(processed_names)