def main():
      A1, A2=map(int,input("input Good1: , Good2 . for nation 1 ").split())
      B1, B2 =map(int,input("input Good1: , Good2 .for nation 2 ").split())
      oc1 , oc2 ,oc3 , oc4 = oppcost(A1,A2,B1,B2)

      AA, CA , OC ,TR , PG , CG = map(int, input("Choose 0 for no 1 for yes: Absolute advantage, Comperative advantage, OppCost, TradeRatio,Production gains, consumption gains").split())
      if AA == 1:
           AbsoluteAdvantage(A1,A2,B1,B2)
      if CA == 1:
           ComperativeAdvantage(oc1,oc3,oc2,oc4,A1,B1,A2,B2)
      if OC == 1:
           print(f'OC of G1 in N1 {oc1}, OC of G2 in N1 {oc2}, OC of G1 in N2 {oc3} OC of G2 in N2 {oc4}')
      if TR == 1:
           traderatio(oc1,oc3,oc2,oc4)
      if PG == 1:
           PCA1,PCA2,PCB1,PCB2 = consumptionNproduction()
           PG1,PG2=productiongain(A1,B1,A2,B2,PCA1,PCB1,PCA2,PCB2)
           print(f'Production gains in G1: {PG1}. Production gains in G2: {PG2}.')
      if CG == 1:
           _, _, G1S, G2S = ComperativeAdvantage (oc1,oc3,oc2,oc4,A1,B1,A2,B2)
           consumptiongains(G1S,G2S,PCA1,PCA2,PCB1,PCB2)
           NGC11,NGC12,NGC21,NGC22 =consumptiongains(G1S,G2S,PCA1,PCA2,PCB1,PCB2)
           print(f'Consumption gains for G1 and G2 in Nation 1 : {NGC11} , {NGC12}')
           print(f'Consumption gains in G1 and G2 in Nation 2 : {NGC21} , {NGC22}')

           
       
           
           
           
          
     
     

     

     
    

def oppcost(A1,A2,B1,B2):
     oc1=int(A2)/int(A1)  #opp cost of good 1 in nation 1
     oc2=1/oc1     #opp cost of good 2 in nation 1
     oc3=int(B2)/int(B1) #opp cost of good 1 in nation 2
     oc4=1/oc3     #opp cost of good 2 in nation 2     
     return oc1,oc2,oc3,oc4 

def AbsoluteAdvantage(A1,A2,B1,B2):
     absolute1 = A1>B1
     absolute2 = A2>B2
     A1B1=False
     A2B2=False
     if A1==B1 or A2==B2:
          print(" Good 1 equal in both nation:",A1==B1,"Good 2 equal in both nation:",A2==B2)
          A1B1= A1==B1
          A2B2= A2==B2
     if absolute1== True:
          print("Nation 1 has an AA in Good 1")
     elif absolute1 == False and A1B1==False:
          print("nation 2 has an AA in Good 1 ")
     if absolute2 == True:
          print(f'nation 1 has an AA in Good 2')
     elif absolute2==False and A2B2==False:
          print('Nation 2 has AA in Good 2')
     return absolute1, absolute2



def ComperativeAdvantage (oc1,oc3,oc2,oc4,A1,B1,A2,B2):
     comperative1= oc1<oc3
     comperative2= oc1>oc3
     if comperative1==True:
          print("nation 1 has a comeprative advantage in good 1, and nation 2 has a comperative advantage in good 2")
     elif comperative2==True:
          print("nation 2 has a comperative advantage in good 1, and nation 1 has a comeprative advantage in good 2")
     elif oc1==oc3:
          print("There is no comperative advantage and no comperative trade")
     if min(oc1,oc3)==oc1:
          G1S=A1
     else:
          G1S=B1
     if min(oc2,oc4)==oc2:
          G2S=A2
     else:
          G2S=B2
     return comperative1, comperative2, G1S , G2S



def traderatio(oc1,oc3,oc2,oc4):
     print("the trade ratio of good 1 is ", min(oc2,oc4), "G2< 1 G1<", max(oc2,oc4),"G2")
     print("the trade ratio of good 2 is ", min(oc1,oc3), "G1< 1 G2<", max(oc1,oc3),"G1")

def consumptionNproduction():
     PCA1, PCA2 = map(int,input(" P&C of Good1: , Good2 . for nation 1 ").split())
     PCB1, PCB2 = map(int,input(" P&C of Good1: , Good2 . for nation 2 ").split())
     return PCA1,PCA2,PCB1,PCB2

def productiongain(A1,B1,A2,B2,PCA1,PCB1,PCA2,PCB2):
     PG1=max(A1,B1)-(PCA1 +PCB1)
     PG2=max(A2,B2)-(PCA2 + PCB2)
     return PG1,PG2
def consumptiongains(G1S,G2S,PCA1,PCA2,PCB1,PCB2):
     T1 , T2 = map(int,input("G1 is traded for G2, ").split())
     NGC11=(G1S-T1)-PCA1
     NGC12=(T2)-PCA2
     NGC21=(T2)-PCB1
     NGC22=(G2S-T2)-PCB2
     return NGC11,NGC12,NGC21,NGC22,
main()