
import json
import time
import os
from openvisualizer.moteState     import moteState

import json

def dataParsingNeighbours(moteStateObject):
    '''Uses Json to parse the data obtained via the getStateElem function from the moteState class
    applied on the ST_NEIGHBOURS parameter'''
    obj = json.loads(moteStateObject.getStateElem(moteStateObject.ST_NEIGHBOURS))
    tab= []
    for k in range(len(obj['data'])):
        if obj['data'][k]['Neighbors'] != ' (None)':
            tab.append([obj['data'][k],obj['data'][k]['numTx'],obj['data'][k]['numTxACK']])
    return tab

def dataParsingSchedule(moteStateObject):
    '''Uses Json to parse the data obtained via the getStateElem function from the moteState class
    applied on the ST_SCHEDULE parameter'''
    obj = json.loads(moteStateObject.getStateElem(moteStateObject.ST_SCHEDULE))
    tab= []
    for k in range(len(obj['data'])):
        if obj['data'][k]['neighbor'] != ' (None)':
            tab.append(obj['data'][k])
    return tab



class Pce:
   Addresses= []       #Contains the addresses (16/32/64 bits) of all known motes and is used as a key to find their datas in other tables
   motes=[]            #Contains all known moteState objects
   NeighboursRow =[]   #Contains the Neighbors of each motes
   NumTx=[]            #Contains the number of sent messages to each Neighbors from each motes
   NumTxACk=[]         #Contains the number of recieved acks from each Neighbors to each motes
   Pdr=[]              #Contains the the Package Delivery Rate of each link
   lastUpdated=[]
   Schedule=[]          #Contains the Scheduling tables of each motes
   memorySize=30
   files=[]


   @classmethod
   def makeRoom(cls,index):
       '''Delete outdated datas from memories'''
       del cls.NeighboursRow[index][0]
       del cls.NumTx[index][0]
       del cls.NumTxACK[index][0]
       del cls.Pdr[index][0]
       del cls.Addresses[index][0]
       del cls.Schedule[index][0]
       del cls.motes[index][0]

   @classmethod
   def delete(cls,index):
       '''Delete all datas corresponding to the mote's index passed as an argument'''
       del cls.NeighboursRow[index]
       del cls.NumTx[index]
       del cls.NumTxACK[index]
       del cls.Pdr[index]
       del cls.Addresses[index]
       del cls.Schedule[index]
       del cls.motes[index]

   @classmethod
   def getID(cls,moteStateObject):
       ''''Is used to retrive the index corresponding to a mote's address
       so that it can be used as a primary key in other tables later on'''
       for i in range(len(cls.Addresses)):
           if (cls.Addresses[i]==moteStateObject.getStateElem(moteStateObject.ST_IDMANAGER)):
               return i
       return "Mote not found"

   @staticmethod
   def GetmoteElem(moteStateObject,elemName):
       '''Retrieves the value of the element elemName'''
       i=getID(moteStateObject)
       return(elemName[i])

   @classmethod
   def add(cls,moteStateObject):
       '''This function is used when a new mote connects on to the network
       It creates new fields in every tables to be completed with the new mote's datas'''
       cls.Addresses.append(moteStateObject.getStateElem(moteStateObject.ST_IDMANAGER))
       cls.motes.append(moteStateObject)
       linkInfo=dataParsingNeighbours(moteStateObject)
       scheduleInfo=dataParsingSchedule(moteStateObject)
       cls.NeighboursRow.append([linkInfo[i][0] for i in range(len(linkInfo))])
       cls.NumTx.append([linkInfo[i][1] for i in range(len(linkInfo))])
       cls.NumTxACk.append([linkInfo[i][2] for i in range(len(linkInfo))])
       cls.Pdr.append([linkInfo[i][1]/linkInfo[i][2] for i in range(len(linkInfo))])
       cls.Schedule.append([scheduleInfo[j] for j in range(len(scheduleInfo))])
       cls.files.append(open("mote"+cls.getID(moteStateObject))+".txt","w")

   @classmethod
   def update(cls,moteStateObject):
       '''This function is used when a mote's datas are updated the updating the values
       contained in each table
       -It only writes the used fields
       -When no Neighbour is detected it means that the mote is disconected and has to be deleted from
       the Network'''
       i=cls.getID(moteStateObject)
       if i== "Mote not found":
           cls.add(moteStateObject)
       else:
           linkInfo=dataParsingNeighbours(motes[i])
           scheduleInfo=dataParsingSchedule(motes[i])
           if len(linkInfo[i]==0):
               cls.delete(motes[i])
           else:
               if len(cls.Neighbours[i])>=memorySize:
                   makeRoom(cls,i)
               cls.NeighboursRow[i].append([linkInfo[j][0] for j in range(len(linkInfo))])
               cls.NumTx[i].append([linkInfo[j][1] for j in range(len(linkInfo))])
               cls.NumTxACK[i].append([linkInfo[j][2] for j in range(len(linkInfo))])
               cls.Pdr[i].append([linkInfo[j][1]/linkInfo[j][2] for j in range(len(linkInfo))])
               cls.Schedule[i].append([scheduleInfo[j] for j in range(len(scheduleInfo))])
               write(cls.files[i]("\n"+"update time:"+time.time()+cls.Addresses+"\n"+cls.NeighboursRow[i]+"\n"+cls.NumTx[i]+"\n"+cls.NumTxACK[i]+"\n"+cls.Schedule[i]+"\n"+"Pdr:"cls.Pdr[i]+"\n"))

    def __init__():
        for file in files:
