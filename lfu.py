def lfu(page_array, frames):
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
            if len(frame_array) < frames:
                frame_array.append(page)
            else:
                # Determine victim page
                victimIndex = determineLFUPageToKick(frame_array, pageUseCount)
                frame_array[victimIndex] = page

    print "LFU: " + str(page_faults)


def determineLFUPageToKick(frame_array, pageUseCount):
    accessCounts = []
    for page in frame_array:
        timesAccessed = pageUseCount[page]
        accessCounts.append(timesAccessed)

    minAccess = 10000
    minIndex = 10000

    for index, accessCount in enumerate(accessCounts):
        if accessCount < minAccess:
            minAccess = accessCount
            minIndex = index

    return minIndex
