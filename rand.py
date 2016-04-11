from random import randint

def rand(page_array, frames):
    frame_array = []
    frame_index = 0
    page_faults = 0
    insertions = 0

    for index, page in enumerate(page_array):
        if page in frame_array:
            continue # should skip to next iteration
        else:
            # Find the victim frame at random
            toKick = randint(0, (frames - 1))

            # Increment the number of page faults
            page_faults = page_faults + 1

            # Put new page into list of frames
            if index < frames:
                frame_array.insert(toKick, page)
            else:
                frame_array[toKick] = page

    print "RAND: " + str(page_faults)
