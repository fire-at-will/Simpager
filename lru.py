def lru():
    frame_array = []
    frame_index = 0
    page_faults = 0
    event_time = 0
    counter_array = []

    for page in page_array:
        if page in frame_array:
            continue #should skip to next iteration
        else:
            if event_time >= frames:
                #calculate min of counts of pages in frame_array

                frame_array[frame_index] = page
            else:
                frame_array.insert(frame_index, page)
                frame_index = frame_index + 1
                frame_index = frame_index % (frames)
            page_faults = page_faults + 1

        #increment page counts
        if counter_array[page] == None:
            counter_array.insert(page, event_time)
        else:
            counter_array[page] = event_time

        #increment event counter
        event_time = event_time + 1

    print "LRU: " + str(page_faults)
