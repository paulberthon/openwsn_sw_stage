import 




class PCE:
   ADDRESSES= []
   NeighboursRow =[]
   NumTx=[]
   NumTxACk=[]
  
  def GetID(self,Addr):
    k=0
    for i in range(len(self.ADDRESSES)-1):
      if (self.ADDRESSES[i]==Addr):
        return i
    raise SystemError('Unable to find Mote')
    
  def GetPDR(self,Addr)
    i=get_ID(Addr)
    return(self.NumTxACK[i]/self.NumTx[i])
    
  def GetNeighbours(self,Addr)
    i=get_ID(Addr)
    return(self.NeigboursRow[i])
           
  def add(self,Addr,Neighbours,NumTx,NumTxACK)
    self.self.ADDRESSES.append(Addr)
    self.NeighboursRow.append(Neighbours)
    self.NumTx.append(NumTx)
    self.NumTxACk.append(NumTxACK)
    
  
 def update(self,Addr,Neighbours,NumTx,NumTxACK)
    i=self.get_ID(Addr)
    self.NeighboursRow[i]=Neighbours
    self.NumTx[i]+=NumTx
    self.NumTxACK[i]+=NumTxACK
  
  


