def dict_invert(d):
    '''
    d: dict
    '''
    inverted_dict = {}
    
    # For every elment in the dictionary keys:
    for key in d:

        #If the corresponding value is not a key in the inverted dict
        if d[key] not in inverted_dict:

            #Create an empty list with the value as the key
            inverted_dict[d[key]] = []

        #Append the key as the value
        inverted_dict[d[key]].append(key)

            
    #For every element(list) in the inverted dictioanry's values:
    for value in inverted_dict.values():

        #If len(element) > 1:
        if len(value) > 1:

            #Sort the list
            value.sort()

    return inverted_dict
