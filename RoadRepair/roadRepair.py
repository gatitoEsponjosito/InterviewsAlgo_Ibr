
from numpy import sort

def solvingRoadRepair(crewsid,jobid):
    crewsid=sort(crewsid);
    jobid=sort(jobid);
    minimumCost=0;
    for i in range(len(crewsid)):
        minimumCost+=abs(crewsid[i]-jobid[i]);
    return minimumCost;

def readingText():
    with open("textRoadRepair.txt","r") as f:
        n=f.readline().strip();
        blankLine=f.readline();
        n=int(n);
        i=0;
        crewsid=[None]*n;
        jobid=[None]*n;
        while i<n:
            crew=f.readline().strip();
            blankLine=f.readline();
            crewsid[i]=int(crew);
            i+=1;
        n=f.readline().strip();
        n=int(n);
        blankLine=f.readline();
        i =0;
        while i<n:
            crew=f.readline().strip();
            blankLine=f.readline();
            jobid[i]=int(crew);
            i+=1;
        print(solvingRoadRepair(crewsid,jobid));

if __name__=="__main__":
    readingText();