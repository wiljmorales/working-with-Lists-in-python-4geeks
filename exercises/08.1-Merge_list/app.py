chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    full_list = []
    for person in chunk_one:
        full_list.append(person)
    for person in chunk_two:
        full_list.append(person)
    return full_list


print(merge_list(chunk_one, chunk_two))
