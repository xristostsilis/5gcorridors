import math

print("5G NR LINK BUDGET CALCULATOR BASED ON 3GPP TR 38.901 V17.0.0 2022-03 \n")



print("Do you want to see stats for nerds? (type y or n)\n")

stats=input()

##default values:

d2d=4508 ## for basic link budget test pass or fail
fc=1500 ##center frequency in Mhz, you can change this one if you know what you are doing :)
fc=fc*1000000 ##fc in hz
hbs=23 ##base station height
hut=1.5 ##reciever height
h=5
w=20 #street width



#calculate d3d (pythagorean theorim)

d3d = math.sqrt((hbs-hut)**2 + d2d**2) ##square root - exponation in python is ** not ^


if stats==("y"):
    print("d3d:",d3d,"\n")


c= 3*(10**8) #speed of light in meters per second :)

###dbp=breakpoint distance

dbp=(2*(math.pi)*hbs*hut*fc)/c 

if stats==("y"):
    print("Breakpoint distance is:", dbp, "meters \n")

##RMA LOS

if stats==("y"):
    print("Rural Macro 3D-RMa LOS: \n")

if 10<d2d<dbp:
    if stats==("y"):
        print("Calculating PL1 :) ..... (because d2d entered by user is 10<d2s<dbp) \n")
    Rma_LOS_PL1=(20*math.log10(40*math.pi*d3d*(fc/1000000000)/3)) + min(0.03*(h**1.72),10)*math.log10(d3d) - min(0.044*(h**1.72),14.77) + 0.002*math.log10(h)*d3d ##this formula needs fc in ghz
    if stats==("y"):
        print("Propagation model Path loss Rma: ",Rma_LOS_PL1," dB\n")
    ##for RMA NLOS:
    PL_los=Rma_LOS_PL1
    
elif dbp<d2d<10000:
    if stats==("y"):
        print("Calculating PL2 :)..... (because d2d entered by user is dbp<d2d<10km)\n")
    Rma_LOS_PL1_for_dbp=(20*math.log10(40*math.pi*dbp*(fc/1000000000)/3)) + min(0.03*(h**1.72),10)*math.log10(d3d) - min(0.044*(h**1.72),14.77) + 0.002*math.log10(h)*dbp ##this formula needs fc in ghz
    Rma_LOS_PL2= Rma_LOS_PL1_for_dbp + 40*math.log10(d3d/dbp)+12 ##in db
    if stats==("y"):
        print("Propagation model Path loss Rma: ",Rma_LOS_PL2, " dB\n")
    PL_los=Rma_LOS_PL2
else:
    if stats==("y"):
        print("d2d should be between 10m and 10km :( please try again.")




##RMA NLOS

PLnew=161.04 - 7.1*math.log10(w)+7.5*math.log10(h)-(24.37-3.7*((h/hbs)**2))*math.log10(hbs)+(43.42-3.1*math.log10(hbs))*(math.log10(d3d)-3) + 20*math.log10(fc/1000000000)-3.2*(((math.log10(11.75*hut))**2)-4.97)

Rma_NLOS_PL= max(PL_los,PLnew)

if stats==("y"):
    print("\nPropagation model Path loss Rma NLOS= ", Rma_NLOS_PL, "dB \n")



print("\n Press 1 for RMA LOS or 2 for RMA NLOS.......\n")

x=int(input())

while (x!=1 and x!=2):
    x=int(input())



if x==1:
    pathlossPropagationModel=PL_los
elif x==2:
    pathlossPropagationModel= Rma_NLOS_PL


##arxikopoihsh parametrwn gia link budget

transmitPowerTX=20.21 ##dbm
antennaGainTX=17 ##db
cableLossTX = 2 ##db
antennaGainRX = 0 ##db
cableLossRX = 0 ##db
penetrationLoss=3
foliageLoss=4
bodyLoss=3
interferenceMargin=3
rainIceMargin=0
slowFadingMargin=7
penetrationLossin=0
attenuation=0

link_budget= transmitPowerTX + antennaGainTX - cableLossTX + antennaGainRX - cableLossRX - pathlossPropagationModel - penetrationLoss -foliageLoss - bodyLoss - interferenceMargin - rainIceMargin - slowFadingMargin - penetrationLossin- attenuation

print("\nLink Budget:",link_budget, "\n")


##reciever sensitivity (dBm)

bandwidth = 20 ##in mhz, default is 20 mhz

thermalNoise = -174 + 10*math.log2(bandwidth)

noiseFigure=16 #default value

sinr= -6 #default value

recieverSensitivity = noiseFigure + thermalNoise +sinr

print("Reciever sensitivity", recieverSensitivity, "\n")

if recieverSensitivity<link_budget:
    print("Pass :)\n")
else:
    print("Fail :(\n")


print("\n\n--------------------------------------------\n\n")
    



def maximiseModel(fc,x,stats):

    result="fail"

    ##default values:

    d2d=10000 #max 10km

    fc=fc*1000000 ##fc in hz
    bs=23 ##base station height
    hut=1.5 ##reciever height
    h=5
    w=20 #street width
    c= 3*(10**8) #speed of light in meters per second :)


    dbp=(2*(math.pi)*hbs*hut*fc)/c
    while (result!="pass"):

        #print("Do you want to see stats for nerds? (type y or n)\n")

        #stats="n"

        


        #calculate d3d (pythagorean theorim)

        d3d = math.sqrt((hbs-hut)**2 + d2d**2) ##square root - exponation in python is ** not ^


        if stats==("y"):
            print("d3d:",d3d,"\n")


        

        ###dbp=breakpoint distance

        



        if stats==("y"):
            print("Breakpoint distance is:", dbp, "meters \n")

        ##RMA LOS

        if stats==("y"):
            print("Rural Macro 3D-RMa LOS: \n")

        if 10<d2d<dbp:
            if stats==("y"):
                print("Calculating PL1 :) ..... (because d2d entered by user is 10<d2s<dbp) \n")
            Rma_LOS_PL1=(20*math.log10(40*math.pi*d3d*(fc/1000000000)/3)) + min(0.03*(h**1.72),10)*math.log10(d3d) - min(0.044*(h**1.72),14.77) + 0.002*math.log10(h)*d3d ##this formula needs fc in ghz
            if stats==("y"):
                print("Propagation model Path loss Rma: ",Rma_LOS_PL1," dB\n")
            ##for RMA NLOS:
            PL_los=Rma_LOS_PL1
            
        elif 10<dbp<d2d<=10000:
            if stats==("y"):
                print("Calculating PL2 :)..... (because d2d entered by user is dbp<d2d<10km)\n")
            Rma_LOS_PL1_for_dbp=(20*math.log10(40*math.pi*dbp*(fc/1000000000)/3)) + min(0.03*(h**1.72),10)*math.log10(d3d) - min(0.044*(h**1.72),14.77) + 0.002*math.log10(h)*dbp ##this formula needs fc in ghz
            Rma_LOS_PL2= Rma_LOS_PL1_for_dbp + 40*math.log10(d3d/dbp)+12 ##in db
            if stats==("y"):
                print("Propagation model Path loss Rma: ",Rma_LOS_PL2, " dB\n")
            PL_los=Rma_LOS_PL2
        else:
            if stats==("y"):
                print("d2d should be between 10m and 10km :( please try again.")




        ##RMA NLOS

        PLnew=161.04 - 7.1*math.log10(w)+7.5*math.log10(h)-(24.37-3.7*((h/hbs)**2))*math.log10(hbs)+(453.42-3.1*math.log10(hbs))*(math.log10(d3d)-3) + 20*math.log10(fc/1000000000)-3.2*(((math.log10(11.75*hut))**2)-4.97)

        Rma_NLOS_PL= max(PL_los,PLnew)

        if stats==("y"):
            print("\nPropagation model Path loss Rma NLOS= ", Rma_NLOS_PL, "dB \n")



        x=int(x)

        while (x!=1 and x!=2):
            x=int(input())



        if x==1:
            pathlossPropagationModel=PL_los
        elif x==2:
            pathlossPropagationModel= Rma_NLOS_PL


        ##arxikopoihsh parametrwn gia link budget

        transmitPowerTX=20.21 ##dbm
        antennaGainTX=17 ##db
        cableLossTX = 2 ##db
        antennaGainRX = 0 ##db
        cableLossRX = 0 ##db
        penetrationLoss=3
        foliageLoss=4
        bodyLoss=3
        interferenceMargin=3
        rainIceMargin=0
        slowFadingMargin=7
        penetrationLossin=0
        attenuation=0

        link_budget= transmitPowerTX + antennaGainTX - cableLossTX + antennaGainRX - cableLossRX - pathlossPropagationModel - penetrationLoss -foliageLoss - bodyLoss - interferenceMargin - rainIceMargin - slowFadingMargin - penetrationLossin- attenuation


        if stats==("y"):
            print("\nLink Budget:",link_budget, "\n")


        ##reciever sensitivity (dBm)

        bandwidth = 20 ##in mhz, default is 20 mhz

        thermalNoise = -174 + 10*math.log2(bandwidth)

        noiseFigure=16 #default value

        sinr= -6 #default value

        recieverSensitivity = noiseFigure + thermalNoise +sinr


        if stats==("y"):
            print("Reciever sensitivity", recieverSensitivity, "\n")

        

        if recieverSensitivity<link_budget:
            result="pass"
        else:
            d2d=d2d-100

            



        if (result=="pass"):
            print("\nMax 2d distance for this frequency is somewhere close", d2d,"meters ...... \n\n\n")
            d2dfinal=d2d+100 ##i may have decreased it a lot so i will create a new function called akriveia to make it perfect

            print("Do you want to see stats for nerds for intensive calculations? Type y or n.....\n")

            statistics=input()
            
            akriveia(fc,losornlos,d2dfinal,statistics) 





                            

def akriveia(fc,x,d2d,stats):
            #
           
            
            dbp=0 ##
            

            result="fail"

            ##default values:

            

            ##fc in hz
            bs=23 ##base station height
            hut=1.5 ##reciever height
            h=5
            w=20 #street width
            c= 3*(10**8) #speed of light in meters per second :)


            dbp=(2*(math.pi)*hbs*hut*fc)/c

         
            
            while (result!="pass"):

            

                #print("Do you want to see stats for nerds? (type y or n)\n")

                

                


                #calculate d3d (pythagorean theorim)

                d3d = math.sqrt((hbs-hut)**2 + d2d**2) ##square root - exponation in python is ** not ^


                if stats==("y"):
                    print("d3d:",d3d,"\n")


                

                ###dbp=breakpoint distance

                
               


                if stats==("y"):
                    print("Breakpoint distance is:", dbp, "meters \n")

                ##RMA LOS

                if stats==("y"):
                    print("Rural Macro 3D-RMa LOS: \n")

                if 10<d2d<dbp:
                    if stats==("y"):
                        print("Calculating PL1 :) ..... (because d2d entered by user is 10<d2s<dbp) \n")
                    Rma_LOS_PL1=(20*math.log10(40*math.pi*d3d*(fc/1000000000)/3)) + min(0.03*(h**1.72),10)*math.log10(d3d) - min(0.044*(h**1.72),14.77) + 0.002*math.log10(h)*d3d ##this formula needs fc in ghz
                    if stats==("y"):
                        print("Propagation model Path loss Rma: ",Rma_LOS_PL1," dB\n")
                    ##for RMA NLOS:
                    PL_los=Rma_LOS_PL1
                    
                elif 10<dbp<d2d<=10000:
                    if stats==("y"):
                        print("Calculating PL2 :)..... (because d2d entered by user is dbp<d2d<10km)\n")
                    Rma_LOS_PL1_for_dbp=(20*math.log10(40*math.pi*dbp*(fc/1000000000)/3)) + min(0.03*(h**1.72),10)*math.log10(d3d) - min(0.044*(h**1.72),14.77) + 0.002*math.log10(h)*dbp ##this formula needs fc in ghz
                    Rma_LOS_PL2= Rma_LOS_PL1_for_dbp + 40*math.log10(d3d/dbp)+12 ##in db
                    if stats==("y"):
                        print("Propagation model Path loss Rma: ",Rma_LOS_PL2, " dB\n")
                    PL_los=Rma_LOS_PL2
                else:
                    if stats==("y"):
                        print("d2d should be between 10m and 10km :( please try again.")


              

                ##RMA NLOS

                PLnew=161.04 - 7.1*math.log10(w)+7.5*math.log10(h)-(24.37-3.7*((h/hbs)**2))*math.log10(hbs)+(43.42-3.1*math.log10(hbs))*(math.log10(d3d)-3) + 20*math.log10(fc/1000000000)-3.2*(((math.log10(11.75*hut))**2)-4.97)

                Rma_NLOS_PL= max(PL_los,PLnew)

                if stats==("y"):
                    print("\nPropagation model Path loss Rma NLOS= ", Rma_NLOS_PL, "dB \n")



                x=int(x)

                while (x!=1 and x!=2):
                    x=int(input())



                if x==1:
                    pathlossPropagationModel=PL_los
                elif x==2:
                    pathlossPropagationModel= Rma_NLOS_PL

       
                ##arxikopoihsh parametrwn gia link budget

                transmitPowerTX=20.21 ##dbm
                antennaGainTX=17 ##db
                cableLossTX = 2 ##db
                antennaGainRX = 0 ##db
                cableLossRX = 0 ##db
                penetrationLoss=3
                foliageLoss=4
                bodyLoss=3
                interferenceMargin=3
                rainIceMargin=0
                slowFadingMargin=7
                penetrationLossin=0
                attenuation=0

             


                link_budget= transmitPowerTX + antennaGainTX - cableLossTX + antennaGainRX - cableLossRX - pathlossPropagationModel - penetrationLoss -foliageLoss - bodyLoss - interferenceMargin - rainIceMargin - slowFadingMargin - penetrationLossin- attenuation

                

                if stats==("y"):
                    print("\nLink Budget:",link_budget, "\n")


                ##reciever sensitivity (dBm)

                bandwidth = 20 ##in mhz, default is 20 mhz

                thermalNoise = -174 + 10*math.log2(bandwidth)

                noiseFigure=16 #default value

                sinr= -6 #default value

                recieverSensitivity = noiseFigure + thermalNoise +sinr


                if stats==("y"):
                    print("Reciever sensitivity", recieverSensitivity, "\n")

                

                if recieverSensitivity<link_budget:
                    result="pass"
                else:
                    d2d=d2d-1




                if (result=="pass"):
                    print("\nMax 2D distance for",fc/1000000000 ," Ghz, is exactly", d2d," meters:)\n")



                    print("let's calculate the cost\n")

                    capexpernewsitethroughput=150  ###capex for new site at 3.5ghz   divided by 1000 euros
                    capexexistingupgradethroughput=70 ###capex for existing site upgrade to 3.5  divided by 1000 euros
                    capexexistingslow=60 ##capex existing upgrade to 700mhz  divided by 1000 euros
                    capexnewslow=70 ##capex new at 700mhz  divided by 1000 euros
                    opex=17 ## opex divided by 1000 euros per year 

                    sitesneeded=100/(2*(d2d/1000))  ##sites needed per 100km divided by 2 times the d2d distance at km because a site transmitts at all direction

                    
                    site=sitesneeded/100 ##sites needed per km

                    frequensyinghz=fc/1000000000

                    if(frequensyinghz<4 and frequensyinghz>2):  ##checking to see if high throughput is needed

                        print("Type new for new site or old for existing site upgrade\n")

                        typesite=input()

                        if (typesite=="new"):

                            totalcost=site*capexpernewsitethroughput+site*opex ##multiplied eiach cost per site to give price per km

                            print("The Capex needed for transmitting at", fc/1000000000 , " by installing new sites is:",site*capexpernewsitethroughput,"plus OPEX for one year:",site*opex, "\n\nTOTAL COST PER KM FOR ONE YEAR:",totalcost)


                        else:

                            totalcost=site*capexexistingupgradethroughput+site*opex
                            print("The Capex needed for transmitting at", fc/1000000000 , "with the use of existing sites is:",site*capexexistingupgradethroughput, "plus OPEX for one year :",site*opex, "\n\nTOTAL COST PER KM FOR ONE YEAR:",totalcost)



                    else:  ##checking if high range is needed

                        print("Type new for new site or old for existing site upgrade\n")

                        typesite=input()

                        if (typesite=="new"):

                            totalcost=site*capexnewslow+site*opex
                            

                            print("The Capex needed for transmitting at", fc/1000000000 , " by installing new sites is:",site*capexnewslow,"plus OPEX for one year:",site*opex, "\n\nTOTAL COST PER KM FOR ONE YEAR :",totalcost)


                        else:

                            totalcost=site*capexexistingslow+site*opex

                            
                            print("The Capex needed for transmitting at", fc/1000000000 , "with the use of existing sites is:",site*capexexistingslow, "plus OPEX for one year:",site*opex, "\n\nTOTAL COST PER KM FOR ONE YEAR:",totalcost)
                        
                        

print("Do you want to see stats for nerds? Type y or n...\n")

stats1=input()

print("\n Enter the frequency you want to find max D2D distance for example 3500 (Mhz) :)\n")
userinputfrequency=int(input())

print("\n Enter 1 for LOS and 2 for NLOS \n")

losornlos=int(input())

maximiseModel(userinputfrequency,losornlos,stats1)






