import random
characters=[]
money=50
military=50
civWellbeing=50
environment=50
nations=[]
month=0
class Character:
   def __init__(self, name, job, respect, dialogue1, response1, dialogue2, response2, consequences):
       self.name=name
       self.job=job
       self.respect=respect
       self.dialogue1=dialogue1
       self.response1=response1
       self.dialogue2=dialogue2
       self.response2=response2
       self.consequences=consequences


   def getName(self):
       return self.name


   def getJob(self):
       return self.job


   def getRespect(self):
       return self.respect


   def getDialogue1(self):
       return self.dialogue1


   def getResponse1(self):
       return self.response1


   def getDialogue2(self):
       return self.dialogue2


   def getResponse2(self):
       return self.response2


   def getConsequences(self):
       return self.consequences


   def changeRespect(self, amt):
       self.respect += amt




class ForeignNations:
   def __init__(self, name, moneyamt, militaryamt, civwellbeingamt, environmentamt, relation):
       self.name=name
       self.moneyamt=moneyamt
       self.militaryamt=militaryamt
       self.civwellbeingamt=civwellbeingamt
       self.environmentamt=environmentamt
       self.relation=relation


   def getName(self):
       return self.name


   def getMoney(self):
       return self.moneyamt


   def getMilitary(self):
       return self.militaryamt


   def getCivWellbeing(self):
       return self.civwellbeingamt


   def getEnviroment(self):
       return self.environmentamt


   def getRelation(self):
       return self.relation


   def changeMoney(self, amt):
       self.moneyamt += amt


   def changeMilitary(self, amt):
       self.militaryamt += amt


   def changeCivWellbeing(self, amt):
       self.civwellbeingamt += amt


   def changeEnvironment(self, amt):
       self.environmentamt += amt


   def changeRelation(self, amt):
       self.relation += amt


   def setRelation(self, amt):
       self.relation = amt


def makeCharacters():


   for x in range(10):


       jobs = ["Vice President", "Treasury", "General", "Minister of Health", "Head of Environmental Protection",
               "Head of Secret Service", "Head of Research", "Governor", "Representative", "Diplomat"]
       names = ["Erik Guthrie","Vince Reilly","Chad Kane","Joyce Reeves","Julian Graves","Joel McKluwer","Sonja Henderson","Joyce Reeves","Gayle Snider","Eric Kemp"]
       dialogues1=[
           """ "Technology companies are asking for grants to enhance their research. They could help increase the quality of our citizens' lifes." """
           ,""" "The economy is booming we should increase our taxes on civilians." """
           ,""" "The surrounding nations are weak, we should go to war with them before they attack us." """
           ,""" "A pandemic is spreading throughout our country! What should we do?" """
           ,""" "We should invest in green technology, it would help our country's environment." """
           ,""" "There is an influx of refugees at our borders due to wars in our neighbouring nations. Should we let them in?" """
           ,""" "Should we invest in bioweapon research? It would greatly improve our nation's military strength." """
           ,""" "Sir, one of your political opponents is getting a lot of fame... It would be a lot simpler if he were to just disappear..." """
           ,""" "Our roads are severely underfunded, we should improve the quality of them." """
           ,""" "Foreign relations are at an all-time high. We should form an alliance with the neighboring countries." """]
       #good respect
       response1=[
           "Yes, I'll sign the grant/No way"
           ,"Increase tax slightly/Double the tax"
           ,"To arms!/No way"
           ,"Invest in a cure/Isolate the sick"
           ,"Yes, invest/No, don't invest"
           ,"Yes, let them in/No, close the borders"
           ,"Yes, invest in bioweapon research/No, don't invest"
           ,"Do what you must/What?! No way!"
           ,"Yes, let's fix our roads/No, I don't agree to any more funding"
           ,"Yes, let's form an alliance/No, we shouldn't"]
       dialogues2=[
           """ "Riots are breaking out in the nation. How should we address them?" """
           ,""" "Our citizens are demanding more funding for recreational activities." """
           ,""" "Our army is weak, we should impose a draft on half of our able men in the nation." """
           ,""" "The majority of our country does not have enough hospitals to treat the sick. Can we build more?" """
           ,""" "Companies are releasing excess pollution, we should regulate them more." """
           ,""" "Gangs have been smuggling in illegal contraband through our borders. Should we increase border patrols?" """
           ,""" "Foreign countries steal our nation's patents! Can we invest in lawyers to legally protect ourselves?" """
           ,""" "Crimes are surging throughout the night. We should impose a curfew for all our citizens." """
           ,""" "I think our citizen's would greatly benefit from the construction of more highways in our country." """
           ,""" "Too much hostility has been going on between our neighboring nations. They are now asking you to sign a peace treaty. I think you should." """]
       #bad respect
       response2=[
           "Recruit new police officers/Buy newer gear"
           ,"Yes, increase funding/No, don't increase funding"
           ,"Yes, impose the daft/No, don't draft them"
           ,"Yes, build more/No, don't build more"
           ,"Yes, regulate companies/No, don't"
           ,"Yes, increase border patrols/No, let them"
           ,"Yes, invest in lawyers/No, don't invest in lawyers"
           ,"Yes, impose a curfew/No, don't impose a curfew"
           ,"Yes, build more highways/No, don't build any more"
           ,"Yes, I'll sign the treaty/No, I won't sign"]
       consequences=[
           "05civ05mon/00civ00civ/10mil05civ/10mil05mon"
           ,"05mon00civ/20mon10civ/10civ05mon/00mon02civ"
           ,"10mon20mil/00mon00mon/20mil15civ/00mon02mil"
           ,"05civ20mon/05env20civ/10civ08mon/00mon15civ"
           ,"10env05mon/00mon06env/13env07mon/00mon10env"
           ,"05civ10mon/02civ00mon/07civ05mil/05mon03civ"
           ,"20mil10env/02env00mon/07civ10mon/00mon05civ"
           ,"10mil15civ/00mon05mil/10civ05mon/00mon07civ"
           ,"10civ10mon/00mon05civ/08civ15mon/00mon03civ"
           ,"10civ02mon/00mon02mil/10civ05mil/00mil10civ"]
                       # the first number is for positive consequence of first option of first dialogue
                       # the second number is for negative consequence of first option of first dialogue
                       # the third number is for positive consequence of second option of first dialogue
                       # the fourth number is for negative consequence of second option of first dialogue
                       # the fifth number is for positive consequence of first option of second dialogue
                       # the sixth number is for negative consequence of first option of second dialogue
                       # the seventh number is for positive consequence of second option of second dialogue
                       # the eith number is for negative consequence of second option of second dialogue


       name=names[x]
       job=jobs[x]
       respect=random.randrange(1,11)
       dialogue1=dialogues1[x]
       response1=response1[x]
       dialogue2=dialogues2[x]
       response2 = response2[x]
       consequences = consequences[x]


       characters.append(Character(name, job, respect, dialogue1, response1, dialogue2, response2, consequences))


