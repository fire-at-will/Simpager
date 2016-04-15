def opt(page_array, frames):

    #map string array to ints
    page_array = map(int, page_array)

    frame_array = []
    frame_index = 0
    page_faults = 0
    insertions = 0
    cur_index = 0

    for page in page_array:
        if page in frame_array:
            cur_index = cur_index + 1
            continue
        else:
            #if we know frame_array has no empty slots
            if insertions >= frames:
                replace_index = findIndex(cur_index, page_array, frame_array)
            #if frame_array is not yet full
            else:
                frame_array.insert(frame_index, page)
                frame_index = frame_index + 1

            page_faults = page_faults + 1
        cur_index = cur_index + 1

    print "OPT: " + str(page_faults)

def findIndex(cur_index, page_array, frame_array):
    cur_frame_index = 0
    longest_till_occurence = frame_array[0] #initialize page with longest time to occ.
    index_to_return = 0
    max_index_count = 0
    for page_in_frame in frame_array:
        index_count = 1
        for page in page_array[cur_index+1:]: #hopefully start at cur_index?
            if page == page_in_frame:
                continue #break out of inner for loop
            else:
                index_count = index_count + 1
        if index_count > max_index_count:
            longest_till_occurence = page_in_frame
            index_to_return = frame_array.index(longest_till_occurence)

    return index_to_return
