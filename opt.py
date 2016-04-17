def opt(page_array, frames):

    #map string array to ints
    page_array = map(int, page_array)

    frame_array = []
    frame_index = 0
    page_faults = 0
    insertions = 0
    cur_index = -1

    for page in page_array:
        cur_index = cur_index + 1
        if page in frame_array:
            continue
        else:
            #if we know frame_array has no empty slots
            if insertions >= frames:
                replace_index = findIndex(cur_index, page_array, frame_array)
                frame_array[replace_index] = page
            #if frame_array is not yet full
            else:
                frame_array.insert(frame_index, page)
                frame_index = frame_index + 1
            insertions = insertions + 1
            page_faults = page_faults + 1

    print "OPT: " + str(page_faults)

def findIndex(cur_index, page_array, frame_array):
    index_to_return = 0
    max_index_count = 0
    for page_in_frame in frame_array:
        index_count = 0
        for page in page_array[cur_index+1:]:
            if page == page_in_frame:
                break
            else:
                index_count = index_count + 1
        if index_count > max_index_count:
            max_index_count = index_count
            index_to_return = frame_array.index(page_in_frame)

    return index_to_return