def makeForeignNations():


   for x in range(3):
       names=["Friso","Lyger","Badenia"]
       name=names[x]
       moneyamt=random.randrange(25,76)
       militaryamt=random.randrange(25,76)
       civWellbeingamt=random.randrange(25,76)
       environmentamt=random.randrange(25,76)
       relation=random.randrange(45,56)


       nations.append(ForeignNations(name, moneyamt, militaryamt, civWellbeingamt, environmentamt, relation))


def talk():
   global money,military,civWellbeing,environment,month


   x=random.randrange(0, len(characters)-1)
   print("---------------------------------")
   print(characters[x].getJob(),characters[x].getName(),"walks into your office.")
   if characters[x].getRespect()>5:
       print(characters[x].getDialogue1())


       response=characters[x].getResponse1()
       dialogue=1
   else:
       print(characters[x].getDialogue2())


       response = characters[x].getResponse2()
       dialogue=2


   response=response.split("/")
   response1=response[0]
   response2=response[1]


   print("1)", response1)
   print("2)", response2)


   choice = int(input("Please enter your choice. (1/2)"))
   consequences = characters[x].getConsequences()
   consequences = consequences.split("/")


   if dialogue==1:
       if choice==1:
           results=consequences[0]
           characters[x].changeRespect(random.randrange(1, 4))
       if choice==2:
           results=consequences[1]
           characters[x].changeRespect(random.randrange(-2, 1))
   if dialogue==2:
       if choice==1:
           results=consequences[2]
           characters[x].changeRespect(random.randrange(1, 4))
       if choice==2:
           results=consequences[3]
           characters[x].changeRespect(random.randrange(-2, 1))


   print("------------------------")
   if results[2]+results[3]+results[4]=="mon":
       print("+",int(results[0]+results[1]),"Money")
       money += int(results[0] + results[1])


   if results[2]+results[3]+results[4]=="mil":
       print("+",int(results[0]+results[1]),"Military Strength")
       military += int(results[0] + results[1])


   if results[2]+results[3]+results[4]=="civ":
       print("+",int(results[0]+results[1]),"Civilian Wellbeing")
       civWellbeing += int(results[0] + results[1])


   if results[2]+results[3]+results[4]=="env":
       print("+",int(results[0]+results[1]),"Environment")
       environment += int(results[0] + results[1])


   if results[7]+results[8]+results[9]=="mon":
       print("-",int(results[5]+results[6]),"Money")
       money -= int(results[5] + results[6])


   if results[7]+results[8]+results[9]=="mil":
       print("-",int(results[5]+results[6]),"Military Strength")
       military -= int(results[5] + results[6])


   if results[7]+results[8]+results[9]=="civ":
       print("-",int(results[5]+results[6]),"Civilian Wellbeing")
       civWellbeing -= int(results[5] + results[6])


   if results[7]+results[8]+results[9]=="env":
       print("-",int(results[5]+results[6]),"Environment")
       environment -= int(results[5] + results[6])


   month+=1


   print("------------------------")
   print("Money:", money)
   print("Military Strength:", military)
   print("Civilian Wellbeing:", civWellbeing)
   print("Environment:", environment)
   print("------------------------")


