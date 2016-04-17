def lru(page_array, frames):

    #map string array to ints
    page_array = map(int, page_array)

    #find the largest page in the array for counter_array size
    maximum = 0
    for val in page_array:
        page = val
        if page > maximum:
            maximum = page

    frame_array = []
    frame_index = 0
    page_faults = 0
    event_time = 0

    #fill counter_array with 0s
    counter_array = [0] * (maximum + 1)

    for page in page_array:
        if page in frame_array:
            #increment event counter and store in counter_array
            event_time = event_time + 1
            counter_array[page] = event_time
            continue #should skip to next iteration
        else:
            #if we know frame_array has no empty slots
            if event_time >= frames:
                lru_page = frame_array[0]
                #check pages in frame_array for smallest clock value to replace
                for page_in_frame in frame_array:
                    if(counter_array[page_in_frame] < counter_array[lru_page]):
                        lru_page = page_in_frame
                #need to replace lru_page with the current page
                frame_index = frame_array.index(lru_page)
                frame_array[frame_index] = page
            #if frame_array has empty slots
            else:
                frame_array.insert(frame_index, page)
                frame_index = frame_index + 1
            page_faults = page_faults + 1

        #increment event counter
        event_time = event_time + 1
        #put event_time in counter_array at loc. page
        counter_array[page] = event_time

    print "LRU: " + str(page_faults)
