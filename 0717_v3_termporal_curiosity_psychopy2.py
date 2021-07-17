#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on Sat Jul 17 20:32:32 2021
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = '0717_v1_termporal_curiosity_psychopy2'  # from the Builder filename that created this script
expInfo = {u'Gender': u'', u'Session': u'001', u'ParticipantID': u'', u'Name(English)': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['ParticipantID'], expName, expInfo['Name(English)'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1368, 912], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
instruction_pic = visual.ImageStim(
    win=win, name='instruction_pic',units='height', 
    image='pic_instruction.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
import numpy as np
import random
from PIL import Image, ImageFilter
from psychopy.visual import Window, TextStim

practice_cond = [1,1,7,1,5]
cond = np.concatenate((np.ones(90), 2*np.ones(5), 3*np.ones(5), 4*np.ones(5), 5*np.ones(5), 6*np.ones(5), 7*np.ones(5),8*np.ones(5),9*np.ones(5),10*np.ones(5)),axis=0)
random.shuffle(cond)
condi = list(map(int,cond))
# set to True before start egi exp
#netstation = True
#recording = True

netstation = False
recording = False

if netstation:
    import egi.simple as egi
    ns = egi.Netstation()
    print("import pynetstation")
    # set ip address
    ns.connect("10.10.10.42", 55513)
    ns.BeginSession()
    print("connected to netstation")
    if recording:
        ns.StartRecording()
        print("start recording")

def send_to_NS(key_):
    if netstation:
        ns.sync()
        ns.send_event(key=key_)


# Initialize components for Routine "Precedure"
PrecedureClock = core.Clock()
procedure_pic = visual.ImageStim(
    win=win, name='procedure_pic',units='height', 
    image='pic_procedure_1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "Precedure_2"
Precedure_2Clock = core.Clock()
procedure_pic_2 = visual.ImageStim(
    win=win, name='procedure_pic_2',units='height', 
    image='pic_procedure_2.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "Precedure_3"
Precedure_3Clock = core.Clock()
procedure_pic_3 = visual.ImageStim(
    win=win, name='procedure_pic_3',units='height', 
    image='pic_procedure_3.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "Practice_initiation"
Practice_initiationClock = core.Clock()
initiation_pic = visual.ImageStim(
    win=win, name='initiation_pic',units='height', 
    image='test_initiation.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)


# Initialize components for Routine "practice_ITI"
practice_ITIClock = core.Clock()
fixation_trial = visual.ShapeStim(
    win=win, name='fixation_trial', vertices='cross',units='height', 
    size=(0.16, 0.16),
    ori=0, pos=(0, 0),
    lineWidth=0.6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "practice_Blurred"
practice_BlurredClock = core.Clock()

practice_blurred = visual.ImageStim(
    win=win, name='practice_blurred',units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
fixation_trial_3 = visual.ShapeStim(
    win=win, name='fixation_trial_3', vertices='cross',units='height', 
    size=(0.16, 0.16),
    ori=0, pos=(0, 0),
    lineWidth=0.6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Practice_curiosity_rating"
Practice_curiosity_ratingClock = core.Clock()
curiosity_rating_practice = visual.RatingScale(win=win, name='curiosity_rating_practice', scale = u'1=一点也不好奇                    6=非常好奇',
low=1,
high=6,
labels=(1,2,3,4,5,6),
tickMarks=(1,2,3,4,5,6),
marker='triangle',
stretch=1.2,
textFont='msyh',
showValue=False,
showAccept=True,
acceptKeys='space',
leftKeys='left',
rightKeys='right',
noMouse=True,
acceptSize=1.2,
acceptPreText = u'请用方向键控制',
acceptText = u'请按空格键确认',
pos=[0,-0.1])
curious_text_practice = visual.TextStim(win=win, name='curious_text_practice',
    text=u'\u4f60\u5bf9\u56fe\u7247\u63cf\u8ff0\u7684\u7269\u4f53\u7684\u597d\u5947\u7a0b\u5ea6',
    font='msyh',
    pos=(0, 0.3), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Practice_confidence_rating"
Practice_confidence_ratingClock = core.Clock()
confidence_rating__practice = visual.RatingScale(win=win, name='confidence_rating__practice', scale = u'0=完全没有信心                                           100=完全有信心',
low=0,
high=10,
labels = (0,10,20,30,40,50,60,70,80,90,100),
tickMarks= (0,1,2,3,4,5,6,7,8,9,10),
marker='triangle',
stretch=1.7,
textFont='msyh',
showValue=False,
showAccept=True,
acceptKeys='space',
leftKeys='left',
rightKeys='right',
noMouse=True,
acceptSize=1.2,
acceptPreText=u'请用方向键控制',
acceptText= u'请按空格键确认',
pos=[0,-0.1],
markerStart=5)
confidence_text_practice = visual.TextStim(win=win, name='confidence_text_practice',
    text=u'\u4f60\u5bf9\u81ea\u5df1\u731c\u6d4b\u7684\u4fe1\u5fc3\u7a0b\u5ea6',
    font='msyh',
    pos=(0, 0.3), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
fixation_trial_3 = visual.ShapeStim(
    win=win, name='fixation_trial_3', vertices='cross',units='height', 
    size=(0.16, 0.16),
    ori=0, pos=(0, 0),
    lineWidth=0.6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Practice_clear"
Practice_clearClock = core.Clock()
clear_answer_2 = visual.ImageStim(
    win=win, name='clear_answer_2',units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
fixation_trial_3 = visual.ShapeStim(
    win=win, name='fixation_trial_3', vertices='cross',units='height', 
    size=(0.16, 0.16),
    ori=0, pos=(0, 0),
    lineWidth=0.6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Practice_surprise_rating"
Practice_surprise_ratingClock = core.Clock()
surprise_rating_practice = visual.RatingScale(win=win, name='surprise_rating_practice', scale=u'1=一点也不惊讶                  6=非常惊讶',
low=1,
high=6,
labels=(1,2,3,4,5,6),
tickMarks=(1,2,3,4,5,6),
marker='triangle',
stretch=1.2,
textFont='msyh',
showValue=False,
showAccept=True,
acceptKeys='space',
leftKeys='left',
rightKeys='right',
noMouse=True,
acceptSize=1.2,
acceptPreText=u'请用方向键控制',
acceptText= u'请按空格键确认',
pos=[0,-0.1])
surprise_text_practice = visual.TextStim(win=win, name='surprise_text_practice',
    text=u'\u4f60\u5bf9\u7b54\u6848\u7684\u60ca\u8bb6\u7a0b\u5ea6',
    font='msyh',
    pos=(0, 0.3), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Practice_end"
Practice_endClock = core.Clock()
test_end_pic = visual.ImageStim(
    win=win, name='test_end_pic',units='height', 
    image='test_end.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "Rest"
RestClock = core.Clock()
rest_pic = visual.ImageStim(
    win=win, name='rest_pic',units='height', 
    image='rest.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
isPause = False

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fixation_trial_2 = visual.ShapeStim(
    win=win, name='fixation_trial_2', vertices='cross',units='height', 
    size=(0.16, 0.16),
    ori=0, pos=(0, 0),
    lineWidth=0.6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)


# Initialize components for Routine "Blurred"
BlurredClock = core.Clock()

blurredpicture_2_ = visual.ImageStim(
    win=win, name='blurredpicture_2_',units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ISI_afterblurr"
ISI_afterblurrClock = core.Clock()
fixation_trial_4 = visual.ShapeStim(
    win=win, name='fixation_trial_4', vertices='cross',units='height', 
    size=(0.16, 0.16),
    ori=0, pos=(0, 0),
    lineWidth=0.6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)


# Initialize components for Routine "Curiosity_rating"
Curiosity_ratingClock = core.Clock()
Curiosity = visual.RatingScale(win=win, name='Curiosity', scale=u'1=一点也不好奇                  6=非常好奇',
low=1,
high=6,
labels=(1,2,3,4,5,6),
tickMarks=(1,2,3,4,5,6),
marker='triangle',
stretch=1.2,
textFont='msyh',
showValue=False,
showAccept=True,
acceptKeys='space',
leftKeys='left',
rightKeys='right',
noMouse=True,
acceptSize=1.2,
acceptPreText=u'请用方向键控制',
acceptText= u'请按空格键确认',
pos=[0,-0.1])

# Initialize components for Routine "Confidence_rating"
Confidence_ratingClock = core.Clock()
Confidence = visual.RatingScale(win=win, name='Confidence', scale = u'0=完全没有信心                                         100=完全有信心',
low=0,
high=10,
labels = (0,10,20,30,40,50,60,70,80,90,100),
tickMarks= (0,1,2,3,4,5,6,7,8,9,10),
marker='triangle',
stretch=1.7,
textFont='msyh',
showValue=False,
showAccept=True,
acceptKeys='space',
leftKeys='left',
rightKeys='right',
noMouse=True,
acceptSize=1.2,
acceptPreText= u'请用方向键控制',
acceptText= u'请按空格键确认',
pos=[0,-0.1],
markerStart=5)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
fixation_trial_3 = visual.ShapeStim(
    win=win, name='fixation_trial_3', vertices='cross',units='height', 
    size=(0.16, 0.16),
    ori=0, pos=(0, 0),
    lineWidth=0.6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Clear"
ClearClock = core.Clock()
Clear_answer = visual.ImageStim(
    win=win, name='Clear_answer',units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
fixation_trial_3 = visual.ShapeStim(
    win=win, name='fixation_trial_3', vertices='cross',units='height', 
    size=(0.16, 0.16),
    ori=0, pos=(0, 0),
    lineWidth=0.6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Surprise_rating"
Surprise_ratingClock = core.Clock()
Surprise = visual.RatingScale(win=win, name='Surprise', scale=u'1=一点也不惊讶                  6=非常惊讶',
high=6,
labels=(1,2,3,4,5,6),
tickMarks=(1,2,3,4,5,6),
marker='triangle',
stretch=1.2,
textFont='msyh',
showValue=False,
showAccept=True,
acceptKeys='space',
leftKeys='left',
rightKeys='right',
noMouse=True,
acceptSize=1.2,
acceptPreText=u'请用方向键控制',
acceptText= u'请按空格键确认',
pos=[0,-0.1])

# Initialize components for Routine "End"
EndClock = core.Clock()
end_pic = visual.ImageStim(
    win=win, name='end_pic',units='height', 
    image='all_end.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
t = 0
InstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instru_resp = event.BuilderKeyResponse()


# keep track of which components have finished
InstructionComponents = [instruction_pic, instru_resp]
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_pic* updates
    if t >= 0.0 and instruction_pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction_pic.tStart = t
        instruction_pic.frameNStart = frameN  # exact frame index
        instruction_pic.setAutoDraw(True)
    
    # *instru_resp* updates
    if t >= 0.0 and instru_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instru_resp.tStart = t
        instru_resp.frameNStart = frameN  # exact frame index
        instru_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instru_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Precedure"-------
t = 0
PrecedureClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
procedure_resp = event.BuilderKeyResponse()
# keep track of which components have finished
PrecedureComponents = [procedure_pic, procedure_resp]
for thisComponent in PrecedureComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Precedure"-------
while continueRoutine:
    # get current time
    t = PrecedureClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *procedure_pic* updates
    if t >= 0.0 and procedure_pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        procedure_pic.tStart = t
        procedure_pic.frameNStart = frameN  # exact frame index
        procedure_pic.setAutoDraw(True)
    
    # *procedure_resp* updates
    if t >= 0.0 and procedure_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        procedure_resp.tStart = t
        procedure_resp.frameNStart = frameN  # exact frame index
        procedure_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if procedure_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PrecedureComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Precedure"-------
for thisComponent in PrecedureComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Precedure" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Precedure_2"-------
t = 0
Precedure_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
b_procedure_resp_2_ = event.BuilderKeyResponse()
# keep track of which components have finished
Precedure_2Components = [procedure_pic_2, b_procedure_resp_2_]
for thisComponent in Precedure_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Precedure_2"-------
while continueRoutine:
    # get current time
    t = Precedure_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *procedure_pic_2* updates
    if t >= 0.0 and procedure_pic_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        procedure_pic_2.tStart = t
        procedure_pic_2.frameNStart = frameN  # exact frame index
        procedure_pic_2.setAutoDraw(True)
    
    # *b_procedure_resp_2_* updates
    if t >= 0.0 and b_procedure_resp_2_.status == NOT_STARTED:
        # keep track of start time/frame for later
        b_procedure_resp_2_.tStart = t
        b_procedure_resp_2_.frameNStart = frameN  # exact frame index
        b_procedure_resp_2_.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if b_procedure_resp_2_.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Precedure_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Precedure_2"-------
for thisComponent in Precedure_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Precedure_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Precedure_3"-------
t = 0
Precedure_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
b_procedure_resp_3_ = event.BuilderKeyResponse()
# keep track of which components have finished
Precedure_3Components = [procedure_pic_3, b_procedure_resp_3_]
for thisComponent in Precedure_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Precedure_3"-------
while continueRoutine:
    # get current time
    t = Precedure_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *procedure_pic_3* updates
    if t >= 0.0 and procedure_pic_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        procedure_pic_3.tStart = t
        procedure_pic_3.frameNStart = frameN  # exact frame index
        procedure_pic_3.setAutoDraw(True)
    
    # *b_procedure_resp_3_* updates
    if t >= 0.0 and b_procedure_resp_3_.status == NOT_STARTED:
        # keep track of start time/frame for later
        b_procedure_resp_3_.tStart = t
        b_procedure_resp_3_.frameNStart = frameN  # exact frame index
        b_procedure_resp_3_.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if b_procedure_resp_3_.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Precedure_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Precedure_3"-------
for thisComponent in Precedure_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Precedure_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Practice_initiation"-------
t = 0
Practice_initiationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
initiation_resp = event.BuilderKeyResponse()

send_to_NS('test')
# keep track of which components have finished
Practice_initiationComponents = [initiation_pic, initiation_resp]
for thisComponent in Practice_initiationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Practice_initiation"-------
while continueRoutine:
    # get current time
    t = Practice_initiationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *initiation_pic* updates
    if t >= 0.0 and initiation_pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        initiation_pic.tStart = t
        initiation_pic.frameNStart = frameN  # exact frame index
        initiation_pic.setAutoDraw(True)
    
    # *initiation_resp* updates
    if t >= 0.0 and initiation_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        initiation_resp.tStart = t
        initiation_resp.frameNStart = frameN  # exact frame index
        initiation_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if initiation_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_initiationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice_initiation"-------
for thisComponent in Practice_initiationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Practice_initiation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practicetrial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_picture.xlsx'),
    seed=None, name='practicetrial')
thisExp.addLoop(practicetrial)  # add the loop to the experiment
thisPracticetrial = practicetrial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
if thisPracticetrial != None:
    for paramName in thisPracticetrial:
        exec('{} = thisPracticetrial[paramName]'.format(paramName))

for thisPracticetrial in practicetrial:
    currentLoop = practicetrial
    # abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
    if thisPracticetrial != None:
        for paramName in thisPracticetrial:
            exec('{} = thisPracticetrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_ITI"-------
    t = 0
    practice_ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    practice_ITIComponents = [fixation_trial]
    for thisComponent in practice_ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice_ITI"-------
    while continueRoutine:
        # get current time
        t = practice_ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_trial* updates
        if t >= 0.25 and fixation_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_trial.tStart = t
            fixation_trial.frameNStart = frameN  # exact frame index
            fixation_trial.setAutoDraw(True)
        frameRemains = 0.25 + np.around(np.random.uniform(3,4), 3)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_trial.status == STARTED and t >= frameRemains:
            fixation_trial.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_ITI"-------
    for thisComponent in practice_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_blurr = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('practice_blurr.xlsx'),
        seed=None, name='practice_blurr')
    thisExp.addLoop(practice_blurr)  # add the loop to the experiment
    thisPractice_blurr = practice_blurr.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_blurr.rgb)
    if thisPractice_blurr != None:
        for paramName in thisPractice_blurr:
            exec('{} = thisPractice_blurr[paramName]'.format(paramName))
    
    for thisPractice_blurr in practice_blurr:
        currentLoop = practice_blurr
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_blurr.rgb)
        if thisPractice_blurr != None:
            for paramName in thisPractice_blurr:
                exec('{} = thisPractice_blurr[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practice_Blurred"-------
        t = 0
        practice_BlurredClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        practice_confirm = event.BuilderKeyResponse()
        if practice_cond[practicetrial.thisN] != 1 and practice_cond[practicetrial.thisN]+2 == practice_blurr.thisN:
            blurr=0
        continueRoutine = True
        clearpicture=Image.open(picturenum)
        blurredpicture= clearpicture.filter(ImageFilter.GaussianBlur(radius=blurr))
        practice_blurred.setImage(blurredpicture)
        # keep track of which components have finished
        practice_BlurredComponents = [practice_confirm, practice_blurred]
        for thisComponent in practice_BlurredComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "practice_Blurred"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practice_BlurredClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_confirm* updates
            if t >= 0.0 and practice_confirm.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_confirm.tStart = t
                practice_confirm.frameNStart = frameN  # exact frame index
                practice_confirm.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(practice_confirm.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_confirm.status == STARTED and t >= frameRemains:
                practice_confirm.status = STOPPED
            if practice_confirm.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    practice_confirm.keys = theseKeys[-1]  # just the last key pressed
                    practice_confirm.rt = practice_confirm.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            #print(confirm_space.status)
            if practice_confirm.keys == 'space':
                continueRoutine=False
            
            # *practice_blurred* updates
            if t >= 0.0 and practice_blurred.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_blurred.tStart = t
                practice_blurred.frameNStart = frameN  # exact frame index
                practice_blurred.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_blurred.status == STARTED and t >= frameRemains:
                practice_blurred.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_BlurredComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_Blurred"-------
        for thisComponent in practice_BlurredComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if practice_confirm.keys in ['', [], None]:  # No response was made
            practice_confirm.keys=None
        practice_blurr.addData('practice_confirm.keys',practice_confirm.keys)
        if practice_confirm.keys != None:  # we had a response
            practice_blurr.addData('practice_confirm.rt', practice_confirm.rt)
        if practice_confirm.keys == 'space':
            practice_blurr.finished=True
        thisExp.nextEntry()
        
    # completed 1 repeats of 'practice_blurr'
    
    # get names of stimulus parameters
    if practice_blurr.trialList in ([], [None], None):
        params = []
    else:
        params = practice_blurr.trialList[0].keys()
    # save data for this loop
    practice_blurr.saveAsText(filename + 'practice_blurr.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [fixation_trial_3]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_trial_3* updates
        if t >= 0.25 and fixation_trial_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_trial_3.tStart = t
            fixation_trial_3.frameNStart = frameN  # exact frame index
            fixation_trial_3.setAutoDraw(True)
        frameRemains = 0.25 + np.around(np.random.uniform(1,2), 3)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_trial_3.status == STARTED and t >= frameRemains:
            fixation_trial_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Practice_curiosity_rating"-------
    t = 0
    Practice_curiosity_ratingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    curiosity_rating_practice.reset()
    # keep track of which components have finished
    Practice_curiosity_ratingComponents = [curiosity_rating_practice, curious_text_practice]
    for thisComponent in Practice_curiosity_ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Practice_curiosity_rating"-------
    while continueRoutine:
        # get current time
        t = Practice_curiosity_ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *curiosity_rating_practice* updates
        if t >= 0.0 and curiosity_rating_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            curiosity_rating_practice.tStart = t
            curiosity_rating_practice.frameNStart = frameN  # exact frame index
            curiosity_rating_practice.setAutoDraw(True)
        continueRoutine &= curiosity_rating_practice.noResponse  # a response ends the trial
        
        # *curious_text_practice* updates
        if t >= 0.0 and curious_text_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            curious_text_practice.tStart = t
            curious_text_practice.frameNStart = frameN  # exact frame index
            curious_text_practice.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_curiosity_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_curiosity_rating"-------
    for thisComponent in Practice_curiosity_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practicetrial (TrialHandler)
    practicetrial.addData('curiosity_rating_practice.response', curiosity_rating_practice.getRating())
    practicetrial.addData('curiosity_rating_practice.rt', curiosity_rating_practice.getRT())
    # the Routine "Practice_curiosity_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Practice_confidence_rating"-------
    t = 0
    Practice_confidence_ratingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    confidence_rating__practice.reset()
    # keep track of which components have finished
    Practice_confidence_ratingComponents = [confidence_rating__practice, confidence_text_practice]
    for thisComponent in Practice_confidence_ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Practice_confidence_rating"-------
    while continueRoutine:
        # get current time
        t = Practice_confidence_ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confidence_rating__practice* updates
        if t >= 0.0 and confidence_rating__practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            confidence_rating__practice.tStart = t
            confidence_rating__practice.frameNStart = frameN  # exact frame index
            confidence_rating__practice.setAutoDraw(True)
        continueRoutine &= confidence_rating__practice.noResponse  # a response ends the trial
        
        # *confidence_text_practice* updates
        if t >= 0.0 and confidence_text_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            confidence_text_practice.tStart = t
            confidence_text_practice.frameNStart = frameN  # exact frame index
            confidence_text_practice.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_confidence_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_confidence_rating"-------
    for thisComponent in Practice_confidence_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practicetrial (TrialHandler)
    practicetrial.addData('confidence_rating__practice.response', confidence_rating__practice.getRating())
    practicetrial.addData('confidence_rating__practice.rt', confidence_rating__practice.getRT())
    # the Routine "Practice_confidence_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [fixation_trial_3]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_trial_3* updates
        if t >= 0.25 and fixation_trial_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_trial_3.tStart = t
            fixation_trial_3.frameNStart = frameN  # exact frame index
            fixation_trial_3.setAutoDraw(True)
        frameRemains = 0.25 + np.around(np.random.uniform(1,2), 3)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_trial_3.status == STARTED and t >= frameRemains:
            fixation_trial_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Practice_clear"-------
    t = 0
    Practice_clearClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    clear_answer_2.setImage(picturenum)
    # keep track of which components have finished
    Practice_clearComponents = [clear_answer_2]
    for thisComponent in Practice_clearComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Practice_clear"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Practice_clearClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *clear_answer_2* updates
        if t >= 0.0 and clear_answer_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            clear_answer_2.tStart = t
            clear_answer_2.frameNStart = frameN  # exact frame index
            clear_answer_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if clear_answer_2.status == STARTED and t >= frameRemains:
            clear_answer_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_clearComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_clear"-------
    for thisComponent in Practice_clearComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [fixation_trial_3]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_trial_3* updates
        if t >= 0.25 and fixation_trial_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_trial_3.tStart = t
            fixation_trial_3.frameNStart = frameN  # exact frame index
            fixation_trial_3.setAutoDraw(True)
        frameRemains = 0.25 + np.around(np.random.uniform(1,2), 3)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_trial_3.status == STARTED and t >= frameRemains:
            fixation_trial_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Practice_surprise_rating"-------
    t = 0
    Practice_surprise_ratingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    surprise_rating_practice.reset()
    # keep track of which components have finished
    Practice_surprise_ratingComponents = [surprise_rating_practice, surprise_text_practice]
    for thisComponent in Practice_surprise_ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Practice_surprise_rating"-------
    while continueRoutine:
        # get current time
        t = Practice_surprise_ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *surprise_rating_practice* updates
        if t >= 0.0 and surprise_rating_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            surprise_rating_practice.tStart = t
            surprise_rating_practice.frameNStart = frameN  # exact frame index
            surprise_rating_practice.setAutoDraw(True)
        continueRoutine &= surprise_rating_practice.noResponse  # a response ends the trial
        
        # *surprise_text_practice* updates
        if t >= 0.0 and surprise_text_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            surprise_text_practice.tStart = t
            surprise_text_practice.frameNStart = frameN  # exact frame index
            surprise_text_practice.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_surprise_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_surprise_rating"-------
    for thisComponent in Practice_surprise_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practicetrial (TrialHandler)
    practicetrial.addData('surprise_rating_practice.response', surprise_rating_practice.getRating())
    practicetrial.addData('surprise_rating_practice.rt', surprise_rating_practice.getRT())
    # the Routine "Practice_surprise_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practicetrial'

# get names of stimulus parameters
if practicetrial.trialList in ([], [None], None):
    params = []
else:
    params = practicetrial.trialList[0].keys()
# save data for this loop
practicetrial.saveAsText(filename + 'practicetrial.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Practice_end"-------
t = 0
Practice_endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_resp = event.BuilderKeyResponse()
# keep track of which components have finished
Practice_endComponents = [test_end_pic, end_resp]
for thisComponent in Practice_endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Practice_end"-------
while continueRoutine:
    # get current time
    t = Practice_endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test_end_pic* updates
    if t >= 0.0 and test_end_pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        test_end_pic.tStart = t
        test_end_pic.frameNStart = frameN  # exact frame index
        test_end_pic.setAutoDraw(True)
    
    # *end_resp* updates
    if t >= 0.0 and end_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_resp.tStart = t
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if end_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice_end"-------
for thisComponent in Practice_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Practice_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experiment_picture.xlsx'),
    seed=None, name='Trials')
thisExp.addLoop(Trials)  # add the loop to the experiment
thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in Trials:
    currentLoop = Trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Rest"-------
    t = 0
    RestClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rest_resp = event.BuilderKeyResponse()
    if Trials.thisN == 0 or Trials.thisN % 25 != 0:
        continueRoutine = False
    else:
        isPause = True
        if netstation and recording:
            ns.StopRecording()
            print("pause recording")
    # keep track of which components have finished
    RestComponents = [rest_pic, rest_resp]
    for thisComponent in RestComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Rest"-------
    while continueRoutine:
        # get current time
        t = RestClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_pic* updates
        if t >= 0.0 and rest_pic.status == NOT_STARTED:
            # keep track of start time/frame for later
            rest_pic.tStart = t
            rest_pic.frameNStart = frameN  # exact frame index
            rest_pic.setAutoDraw(True)
        
        # *rest_resp* updates
        if t >= 0.0 and rest_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            rest_resp.tStart = t
            rest_resp.frameNStart = frameN  # exact frame index
            rest_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if rest_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rest"-------
    for thisComponent in RestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if isPause:
        isPause = False
        if netstation and recording:
            ns.StartRecording()
            print("start recording")
    # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    send_to_NS(str(Trials.thisN).zfill(4))  #0000-0104
    
    cond_mark = 200 + condi[Trials.thisN] 
    send_to_NS(str(cond_mark).zfill(4)) #0201-0210
    
    Trials.addData('condition',condi[Trials.thisN])
    # keep track of which components have finished
    ITIComponents = [fixation_trial_2]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_trial_2* updates
        if t >= 0.25 and fixation_trial_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_trial_2.tStart = t
            fixation_trial_2.frameNStart = frameN  # exact frame index
            fixation_trial_2.setAutoDraw(True)
        frameRemains = 0.25 + np.around(np.random.uniform(3,4), 3)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_trial_2.status == STARTED and t >= frameRemains:
            fixation_trial_2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Intrial = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('experiment_blurr.xlsx'),
        seed=None, name='Intrial')
    thisExp.addLoop(Intrial)  # add the loop to the experiment
    thisIntrial = Intrial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIntrial.rgb)
    if thisIntrial != None:
        for paramName in thisIntrial:
            exec('{} = thisIntrial[paramName]'.format(paramName))
    
    for thisIntrial in Intrial:
        currentLoop = Intrial
        # abbreviate parameter names if possible (e.g. rgb = thisIntrial.rgb)
        if thisIntrial != None:
            for paramName in thisIntrial:
                exec('{} = thisIntrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Blurred"-------
        t = 0
        BlurredClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        blurr_confirm = event.BuilderKeyResponse()
        intrial_mark = intrials + 300
        send_to_NS(str(intrial_mark).zfill(4))   #0301-0315
        
        if condi[Trials.thisN] != 1 and condi[Trials.thisN]+1 == Intrial.thisN:
            blurr=0
        continueRoutine = True
        clearpicture=Image.open(picturenum)
        blurredpicture= clearpicture.filter(ImageFilter.GaussianBlur(radius=blurr))
        
        press_mark=400
        blurredpicture_2_.setImage(blurredpicture)
        # keep track of which components have finished
        BlurredComponents = [blurr_confirm, blurredpicture_2_]
        for thisComponent in BlurredComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Blurred"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BlurredClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blurr_confirm* updates
            if t >= 0.0 and blurr_confirm.status == NOT_STARTED:
                # keep track of start time/frame for later
                blurr_confirm.tStart = t
                blurr_confirm.frameNStart = frameN  # exact frame index
                blurr_confirm.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(blurr_confirm.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blurr_confirm.status == STARTED and t >= frameRemains:
                blurr_confirm.status = STOPPED
            if blurr_confirm.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    blurr_confirm.keys = theseKeys[-1]  # just the last key pressed
                    blurr_confirm.rt = blurr_confirm.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            #print(confirm_space.status)
            if blurr_confirm.keys == 'space':
                continueRoutine=False
                send_to_NS(str(press_mark).zfill(4))   #0400
            
            # *blurredpicture_2_* updates
            if t >= 0.0 and blurredpicture_2_.status == NOT_STARTED:
                # keep track of start time/frame for later
                blurredpicture_2_.tStart = t
                blurredpicture_2_.frameNStart = frameN  # exact frame index
                blurredpicture_2_.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blurredpicture_2_.status == STARTED and t >= frameRemains:
                blurredpicture_2_.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlurredComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blurred"-------
        for thisComponent in BlurredComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if blurr_confirm.keys in ['', [], None]:  # No response was made
            blurr_confirm.keys=None
        Intrial.addData('blurr_confirm.keys',blurr_confirm.keys)
        if blurr_confirm.keys != None:  # we had a response
            Intrial.addData('blurr_confirm.rt', blurr_confirm.rt)
        if blurr_confirm.keys == 'space':
            Intrial.finished=True
            press=1
            Trials.addData('Press', press)
            Trials.addData('Whenpress',intrials)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Intrial'
    
    # get names of stimulus parameters
    if Intrial.trialList in ([], [None], None):
        params = []
    else:
        params = Intrial.trialList[0].keys()
    # save data for this loop
    Intrial.saveAsText(filename + 'Intrial.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "ISI_afterblurr"-------
    t = 0
    ISI_afterblurrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if blurr_confirm.keys != 'space':
        press=0
        Trials.addData('Press', press)
    # keep track of which components have finished
    ISI_afterblurrComponents = [fixation_trial_4]
    for thisComponent in ISI_afterblurrComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI_afterblurr"-------
    while continueRoutine:
        # get current time
        t = ISI_afterblurrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_trial_4* updates
        if t >= 0.25 and fixation_trial_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_trial_4.tStart = t
            fixation_trial_4.frameNStart = frameN  # exact frame index
            fixation_trial_4.setAutoDraw(True)
        frameRemains = 0.25 + np.around(np.random.uniform(1,2), 3)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_trial_4.status == STARTED and t >= frameRemains:
            fixation_trial_4.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_afterblurrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI_afterblurr"-------
    for thisComponent in ISI_afterblurrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ISI_afterblurr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Curiosity_rating"-------
    t = 0
    Curiosity_ratingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Curiosity.reset()
    # keep track of which components have finished
    Curiosity_ratingComponents = [Curiosity]
    for thisComponent in Curiosity_ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Curiosity_rating"-------
    while continueRoutine:
        # get current time
        t = Curiosity_ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *Curiosity* updates
        if t >= 0.0 and Curiosity.status == NOT_STARTED:
            # keep track of start time/frame for later
            Curiosity.tStart = t
            Curiosity.frameNStart = frameN  # exact frame index
            Curiosity.setAutoDraw(True)
        continueRoutine &= Curiosity.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Curiosity_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Curiosity_rating"-------
    for thisComponent in Curiosity_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for Trials (TrialHandler)
    Trials.addData('Curiosity.response', Curiosity.getRating())
    Trials.addData('Curiosity.rt', Curiosity.getRT())
    # the Routine "Curiosity_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Confidence_rating"-------
    t = 0
    Confidence_ratingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Confidence.reset()
    # keep track of which components have finished
    Confidence_ratingComponents = [Confidence]
    for thisComponent in Confidence_ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Confidence_rating"-------
    while continueRoutine:
        # get current time
        t = Confidence_ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *Confidence* updates
        if t >= 0.0 and Confidence.status == NOT_STARTED:
            # keep track of start time/frame for later
            Confidence.tStart = t
            Confidence.frameNStart = frameN  # exact frame index
            Confidence.setAutoDraw(True)
        continueRoutine &= Confidence.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Confidence_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Confidence_rating"-------
    for thisComponent in Confidence_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for Trials (TrialHandler)
    Trials.addData('Confidence.response', Confidence.getRating())
    Trials.addData('Confidence.rt', Confidence.getRT())
    # the Routine "Confidence_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [fixation_trial_3]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_trial_3* updates
        if t >= 0.25 and fixation_trial_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_trial_3.tStart = t
            fixation_trial_3.frameNStart = frameN  # exact frame index
            fixation_trial_3.setAutoDraw(True)
        frameRemains = 0.25 + np.around(np.random.uniform(1,2), 3)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_trial_3.status == STARTED and t >= frameRemains:
            fixation_trial_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Clear"-------
    t = 0
    ClearClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    Clear_answer.setImage(picturenum)
    clear_mark=500
    send_to_NS(str(clear_mark).zfill(4))
    # keep track of which components have finished
    ClearComponents = [Clear_answer]
    for thisComponent in ClearComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Clear"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ClearClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Clear_answer* updates
        if t >= 0.0 and Clear_answer.status == NOT_STARTED:
            # keep track of start time/frame for later
            Clear_answer.tStart = t
            Clear_answer.frameNStart = frameN  # exact frame index
            Clear_answer.setAutoDraw(True)
        frameRemains = 0.0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Clear_answer.status == STARTED and t >= frameRemains:
            Clear_answer.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ClearComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Clear"-------
    for thisComponent in ClearComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [fixation_trial_3]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_trial_3* updates
        if t >= 0.25 and fixation_trial_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_trial_3.tStart = t
            fixation_trial_3.frameNStart = frameN  # exact frame index
            fixation_trial_3.setAutoDraw(True)
        frameRemains = 0.25 + np.around(np.random.uniform(1,2), 3)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_trial_3.status == STARTED and t >= frameRemains:
            fixation_trial_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Surprise_rating"-------
    t = 0
    Surprise_ratingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Surprise.reset()
    # keep track of which components have finished
    Surprise_ratingComponents = [Surprise]
    for thisComponent in Surprise_ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Surprise_rating"-------
    while continueRoutine:
        # get current time
        t = Surprise_ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *Surprise* updates
        if t >= 0.0 and Surprise.status == NOT_STARTED:
            # keep track of start time/frame for later
            Surprise.tStart = t
            Surprise.frameNStart = frameN  # exact frame index
            Surprise.setAutoDraw(True)
        continueRoutine &= Surprise.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Surprise_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Surprise_rating"-------
    for thisComponent in Surprise_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for Trials (TrialHandler)
    Trials.addData('Surprise.response', Surprise.getRating())
    Trials.addData('Surprise.rt', Surprise.getRT())
    # the Routine "Surprise_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Trials'

# get names of stimulus parameters
if Trials.trialList in ([], [None], None):
    params = []
else:
    params = Trials.trialList[0].keys()
# save data for this loop
Trials.saveAsText(filename + 'Trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
all_end_resp = event.BuilderKeyResponse()
if netstation:
    if recording:
        ns.StopRecording()
    ns.EndSession()
    ns.disconnect()
# keep track of which components have finished
EndComponents = [end_pic, all_end_resp]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_pic* updates
    if t >= 0.0 and end_pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_pic.tStart = t
        end_pic.frameNStart = frameN  # exact frame index
        end_pic.setAutoDraw(True)
    
    # *all_end_resp* updates
    if t >= 0.0 and all_end_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        all_end_resp.tStart = t
        all_end_resp.frameNStart = frameN  # exact frame index
        all_end_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if all_end_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()










# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