def foriegnRelations():
   done = False
   while not done:
       print("--------------------------------------------------")
       choice = int(input("Diplomacy (1), Trade (2), Back to Home Screen (3)"))
       if choice == 1:
           diplomacy()
       elif choice == 2:
           trade()
       elif choice==3:
           done = True
atWar=["","",""]
atWar[0] = "Not at War"
atWar[1] = "Not at War"
atWar[2] = "Not at War"
relationInfo = ["", "", ""]
howFarIsWar=0


def diplomacy():
   global money, military, civWellbeing, environment,howFarIsWar


   for x in range(3):
       if nations[x].getRelation() == 0:
           atWar[x]="At War"
       if nations[x].getRelation() >= 90:
           relationInfo[x] = "(Excellent)"
       elif nations[x].getRelation() >= 70:
           relationInfo[x] = "(Great)"
       elif nations[x].getRelation() >= 50:
           relationInfo[x] = "(Good)"
       elif nations[x].getRelation() >= 30:
           relationInfo[x] = "(Poor)"
       else:
           relationInfo[x] = "(Bad)"


   print("What country do you want to manage your relation with?")
   print("(1)", nations[0].getName(),"| Status:",atWar[0])
   print("(2)", nations[1].getName(),"| Status:",atWar[1])
   print("(3)", nations[2].getName(),"| Status:",atWar[2])
   nationNum = int(input("Please enter your choice. (1/2/3)"))
   nationNum-=1
   if atWar[nationNum]=="Not at War":
       print("You are currently at peace with", nations[nationNum].getName(),"who has a military strength of",
             nations[nationNum].getMilitary(),". Your relation with them has been given a score of",
             nations[nationNum].getRelation(),"out of 100",relationInfo[nationNum])
       choice=input("Do you want to declare war on "+nations[nationNum].getName()+"? (Y/N)")
       if choice=="Y"or choice=="y":
           print("You have declared war on "+nations[nationNum].getName()+"!")
           money-=round((money/5))
           atWar[nationNum] = "At War"
           nations[nationNum].setRelation(0)
           print("Please check back later for an update on the war.")
   else:
       if military>nations[nationNum].getMilitary():
           howFarIsWar = random.randrange(0, int((round(military-nations[nationNum].getMilitary())/10)+2))
           if howFarIsWar>0:
               print("You seem to be winning the war... Please check back later for more updates...")
               nations[nationNum].changeMoney(-round((nations[nationNum].getMoney() / 8)))
               nations[nationNum].changeMilitary(-round((nations[nationNum].getMilitary() / 4)))
               money -= round((money / 16))
               military -= round((military / 8))
               howFarIsWar -= random.randrange(0, howFarIsWar)
           else:
               print("You have been winning the war for a while now! "+nations[nationNum].getName()+" is asking for a peace treaty.")
               print("They offer",(round((nations[nationNum].getMoney()/2))),"of their money as a reparation for the war.")
               choice=input("Do you accept? (Y/N)")
               if choice=="Y" or choice=="y":
                   money += round((nations[nationNum].getMoney()/2))
                   nations[nationNum].changeMoney(-round((nations[nationNum].getMoney()/2)))
                   nations[nationNum].changeRelation(50-round((nations[nationNum].getMoney()/2)))
                   atWar[nationNum] = "Not at War"
                   howFarIsWar=-1
                   print("You have successfully signed a peace treaty with",nations[nationNum].getName())
       else:
           howFarIsWar = random.randrange(0, int(round((nations[nationNum].getMilitary() - military) / 10)+2))
           if howFarIsWar > 0:
               print("Unfortunately, you seem to be losing the war... Please check back later for more updates...")
               money -= round((money / 8))
               military -= round((military / 4))
               nations[nationNum].changeMoney(-round((nations[nationNum].getMoney() / 16)))
               nations[nationNum].changeMilitary(-round((nations[nationNum].getMilitary() / 8)))
               howFarIsWar -= random.randrange(0, howFarIsWar)
           else:
               print("Unfortunately, you have been losing the war for a while now. " + nations[
                   nationNum].getName() + " is allowing you a chance to surrender.")
               print("They ask you to offer" , (
                   round((nations[nationNum].getMoney() / 2))) , "of your money as a reparation for the war.")
               choice = input("Do you agree? (Y/N)")
               if choice=="Y" or choice=="y":
                   money -= round((nations[nationNum].getMoney() / 2))
                   nations[nationNum].changeMoney(round((nations[nationNum].getMoney() / 2)))
                   nations[nationNum].changeRelation(50 + round((money / 10)))
                   atWar[nationNum] = "Not at War"
                   howFarIsWar = -1
                   print("You have successfully signed a peace treaty with", nations[nationNum].getName())


