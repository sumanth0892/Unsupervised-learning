#k clustering means
#This is a simple algorithm for unsupervised learning
from numpy import *
def GetData(' ')
    dataMatrix=[]
    fr = open(' ')
    return dataMatrix

def EucDist(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet,k):
    n = shape(dataSet)[1]
    centroid = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = max(dataSet[:,j])
        centroid[:,j] = minJ+rangeJ*random.rand(k,1)
    return centroid

def kM(dataSet,k,distmeans = EucDist,createCent = randCent):
    m = dataSet.shape[0]
    clusterAssessed = mat(zeros((m,2)))
    centroids = createCent(datSet,k)
    ChangeOfCluster = True
    while ChangeOfCluster:
        ChangeOfCluster = False
        for i in range(m):
            minDist = inf; minIndex=-1
            for j in range(k):
                distJI = distmeans(centroid[j,:],dataSet[i,:])
                if distJI<minDist:
                    minDist = distJI; minIndex=j
            if clusterAssessed[i,0]!=minIndex:ChangeOfCluster = True
            clusterAssessed[i,:] = minIndex,minDist**2
        print centroids
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssessed[:,0].A==cent)[0]]
            centroids[cent,:] = mean(ptsInclust,axis=0)
    return centroids clusterAssessed

    
