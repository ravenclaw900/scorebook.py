import sys, datetime
from PyQt4 import QtCore, QtGui, uic
first=False
second=False
third=False
homeRuns=0
awayRuns=0
homeLineup = []
homeLineupNumber=0
awayLineup = []
awayLineupNumber=0
outs=0
awayBatting=True
homeTeam=''
awayTeam=''
intro=True
Type=0
firstBackup=False
secondBackup=False
thirdBackup=False
homeRunsBackup=0
awayRunsBackup=0
strikes=0
balls=0
fileName=''
outBackup=0

def homeProgress():
    global homeLineupNumber, homeBatter, homeLineup
    homeLineupNumber = homeLineupNumber + 1
    if homeLineupNumber > 8:
        homeLineupNumber = 0
    homeBatter=homeLineup[homeLineupNumber]

def awayProgress():
    global awayLineupNumber, awayBatter, awayLineup
    awayLineupNumber = awayLineupNumber + 1
    if awayLineupNumber > 8:
        awayLineupNumber = 0
    awayBatter=awayLineup[awayLineupNumber]


baseclass, formclass = uic.loadUiType("Scorebook.ui")

class MyWindow(baseclass, formclass):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.actionSingle.triggered.connect(self.single_Click)
        self.actionDouble.triggered.connect(self.double_Click)
        self.actionTriple.triggered.connect(self.triple_Click)
        self.actionHomeRun.triggered.connect(self.homeRun_Click)
        self.actionHitByPitch.triggered.connect(self.hitByPitch_Click)
        self.actionError.triggered.connect(self.error_Click)
        self.actionSteal.triggered.connect(self.steal_Click)
        self.done.clicked.connect(self.done_Click)
        self.start.clicked.connect(self.start_Click)
        self.next.clicked.connect(self.next_Click)
        self.next.hide()
        self.toolBar.hide()
        self.awayRuns.hide()
        self.actionFoul.triggered.connect(self.foul_Click)
        self.actionStrike.triggered.connect(self.strike_Click)
        self.actionBall.triggered.connect(self.ball_Click)
        self.actionPinchHitter.triggered.connect(self.pinchHitter_Click)
        self.actionOut.triggered.connect(self.out_Click)
        self.actionReminder.triggered.connect(self.reminder_Click)

    def done_Click(self):
        global homeTeam, awayTeam, intro, Type, homeLineup, awayLineup, first, second, third, awayBatting, homeRuns, awayRuns, firstBackup, secondBackup, thirdBackup, outs, awayRunsBackup, homeRunsBackup, homeLineupNumber, awayLineupNumber, fileName
        self.question.setText('')
        if intro and Type==0:
            homeTeam = str(self.answer.text())
            
            self.question.setText("Please enter the away team name.")
            Type=1
        elif intro and Type==1:
            awayTeam = str(self.answer.text())
            self.awayRuns.show()
            dateString=datetime.datetime.now()
            fileList=[str(dateString.month), '-', str(dateString.day), '-', str(dateString.year), ' ', str(awayTeam), ' ', '@', ' ', str(homeTeam), '.txt']
            fileName = ''.join(fileList)
