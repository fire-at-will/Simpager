def mfu(page_array, frames):
    frame_array = []
    frame_index = 0
    page_faults = 0
    insertions = 0

    # Dictionary to hold page usage counts
    pageUseCount = {}

    for index, page in enumerate(page_array):

        if page in frame_array:
            pageUseCount[page] += 1     # Increment this page used
            continue # should skip to next iteration
        else:
            if page in pageUseCount:
                pageUseCount[page] += 1     # Increment this page used
            else:
                pageUseCount[page] = 1      # We have used this page once now

            # Increment the number of page faults
            page_faults = page_faults + 1

            # Put new page into list of frames
            if index <= frames:
                frame_array.append(page)
            else:
                # Determine victim page
                victimIndex = determineMFUPageToKick(frame_array, pageUseCount)
                frame_array[victimIndex] = page

    print "MFU: " + str(page_faults)


def determineMFUPageToKick(frame_array, pageUseCount):
    # Figure out which page to kick.
    # Here we want to kick the page that has the highest usage count

    # Generate array of counts
    accessCounts = []
    for page in frame_array:
        timesAccessed = pageUseCount[page]
        accessCounts.append(timesAccessed)

    # Max algorithm
    maxAccess = -1
    maxIndex = -1

    for index, accessCount in enumerate(accessCounts):
        if accessCount > maxAccess:
            maxAccess = accessCount
            maxIndex = index

    return maxIndex
