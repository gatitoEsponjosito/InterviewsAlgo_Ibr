def findEventualSafeStates(graph):
    n=len(graph);
    safe={};
    def isSafe(i):
        if i in safe:
            return safe[i];
        safe[i]=False;
        for nei in graph[i]:
            if not isSafe(nei):
                return safe[i];
        safe[i]=True;
        return True;
    res=[];
    for i in range(n):
        if isSafe(i):
            res.append(i);
    return res;