def trade():
   global money,military,civWellbeing,environment


   print("What country do you want to trade with?")
   print("(1)", nations[0].getName())
   print("(2)", nations[1].getName())
   print("(3)", nations[2].getName())
   nationNum = int(input("Please enter your choice. (1/2/3)"))
   nationNum-=1


   print("What resource are you looking for?")
   choice = int(input("Money (1), Military (2)"))
   if choice==1:
       if nations[nationNum].getRelation()>=50 and nations[nationNum].getMoney()>=30:
           print(nations[nationNum].getName() , "proposes to trade" , round(
               nations[nationNum].getMoney() / 3) , "of their money for" , round(
               nations[nationNum].getMilitary() / 3) , "of your military.")
           choice = input("Do you accept? (Y/N)")
           if choice=="Y"or choice=="y":
               money += round(nations[nationNum].getMoney() / 3)
               military -= round(nations[nationNum].getMilitary() / 3)
               nations[nationNum].changeMoney(-round(nations[nationNum].getMoney() / 3))
               nations[nationNum].changeMilitary(round(nations[nationNum].getMilitary() / 3))
               nations[nationNum].changeRelation(5)
               print("Trade complete.")
           else:
               nations[nationNum].changeRelation(-2)
       else:
           print(nations[nationNum].getName(), "does not want to trade with you.")
   elif choice == 2:
       if nations[nationNum].getRelation() >= 50 and nations[nationNum].getMilitary() >= 30:
           print(nations[nationNum].getName(), "proposes to trade", round(
               nations[nationNum].getMilitary() / 3), "of their military for", round(
               nations[nationNum].getMoney() / 3), "of your money.")
           choice = input("Do you accept? (Y/N)")
           if choice == "Y" or choice == "y":
               military += round(nations[nationNum].getMilitary() / 3)
               money -= round(nations[nationNum].getMoney() / 3)
               nations[nationNum].changeMilitary(-round(nations[nationNum].getMilitary() / 3))
               nations[nationNum].changeMoney(round(nations[nationNum].getMoney() / 3))
               nations[nationNum].changeRelation(5)
               print("Trade complete.")
           else:
               nations[nationNum].changeRelation(-2)
       else:
           print(nations[nationNum].getName(), "does not want to trade with you.")


def main():
   global money, military, civWellbeing, environment,month


   makeCharacters()
   makeForeignNations()


   done=False
   while not done:


       if money<=0 or military<=0 or civWellbeing<=0 or environment<=0:


           print("One of your stats dropped to zero!")
           print("You have been overthrown and have lost your power.")
           print("You led your nation for ",month," months.")
           print("Thank you for playing.")
           done=True


       if done!=True:
           choice = int(input("Talk to Advisors (1), Foreign Relations (2), Objective (3), How to Play (4), Credits (5), Quit (6)"))
           if choice==1:
               talk()
           elif choice==2:
               foriegnRelations()
           elif choice==3:
               print("Lead your nation effectively by balancing various factors such as")
               print("financial stability, military strength, citizen happiness, and environmental conservation.")
               print("Make strategic decisions to ensure the prosperity and security of your country.")
           elif choice==4:
               print("One month passes everytime you talk to one of your advisors. You can also trade or enact war with foreign nations. Good luck!")
           elif choice==5:
               print("Made by: Adrian Klos")
           elif choice==6:
               print("Thank you for playing.")
               done=True


main()
