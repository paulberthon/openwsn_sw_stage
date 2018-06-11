import 




class PCE:
  def __init__(self):
    self.ADDRESSES= []
    self.NeighboursRow =[]
    self.NumTx=[]
    self.NumTxACk=[]
  
  def get_ID(Addr):
    k=0
    for i in range(len(self.ADDRESSES)-1)
      if self.ADDRESSES[i]==Addr
        return i
    raise SystemError('Unable to find Mote')
    
  def get_PDR(Addr)
    i=get_ID(Addr)
    return(self.NumTxACK[i]/self.NumTx[i])
    
  def get_Neighbours(Addr)
    i=get_ID(Addr)
    return(self.NeigboursRow[i])
           
  def add(Addr,Neighbours,NumTx,NumTxACK)
    self.self.ADDRESSES.append(Addr)
    self.NeighboursRow.append(Neighbours)
    self.NumTx.append(NumTx)
    self.NumTxACk.append(NumTxACK)
    
  
 def update(Addr,Neighbours,NumTx,NumTxACK)
    i=get_ID(Addr)
    self.NeighboursRow[i]=Neighbours
    self.NumTx[i]+=NumTx
    self.NumTxACK[i]+=NumTxACK
  
  


