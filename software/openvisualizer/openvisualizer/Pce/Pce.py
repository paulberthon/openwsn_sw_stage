import 




class PCE(     ):
  ADDRESSKEY = []
  NeighboursRow =[]
  NumTx=[]
  NumTxACk=[]
  
  def get_ID(Addr):
    k=0
    for i in range(len(ADDRESSKEY)-1)
      if ADDRESSKEY[i]==Addr
        return i
    return()
    
  def get_PDR(Addr)
    i=get_ID(Addr)
    return(NumTxACK[i]/NumTx[i])
    
  def get_Neighbours(Addr)
    i=get_ID(Addr)
    return(NeigboursRow[i])
           
  def add(Addr,Neighbours,NumTx,NumTxACK)
    ADDRESSKEY.append(Addr)
    NeighboursRow.append(Neighbours)
    NumTx.append(NumTx)
    NumTxACk.append(NumTxACK)
    
  
 def update(Addr,Neighbours,NumTx,NumTxACK)
    i=get_ID(Addr)
    NeighboursRow[i]=Neighbours
    NumTx[i]=NumTx
    NumTxACK[i]=NumTxACK
  
  


