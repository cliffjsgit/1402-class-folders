import os
import string

def WalkDirectory(sDir, sType):
    
    oPathList = []
    
    for sObject in os.listdir(sDir):

        sPath = os.path.join(sDir, sObject)
        
        
        if(os.path.isdir(sPath)):
            oPathList.extend(WalkDirectory(sPath, sType))
        elif(sObject.find(sType) != -1):
                oPathList.append(os.path.abspath(os.path.join(sDir, sObject)))
                
    return oPathList
    
def ComputeCheckSums(oFileList):
    
    oDict = dict()
    
    for sFile in oFileList:

        oF = os.popen('md5sum ' + sFile)
        sResult = oF.read()
        oF.close()
        
        sResult = sResult.split()[0]
        
        oDict.setdefault(sResult, []).append(sFile)
        
    return oDict
    
def Main():
    
    oList = WalkDirectory('.', '.txt')

    oDict = ComputeCheckSums(oList)
    
    if(len(oList) > 0):
        print('Files Found:')
        
    for sItem in oList:
        print(sItem)
        
    
    if(len(oDict) > 1):
        
        print('')
        
        for sKey in oDict:
            
            if(len(oDict[sKey]) >  1):

                print('Files ' +  ', '.join(oDict[sKey]) + ' are the same')
                

            
Main()