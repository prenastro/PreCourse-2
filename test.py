def getMinimumTime(requestedHubs, transitionTime):
    m = len(requestedHubs)

    pre = [0] * (m+1)
    for i in range(1, m+1):
        pre[i] = pre[i-1] + requestedHubs[i]
