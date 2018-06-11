import 




class PCE(     ):
  ADDRESSES= []
  NeighboursRow =[]
  NumTx=[]
  NumTxACk=[]
  
  def get_ID(Addr):
    k=0
    for i in range(len(ADDRESSES)-1)
      if ADDRESSES[i]==Addr
        return i
    raise SystemError('Unable to find Mote')
    
  def get_PDR(Addr)
    i=get_ID(Addr)
    return(NumTxACK[i]/NumTx[i])
    
  def get_Neighbours(Addr)
    i=get_ID(Addr)
    return(NeigboursRow[i])
           
  def add(Addr,Neighbours,NumTx,NumTxACK)
    ADDRESSES.append(Addr)
    NeighboursRow.append(Neighbours)
    NumTx.append(NumTx)
    NumTxACk.append(NumTxACK)
    
  
 def update(Addr,Neighbours,NumTx,NumTxACK)
    i=get_ID(Addr)
    NeighboursRow[i]=Neighbours
    NumTx[i]+=NumTx
    NumTxACK[i]+=NumTxACK
  
  


