def lru():
    frame_array = []
    frame_index = 0
    page_faults = 0
    insertions = 0
    counter_array = []

    for page in page_array:
        if page in frame_array:
            continue #should skip to next iteration
        else:
            if insertions >= 3:
                #calculate min of counts of pages in frame_array

                frame_array[frame_index] = page
            else:
                frame_array.insert(frame_index, page)
                frame_index = frame_index + 1
                frame_index = frame_index % (frames)
            page_faults = page_faults + 1
            insertions = insertions + 1

        #increment page counts
        if counter_array[page] == None:
            counter_array.insert(page, 1)
        else:
            counter_array[page] = counter_array[page] + 1

    print "LRU: " + str(page_faults)
