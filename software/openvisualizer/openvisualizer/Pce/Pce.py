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
    return("The given addres is not recognised"
    
  def get_PDR(Addr)
    i=get_ID(Addr)
    return(NumTxACK[i]/NumTx[i])
    
 def get_Neighbours(Addr)
    i=get_ID(Addr)
    return(NeigboursRow[i])
