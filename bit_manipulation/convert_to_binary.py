def convert_to_binary(value):
    bit_representation = [0]
    counter = 0
    while counter < value:
        counter += 1
        current_length = len(bit_representation)
        print current_length
        print bit_representation
        print ''        
        last_index = current_length-1
        last_item = bit_representation[last_index]
        if last_item == 0:
            bit_representation[last_index] = 1
        elif 0 in bit_representation:
            indices = [i for i, x in enumerate(bit_representation) if x == 0]
            index_of_last_zero = max(indices)
            num_empty_places = current_length - index_of_last_zero - 1
            bit_representation[(index_of_last_zero+1):current_length] = [0]*num_empty_places
            bit_representation[index_of_last_zero] = 1            
        else: # case where all 1's
            bit_representation = [0]*(current_length+1)
            bit_representation[0] = 1
    return '0b' + ''.join(map(str, bit_representation))


#convert_to_binary(247)