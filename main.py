def party_people(list_people, people_counter=0):
    if len(list_people) == 0:
        return people_counter
    min_req = min(list_people)
    if min_req <= people_counter+1:
        list_people.remove(min_req)
        people_counter += 1
        return party_people(list_people, people_counter)
    return people_counter




print(party_people([4, 5, 4, 1]))
