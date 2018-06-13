
import json

from openvisualizer.moteState import moteState




class PCE:
   ADDRESSES= []
   NeighboursRow =[]
   NumTx=[]
   NumTxACk=[]
   PDR=[)
  
  def getID(self,moteState.ms):
    k=0
    Addr=ms.getStateElem(ms.ST_IDMANAGER)
    for i in range(len(self.ADDRESSES)):
      if (self.ADDRESSES[i]==Addr):
        return i
    raise SystemError('Unable to find Mote')
  
  def GetMoteElem(self,moteState.ms,elemName)
      i=self.getID(ms)
      return(self.elemName[i]
             
             
  def add(self,moteState.ms)
    self.ADDRESSES.append(ms.getStateElem(ms.ST_IDMANAGER))
    linkInfo=self.dataParsingNeigbours(moteState.ms)
    self.NeighboursRow.append([linkInfo[i][0] for i in range(len(linkInfo))])
    self.NumTx.append([linkInfo[i][1] for i in range(len(linkInfo))])
    self.NumTxACk.append([linkInfo[i][2] for i in range(len(linkInfo))])
    self.PDR.append([linkInfo[i][1]/linkInfo[i][2] for i in range(len(linkInfo))])
    
  
 def update(self,moteState.ms)
    i=self.getID(ms)
    linkInfo=self.dataParsingNeigbours(moteState.ms)
    self.NeighboursRow[i]=[linkInfo[i][0] for i in range(len(linkInfo))]
    self.NumTx[i]=[linkInfo[i][1] for i in range(len(linkInfo))]
    self.NumTxACK[i]=[linkInfo[i][2] for i in range(len(linkInfo))]
    self.PDR=[linkInfo[i][1]/linkInfo[i][2] for i in range(len(linkInfo))]
  
  
def dataParsingNeigbours(self,moteState.ms)
   obj = json.loads(ms.getStateElem(ms.ST_NEIGHBOURS))
   tab= []
   for i in range(len(obj['data'])):
      tab.append([obj['data'][i],obj['data'][i]['numTx'],obj['data'][i]['numTxACK']])
   return tab
