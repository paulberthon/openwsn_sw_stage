
import json
import time
from openvisualizer.moteState import moteState




class PCE:
   Addresses= []
   Motes=[]
   NeighboursRow =[]
   NumTx=[]
   NumTxACk=[]
   Pdr=[]
   lastUpdated=[]
   
   
  @staticmethod
  def getID(self,Addr):
    for i in range(len(self.Addresses)):
      if (self.Addresses[i]==Addr):
        return i
    raise SystemError('Unable to find Mote')
  
  @staticmethod
  def GetMoteElem(self,moteState.ms,elemName):
      i=self.getID(ms)
      return(self.elemName[i])
             
   @staticmethod            
   def add(self,moteState.ms):
      self.Addresses.append(ms.getStateElem(ms.ST_IDMANAGER))
      Motes.append(ms)
      linkInfo=self.dataParsingNeigbours(moteState.ms)
      self.NeighboursRow.append([linkInfo[i][0] for i in range(len(linkInfo))])
      self.NumTx.append([linkInfo[i][1] for i in range(len(linkInfo))])
      self.NumTxACk.append([linkInfo[i][2] for i in range(len(linkInfo))])
      self.Pdr.append([linkInfo[i][1]/linkInfo[i][2] for i in range(len(linkInfo))])
      self.lastUpdated.append(time.clock())
  
   @staticmethod
   def update(self,Addr):
      i=self.getID(Addr)
      linkInfo=self.dataParsingNeigbours(Motes[i])
      if len(linkInfo[i]==0):
         self.delete(Motes[i])
      else:
         self.NeighboursRow[i]=[linkInfo[j][0] for j in range(len(linkInfo))]
         self.NumTx[i]=[linkInfo[j][1] for j in range(len(linkInfo))]
         self.NumTxACK[i]=[linkInfo[j][2] for j in range(len(linkInfo))]
         self.Pdr[i]=[linkInfo[j][1]/linkInfo[j][2] for j in range(len(linkInfo))]
  
   @staticmethod  
   def dataParsingNeigbours(self,moteState.ms):
      obj = json.loads(ms.getStateElem(ms.ST_NEIGHBOURS))
      tab= []
      k=0
      while obj['data'][k]['Neighbors'] != ' (None)':
         tab.append([obj['data'][i],obj['data'][i]['numTx'],obj['data'][i]['numTxACK']])
         k+=1
      return tab
   
   
   @staticmethod
   def delete(self,index):
      del self.NeighboursRow[index]
      del self.NumTx[index]
      del self.NumTxACK[index]
      del self.Pdr[index]
      del self.Addresses[i]
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