##            recapFile = open(fileName, 'w')
            homeList1 = ['What is the last name of the first person in the', homeTeam, 'lineup']
            homeString1 = ' '.join(homeList1)
            self.question.setText(homeString1)
            Type=2
        elif intro and Type==2:
            homeLineup.append(str(self.answer.text()))
            
            homeList2 = ['What is the last name of the second person in the', homeTeam, 'lineup']
            homeString2 = ' '.join(homeList2)
            self.question.setText(homeString2)
            Type=3
        elif intro and Type==3:
            homeLineup.append(str(self.answer.text()))
            
            homeList3 = ['What is the last name of the third person in the', homeTeam, 'lineup']
            homeString3 = ' '.join(homeList3)
            self.question.setText(homeString3)
            Type=4
        elif intro and Type==4:
            homeLineup.append(str(self.answer.text()))
            
            homeList4 = ['What is the last name of the fourth person in the', homeTeam, 'lineup']
            homeString4 = ' '.join(homeList4)
            self.question.setText(homeString4)
            Type=5
        elif intro and Type==5:
            homeLineup.append(str(self.answer.text()))
            
            homeList5 = ['What is the last name of the fifth person in the', homeTeam, 'lineup']
            homeString5 = ' '.join(homeList5)
            self.question.setText(homeString5)
            Type=6
        elif intro and Type==6:
            homeLineup.append(str(self.answer.text()))
            
            homeList6 = ['What is the last name of the sixth person in the', homeTeam, 'lineup']
            homeString6 = ' '.join(homeList6)
            self.question.setText(homeString6)
            Type=7
        elif intro and Type==7:
            homeLineup.append(str(self.answer.text()))
            
            homeList7 = ['What is the last name of the seventh person in the', homeTeam, 'lineup']
            homeString7 = ' '.join(homeList7)
            self.question.setText(homeString7)
            Type=8
        elif intro and Type==8:
            homeLineup.append(str(self.answer.text()))
            
            homeList8 = ['What is the last name of the eighth person in the', homeTeam, 'lineup']
            homeString8 = ' '.join(homeList8)
            self.question.setText(homeString8)
            Type=9
        elif intro and Type==9:
            homeLineup.append(str(self.answer.text()))
            
            homeList9 = ['What is the last name of the ninth person in the', homeTeam, 'lineup']
            homeString9 = ' '.join(homeList9)
            self.question.setText(homeString9)
            Type=10
        elif intro and Type==10:
            homeLineup.append(str(self.answer.text()))
            
            awayList1 = ['What is the last name of the first person in the', awayTeam, 'lineup']
            awayString1 = ' '.join(awayList1)
            self.question.setText(awayString1)
            Type=11
        elif intro and Type==11:
            awayLineup.append(str(self.answer.text()))
            
            awayList2 = ['What is the last name of the second person in the', awayTeam, 'lineup']
            awayString2 = ' '.join(awayList2)
            self.question.setText(awayString2)
            Type=12
        elif intro and Type==12:
            awayLineup.append(str(self.answer.text()))
            
            awayList3 = ['What is the last name of the third person in the', awayTeam, 'lineup']
            awayString3 = ' '.join(awayList3)
            self.question.setText(awayString3)
            Type=13
        elif intro and Type==13:
            awayLineup.append(str(self.answer.text()))
            
            awayList4 = ['What is the last name of the fourth person in the', awayTeam, 'lineup']
            awayString4 = ' '.join(awayList4)
            self.question.setText(awayString4)
            Type=14
        elif intro and Type==14:
            awayLineup.append(str(self.answer.text()))
            
            awayList5 = ['What is the last name of the fifth person in the', awayTeam, 'lineup']
            awayString5 = ' '.join(awayList5)
            self.question.setText(awayString5)
            Type=15
        elif intro and Type==15:
            awayLineup.append(str(self.answer.text()))
            
            awayList6 = ['What is the last name of the sixth person in the', awayTeam, 'lineup']
            awayString6 = ' '.join(awayList6)
            self.question.setText(awayString6)
            Type=16
        elif intro and Type==16:
            awayLineup.append(str(self.answer.text()))
            
            awayList7 = ['What is the last name of the seventh person in the', awayTeam, 'lineup']
            awayString7 = ' '.join(awayList7)
            self.question.setText(awayString7)
            Type=17
        elif intro and Type==17:
            awayLineup.append(str(self.answer.text()))
            
            awayList8 = ['What is the last name of the eighth person in the', awayTeam, 'lineup']
            awayString8 = ' '.join(awayList8)
            self.question.setText(awayString8)
            Type=18
        elif intro and Type==18:
            awayLineup.append(str(self.answer.text()))
            
            awayList9 = ['What is the last name of the ninth person in the', awayTeam, 'lineup']
            awayString9 = ' '.join(awayList9)
            self.question.setText(awayString9)
            Type=19
        elif intro and Type==19:
            awayLineup.append(str(self.answer.text()))
            
            
            self.toolBar.show()
            intro=False

        elif Type==0:
            if first and not second and not third:
               howFar=str(self.answer.text())
               howFar=howFar.lower()
               
               
               if howFar=='second' or howFar=='2':
                   first=True
                   second=True
                   third=False
                   
               elif howFar=='third' or howFar=='3':
                   first=True
                   second=False
                   third=True
                   
               elif howFar=='home':
                   first=True
                   second=False
                   third=False
                   
                   if awayBatting:
                       awayRuns=awayRuns+1
                   else:
                       homeRuns=homeRuns+1
               elif howFar=='out':
                   outs=outs+1
               else:
                  self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
            elif first and second and not third:
                firstBackup=first
                secondBackup=second
                thirdBackup=third
                homeRunsBackup=homeRuns
                awayRunsBackup=awayRuns
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                if howFar=='third' or howFar=='3':
                    first=True
                    second=False
                    third=True
                    Type='0a'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                elif howFar=='home':
                    first=True
                    second=False
                    third=False
                    Type='0a'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='out':
                    outs=outs+1
                    first=True
                    second=False
                    third=False
                    Type='0a'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                else:
                    self.question.setText("That is not a valid action. Click single if you wish to input your action again.")

            elif first and second and third:
                firstBackup=first
                secondBackup=second
                thirdBackup=third
                homeRunsBackup=homeRuns
                awayRunsBackup=awayRuns
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                if howFar=='third' or howFar=='3':
                    first=True
                    second=False
                    third=True
                    Type='0b'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                elif howFar=='home':
                    first=True
                    second=False
                    third=False
                    Type='0b'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='out':
                    outs=outs+1
                    first=True
                    second=False
                    third=False
                    Type='0b'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                else:
                    self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
            elif not first and second and third:
                firstBackup=first
                secondBackup=second
                thirdBackup=third
                homeRunsBackup=homeRuns
                awayRunsBackup=awayRuns
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                if howFar=='home':
                    first=False
                    second=True
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                    Type='0c'
                    self.question.setText("How far did the person at SECOND go? (e.g. third, home, out, none)")
                elif howFar=='none':
                    first=True
                    second=True
                    third=True
                elif howFar=='out':
                    outs=outs+1
                    first=False
                    second=True
                    third=False
                else:
                    self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
            elif first and not second and third:
                firstBackup=first
                secondBackup=second
                thirdBackup=third
                homeRunsBackup=homeRuns
                awayRunsBackup=awayRuns
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                if howFar=='home':
                    third=False
                    second=False
                    first=True
                    Type='0d'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='none':
                    first=True
                    second=False
                    third=True
                    Type='0d'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                elif howFar=='out':
                    outs=outs+1
                    first=True
                    second=False
                    third=False
                    Type='0d'
                    self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
                else:
                    self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
            elif not first and second and not third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='third' or howFar=='3':
                    first=True
                    second=False
                    third=True
                elif howFar=='home':
                    first=True
                    second=False
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='none':
                    first=True
                    second=True
                    third=False
                elif howFar=='out':
                    outs=outs+1
                    first=True
                    second=False
                    third=False
                else:
                    self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
            elif not first and not second and third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='home':
                    first=True
                    second=False
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='none':
                    first=True
                    second=False
                    third=True
                elif howFar=='out':
                    outs=outs+1
                    first=True
                    second=False
                    third=False
                else:
                    self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
        elif Type=='0a':
            howFar=str(self.answer.text())
            howFar=howFar.lower()
            
            
            if howFar=='second' or howFar=='2':
                first=True
                second=True
            elif howFar=='third' or howFar=='3':
                first=True
                second=False
                third=True
            elif howFar=='home':
                first=True
                second=False
                third=False
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
            elif howFar=='out':
                outs=outs+1
            else:
                self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
                first=firstBackup
                second=secondBackup
                third=thirdBackup
                homeRuns=homeRunsBackup
                awayRuns=awayRunsBackup
        elif Type=='0b':
            howFar=str(self.answer.text())
            howFar=howFar.lower()
            
            
            if howFar=='second' or howFar=='2':
                first=True
                second=True
            elif howFar=='third' or howFar=='3':
                first=True
                second=False
                third=True
            elif howFar=='home':
                first=True
                second=False
                third=False
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
            elif howFar=='out':
                outs=outs+1
            else:
                self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
                first=firstBackup
                second=secondBackup
                third=thirdBackup
                homeRuns=homeRunsBackup
                awayRuns=awayRunsBackup
        elif Type=='0c':
            howFar=str(self.answer.text())
            howFar=howFar.lower()
            
            
            if howFar=='third' or howFar=='3':
                first=True
                second=False
                third=True
            elif howFar=='home':
                first=True
                second=False
                third=False
            elif howFar=='none':
                first=True
                second=True
            elif howFar=='out':
                outs=outs+1
                first=True
                second=False
            else:
                self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
                first=firstBackup
                second=secondBackup
                third=thirdBackup
                homeRuns=homeRunsBackup
                awayRuns=awayRunsBackup
        elif Type=='0d':
            howFar=str(self.answer.text())
            howFar=howFar.lower()
            
            
            if howFar=='second' or howFar=='2':
                first=True
                second=True
            elif howFar=='third' or howFar=='3':
                first=True
                second=False
                third=True
            elif howFar=='home':
                first=True
                second=False
                third=False
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
            elif howFar=='out':
                outs=outs+1
            else:
                self.question.setText("That is not a valid action. Click single if you wish to input your action again.")
                first=firstBackup
                second=secondBackup
                third=thirdBackup
                homeRuns=homeRunsBackup
                awayRuns=awayRunsBackup
        elif Type==1:
            if first and not second and not third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='third' or howFar=='3':
                     first=False
                     second=True
                     third=True
                elif howFar=='home':
                    first=False
                    second=True
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='out':
                    outs=outs+1
                    first=False
                    second=True
                    third=False
                else:
                    self.question.setText("That is not a valid action. Click double if you wish to input your action again.")
            elif first and second and not third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='third' or howFar=='3':
                    first=False
                    second=True
                    third=True
                elif howFar=='home':
                    first=False
                    second=True
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='out':
                    outs=outs+1
                    first=False
                    second=True
                    third=False
                else:
                    self.question.setText("That is not a valid action. Click double if you wish to input your action again.")
            elif first and second and third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='third' or howFar=='3':
                    first=False
                    second=True
                    third=True
                elif howFar=='home':
                    first=False
                    second=True
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='out':
                    outs=outs+1
                    first=False
                    second=True
                    third=False
                else:
                   self.question.setText("That is not a valid action. Click double if you wish to input your action again.")
            elif not first and second and third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='third' or howFar=='3':
                    first=False
                    second=True
                    third=True
                elif howFar=='home':
                    first=False
                    second=True
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='out':
                    outs=outs+1
                    first=False
                    second=True
                    third=True
                else:
                    self.question.setText("That is not a valid action. Click double if you wish to input your action again.")
            elif first and not second and third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='third' or howFar=='3':
                    first=False
                    second=True
                    third=True
                elif howFar=='home':
                    first=False
                    second=True
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='out':
                    outs=outs+1
                    first=False
                    second=True
                    third=False
                else:
                    self.question.setText("That is not a valid action. Click double if you wish to input your action again.")
            elif not first and second and not third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='third' or howFar=='3':
                    first=False
                    second=True
                    third=True
                elif howFar=='home':
                    first=False
                    second=True
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='out':
                    outs=outs+1
                else:
                    self.question.setText("That is not a valid action. Click double if you wish to input your action again.")
            elif not first and not second and third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='home':
                    first=False
                    second=True
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                elif howFar=='none':
                    first=False
                    second=True
                    third=True
                elif howFar=='out':
                    outs=outs+1
                    first=False
                    second=True
                    third=False
                else:
                     self.question.setText("That is not a valid action. Click double if you wish to input your action again.")
        elif Type==2:
            if first and not second and third:
                howFar=str(self.answer.text())
                howFar=howFar.lower()
                
                
                if howFar=='first' or howFar=='1':
                    first=False
                    second=True
                    third=True
                elif howFar=='third' or howFar=='3':
                    first=True
                    second=False
                    third=False
                    if awayBatting:
                        awayRuns=awayRuns+1
                    else:
                        homeRuns=homeRuns+1
                else:
                    self.question.setText("That is not a valid base. Click steal if you wish to input your base again.")
        elif Type==3:
            errorDistance=str(self.answer.text())
            errorDistance=errorDistance.lower()
            if errorDistance=='first':
                self.single_Click()
            elif errorDistance=='second':
                self.double_Click()
            elif errorDistance=='third':
                self.triple_Click()
            elif errorDistance=='home':
                self.homeRun_Click()
            else:
                self.question.setText("That is not a valid base. Click error if you wish to input your base again.")
        elif Type==4:
            foulSide=str(self.answer.text())
            foulSide.lower()
            if foulSide=='right':
                pass
                #Add text
            elif foulSide=='left':
                pass
                #Add text
            else:
                self.question.setText("That is not a valid side. Click foul if you wish to input your side again.")
        elif Type==5:
            pinchHitterName=str(self.answer.text())
            if awayBatting:
                awayLineup[awayLineupNumber]=pinchHitterName
            else:
                homeLineup[homeLineupNumber]=pinchHitterName
        elif Type==6:
            outType=str(self.answer.text())
            outType=outType.upper()
            #Add text for all
            baseList=[first, second, third]
            outBackup=outs
            if outType.startswith('F'):
                outs=outs+1
                if outType.endswith('1'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('2'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('3'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('4'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('5'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('6'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('7'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('8'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('9'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
            elif outType.startswith('L'):
                outs=outs+1
                if outType.endswith('1'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('2'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('3'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('4'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('5'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('6'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('7'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('8'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('9'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
            elif outType.startswith('U'):
                outs=outs+1
                if outType.endswith('1'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('2'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('3'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('4'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('5'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('6'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('7'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('8'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
                elif outType.endswith('9'):
                    if True in baseList and outs<3:
                        self.question.setText("Did anyone else move up or get out? (Y/N)")
                        Type='6a'
        elif Type=='6a':
            answer=str(self.answer.text())
            answer=answer.upper()
            if answer=='Y':
                if first and not second and not third:
                    self.question.setText("How far did the person at FIRST go (second, third, home, out)")
                    Type='6b'
                elif first and second and not third:
                    self.question.setText("Who moved up (second, both, out)")
                    Type='6c'

                elif first and second and third:
                    self.question.setText("Who moved up? (first, second, third, out)")
                    Type='6e'
                elif not first and second and third:
                    self.question.setText("Who moved up? (second, third, out)")
                    Type='6g'
                elif first and not second and third:
                    self.question.setText("Who moved up? (first, third, both, out)")
                    Type='6i'
                elif not first and second and not third:
                    self.question.setText("Did the person at SECOND go to third, or get out? (third, out)")
                    Type='6k'
            elif not first and not second and third:
                self.question.setText("Did the person at third get out, or go home? (home, out)")
                Type='6l'
        elif Type=='6b':
            howFar=str(self.answer.text())
            howFar=howFar.lower()
            if howFar=='second' or howFar=='2':
                first=False
                second=True
                third=False
            elif howFar=='third' or howFar=='3':
                first=False
                third=False
                third=True
            elif howFar=='home':
                first=False
                second=False
                third=False
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
            elif howFar=='out':
                outs=outs+1
                first=False
                second=False
                third=False
            else:
                outs=outBackup
                self.question.setText("That is not a valid action. Click out if you wish to input your action again.")
        elif Type=='6c':
            howFar=str(self.answer.text())
            howFar=howFar.lower()
            if howFar=='second' or howFar=='2':
                first=True
                second=False
                third=True
            elif howFar=='both':
                first=False
                second=True
                third=True
            elif howFar=='out':
                self.question.setText("Who got out? (e.g. first, second, both)")
                Type='6d'
            else:
                outs=outBackup
                self.question.setText("That is not a valid action. Click out if you wish to input your action again.")
        elif Type=='6d':
            whoOut=str(self.answer.text())
            whoOut=whoOut.lower()
            if whoOut=='first' or whoOut==1:
                outs=outs+1
                first=False
                second=True
                third=False
            elif whoOut=='second' or whoOut==2:
                outs=outs+1
                first=True
                second=False
                third=False
            elif whoOut=='both':
                outs=outs+2
                first=False
                second=False
                third=False
            else:
                outs=outBackup
                self.question.setText("That is not a valid base. Click out if you wish to input your base again.")
        elif Type=='6e':
            answer=self.answer.text()
            answer=answer.lower()
            if answer=='first' or answer==1:
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                    first=False
                    second=True
                    third=True
            elif answer=='second' or answer==2:
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                    first=True
                    second=False
                third=True
            elif answer=='third' or answer==3:
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                first=True
                second=True
                third=False
            elif answer=='out':
                self.question.setText("Who got out? (first, second, third)")
                Type='6f'
            else:
                outs=outBackup
                self.question.setText("That is not a valid base. Click out if you wish to input your base again.")
        elif Type=='6f':
             whoOut=self.answer.text()
             whoOut=whoOut.lower()
             if whoOut=='first' or whoOut==1:
                first=False
                second=True
                third=True
             elif whoOut=='second' or whoOut==2:
                first=True
                second=False
                third=True
             elif whoOut=='third' or whoOut==3:
                first=True
                second=True
                third=False
             else:
                outs=outBackup
                self.question.setText("That is not a valid base. Click out if you want to input your base again.")
        elif Type=='6g':
            answer=self.answer.text()
            answer=answer.lower()
            if answer=='second' or answer==1:
                if awayBatting:
                    awayruns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                first=False
                second=False
                third=True
            elif answer=='third' or answer==3:
                if awayBatting:
                    awayruns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                first=False
                second=True
                third=False
            elif answer=='out':
                self.question.setText("Who got out? (second, third, both)")
                Type='6h'
            else:
                outs=outBackup
                self.question.setText("That is not a valid action. Click out if you wish to input your action again.")
        elif Type=='6h':
            whoOut=self.answer.text()
            whoOut=whoOut.lower()
            if whoOut=='second' or whoOut==2:
                outs=outs+1
                first=False
                second=False
                third=True
            elif whoOut=='third' or whoOut==3:
                outs=outs+1
                first=False
                second=True
                third=False
            elif whoOut=='both':
                outs=outs+2
                first=False
                second=False
                third=False
            else:
                outs=outBackup
                self.question.setText("That is not a valid base(s). Cick out if you wish to input your base(s) again.")
        elif Type=='6i':
            answer=self.answer.text()
            answer=answer.lower()
            if answer=='first' or answer==1:
                first=False
                second=True
                third=True
            elif answer=='third' or answer==3:
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                first=True
                second=False
                third=False
            elif answer=='both':
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                first=False
                second=True
                third=False
            elif answer=='out':
                self.question.setText("Who got out? (first, third, both)")
                Type='6j'
            else:
                self.question.setText("That is not a valid action. Click out if you wish to input your action again.")
                outs=outBackup
        elif Type=='6j':
            whoOut=self.answer.text()
            whoOut=whoOut.lower()
            if whoOut=='first' or whoOut==1:
                outs=outs+1
                first=False
                second=False
                third=True
            elif whoOut=='third' or whoOut==3:
                outs=outs+1
                first=True
                second=False
                third=False
            elif whoOut=='both':
                outs=outs+2
                first=False
                second=False
                thirt=False
            else:
                self.question.setText("That is not a valid base. Click out if you wish to input your action again.")
        elif Type=='6k':
            howFar=self.answer.text()
            howFar=howFar.lower()
            if howFar=='third' or howFar==3:
                first=False
                second=False
                third=True
            elif howFar=='home':
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                first=False
                second=False
                third=False
            elif howFar=='out':
                outs=outs+1
                first=False
                second=False
                third=False
            else:
                self.question.setText("That is not a valid action. Click out if you wish to input your action again.")
        elif Type=='6l':
            howFar=self.answer.text()
            howFar=howFar.lower()
            if howFar=='home':
                if awayBatting:
                    awayRuns=awayRuns+1
                else:
                    homeRuns=homeRuns+1
                first=False
                second=False
                third=False
            elif howFar=='out':
                outs=outs+1
                first=False
                second=False
                third=False
            else:
                outs=outBackup
                self.question.setText("That is not a valid action. Click out if you wish to input your action again.")
        
        homeRunsList = [homeTeam, 'runs:', str(homeRuns)]
        homeRunsString = ' '.join(homeRunsList)
        self.homeRuns.setText(homeRunsString)
        awayRunsList = [awayTeam, 'runs:', str(awayRuns)]
        awayRunsString = ' '.join(awayRunsList)
        self.awayRuns.setText(awayRunsString)
        if outs > 2:
            outs=0
            first=False
            second=False
            third=False
            if awayBatting:
                awayBatting=False
            else:
                awayBatting=True
        outsList = ['Outs:', str(outs)]
        outsString = ' '.join(outsList)
        self.outs.setText(outsString)
        if first:
           self.firstBase.setText(' O')
        else:
           self.firstBase.setText('')
        if second:
           self.secondBase.setText(' O')
        else:
           self.secondBase.setText('')
        if third:
           self.thirdBase.setText(' O')
        else:
           self.thirdBase.setText('')
        self.answer.setText('')

    def single_Click(self):
       global first, second, third, awayBatting, homeRuns, awayRuns, Type, strikes, balls
       Type=0
       if not first and not second and not third:
           first=True
           second=False
           third=False
           self.firstBase.setText(' O')
           self.secondBase.setText('')
           self.thirdBase.setText('')
       elif first and not second and not third:
           self.question.setText("How far did the person at FIRST go? (e.g. second, third, home, out)")
       elif first and second and not third:
           self.question.setText("How far did the person at SECOND go? (e.g. third, home, out)")
       elif first and second and third:
           if awayBatting:
               awayRuns=awayRuns+1
               awayRunsList = [awayTeam, 'runs:', str(awayRuns)]
               awayRunsString = ' '.join(awayRunsList)
               self.awayRuns.setText(awayRunsString)
           else:
               homeRuns=homeRuns+1
               homeRunsList = [homeTeam, 'runs:', str(homeRuns)]
               homeRunsString = ' '.join(homeRunsList)
               self.homeRuns.setText(homeRunsString)
           self.question.setText("How far did the person at SECOND go (e.g. third, home, out)")
       elif not first and second and third:
           self.question.setText("How far did the person at THIRD go? (e.g. home, out, none)")
       elif first and not second and third:
           self.question.setText("How far did the person at THIRD go? (e.g. home, out, none)")
       elif not first and second and not third:
           self.question.setText("How far did the person at SECOND go? (e.g. third, home, out, none)")
       elif not first and not second and third:
           self.question.setText("How far did the person at THIRD go? (e.g. home, out, none)")

       if awayBatting:
           awayProgress()
           strikes=0
           balls=0
           ballsList = ['Balls:', '0']
           ballsString = ' '.join(ballsList)
           self.balls.setText(ballsString)
           strikesList = ['Strikes:', '0']
           strikesString = ' '.join(strikesList)
           self.strikes.setText(strikesString)
       else:
           homeProgress()
           strikes=0
           balls=0
           ballsList = ['Balls:', '0']
           ballsString = ' '.join(ballsList)
           self.balls.setText(ballsString)
           strikesList = ['Strikes:', '0']
           strikesString = ' '.join(strikesList)
           self.strikes.setText(strikesString)

    def double_Click(self):
        global first, second, third, awayBatting, homeRuns, awayRuns, Type, strikes, balls
        Type=1
        if not first and not second and not third:
               first=False
               second=True
               third=False
               self.firstBase.setText('')
               self.secondBase.setText(' O')
               self.thirdBase.setText('')
        elif first and not second and not third:
            self.question.setText("How far did the person at FIRST go? (e.g. third, home, out)")
        elif first and second and not third:
            if awayBatting:
               awayRuns=awayRuns+1
            else:
               homeRuns=homeRuns+1
            self.question.setText("How far did the person at FIRST go? (e.g. third, home, out)")
        elif first and second and third:
            if awayBatting:
               awayRuns=awayRuns+2
            else:
               homeRuns=homeRuns+2
            self.question.setText("How far did the person at FIRST go? (e.g. third, home, out)")
        elif not first and second and third:
            if awayBatting:
               awayRuns=awayRuns+1
            else:
               homeRuns=homeRuns+1
            self.question.setText("How far did the person at SECOND go? (e.g. third, home, out)")
        elif first and not second and third:
            if awayBatting:
               awayRuns=awayRuns+1
            else:
               homeRuns=homeRuns+1
            self.question.setText("How far did the person at FIRST go? (e.g. third, home, out)")
        elif not first and second and not third:
            self.question.setText("How far did the person at SECOND go? (e.g. third, home, out)")
        elif not first and not second and third:
            self.question.setText("How far did the person at THIRD go? (e.g. home, out, none) ")
        if awayBatting:
            awayProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
            awayRunsList = [awayTeam, 'runs:', str(awayRuns)]
            awayRunsString = ' '.join(awayRunsList)
            self.awayRuns.setText(awayRunsString)
        else:
            homeProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
            homeRunsList = [homeTeam, 'runs:', str(homeRuns)]
            homeRunsString = ' '.join(homeRunsList)
            self.homeRuns.setText(homeRunsString)
    def triple_Click(self):
        global first, second, third, awayBatting, homeRuns, awayRuns, strikes, balls
        bases=0
        if first:
            bases=bases+1
        if second:
            bases=bases+1
        if third:
            bases=bases+1
        if awayBatting:
            awayProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
            awayRuns=awayRuns+bases
            awayRunsList = [awayTeam, 'runs:', str(awayRuns)]
            awayRunsString = ' '.join(awayRunsList)
            self.awayRuns.setText(awayRunsString)
        else:
            homeProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
            homeRuns=homeRuns+bases
            homeRunsList = [homeTeam, 'runs:', str(homeRuns)]
            homeRunsString = ' '.join(homeRunsList)
            self.homeRuns.setText(homeRunsString)
        first=False
        second=False
        third=True
        self.firstBase.setText('')
        self.secondBase.setText('')
        self.thirdBase.setText(' O')

    def homeRun_Click(self):
        global first, second, third, awayBatting, homeRuns, awayRuns, strikes
        bases=0
        if first:
            bases=bases+1
        if second:
            bases=bases+1
        if third:
            bases=bases+1
        if awayBatting:
            awayProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
            awayRuns=awayRuns+bases+1
            awayRunsList = [awayTeam, 'runs:', str(awayRuns)]
            awayRunsString = ' '.join(awayRunsList)
            self.awayRuns.setText(awayRunsString)
        else:
            homeProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
            homeRuns=homeRuns+bases+1
            homeRunsList = [homeTeam, 'runs:', str(homeRuns)]
            homeRunsString = ' '.join(homeRunsList)
            self.homeRuns.setText(homeRunsString)
        first=False
        second=False
        third=False
        self.firstBase.setText('')
        self.secondBase.setText('')
        self.thirdBase.setText('')

    def hitByPitch_Click(self):
        global first, second, third, awayBatting, homeRuns, awayRuns, strikes, balls
        if not first and not second and not third:
            first=True
            second=False
            third=False
        elif first and not second and not third:
            first=True
            second=True
            third=False
        elif first and second and not third:
            first=True
            second=True
            third=True
        elif first and second and third:
            if awayBatting:
                awayRuns=awayRuns+1
                awayRunsList = [awayTeam, 'runs:', str(awayRuns)]
                awayRunsString = ' '.join(awayRunsList)
                self.awayRuns.setText(awayRunsString)
            else:
                homeRuns=homeRuns+1
                homeRunsList = [homeTeam, 'runs:', str(homeRuns)]
                homeRunsString = ' '.join(homeRunsList)
                self.homeRuns.setText(homeRunsString)
        elif not first and second and third:
            first=True
            second=True
            third=True
        elif first and not second and third:
            first=True
            second=True
            third=True
        elif not first and second and not third:
            first=True
            second=True
            third=False
        elif not first and not second and third:
            first=True
            second=False
            third=True
        if first:
           self.firstBase.setText(' O')
        else:
           self.firstBase.setText('')
        if second:
           self.secondBase.setText(' O')
        else:
           self.secondBase.setText('')
        if third:
           self.thirdBase.setText(' O')
        else:
           self.thirdBase.setText('')
        if awayBatting:
            awayProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
        else:
            homeProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
    def error_Click(self):
        global Type
        Type=3
        self.question.setText("How far did the batter reach on the error?")
        if awayBatting:
            awayProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
        else:
            homeProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
    def steal_Click(self):
        global first, second, third, awayBatting, homeRuns, awayRuns, Type
        Type=2
        if not first and not second and not third:
            self.question.setText("You can't steal first!")
        elif first and not second and not third:
            first=False
            second=True
            third=False
            self.firstBase.setText('')
            self.secondBase.setText(' O')
            self.thirdBase.setText('')
        elif first and second and not third:
            first=True
            second=False
            third=True
        elif first and second and third:
            first=True
            second=True
            third=False
            if awayBatting:
                awayRuns=awayRuns+1
            else:
                homeRuns=homeRuns+1
        elif not first and second and third:
            first=False
            second=True
            third=False
            if awayBatting:
                awayRuns=awayRuns+1
            else:
                homeRuns=homeRuns+1
        elif first and not second and third:
            self.question.setText("Who stole (e.g. first, third)")
        elif not first and second and not third:
            first=False
            second=False
            third=True
        elif not first and not second and third:
            if awayBatting:
                awayRuns=awayRuns+1
            else:
                homeRuns=homeRuns+1
            first=False
            second=False
            third=False
        if first:
           self.firstBase.setText(' O')
        else:
           self.firstBase.setText('')
        if second:
           self.secondBase.setText(' O')
        else:
           self.secondBase.setText('')
        if third:
           self.thirdBase.setText(' O')
        else:
           self.thirdBase.setText('')
    def foul_Click(self):
        global Type, strikes, outs
        Type=4
        self.question.setText("Did the batter foul the ball off to the right or the left? (Type right or left.)")
        strikes=strikes+1
        if strikes > 2:
            strikes=2
        strikesList = ['Strikes:', str(strikes)]
        strikesString = ' '.join(strikesList)
        self.strikes.setText(strikesString)
    def strike_Click(self):
        global awayBatting, strikes, outs, first, second, third, balls
        strikes=strikes+1
        if strikes > 2:
            strikes=0
            if awayBatting:
                awayProgress()
                strikes=0
                balls=0
                ballsList = ['Balls:', '0']
                ballsString = ' '.join(ballsList)
                self.balls.setText(ballsString)
                strikesList = ['Strikes:', '0']
                strikesString = ' '.join(strikesList)
                self.strikes.setText(strikesString)
            else:
                homeProgress()
                strikes=0
                balls=0
                ballsList = ['Balls:', '0']
                ballsString = ' '.join(ballsList)
                self.balls.setText(ballsString)
                strikesList = ['Strikes:', '0']
                strikesString = ' '.join(strikesList)
                self.strikes.setText(strikesString)
            outs=outs+1
            if outs > 2:
                outs=0
                if awayBatting:
                    awayBatting=False
                else:
                    awayBatting=True
                first=False
                second=False
                third=False
                self.firstBase.setText('')
                self.secondBase.setText('')
                self.thirdBase.setText('')
        strikesList = ['Strikes:', str(strikes)]
        strikesString = ' '.join(strikesList)
        self.strikes.setText(strikesString)
        outsList = ['Outs:', str(outs)]
        outsString = ' '.join(outsList)
        self.outs.setText(outsString)
    def ball_Click(self):
        global balls, awayBatting
        balls=balls+1
        if balls > 3:
            balls=0
            self.hitByPitch_Click()
        ballsList = ['Balls:', str(balls)]
        ballsString = ' '.join(ballsList)
        self.balls.setText(ballsString)
    def pinchHitter_Click(self):
        global Type
        Type=5
        self.question.setText("What is the last name of the pinch hitter")
    def out_Click(self):
        global Type, awayBatting
        Type=6
        self.question.setText("What kind of out was it? (e.g. F7, 6-3, L4)")
        if awayBatting:
            awayProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
        else:
            homeProgress()
            strikes=0
            balls=0
            ballsList = ['Balls:', '0']
            ballsString = ' '.join(ballsList)
            self.balls.setText(ballsString)
            strikesList = ['Strikes:', '0']
            strikesString = ' '.join(strikesList)
            self.strikes.setText(strikesString)
    def start_Click(self):
        global text, homeTeam, awayTeam
        self.start.hide()
        self.question.setText("Welcome to the scorebook program")
        self.next.show()
    def next_Click(self):
        self.question.setText("Please enter the home team name (and click done) to continue.")
        self.next.hide()



app = QtGui.QApplication(sys.argv)
myApp = MyWindow()
myApp.show()
app.exec_()
