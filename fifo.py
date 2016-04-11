def fifo(page_array, frames):
    frame_array = []
    frame_index = 0
    page_faults = 0
    insertions = 0

    for page in page_array:
        if page in frame_array:
            continue #should skip to next iteration
        else:
            if insertions >= frames:
                frame_array[frame_index] = page
            else:
                frame_array.insert(frame_index, page)
            frame_index = frame_index + 1
            frame_index = frame_index % (frames)
            page_faults = page_faults + 1
            insertions = insertions + 1

    print "FIFO: " + str(page_faults)
