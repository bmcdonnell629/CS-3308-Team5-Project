def word_length_filter(word_list, min_letters, max_letters):   
    length_min = min(int(min_letters), int(max_letters))
    length_max = max(int(min_letters), int(max_letters))
    
    filtered_list = []
    
    for word in word_list:
        if len(word[0]) >= length_min and len(word[0]) <= length_max:
            filtered_list.append(word)
    
    return filtered_list



def starts_with_filter(starting_letters, word_list):
    filtered_list = []
    
    if "?" not in starting_letters:
        for word in word_list:
            if word[0].startswith(starting_letters):
                filtered_list.append(word)
    
    else:        
        new_list = word_length_filter(word_list, len(starting_letters), 15)
        
        for word in new_list:
            match = True
            
            for i in range(len(starting_letters)):
                if starting_letters[i] == "?":
                    continue
                elif word[0][i] == ststarting_lettersart[i]:
                    continue
                else:
                    match = False
                    break
            
            if match:
                filtered_list.append(word)
    
    return filtered_list


def ends_with_filter(ending_letters, word_list):
    filtered_list = []
    
    if "?" not in ending_letters:
        for word in word_list:
            if word[0].endswith(ending_letters):
                filtered_list.append(word)
    
    else:        
        new_list = word_length_filter(word_list, len(ending_letters), 15)
        
        for word in new_list:
            match = True
            reversed_word = word[0][::-1]
            reversed_end = ending_letters[::-1]
            
            for i in range(len(ending_letters)):
                if reversed_end[i] == "?":
                    continue
                elif reversed_word[i] == reversed_end[i]:
                    continue
                else:
                    match = False
                    break
            
            if match:
                filtered_list.append(word)
    
    return filtered_list

def contains_filter(req_letters, word_list):
    filtered_list = []
    
    if "?" not in req_letters:
        for word in word_list:
            if req_letters in word[0]:
                filtered_list.append(word)
    
    else:
        new_list = word_length_filter(word_list, len(req_letters), 15)
        
        for word_score_pair in new_list:
            match = True
            word = word_score_pair[0]
            
            for i in range(len(word) - len(req_letters) + 1):
                if word[i] == req_letters[0] or req_letters[0] == "?":
                    
                    for j in range(len(req_letters)):
                        if req_letters[j] == "?":
                            continue
                        elif word[i+j] == req_letters[j]:
                            continue
                        else:
                            match = False
                            break
                    
                    if match:
                        filtered_list.append(word_score_pair)
                        break
                    else:
                        continue
    
    return filtered_list



def remove_anagrams(search_word, word_list):
    filtered_list = []
    sw = bytes(search_word, "utf-8")
    qm = bytes("?", "utf-8")
    
    if "?" not in search_word:
        for word in word_list:
            if word[0] in search_word:
                filtered_list.append(word)
    
    else:
        for word_score_pair in word_list:
            match = True
            word = word_score_pair[0]
            search_word_length = len(search_word)
            word_length = len(word)
            
            for i in range(search_word_length):
                if word_length > (search_word_length - i):
                    break
                
                if search_word[i] == "?" or search_word[i] == word[0]:
                    for k in range(word_length):
                        if search_word[i+k] == "?":
                            continue
                        elif search_word[i+k] == word[k]:
                            continue
                        else:
                            match = False
                            break
                            
                    if match:
                        filtered_list.append(word_score_pair)
                        break
                    else:
                        continue
    
    return filtered_list

def fixed_position_filter(fixed_word, word_list):
    filtered_list = []
    
    for word in word_list:
        match = True
        
        for i in range(len(fixed_word)):
            if i >= len(word[0]):
                match = False
                break
            elif fixed_word[i] == "*" or fixed_word[i] == "?":
                continue
            elif fixed_word[i] == word[0][i]:
                continue
            else:
                match = False
                break
        
        if match:
            filtered_list.append(word)
    
    return filtered_list