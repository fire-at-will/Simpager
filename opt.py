####################################################################################################
#
#               opt Function
#
#       Purpose -
#       This function will replace the page in the frame_array that will not occur again for the longest
#       amount of time.
#
#       Input -
#       array of pages to be replaced; and the size of the frame_array
#
#       Output -
#       prints out the algorithm name and the number of page faults to standard out
#
####################################################################################################

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

####################################################################################################
#
#               findIndex Function
#
#       Purpose -
#       This function is called by opt to find the index of the page in the frame_array that should
#       be replaced.
#
#       Input -
#       array of pages to be replaced, the size of the frame_array, and the current index in page array
#
#       Output -
#       returns the index of page to be replaced
#
####################################################################################################

def findIndex(cur_index, page_array, frame_array):
    index_to_return = 0
    max_index_count = 0
    for page_in_frame in frame_array:
        index_count = 0
        #loop forward through the array from current location
        for page in page_array[cur_index+1:]:
            #if you find the page occurence then stop
            if page == page_in_frame:
                break
            #otherwise increment swap value
            else:
                index_count = index_count + 1
        #keep track of max swap value and its corresponding index to replace
        if index_count > max_index_count:
            max_index_count = index_count
            index_to_return = frame_array.index(page_in_frame)

    return index_to_return
