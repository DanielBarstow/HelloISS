def ______________________________TOP_OF_FILE():
	return

# IMPORT
import math
import time
import json
import urllib.request
import ephem
import os
import sqlite3
from tkinter import *  # standard tkinter - these use no prefix
from datetime import *

###########################
#  TEST AND DEMO FLAGS
###########################
def _____________________________V_TEST_FLAGS():
	return

autoRefreshFullDisplay = FALSE
refreshGetHamLocations = TRUE
refreshGetNewLocalAprs = TRUE
getNewTLE = TRUE
dataTableDefinedInFunction = TRUE
refreshGetNewGlobalAprs = TRUE

mapShowGlobalAprsAtIssLocations = TRUE  # ISS location at time of msg
mapShowGlobalAprsAtRecStns = TRUE  # Receiving stns
mapShowGlobalAprsLinesIssToRecStns = FALSE  # Lines connecting ISS and rec stns
mapShowGlobalAprsCallSignAtRecStns = FALSE  # Call signs
mapShowMinuteMarkers = FALSE  # Minute markers on ISS path
mapShowCircleAroundIss = TRUE  # Circle around ISS

def ______________________________V_CONSTANTS():
	return

###########################
#  EARTH & ISS CONSTANTS
###########################

issMinsPerOrbit = 92
issAltitudeMiles = 250
issOrbitsPerDay = 24 / (issMinsPerOrbit/60)

###########################
#  MATH CONSTANTS
###########################

radFloatToDegFloatMultiplier = 57.2958

###########################
#       PYEPHEM
###########################
def _____________________________V_PYEPHEM():
	return

# PYEPHEM CONSTANTS
pyephemFlyoverRiseDtPos = 0
pyephemFlyoverRiseAzPos = 1
pyephemFlyoverMaxDtPos = 2
pyephemFlyoverMaxAltPos = 3
pyephemFlyoverSetDtPos = 4
pyephemFlyoverSetAzPos = 5

# LOCALIZE FOR STOW MA
localLatStr = "42.4075"
localLonStr = "-71.5062"
localElev = 64
localTimeZoneOffset = -4  # from UTC - don't change name or caps, first check if used this way by ephem

# FLYOVER CONSTANTS
minVisDeg = 20
goodVisDeg = 45

pyephemSunRiseFix = -2 / 24  # Kludge - pyephem gives local sun RISE 2 hours LATER   than reality.  Why?
pyephemSunSetFix = 2 / 24  # Kludge - pyephem gives local sun SET  2 hours EARLIER than reality.  Why?
pyephemHalfDayCorrection = 0.5  # because pyephem uses noon as starting time for each day


###########################
#       PAGE DESIGN
###########################
def ___________________________V_PAGE_SIZE():
	return

# FULL PAGE
fullPageRightPix = 1700
fullPageBottomPix = 1000

# CHAR SIZE
charWid = 8
charHi = 17

# GLOBAL COLORS
def ___________________________V_PAGE_COLORS():
	return
neutralBg = ""
allTextFg = "black"

stdBoxOutline = "black"

highlightBg = "gold"

sectionTitleBg = "pink"
sectionTitleOutline = "pink"

tableHeaderBg = "white"
tableTextBg = ""
tableLineFg = "black"

flyoverTimelineBg = "medium turquoise"
flyoverTimelineHorizLineColor = "light grey"
flyoverTimelineVertHourLineColor = "light grey"
flyoverTimelineVertDayLineColor = "light grey"
flyoverTimelineNightBlockColor = "dark slate grey"
flyoverTimelineDayLabelColor = "green"
flyoverTimelineIssVisMarkerColor = "gold"
flyoverTimelineIssNotVisMarkerColor = "black"

mapReceiveAreaBestFg = "orange"
mapReceiveAreaFarFg = "cornflower blue"
mapPastOrbitDayColor = "grey"
mapPastOrbitNightColor = "grey"
mapFutureOrbitDayColor = "gold"  #gold
mapFutureOrbitNightColor = "black"   #black
mapMinuteMarkersColor = "white"
mapRecStnColor = "light grey"  # "dark turquoise"
mapMsgLinesColor = "dark grey"

aprsTimelineBg = "medium turquoise"
aprsTimelineMark = "black"
aprsTimelineRs0issMark = "light grey"
aprsTimelineLabel = "green"
aprsTimelineLabelMarker = "green" # "light grey"
aprsTimelineOrbitsMarker = "black"

promptBg = "dark sea green"
actionMsgBg = "powder blue"

def _____________________________V_SCREEN_LAYOUT():
	return

# TOP PIX
flyoverTopPix = regMapTopPix = worldMapTopPix = 0
flyoverTimelineTopPix = 250
sendToIssTopPix = recByLocalRadioTopPix = 305
controlCenterTopPix = recByGlobalNetTopPix = 620
actionMsgTopPix = aprsTimelineTopPix = 880

# LEFT PIX
flyoverLeftPix = flyoverTimelineLeftPix = sendToIssLeftPix = controlCenterLeftPix = actionMsgLeftPix = 0
regMapLeftPix = 490
worldMapLeftPix = recByLocalRadioLeftPix = recByGlobalNetLeftPix = aprsTimelineLeftPix = 800

# BOTTOM PIX (auto calc from top pix)
flyoverBottomPix = flyoverTimelineTopPix - 1
flyoverTimelineBottomPix = sendToIssTopPix - 5
regMapBottomPix = worldMapBottomPix = sendToIssTopPix - 1
sendToIssBottomPix = recByLocalRadioBottomPix = controlCenterTopPix - 1
controlCenterBottomPix = recByGlobalNetBottomPix = actionMsgTopPix - 1
actionMsgBottomPix = aprsTimelineBottomPix = fullPageBottomPix - 85

# RIGHT PIX (autocalc from left pix)
flyoverRightPix = flyoverTimelineRightPix = regMapLeftPix - 20
regMapRightPix = sendToIssRightPix = controlCenterRightPix = actionMsgRightPix = worldMapLeftPix - 10
worldMapRightPix = recByLocalRadioRightPix = recByGlobalNetRightPix = aprsTimelineRightPix = fullPageRightPix

###########################
#  MAPS
###########################
def ____________________________V_MAPS():
	return

worldMapFileName = 'world_equirectangular_60NS_900x300pix.gif'
worldMapLeftLonDeg = -180
worldMapRightLonDeg = 180
worldMapTopLatDeg = 60
worldMapBottomLatDeg = -60

regMapFileName = 'reg_equirectangular_minus87to57lon_28to58lat_300x300.gif'
regMapLeftLonDeg = -87
regMapRightLonDeg = -57
regMapTopLatDeg = 58
regMapBottomLatDeg = 28

###########################
#  GLOBAL DATA TABLES
###########################
def ____________________________V_DATA_TABLES():
	return

# common across all data
allDataDtKeyCol = 0
allDataPriorityCol = 1

# APRS data format
aprsDataFormat = [['DTKEY', 'Priority', 'Date', '  Time', 'Sender', 'Receiver', 'Path', 'Message'],
					['13', 		'1', 		'7', 	'10', 	'10', 		'9', 	'25', 	'55']]
aprsDateCol = 2
aprsTimeCol = 3
aprsSenderCol = 4
aprsReceiverCol = 5

# Local APRS
localAprsNewReceivedSourceFile = "TEMP latest local radio APRS received.txt"
localAprsAllDataJson = 'localReceiveAllData.json'
localAprsData = []

# Global APRS
globalAprsINTERIMtextFile = "ISS data reports.txt"
globalAprsAllDataJson = "globalReceiveAllData.json"
globalAprsData = []

# Global Downlink Stations
allGlobalDownlinkStnsJson = 'allGlobalDownlinkStns.json'
allGlobalDownlinkStns = []

# Email Requests
emailRequestsFile = 'emailRequestsFile.json'
emailRequestsFormat = [
	['DTKEY', 'Priority', 'Date', 'Time', 'Sent', 'Conf', 'First', 'Last', 'Email', 'Message', 'len'],
	['13', 		'1', 		'5', 	'6', 	'4', 	'4', 	'7', 	'8', 	'31', 		'30', 	'6']]
emailRequestsData = []

# Flyovers
flyoversFormat = [
	['DTKEY', 'Priority', 'T-Minus', ' Date', '  Start', '   End', '  Len', 'Peak', 'Rise', 'Set', 'Local', 'ISS', 'Vis'],
	['13', 		'1', 		'7', 		'6', 	'7', 		'7', 	'6', 	'5', 	'4', 	'4', 	'5', 	'4', 	'4']]
flyoversData = []
flyoversPeakDegCol = 7
flyoversVisCol = 12


###########################
#      Catch-Rest
###########################
def _____________________________V_CATCH_REST():
	return

currentAprsMsg = ""

imageIdArray = []

dtTupleYearPos = 0
dtTupleMonPos = 1
dtTupleDayPos = 2
dtTupleHrPos = 3
dtTupleMinPos = 4
dtTupleSecPos = 5


###########################
#       CLASSES
###########################
def _____________________________CLASSES():
	return

class box:
	def __init__(self, left, top, right, bottom):
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom


class mapSpecs:
	def __init__(self, leftPix, topPix, rightPix, bottomPix, leftlon, rightlon, toplat, bottomlat):
		self.LeftPix = leftPix
		self.TopPix = topPix
		self.RightPix = rightPix
		self.BottomPix = bottomPix
		self.leftlon = leftlon
		self.rightlon = rightlon
		self.toplat = toplat
		self.bottomlat = bottomlat
		self.pixperdeg = (rightPix - leftPix) / (rightlon - leftlon)


class dataTable:
	def __init__(self, dataTableData, dataTableFormat):
		self.dataTableData = dataTableData
		self.dataTableFormat = dataTableFormat

	def clearTable(self):
		self.dataTableData.clear()

	def appendData(self, thisData):
		self.dataTableData.append(thisData)

	def prependData(self, thisData):
		self.dataTableData.insert(0,thisData)

	def ifNewInsertData(self, thisDataFromUrl):
		thisDataFromUrlDtKey = thisDataFromUrl[allDataDtKeyCol]
		print("\n searching for DtKey:     ", thisDataFromUrlDtKey)
		for thisRow in range(0,len(self.dataTableData)):
			nextOlderDataFromActiveTableDtKey = self.dataTableData[thisRow][allDataDtKeyCol]
			if FALSE: print("  compare with:   ",nextOlderDataFromActiveTableDtKey)
			if thisRow == 0:
				if thisDataFromUrlDtKey > nextOlderDataFromActiveTableDtKey:
					self.dataTableData.insert(0,thisDataFromUrl)
					print("  ** added NEWER DATA")
					return
				prevNewerDataFromActiveTableDtKey = nextOlderDataFromActiveTableDtKey
			elif thisDataFromUrlDtKey == nextOlderDataFromActiveTableDtKey:  # match, so skip
				print("  ** skipped - already have")
				return
				# elif thisDataFromUrlDtKey > nextOlderDataFromActiveTableDtKey and thisDataFromUrlDtKey < prevNewerDataFromActiveTableDtKey:
			elif prevNewerDataFromActiveTableDtKey > thisDataFromUrlDtKey > nextOlderDataFromActiveTableDtKey:
				self.dataTableData.insert(thisRow,thisDataFromUrl)
				print("  ** added INSERT DATA")
				return
			prevNewerDataFromActiveTableDtKey = nextOlderDataFromActiveTableDtKey
		self.dataTableData.append(thisDataFromUrl)
		print("  ** added OLDER DATA")

	def displayTable(self, thisBox, thisTag):
		# initialize values
		thisFormat = self.dataTableFormat
		thisTable = self.dataTableData
		thisGridLastRow = int((thisBox.bottom - thisBox.top) / charHi) - 2
		thisFormatLastCol = len(thisFormat[0]) # TEST THIS
		thisTableLastRow = len(thisTable)
		if thisTableLastRow < thisGridLastRow:
			thisTableLastDisplayRow = thisTableLastRow
		else:
			thisTableLastDisplayRow = thisGridLastRow
		if FALSE:
			print("in Display Table, for thisTag = "+thisTag)
			print("thisTableLastRow =" + str(thisTableLastRow))
			print(str(thisTable))
			print("\n")

		# clear display
		canvasBox.delete(thisTag)

		# display labels & lines
		displayAnyRectangle(thisBox.left, thisBox.top + charHi,thisBox.right, thisBox.top + charHi * 2 - 1,
							tableHeaderBg, tableHeaderBg, thisTag)
		colpos = 1  # this gives a blank space at beginning of display line
		for labelCol in range(thisFormatLastCol):
			thisText = thisFormat[0][labelCol]  # Label
			if labelCol > 2: colpos = colpos + int(thisFormat[1][labelCol - 1])  # increment colpos
			if labelCol > 1:
				displayAnyText(thisBox.left + colpos * charWid,thisBox.top + charHi,
							   thisText, allTextFg, tableHeaderBg, thisTag)
		displayAnyLine(thisBox.left, thisBox.top + charHi - 1,thisBox.right, thisBox.top + charHi - 1,
					   tableLineFg, thisTag)
		displayAnyLine(thisBox.left, thisBox.top + 2 * charHi - 1,thisBox.right, thisBox.top + 2 * charHi - 1,
					   tableLineFg, thisTag)

		# display data
		if thisTableLastRow>0 and TRUE:  # if this table has data

			# for each row
			for tableRow in range(thisTableLastDisplayRow):
				if FALSE: print("for tableRow= "+str(tableRow) + " = "+str(thisTable[tableRow]))

				# set color & draw background if priority
				if thisTable[tableRow][allDataPriorityCol] == "2":
					thisBgColor = "gold"
					displayAnyRectangle(thisBox.left,thisBox.top + (2 + tableRow) * charHi,thisBox.right,
										thisBox.top + (3 + tableRow) * charHi,thisBgColor, thisBgColor, thisTag)
				else:
					thisBgColor = tableTextBg

				colpos = 1  # re-initialize colpos
				# for every col in the table
				for tableCol in range(thisFormatLastCol):
					if tableCol > 2: # increment colpos in every col except first
						colpos = colpos + int(thisFormat[1][tableCol - 1])
					if tableCol > 1:

						# define text, and make sure it fits
						thisText = thisTable[tableRow][tableCol][0:int(thisFormat[1][tableCol])]
						actualLen = len(thisTable[tableRow][tableCol])
						maxLen = int(thisFormat[1][tableCol])
						if actualLen > maxLen: thisText = thisText + "..."

						# display text
						displayAnyText(thisBox.left + colpos * charWid,
									   thisBox.top + (2 + tableRow) * charHi,
									   thisText,
									   allTextFg,
									   thisBgColor,
									   thisTag)
						if FALSE:
							print("/nin display table, row, col, text:", str(tableRow), " ", str(tableCol)," ",thisText)

				# display lines below each row
				displayAnyLine(thisBox.left, thisBox.top + (tableRow + 3) * charHi - 1,
									thisBox.right, thisBox.top + (tableRow + 3) * charHi - 1, tableLineFg, thisTag)





###########################
#       USER IO
###########################
def _____________________________USER_IO():
	return

def waitSecs(secs):
	time.sleep(secs)

def waitInput():
	input("Press Enter to continue. . .")

def waitInputMsg(thisMess):
	showMess = thisMess + ": Press Enter. . ."
	input(showMess)

def showProgressMsg(thisText):
	thisTag = "tagActionMsg"
	canvasBox.delete(thisTag)
	displayAnyText(actionMsgSectionBox.left + 2,
				   actionMsgSectionBox.top + 10,
				   thisText,
				   allTextFg,
				   actionMsgBg,
				   thisTag)
	canvasBox.update()

def promptForTextInput(thisBoxLeft, thisBoxTop, bothRowChar, promptStartChar, promptWidthChar, entryWidthChar,promptText):
	thisTag = "tagPrompt"
	promptLeftPos = thisBoxLeft + charWid * promptStartChar
	entryLeftPos = promptLeftPos + charWid * promptWidthChar
	promptRightPos = entryLeftPos
	bothTopPos = thisBoxTop + charHi * bothRowChar
	bothBottomPos = bothTopPos + charHi + 1
	displayAnyRectangle(promptLeftPos, bothTopPos+1, promptRightPos, bothBottomPos, promptBg, stdBoxOutline, thisTag)
	displayAnyText(promptLeftPos+1, bothTopPos+2, promptText, allTextFg, promptBg, thisTag)
	thisEntry = Entry(root, width=entryWidthChar)
	thisEntry.place(x=entryLeftPos, y=bothTopPos)

	return thisEntry


###########################
#         MATH
###########################
def ________________________________MATH():
	return

def radFloatToDegFloat(radFloat):
	return radFloat * radFloatToDegFloatMultiplier

def degFloatToRadFloat(degfloat):
	return degfloat / radFloatToDegFloatMultiplier

def radFloatToDirText(radfloat):
	degint = int(radFloatToDegFloat(radfloat))
	if degint < 22:
		textdir = "N"
	elif degint < 67:
		textdir = "NE"
	elif degint < 112:
		textdir = "E"
	elif degint < 157:
		textdir = "SE"
	elif degint < 202:
		textdir = "S"
	elif degint < 247:
		textdir = "SW"
	elif degint < 292:
		textdir = "W"
	elif degint < 337:
		textdir = "NW"
	else:
		textdir = "N"
	return textdir


###########################
#       DATE TIME
###########################
def _____________________________DATE_TIME():
	return

def dtTupleToStr(dtTuple, formatstr, fromzone, tozone):
	allMons = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

	yearint = dtTuple[dtTupleYearPos]
	monint = dtTuple[dtTupleMonPos]
	daysint = dtTuple[dtTupleDayPos]
	hoursint = dtTuple[dtTupleHrPos]
	minsint = dtTuple[dtTupleMinPos]
	secsint = dtTuple[dtTupleSecPos]
	if fromzone == "UTC" and tozone == "LOCAL":
		hoursint += localTimeZoneOffset
		if hoursint < 0:
			hoursint += 24
			daysint -= 1
			if daysint < 0:
				monint -= 1
				if monint < 1:
					monint = 12
					yearint -= 1

	# year
	yearstr = str(yearint)

	# mon
	if formatstr == "DT13":
		addzero_mon = "0" if monint < 10 else ""
		monstr = addzero_mon + str(monint)
	else:
		monstr = str(allMons[monint - 1])

	# day
	if formatstr == "DT13":
		addzero_day = "0" if daysint < 10 else ""
	else:
		addzero_day = ""
	daystr = addzero_day + str(daysint)

	# am pm
	if formatstr == "HM12" or formatstr == "HMS12":
		hrsampm = "p" if hoursint > 12 else "a"
		if hoursint > 12: hoursint -= 12

	# hours
	if hoursint > 9:
		addzero_hour = ""
	elif formatstr == "HM12" or formatstr == "HMS12" or formatstr == "HHHM":
		addzero_hour = "  "
	else:
		addzero_hour = "0"
	hrstr = addzero_hour + str(hoursint)

	# min
	addzero_min = "0" if minsint < 10 else ""
	minstr = addzero_min + str(minsint)

	# sec
	addzero_sec = "0" if secsint < 10 else ""
	secstr = addzero_sec + str(int(secsint))

	# assemble all the pieces
	if formatstr == "MD":
		dtStr = monstr + " " + daystr
	elif formatstr == "HM":
		dtStr = hrstr + ":" + minstr
	elif formatstr == "HM12":
		dtStr = hrstr + ":" + minstr + hrsampm
	elif formatstr == "MS":
		dtStr = minstr + ":" + secstr
	elif formatstr == "HMS":
		dtStr = hrstr + ":" + minstr + ":" + secstr
	elif formatstr == "HMS12":
		dtStr = hrstr + ":" + minstr + ":" + secstr + hrsampm
	elif formatstr == "DHM":
		dtStr = day_str + hrstr + ":" + minstr
	elif formatstr == "HHHM":
		dtStr = hrstr + ":" + minstr
	elif formatstr == "DT13":
		dtStr = yearstr + monstr + daystr + hrstr + minstr + secstr

	if FALSE:
		print("in dtTupleToStr, dtTuple:", dtTuple)
		print("in dtTupleToStr, formatstr:", formatstr)
		print("in dtTupleToStr, dtStr=", dtStr)

	return dtStr

def dt13ToTuple(dt_DT13):
	yearsint = int(dt_DT13[0:4])
	monsint = int(dt_DT13[4:6])
	daysint = int(dt_DT13[6:8])
	hrsint = int(dt_DT13[8:10])
	minsint = int(dt_DT13[10:12])
	secsint = int(dt_DT13[12:])
	return (yearsint, monsint, daysint, hrsint, minsint, secsint)  # returns a tuple

def dt13ToFloat(dt_DT13):
	yearsint = int(dt_DT13[0:4])
	monsint = int(dt_DT13[4:6])
	daysint = int(dt_DT13[6:8])
	hrsint = int(dt_DT13[8:10])
	minsint = int(dt_DT13[10:12])
	secsint = int(dt_DT13[12:])

	localobserver.date = ((yearsint, monsint, daysint, hrsint, minsint, secsint))
	returnDt = localobserver.date  # this two step process makes this float step work

	if FALSE:
		print("\n\n\nin dt13ToFloat, dt_DT13 in:", dt_DT13)
		print("\n************************************************")
		print("in dt13ToFloat, localobserver.date out:", str(float(returnDt)))

	return returnDt

def dtLenSecsToStr(dt_secs, formatstr):
	secsbal = dt_secs
	if formatstr == "DHM":
		dayint = int(secsbal / (24 * 60 * 60)) if secsbal > 24 * 60 * 60 else 0
		secsbal = secsbal - (dayint * 24 * 60 * 60)
	else:
		dayint = 0

	hrint = int(secsbal / (60 * 60)) if secsbal > 60 * 60 else 0
	secsbal = secsbal - (hrint * 60 * 60)
	minint = int(secsbal / 60) if secsbal > 60 else 0
	secsbal = secsbal - (minint * 60)
	secint = int(secsbal) if secsbal > 0 else 0

	timelen_tuple = (0, 0, dayint, hrint, minint, secint)
	timelen_str = dtTupleToStr(timelen_tuple, formatstr, "NONE", "NONE")
	if FALSE:
		print("in dt_TimelenSecsToStrFormat, tuple:", timelen_tuple)
		print("in dt_TimelenSecstoStrFormat, timelen_str:", timelen_str)

	return timelen_str

def dtTupleHmsToSecs(dt_tuple):
	totalsecs = (dt_tuple[dtTupleHrPos] * 60 * 60 + dt_tuple[dtTupleMinPos] * 60 + int(dt_tuple[dtTupleSecPos]))
	if FALSE:
		print("in dtTupleHmsToSecs, totalsecs=", str(totalsecs))
	return totalsecs

def dtFloatToDt13(dtFloat):
	dtFloat += 0.5  # Kludge
	dayFraction = math.fmod(dtFloat, 1)
	hrs = math.floor(dayFraction * 24)
	dayFraction -= hrs / 24
	mins = math.floor(dayFraction * (60 * 24))
	dayFraction -= mins / (60 * 24)
	secs = math.floor(dayFraction * (60 * 60 * 24))
	return str(hrs) + ":" + str(mins) + ":" + str(secs)


###########################
#    PYEPHEM CALCS
###########################
def ____________________________PYEPHEM():
	return

def nightFlyover(peakTimeUtc):
	printDiagnostics = FALSE

	if printDiagnostics:
		print("\nin NightFlyover")
	prevSunSetTimeUtc = localobserver.previous_setting(ephem.Sun(), start=peakTimeUtc) + pyephemSunSetFix
	prevSunRiseTimeUtc = localobserver.previous_rising(ephem.Sun(), start=peakTimeUtc) + pyephemSunRiseFix
	dayLengthDecDay = prevSunSetTimeUtc - prevSunRiseTimeUtc
	if prevSunRiseTimeUtc > prevSunSetTimeUtc:
		dayLengthDecDay += 24
		if printDiagnostics: print("sunrise AFTER sunset")
	else:
		if printDiagnostics: print("sunrise BEFORE sunset")

	if (peakTimeUtc - prevSunRiseTimeUtc)>1:
		offset=-1
	else:
		offset=0
	atNight = (peakTimeUtc - prevSunRiseTimeUtc) + offset > dayLengthDecDay

	if FALSE:
		print(peakTimeUtc)
		print("peakTimeUtc float =" + str(float(peakTimeUtc)))
		print("prevSunRise float =" + str(float(prevSunRiseTimeUtc)))
		print("prevSunSet  float =" + str(float(prevSunSetTimeUtc)))
		print("peak - sunrise fl =" + str(float(peakTimeUtc - prevSunRiseTimeUtc)))
		print("dayLengthDecDay   =" + str(float(dayLengthDecDay)))
		print("at night          =" + str(atNight))
		print("\n")
	if FALSE:
		print("peakTimeUtc Source=" + str(peakTimeUtc))
		print("peakTime    Utc   =" + dtFloatToDt13(float(peakTimeUtc)))
		print("peakTime    Local =" + dtFloatToDt13(float(peakTimeUtc - 4 / 24)))
		print("prevSunRise Utc   =" + dtFloatToDt13(float(prevSunRiseTimeUtc)))
		print("prevSunRise Local =" + dtFloatToDt13(float(prevSunRiseTimeUtc) - 4 / 24))
		print("prevSunSet  Utc   =" + dtFloatToDt13(float(prevSunSetTimeUtc)))
		print("prevSunSet  Local =" + dtFloatToDt13(float(prevSunSetTimeUtc) - 4 / 24))
		print("dayLengthDecDay   =" + str(dayLengthDecDay))

		print("flyover at night   =" + str(atNight))

	return atNight


###########################
#    APRS PRIMITIES
###########################
def ____________________________APRS():
	return

def parsAprsRawToAprsData(thisAprsRaw):
	searchendofsender = "]"
	searchendofpath = ":"
	pathsteps_marker = ","

	# set Keyfield
	keyfield_dt13 = thisAprsRaw[0:14]
	if FALSE: waitInputMsg("keyfield:" + keyfield_dt13)

	# set date and time
	thisdate = dtTupleToStr(dt13ToTuple(keyfield_dt13), "MD", "UTC", "LOCAL")
	thistime = dtTupleToStr(dt13ToTuple(keyfield_dt13), "HMS12", "UTC", "LOCAL")

	# set sender
	endsenderpos = thisAprsRaw.find(searchendofsender)
	if endsenderpos > 0:
		thissender = str(thisAprsRaw[17:endsenderpos])

	# set path and message
	endpathpos = thisAprsRaw.find(searchendofpath, endsenderpos)
	if endpathpos > 0:
		thispath = str(thisAprsRaw[endsenderpos + 1:endpathpos])
		if thisAprsRaw[endpathpos + 1].isalnum():
			startmessagepos = endpathpos + 1
		else:
			startmessagepos = endpathpos + 2
		thismessage = str(thisAprsRaw[startmessagepos:len(thisAprsRaw) - 4])  # -4 to remove end of line break chars

	# set receiver
	# startreceiverpos = endpathpos - 6
	startreceiverpos = thispath.rfind(pathsteps_marker)
	if startreceiverpos > 0:
		thisreceiver = str(thispath[startreceiverpos + 1:])

		# if new, add to Receive Station list
		if isHamInDatatable(thisreceiver) == FALSE:
			thisRecStnData = webGetHamLocation(thisreceiver)
			if FALSE:
				print("\nthisRecStnData" + str(thisRecStnData))
			if thisRecStnData is not None:
				allGlobalDownlinkStns.append((thisRecStnData[0], thisRecStnData[1], thisRecStnData[2]))
				saveDownlinkStnsToJson()
				if FALSE:
					print("\nthisRecStnData" + str(thisRecStnData))
					print("thisRecStnData ham call sign" + thisRecStnData[0])

	# append this full report to data table
	newcontactstr = keyfield_dt13, '1', thisdate, thistime, thissender, thisreceiver, thispath, thismessage
	return(newcontactstr)


###########################
#    CREATE DATA TABLES
###########################
def ____________________________PRE_CREATE():
	return

def preCreateJsonForDataTable():  # do this once to create the initial json file
	with open(globalAprsAllDataJson, 'w') as writeFile:
		json.dump(globalAprsData, writeFile)
	print("in precreate Json, just opened and dumped data")
	return

def clearJsonDataTable():
	allGlobalDownlinkStns.clear()
	if FALSE:
		print("cleared before save\n" + str(allGlobalDownlinkStns))
	with open(allGlobalDownlinkStnsJson, 'w') as fileObject:
		json.dump(allGlobalDownlinkStns, fileObject)


###########################
#      DATA - STARTUP
###########################
def ____________________________DATA_STARTUP():
	return

def webGetIssEphem():
	thisSourceUrl = 'http://www.celestrak.com/NORAD/elements/stations.txt'

	foundISS = -1
	gotallISS = FALSE
	issline = 0
	issephem = ['', '', '']
	if getNewTLE:
		f = urllib.request.urlopen(thisSourceUrl)
		for line in f:
			thisstr = str(line.rstrip(), encoding="utf-8")  # WEB TEXT IS UTF-8 ENCODED, THIS REMOVES B'
			if FALSE: print("thisstr=", thisstr)
			if foundISS > -1 and gotallISS == FALSE:
				issline += 1
				issephem[issline] = thisstr
				if issline == 2:
					f.close()
					if FALSE: print("issephem: ", issephem)
					issephemcorrected = (issephem[0], issephem[1], issephem[2])
					if FALSE: print("issephemcorrected: ", issephemcorrected)
					return issephemcorrected
			elif foundISS == -1:
				foundISS = thisstr.find('ISS (ZARYA)')
				if foundISS > -1:
					issephem[issline] = thisstr
					if FALSE: print("found it %s" % issephem[issline])
		f.close()
	else:
		issephem = ("ISS",
					"1 25544U 98067A   17172.89442130  .00001906  00000-0  36110-4 0  9990",
					"2 25544  51.6433  14.8648 0004452 307.3885 252.6376 15.54069411 62481")
		issephemcorrected = (issephem[0], issephem[1], issephem[2])
		return issephemcorrected

def calculateDatatableFlyovers():
	localobserver.date = ephem.now()
	flyoversLastDataTableRow = 12  # no scrolling, so same as number of display rows
	showrow = 0
	flyoversDataTable.clearTable()
	if FALSE:
		print("\n CREATE DATATABLE FLYOVERS")
	while showrow < flyoversLastDataTableRow:

		# Get nextpass
		nextpass = localobserver.next_pass(iss)

		# determine if high enough flyover
		issPeakDeg = str(int(radFloatToDegFloat(nextpass[pyephemFlyoverMaxAltPos])))

		if int(issPeakDeg) >= minVisDeg:

			# Calculate keyfield
			keyfield_dt13 = dtTupleToStr(nextpass[pyephemFlyoverRiseDtPos].tuple(), "DT13", "UTC", "UTC")
			if FALSE:
				print("***setting keyfield_dt13:")
				print("   source is ristime")
				print(nextpass[pyephemFlyoverRiseDtPos].tuple())
				print("   result is: " + keyfield_dt13)

			# Calculate rise & set dt
			risedate = dtTupleToStr(nextpass[pyephemFlyoverRiseDtPos].tuple(), "MD", "UTC", "LOCAL")
			risetime = dtTupleToStr(nextpass[pyephemFlyoverRiseDtPos].tuple(), "HM12", "UTC", "LOCAL")
			settime = dtTupleToStr(nextpass[pyephemFlyoverSetDtPos].tuple(), "HM12", "UTC", "LOCAL")

			# calculate rise & set angles
			riseazimuth = radFloatToDirText(nextpass[pyephemFlyoverRiseAzPos])
			setazimuth = radFloatToDirText(nextpass[pyephemFlyoverSetAzPos])

			# calculate fly-over length
			rise_secs = dtTupleHmsToSecs(nextpass[pyephemFlyoverRiseDtPos].tuple())
			set_secs = dtTupleHmsToSecs(nextpass[pyephemFlyoverSetDtPos].tuple())
			flyoverlen_secs = set_secs - rise_secs
			if flyoverlen_secs < 0: flyoverlen_secs += 24 * 60 * 60  # if midnight happens between rise and set times
			flyoverlen = dtLenSecsToStr(flyoverlen_secs, "MS")

			# get now
			now = ephem.now()

			# Calculate T-minus for this flyover
			tminus_total_secs = int((nextpass[pyephemFlyoverRiseDtPos] - now) * 24 * 60 * 60)
			tminus = dtLenSecsToStr(tminus_total_secs, "HHHM")

			if FALSE:
				print("In calculate flyover table, now= " + str(now))
				print("In calculate flyover table, nextpass rise= " + str(nextpass[pyephemFlyoverRiseDtPos]))
				print("In calculate flyover table, nextpass set= " + str(nextpass[pyephemFlyoverSetDtPos]))

			# sent and conf - temporary surrogate
			sent = "0"
			conf = "0"

			# is ISS flyover at night and visible
			atNight = nightFlyover(nextpass[pyephemFlyoverRiseDtPos])
			localobserver.date = nextpass[pyephemFlyoverRiseDtPos].tuple()

			iss.compute(localobserver)
			issInSun = (iss.eclipsed == FALSE)
			localDayOrNight = "night" if atNight else "day"
			issDayOrNight = "sun" if issInSun else "dark"
			passVis = "vis" if atNight and issInSun else "-"

			prioritylevel = "2" if passVis == "vis" else "1"

			# ASSEMBLE FLYOVER full row of data
			thisflyover_fullrow = (keyfield_dt13, prioritylevel, tminus, risedate, risetime, settime,
								   flyoverlen, issPeakDeg, riseazimuth, setazimuth, localDayOrNight, issDayOrNight,
								   passVis)

			flyoversDataTable.appendData(thisflyover_fullrow)

			showrow += 1

			if FALSE:
				print("\nin define flyover, 1 calc nextpass, risetime:", nextpass[pyephemFlyoverRiseDtPos].tuple())
				print("  keyfield_dt13=" + keyfield_dt13)
				print("  rise_time:%s  rise_az:%s" % (
					nextpass[pyephemFlyoverRiseDtPos], nextpass[pyephemFlyoverRiseAzPos]))
				print("  max_time: %s  max_alt:%s" % (
					nextpass[pyephemFlyoverMaxDtPos], nextpass[pyephemFlyoverMaxAltPos]))
				print(
					"  set_time: %s  set_az: %s" % (nextpass[pyephemFlyoverSetDtPos], nextpass[pyephemFlyoverSetAzPos]))
				print("  rise_time tuple:", nextpass[pyephemFlyoverRiseDtPos].tuple())
				print("In flyover, 2 set nextpass, localobserver.date:", localobserver.date.tuple())

		if TRUE:  # THIS FIXED ERROR with NEXTPASS returning bad times occasionally, see below
			localobserver.date = nextpass[pyephemFlyoverSetDtPos].tuple()
			localobserver.date += 0.05  # increment for next pass
##              if FALSE: # normal
##                      localobserver.date=nextpass[flyover_setdt_pos].tuple()
##              if FALSE: # good date
##                      localobserver.date=(2017, 7, 3, 13, 59, 49.905373309738934)  # GOOD DATE
##              if FALSE: # bad date
##                      localobserver.date=(2017, 7, 3, 15, 37, 15.827914369292557)  # BAD DATE
##              if FALSE: # experiment with direct change of date
##                      localobserver.date=(2017, 7, 3, 15, 37, 15.827924369292557)  # MinDif for good 15.8279*2*
##              if FALSE: # experiment with increment amount
##                      localobserver.date=nextpass[flyover_setdt_pos].tuple()
##                      localobserver.date+=0.01                                    # test increment to fix

def globalAprsCreateDataTableFromJson():
	global globalAprsDataTable
	with open(globalAprsAllDataJson, 'r') as readFile:
		globalAprsData = json.load(readFile)
	globalAprsDataTable = dataTable(globalAprsData, aprsDataFormat)
	if FALSE: print(globalAprsData)

def localRadioAprsCreateDataTableFromJson():
	global localAprsDataTable
	with open(localAprsAllDataJson, 'r') as readFile:
		localAprsData = json.load(readFile)
	localAprsDataTable = dataTable(localAprsData,aprsDataFormat)
	if FALSE: print(localAprsData)

def emailRequestsCreateDataTableFromJson():
	global emailRequestsDataTable
	with open(emailRequestsFile, 'r') as readFile:
		emailRequestsData = json.load(readFile)
	emailRequestsDataTable = dataTable(emailRequestsData, emailRequestsFormat)
	if FALSE: print(emailRequestsData)

def downlinkStnsCreateReferenceDataFromJson():
	global allGlobalDownlinkStns
	with open(allGlobalDownlinkStnsJson) as readFile:
		allGlobalDownlinkStns = json.load(readFile)
	if FALSE: print("after Get from Json\n" + str(allGlobalDownlinkStns))

###########################
#     DATA - UPDATE
###########################
def _____________________________UPDATE_DATA():
	return

def saveDownlinkStnsToJson():
	with open(allGlobalDownlinkStnsJson, 'w') as fileObject:
		json.dump(allGlobalDownlinkStns, fileObject)

def saveGlobalAprsToJson():
	with open(globalAprsAllDataJson, 'w') as fileObject:
		json.dump(globalAprsDataTable.dataTableData, fileObject)

def globalAprsUpdateFromWeb():
	if refreshGetNewGlobalAprs:  # TEMP - DISABLE WHILE ISS APRS IS BROKEN  July 25, 2017
		thisSourceUrl = "http://www.findu.com/cgi-bin/ariss/index.cgi?absolute=1"
		searchforstart_text = "Recent activity"
		gooddataval = " : "
		startdata = FALSE
		mostRecentInDataTableDt = globalAprsDataTable.dataTableData[0][allDataDtKeyCol]
		try:
			with urllib.request.urlopen(thisSourceUrl) as webSource:
				for line in webSource:
					try:
						thisStr = str(line.rstrip(), encoding="utf-8")
						if FALSE: print("in web get latest, thisstr=", thisStr)
						if startdata == FALSE and searchforstart_text in thisStr:
							startdata = TRUE
						elif startdata and gooddataval in thisStr:
							aprsData = parsAprsRawToAprsData(thisStr)
							if aprsData[allDataDtKeyCol] == mostRecentInDataTableDt:
								if FALSE: print("\n Don't process, because we already have newest from URL")
								return # if first data from Url matches most recent in data table
							globalAprsDataTable.ifNewInsertData(aprsData)
							saveGlobalAprsToJson()
					except UnicodeDecodeError:
						print("in webGetGlobalAprs, UnicodeDecodeError with: ", line)
		except urllib.error.URLError:
			print("in webGetGlobalAprs, can't open: ", thisSourceUrl)

def OLDglobalAprsUpdateFromWeb():
	if refreshGetNewGlobalAprs:  # TEMP - DISABLE WHILE ISS APRS IS BROKEN  July 25, 2017
		thisSourceUrl = "http://www.findu.com/cgi-bin/ariss/index.cgi?absolute=1"
		searchforstart_text = "Recent activity"
		gooddataval = " : "
		startdata = FALSE
		newestDataRow = 0
		thisStr = "this str has no value yet"  # used for debugging

		try:
			with urllib.request.urlopen(thisSourceUrl) as webSource:
				for line in webSource:
					try:
						thisStr = str(line.rstrip(), encoding="utf-8")
						if FALSE:
							print("in web get latest, thisstr=", thisStr)
						if startdata == FALSE and searchforstart_text in thisStr:
							startdata = TRUE
						elif startdata and gooddataval in thisStr:
							aprsData = parsAprsRawToAprsData(thisStr)
							thisDateTime = aprsData[allDataDtKeyCol]
							oldestDataRow = len(globalAprsDataTable.dataTableData) - 1
							if oldestDataRow > -1:
								newestDateTime = globalAprsDataTable.dataTableData[newestDataRow][allDataDtKeyCol]
								oldestDateTime = globalAprsDataTable.dataTableData[oldestDataRow][allDataDtKeyCol]
								newerData = thisDateTime > newestDateTime
								olderData = thisDateTime < oldestDateTime
								if FALSE:
									print("this   date time=" + str(thisDateTime))
									print("newest data time=" + str(newestDateTime))
									print("oldest date time=" + str(oldestDateTime))
							else: # if datatable is empty
								newerData = TRUE
								olderData = FALSE
								if TRUE:
									print("empty table, so add this one")
							if FALSE:
								print("source:   " + thisStr)
								print("converted:  " + str(aprsData))
							if FALSE:
								print("newer Data = " + str(newerData))
								print("older data = " + str(olderData))
							if newerData:
								# globalAprsDataTable.prependData(aprsData)
								globalAprsDataTable.ifNewInsertData(aprsData)
								saveGlobalAprsToJson()
								if TRUE: print("newer added: " + str(thisDateTime))
							if olderData:
								globalAprsDataTable.appendData(aprsData)
								saveGlobalAprsToJson()
								if TRUE: print("older added: " + str(thisDateTime))
							if olderData == FALSE and newerData == FALSE:
								if FALSE:
									print("not added: "+str(thisDateTime))

					except UnicodeDecodeError:
						print("in webGetGlobalAprs, UnicodeDecodeError with: ", line)
		except urllib.error.URLError:
			print("in webGetGlobalAprs, can't open: ", thisSourceUrl)
			print("    and thisStr: ", thisStr)


def globalAprsClearAndRefreshDataTableFromWeb():
	global globalAprsData
	# globalAprsDataTable.clearTable()
	globalAprsUpdateFromWeb()

def checkAndGetLocalAprs():
	return


def OLDupdateDataTableGlobalAprs():
	global globalAprsData
	globalAprsDataTable.clearTable()
	webGetGlobalAprs()
	with open(globalAprsINTERIMtextFile) as readTextFile:
		for line in readTextFile:
			aprsRaw = str(line.rstrip())
			aprsData = parsAprsRawToAprsData(aprsRaw)
			if FALSE:
				print(aprsRaw)
				print(aprsData)
				print("\n")
			globalAprsDataTable.appendData(aprsData)
	saveGlobalAprsToJson()

###########################
#    HAM LOCATION
###########################
def ____________________________HAM_LOCATION():
	return

def webGetHamLocation(thisHamCallSign):
	thisSourceUrl = "http://www.findu.com/cgi-bin/find.cgi?" + thisHamCallSign
	searchForStartText = "&P=|"
	searchForMidText = "%2c"
	searchForStopText = "|1|"
	printDiagnostics = FALSE
	if printDiagnostics:
		print("entered webGetHamLocation: ", webSourceUrl)
	# NOTE THAT WEB GET ISS EPHEM USES DIFFERENT CODE STRUCTURE
	if refreshGetHamLocations == FALSE:
		return None

	try:
		with urllib.request.urlopen(
				thisSourceUrl) as file_object:  # sometimes this call fails, timeout to deal with exception?
			for line in file_object:
				thisstr = str(line.rstrip())
				if searchForStartText in thisstr:
					startPos = thisstr.find(searchForStartText) + len(searchForStartText)
					endPos = thisstr.find(searchForStopText)
					latLonStr = thisstr[startPos:endPos]
					midPos = latLonStr.find(searchForMidText)
					latstr = latLonStr[0:midPos]
					lonstr = latLonStr[midPos + len(searchForMidText):endPos]
					if printDiagnostics:
						print("in web get latest, thisstr=", thisstr)
						print("Ham=" + thisHamCallSign)
						print("lat and lon str=", thisstr[startPos:endPos])
						print("latstr=" + latstr)
						print("lonstr=" + lonstr)
						print("\n")
					return (thisHamCallSign, float(latstr), float(lonstr))
	except urllib.error.URLError:
		print("got error in webGetHamLocation for: ", thisHamCallSign)
		return None

def isHamInDatatable(thisHamCallSign):
	if FALSE:
		print("\nIN IS HAM IN DATA TABLE")
		print("searching for:" + thisHamCallSign)
		print(str(allGlobalDownlinkStns))
	lastStn = len(allGlobalDownlinkStns)
	if lastStn > 0:
		for stnNumber in range(0, lastStn):
			if allGlobalDownlinkStns[stnNumber][0] == thisHamCallSign:
				if FALSE:
					print("found it")
				return TRUE
	if FALSE:
		print("didn't find it")
	return FALSE

def datatableGetHamLocation(thisHamCallSign):
	lastStn = len(allGlobalDownlinkStns)
	if lastStn > 0:
		for stnNumber in range(0, lastStn):
			if allGlobalDownlinkStns[stnNumber][0] == thisHamCallSign:
				if FALSE:
					print("lat is" + str(allGlobalDownlinkStns[stnNumber][1]))
				return (allGlobalDownlinkStns[stnNumber][0], allGlobalDownlinkStns[stnNumber][1],
						allGlobalDownlinkStns[stnNumber][2])
	if FALSE:
		print("didn't find the location")
	return FALSE


###########################
#   USE PHYSICAL RADIO
###########################

def ____________________________USE_PHYSICAL_RADIO():
	return

def createSampleRecAprsInFile(thisAprsRaw):
	folderName = "./localRec/"
	fileName = folderName + "localRec_" + thisAprsRaw[0:14]
	with open(fileName, 'w') as writeFile:
		writeFile.write(thisAprsRaw)

def createNextMsgToSend():
	thisTag = "tagNextMsg"
	canvasBox.delete(thisTag)
	thisBox = controlCenterSectionBox
	thisRowChar = 7
	thisColChar = 5

	global currentAprsMsg

	APRSprefix = "KA1ARD>ARISS ::EMAIL  :"
	APRSpostfix = " Hello from ISS spacestnexp.org/ham"
	this_row = 4
	email_col = 8
	APRScuremail = emailRequestsDataTable.dataTableData[this_row][email_col]

	currentAprsMsg = (APRSprefix + APRScuremail + APRSpostfix)

	displayAnyRectangle(thisBox.left + thisColChar * charWid - 1, thisBox.top + thisRowChar * charHi - 1,
						thisBox.right, thisBox.top + (thisRowChar + 1) * charHi - 1,
						highlightBg, stdBoxOutline, thisTag)
	displayAnyText(thisBox.left + thisColChar * charWid + 4,
				   thisBox.top + thisRowChar * charHi,
				   currentAprsMsg,
				   allTextFg, highlightBg, thisTag)

def receiveNow():
	print("\nEntered receiveMsg")

def sendCurrentMsg():
	global currentAprsMsg
# print("\nRadio send: " + currentAprsMsg)


###########################
#   SCREEN display Primitives
###########################
def ____________________________DISPLAY_PRIMITIVES():
	return

def displayAnyImage(imageLeftPix, imageTopPix, imagefile, thisTag):
	global regMapId, worldMapId
	if imagefile == 'Green Circle 2pix 64x64.gif':
		thisimage = PhotoImage(file=imagefile, width=64, height=64)
	elif imagefile == 'ISS small graphic 20x20 pix.gif':
		thisimage = PhotoImage(file=imagefile, width=20, height=20)
	else:
		thisimage = PhotoImage(file=imagefile)
	if FALSE and imagefile != regMapFileName and imagefile != worldMapFileName:
		thislabel = Label(image=thisimage, border=0)
		thislabel.image = thisimage
		thislabel.place(x=imageLeftPix, y=imageTopPix)
	else:
		canvasBox.create_image(imageLeftPix, imageTopPix, image=thisimage, anchor=NW, tags=thisTag)
		if imagefile == regMapFileName:
			regMapId = thisimage
		elif imagefile == worldMapFileName:
			worldMapId = thisimage
		# BUG - add if imagefile is greencircle or ISS, to prevent massive growth of this array
		else:
			imageIdArray.append(thisimage)

def displayAnyRectangle(thisRect_left, thisRect_top, thisRect_right, thisRect_bottom, fillcolor, outlinecolor, thisTag):
	canvasBox.create_rectangle(thisRect_left, thisRect_top, thisRect_right, thisRect_bottom, fill=fillcolor,
							   outline=outlinecolor, tags=thisTag)

def displayAnyBox(thisBox, fillcolor, outlinecolor, thisTag):
	displayAnyRectangle(thisBox.left, thisBox.top, thisBox.right, thisBox.bottom, fillcolor, outlinecolor, thisTag)

def displayAnyLine(thisLeft, thisTop, thisRight, thisBottom, thisColor, thisTag):
	canvasBox.create_line(thisLeft, thisTop, thisRight, thisBottom, fill=thisColor, tags=thisTag)

def displayAnyText(thisLeftPix, thisTopPix, thisText, thisTextColor, thisBgColor, thisTag):
	canvasBox.create_text(thisLeftPix, thisTopPix, text=thisText, fill=thisTextColor, anchor=NW, tags=thisTag)


#################################
#     display BASE SCREENS
#################################
def ___________________________DISPLAY_BASE_SCREENS():
	return

def displaySectionTitle(thisBox, sectiontitle_text):
	thisTag = "tagSectionTitle"
	displayAnyRectangle(thisBox.left, thisBox.top, thisBox.right, thisBox.top + charHi - 1, sectionTitleBg,
						sectionTitleOutline, thisTag)

	displayAnyText(thisBox.left + (thisBox.right - thisBox.left - len(sectiontitle_text) * charWid) / 2,
				   thisBox.top,
				   sectiontitle_text,
				   allTextFg,
				   sectionTitleBg,
				   thisTag)



def displayRegMapBase(thisBox):
	thisTag = "tagRegMapBase"
	displayAnyImage(thisBox.left, thisBox.top, regMapFileName, thisTag)


def displayWorldMapBase(thisBox):
	thisTag = "tagWorldMapBase"
	displayAnyImage(thisBox.left, thisBox.top, worldMapFileName, thisTag)


def displayFlyoverTimelineBase(thisBox):
	thisTag = "tagFlyoverTimelineBase"
	displayAnyBox(thisBox, flyoverTimelineBg, stdBoxOutline, thisTag)


def displayProgressMsgBase(thisBox):
	thisTag = "tagActionMsgBase"
	displayAnyBox(thisBox, actionMsgBg, stdBoxOutline, thisTag)


def displayAprsTimelineBase(thisBox):
	thisTag = "tagActionAprsTimelineBase"
	displayAnyBox(thisBox, aprsTimelineBg, stdBoxOutline, thisTag)



###########################
#    display MAPS - Primitives
###########################
def ___________________________DISPLAY_MAP_PRIMITIVES():
	return

# MATH FOR MAPS #
def lonRadtoPix(thisMap, thisLonRad):
	return (int((0 - thisMap.leftlon + radFloatToDegFloat(thisLonRad)) * thisMap.pixperdeg))

def latRadtoPix(thisMap, thisLatRad):
	return (int((thisMap.toplat - radFloatToDegFloat(thisLatRad)) * thisMap.pixperdeg))

def ifPixOnMap(thisMap, xPix, yPix):
	return (xPix > thisMap.LeftPix and xPix < thisMap.RightPix and yPix > thisMap.TopPix and yPix < thisMap.BottomPix)

# ONE MAP #
def displayImageAtLatLonRadOnMap(thisMap, imagefile, imagewid, imagehi, thisLatRad, thisLonRad, thisTag):
	xPix = thisMap.LeftPix + lonRadtoPix(thisMap,
										 thisLonRad) - imagewid / 2 + 1  # tweaked for contact marker to align exactly on orbital path
	yPix = thisMap.TopPix + latRadtoPix(thisMap, thisLatRad) - imagehi / 2
	if ifPixOnMap(thisMap, xPix, yPix):
		displayAnyImage(xPix, yPix, imagefile, thisTag)

def displayImageAtCurIssLocOnMap(thisMap, imagefile, imagewid, imagehi, thisTag):
	displayImageAtLatLonRadOnMap(thisMap, imagefile, imagewid, imagehi, float(iss.sublat), float(iss.sublong), thisTag)

def displayLineBetweenLatLonRadsOnMap(thisMap, thisColor, startLatRad, startLonRad, stopLatRad, stopLonRad, thisTag):
	maxLineLen = 100  # this keeps line from traversing the full map
	xStartPix = thisMap.LeftPix + lonRadtoPix(thisMap, startLonRad)
	yStartPix = thisMap.TopPix + latRadtoPix(thisMap, startLatRad)
	xSTopPix = thisMap.LeftPix + lonRadtoPix(thisMap, stopLonRad)
	ySTopPix = thisMap.TopPix + latRadtoPix(thisMap, stopLatRad)
	if ifPixOnMap(thisMap, xStartPix, yStartPix) and ifPixOnMap(thisMap, xSTopPix, ySTopPix) and abs(
					xSTopPix - xStartPix) < maxLineLen:
		displayAnyLine(xStartPix, yStartPix, xSTopPix, ySTopPix, thisColor, thisTag)

def displayTextAtLatLonRadOnMap(thisMap, thisText, thisTextColor, thisBgColor, thisLatRad, thisLonRad, thisTag):
	xPix = thisMap.LeftPix + lonRadtoPix(thisMap, thisLonRad) - len(thisText) * charWid / 2
	yPix = thisMap.TopPix + latRadtoPix(thisMap, thisLatRad) - charHi / 2
	if ifPixOnMap(thisMap, xPix, yPix):
		displayAnyText(xPix, yPix, thisText, thisTextColor, thisBgColor, thisTag)

# ALL MAPS #
def displayImageAtLatLonRadOnAllMaps(imagefile, imagewid, imagehi, thisLatRad, thisLonRad, thisTag):
	displayImageAtLatLonRadOnMap(worldMapSpecs, imagefile, imagewid, imagehi, thisLatRad, thisLonRad, thisTag)
	displayImageAtLatLonRadOnMap(regMapSpecs, imagefile, imagewid, imagehi, thisLatRad, thisLonRad, thisTag)

def displayImageAtCurIssLocOnAllMaps(imagefile, imagewid, imagehi, thisTag):
	displayImageAtCurIssLocOnMap(worldMapSpecs, imagefile, imagewid, imagehi, thisTag)
	displayImageAtCurIssLocOnMap(regMapSpecs, imagefile, imagewid, imagehi, thisTag)

def displayLineBetweenLatLonRadsOnAllMaps(thisColor, startLatRad, startLonRad, stopLatRad, stopLonRad, thisTag):
	displayLineBetweenLatLonRadsOnMap(worldMapSpecs, thisColor, startLatRad, startLonRad, stopLatRad, stopLonRad,
									  thisTag)
	displayLineBetweenLatLonRadsOnMap(regMapSpecs, thisColor, startLatRad, startLonRad, stopLatRad, stopLonRad, thisTag)

def displayTextAtLatLonRadsOnAllMaps(thisText, thisTextColor, thisBgColor, thisLatRad, thisLonRad, thisTag):
	displayTextAtLatLonRadOnMap(worldMapSpecs, thisText, thisTextColor, thisBgColor, thisLatRad, thisLonRad, thisTag)
	displayTextAtLatLonRadOnMap(regMapSpecs, thisText, thisTextColor, thisBgColor, thisLatRad, thisLonRad, thisTag)


###########################
#    display MAPS -
###########################
def __________________________DISPLAY_MAPS_TOP_LEVEL():
	return

def displayIssNowOnAllMaps():
	thisTag = "tagIssNow"
	issImageFile = 'ISS small graphic 20x20 pix.gif'
	circleAroundIssFile = 'Green Circle 2pix 64x64.gif'
	canvasBox.delete(thisTag)

	localobserver.date = ephem.now()
	iss.compute(localobserver)
	displayImageAtCurIssLocOnAllMaps(issImageFile, 20, 20, thisTag)
	if mapShowCircleAroundIss:
		displayImageAtCurIssLocOnMap(worldMapSpecs, circleAroundIssFile, 64, 64, thisTag)  # NOTE:  on world map only

def displayIssPathOnAllMaps():
	thisTag = "tagIssPath"
	canvasBox.delete(thisTag)
	pastOrbits = 1
	futureOrbits = 1

	if FALSE:
		print("\n\n\n**entered Display ISS path on all maps")
	orbitChangeWhileEarthRotates = 0  # 23/360
	pastOrbitsToShow = pastOrbits + orbitChangeWhileEarthRotates
	futureOrbitsToShow = futureOrbits + orbitChangeWhileEarthRotates
	pastmins = int(0 - issMinsPerOrbit * pastOrbitsToShow)
	futuremins = int(issMinsPerOrbit * futureOrbitsToShow)
	minsbetweenpts = 0.1
	localobserver.date = ephem.now()
	now = localobserver.date
	startrange = int(pastmins / minsbetweenpts)
	stoprange = int(futuremins / minsbetweenpts)
	for thisPoint in range(startrange, stoprange):
		if FALSE:
			print("thisPoint=" + str(thisPoint))
			print("points*minsbetweenpts/(24*60)=" + str((thisPoint * minsbetweenpts) / (24 * 60)))
			print("now=" + str(now))
			print("\n")
		localobserver.date = ephem.date(now + (thisPoint * minsbetweenpts) / (24 * 60))
		iss.compute(localobserver)
		lonrad = float(iss.sublong)
		latrad = float(iss.sublat)
		if FALSE:
			print(iss.eclipsed)
		if thisPoint < 0 and iss.eclipsed:
			thisColor = mapPastOrbitNightColor
		if thisPoint < 0 and iss.eclipsed == FALSE:
			thisColor = mapPastOrbitDayColor
		if thisPoint >= 0 and iss.eclipsed:
			thisColor = mapFutureOrbitNightColor
		if thisPoint >= 0 and iss.eclipsed == FALSE:
			thisColor = mapFutureOrbitDayColor
		stopLonRad = lonrad
		stopLatRad = latrad
		minuteMarkerSteps = 5
		if thisPoint > startrange:
			displayLineBetweenLatLonRadsOnAllMaps(thisColor, startLatRad, startLonRad, stopLatRad, stopLonRad, thisTag)
			if mapShowMinuteMarkers and math.fmod(thisPoint, minuteMarkerSteps / minsbetweenpts) == 0:
				displayTextAtLatLonRadsOnAllMaps("-", mapMinuteMarkersColor, thisColor, startLatRad, startLonRad,
												 thisTag)

		startLatRad = latrad
		startLonRad = lonrad

def displayOneRecStnOnAllMaps(thisHamCallsign):
	thisTag = "tagAprsContactsOnMaps"
	thisRecStnData = datatableGetHamLocation(thisHamCallsign)
	if thisRecStnData != FALSE:
		if mapShowGlobalAprsCallSignAtRecStns:
			displayTextAtLatLonRadsOnAllMaps(
				thisRecStnData[0],
				mapRecStnColor, neutralBg,
				degFloatToRadFloat(thisRecStnData[1]), degFloatToRadFloat(thisRecStnData[2]),
				thisTag)
		if mapShowGlobalAprsAtRecStns:
			displayTextAtLatLonRadsOnAllMaps(
				"o",
				mapRecStnColor, neutralBg,
				degFloatToRadFloat(thisRecStnData[1]), degFloatToRadFloat(thisRecStnData[2]),
				thisTag)

def displayAllRecStnOnAllMaps():
		lastStn = len(allGlobalDownlinkStns)
		if lastStn > 0:
			for stnNumber in range(0, lastStn):
				displayOneRecStnOnAllMaps(allGlobalDownlinkStns[stnNumber][0])



def displayGlobalAprsOnAllMaps():
	thisTag = "tagAprsContactsOnMaps"
	canvasBox.delete(thisTag)

	thisDataTable = globalAprsDataTable.dataTableData

	# define NOW
	now = ephem.now()  # now is float
	if FALSE:  print("  now as float:   %f" % now)

	# Loop for both WORLDMAP and TIMELINE
	for recmsg in range(0, len(thisDataTable)):

		# EXTRACT DATE & TIME VALUES
		dt_tuple = dt13ToTuple(thisDataTable[recmsg][allDataDtKeyCol])

		thissender = thisDataTable[recmsg][aprsSenderCol]
		if FALSE:
			print("\nthis date:-%s-" % str(thisdate))
			print("this year:-%s-" % str(thisyear))
			print("this mon:-%s-" % str(thismon))
			print("this day:-%s-" % str(thisday))
			print("this time:-%s-" % str(thistime))
			print("this hour:-%s-" % str(thishour))
			print("this min:-%s-" % str(thismin))
			print("this sec:-%s-" % str(thissec))

		# SET LOCAL OBSERVER DATA
		localobserver.date = dt_tuple
		iss.compute(localobserver)

		#                if FALSE:
		#                        imagefile="greendot2x2.gif" if thissender=="RS0ISS" else "reddot2x2.gif"
		#                else:
		imagefile = "reddot2x2.gif"
		if FALSE:
			print(thisDataTable[recmsg][allDataDtKeyCol])
		if mapShowGlobalAprsAtIssLocations:
			displayImageAtCurIssLocOnAllMaps(imagefile, 2, 2, thisTag)

		# DISPLAY RECEIVING STATION
		if FALSE:
			print("Receiving Station:" + thisDataTable[recmsg][aprsReceiverCol])

		if mapShowGlobalAprsAtRecStns:
			displayOneRecStnOnAllMaps(thisDataTable[recmsg][aprsReceiverCol])

		if mapShowGlobalAprsLinesIssToRecStns:
			thisRecStnData = datatableGetHamLocation(thisDataTable[recmsg][aprsReceiverCol])
			if thisRecStnData != FALSE:
					displayLineBetweenLatLonRadsOnAllMaps(
						mapMsgLinesColor,
						float(iss.sublat), float(iss.sublong),
						degFloatToRadFloat(thisRecStnData[1]), degFloatToRadFloat(thisRecStnData[2]),
						thisTag)


def displayReceptionRegionOnAllMaps():
	thisTag = "tagReceptionRegionOnMaps"
	earthRadiusMiles = 3959

	closerdistmiles = int(issAltitudeMiles / math.tan(degFloatToRadFloat(goodVisDeg)))
	fartherdistmiles = int(issAltitudeMiles / math.tan(degFloatToRadFloat(minVisDeg)))
	if FALSE:
		waitInputMsg("closer=" + str(closerdistmiles) + " farther=" + str(fartherdistmiles))
	adjust_for_Earth_curve = 0.83  # empirical - .83 works for 20 degrees (SE of home)
	centerlatrad = degFloatToRadFloat(float(localLatStr))
	centerlonrad = degFloatToRadFloat(float(localLonStr))
	for circle in range(0, 2):
		if circle == 0:
			distmiles = closerdistmiles
			#                        thisColor=mapReceiveAreaBestFg
			thisColor = mapReceiveAreaFarFg
		else:
			distmiles = fartherdistmiles
			thisColor = mapReceiveAreaFarFg
		distmiles *= adjust_for_Earth_curve
		earthratio = float(distmiles / earthRadiusMiles)
		for bearingtendeg in range(0, 37):
			bearingrad = degFloatToRadFloat(float(bearingtendeg * 10))
			lat2rad = math.asin(
				math.cos(earthratio) * math.sin(centerlatrad) +
				math.sin(earthratio) * math.cos(centerlatrad) * math.cos(bearingrad))
			lon2rad = centerlonrad + math.atan2(
				math.sin(earthratio) * math.cos(centerlatrad) * math.sin(bearingrad),
				math.cos(earthratio) - math.sin(centerlatrad) * math.sin(lat2rad))
			stopLonRad = lon2rad
			stopLatRad = lat2rad
			if bearingrad > 0:
				displayLineBetweenLatLonRadsOnAllMaps(thisColor, startLatRad, startLonRad, stopLatRad, stopLonRad,
													  thisTag)
			startLatRad = lat2rad
			startLonRad = lon2rad


###########################
#   display - FLYOVER TIMES
###########################
def ___________________________DISPLAY_FLYOVERS():
	return

def displayFlyoverGrid():
	thisTag = "tagFlyoverGrid"
	thisBox = flyoverTimesSectionBox
	displaySectionTitle(thisBox, "Flyover times")
	flyoversDataTable.displayTable(thisBox, thisTag)

def displayFlyoverTimeline():
	thisTag = "tagFlyoverTimeline"

	printDiagnostics = FALSE

	# clear tags
	canvasBox.delete(thisTag)

	# control parameters
	hoursInTimeline = 80
	pixGraphDownFromBoxTop = 20
	pixDtLabelDownFromBoxTop = 6
	pixHiNightBox = 6
	pixHiHourMarker = 7
	pixHiIssMarker = 3
	pixWidIssMarker = 3
	pixHiGraph = 30
	degHiGraph = 90
	graphLineDegStep = 30
	hourMarkerStep = 3

	# derived parameters
	flyoversLastDisplayRow = len(flyoversDataTable.dataTableData)
	thisBox = flyoverTimelineSectionBox
	pixWidTimeline = thisBox.right - thisBox.left
	minsInTimeline = hoursInTimeline * 60
	daysInTimeline = int(hoursInTimeline / 24)
	pixPerHour = float(pixWidTimeline / hoursInTimeline)
	pixPerMin = pixPerHour / 60
	pixPerDay = pixPerHour * 24
	pixPerDegGraph = pixHiGraph / degHiGraph

	# display graph horiz lines
	for graphHorizLine in range(0, degHiGraph, graphLineDegStep):
		yPixGraphHorizLine = thisBox.top + pixGraphDownFromBoxTop + (graphHorizLine * pixPerDegGraph)
		displayAnyLine(thisBox.left, yPixGraphHorizLine,
					   thisBox.right, yPixGraphHorizLine,
					   flyoverTimelineHorizLineColor, thisTag)

	# display night bars
	localobserver.date = ephem.now()
	nextSunSetTimeUtc = localobserver.next_setting(ephem.Sun()) + pyephemSunSetFix
	nextSunRiseTimeUtc = localobserver.next_rising(ephem.Sun()) + pyephemSunRiseFix
	decDayToNextSunRise = nextSunRiseTimeUtc - ephem.now()
	decDayToNextSunSet = nextSunSetTimeUtc - ephem.now()
	decDayLightLength = nextSunSetTimeUtc - nextSunRiseTimeUtc
	if nextSunRiseTimeUtc > nextSunSetTimeUtc: decDayLightLength += 24
	xPixDayLightLength = int(decDayLightLength * pixPerDay)
	if TRUE and printDiagnostics:
		print("\n")
		print("nextSunSetTimeUtc=" + str(nextSunSetTimeUtc))
		print("nextSunRiseTimeUtc=" + str(nextSunRiseTimeUtc))
		print("decDayToNextSunRise=" + str(decDayToNextSunRise))
		print("decDayToNextSunSet=" + str(decDayToNextSunSet))
		print("decDayLightLength=" + str(decDayLightLength))
		print("xPixDayLightLength=" + str(xPixDayLightLength))
	for nightBlockNumber in range(-1, 4):
		xPixThisSunSet = int(thisBox.left + decDayToNextSunSet * pixPerDay + nightBlockNumber * pixPerDay)
		xPixThisSunRise = int(thisBox.left + decDayToNextSunRise * pixPerDay + nightBlockNumber * pixPerDay)
		if xPixThisSunRise < xPixThisSunSet: xPixThisSunRise += pixPerDay  # does this fix it?
		if TRUE and printDiagnostics:
			print("\n")
			print("xPixThisSunSet=" + str(xPixThisSunSet))
			print("xPixThisSunRise=" + str(xPixThisSunRise))
		if TRUE:  # xPixThisSunRise>thisBox.left and xPixThisSunRise<thisBox.right:
			xPixStartNightBlock = xPixThisSunSet if xPixThisSunSet > thisBox.left else thisBox.left
			xPixStopNightBlock = xPixThisSunRise if xPixThisSunRise < thisBox.right else thisBox.right
			if xPixStopNightBlock > xPixStartNightBlock:
				displayAnyRectangle(xPixStartNightBlock, thisBox.top,
									xPixStopNightBlock, thisBox.top + pixHiNightBox,
									flyoverTimelineNightBlockColor, flyoverTimelineNightBlockColor, thisTag)
			if TRUE and printDiagnostics:
				print("xPixStartNightBlock=" + str(xPixStartNightBlock))
				print("xPixStopNightBlock=" + str(xPixStopNightBlock))

	# display hour markers
	localobserver.date = ephem.now() + localTimeZoneOffset / 24
	iss.compute(localobserver)
	hoursToLocalMidnight = 24 - math.fmod(localobserver.date + pyephemHalfDayCorrection, 1) * 24
	pixToLocalMidnight = int(hoursToLocalMidnight * pixPerHour)
	pixToFirstHourMarker = int(math.fmod(pixToLocalMidnight, pixPerHour * hourMarkerStep))
	if FALSE and printDiagnostics:
		print("ephem.now=" + str(ephem.now()))
		print("local now=" + str(localobserver.date))
		print("hours to local midnight=" + str(hoursToLocalMidnight))
		print("pixToFirstHourMarker=" + str(pixToFirstHourMarker))
	for hourMarker in range(0, hoursInTimeline - 1, hourMarkerStep):
		xPixHourMarker = thisBox.left + hourMarker * pixPerHour + pixToFirstHourMarker
		displayAnyLine(xPixHourMarker, thisBox.top + 1,
					   xPixHourMarker, thisBox.top + pixHiHourMarker,
					   flyoverTimelineVertHourLineColor, thisTag)

	# display day label and line
	for dayMarker in range(0, daysInTimeline + 1):
		localobserver.date += 1
		iss.compute(localobserver)
		thisdate = localobserver.date
		mon = thisdate.tuple()[1]
		day = thisdate.tuple()[2]
		monDayStr = (str(mon) + "/" + str(day))
		xPixDayMarker = thisBox.left + pixToLocalMidnight + dayMarker * pixPerDay
		if xPixDayMarker < thisBox.right:
			displayAnyLine(xPixDayMarker, thisBox.top + 1,
						   xPixDayMarker, thisBox.bottom,
						   flyoverTimelineVertDayLineColor, thisTag)
		if xPixDayMarker < thisBox.right - len(monDayStr) * charWid:
			displayAnyText(xPixDayMarker + 2, thisBox.top + pixDtLabelDownFromBoxTop,
						   monDayStr, flyoverTimelineDayLabelColor, neutralBg, thisTag)

	# display ISS flyover markers
	for showRow in range(0, flyoversLastDisplayRow):

		# get now
		now = ephem.now()

		# Calculate T-minus for this flyover
		############################################################################################################
		dtThisFlyover = dt13ToFloat(flyoversDataTable.dataTableData[showRow][allDataDtKeyCol])
		minsAfterNow = int((dtThisFlyover - now) * 24 * 60)

		# display on timeline:
		pixAfterNow = minsAfterNow * pixPerMin - pixWidIssMarker / 2
		degPeak = int(flyoversDataTable.dataTableData[showRow][flyoversPeakDegCol])
		pixDownFromGraphTop = int((degHiGraph - degPeak) * pixPerDegGraph - pixHiIssMarker / 2)
		if FALSE and printDiagnostics:
			print("\nIn display flyover timeline")
			print("     dtThisFlyover:", str(dtThisFlyover))
			print("     now           :", now)
			print("     minsAfterNow:", minsAfterNow)
			print("     pixsAfterNow:", pixAfterNow)
			print("     degPeak:", degPeak)
			print("     pixDown:", pixDownFromGraphTop)
		visible = flyoversDataTable.dataTableData[showRow][flyoversVisCol] == "vis"
		thisColor = flyoverTimelineIssVisMarkerColor if visible else flyoverTimelineIssNotVisMarkerColor
		if thisBox.left + pixAfterNow < thisBox.right:
			displayAnyRectangle(
				thisBox.left + pixAfterNow,
				thisBox.top + pixGraphDownFromBoxTop + pixDownFromGraphTop,
				thisBox.left + pixAfterNow + pixWidIssMarker,
				thisBox.top + pixGraphDownFromBoxTop + pixDownFromGraphTop + pixHiIssMarker,
				thisColor, thisColor, thisTag)


###########################
#   display - EMAIL REQUESTS
###########################
def __________________________DISPLAY_EMAIL_REQUESTS():
	return

def displayEmailRequestsGrid():
	global emailRequestsDataTable
	thisTag = "tagEmailRequestGrid"
	thisBox = sendToIssSectionBox
	displaySectionTitle(thisBox, "Email Requests")
	emailRequestsDataTable.displayTable(thisBox, thisTag)


###########################
#   display - APRS MSGS
###########################
def __________________________DISPLAY_APRS_MSGS():
	return

def displayLocalReceiveGrid():
	thisTag = "tagLocalReceiveGrid"
	thisBox = recByLocalRadioSectionBox
	displaySectionTitle(thisBox, "Received by local radio")
	localAprsDataTable.displayTable(thisBox, thisTag)

def displayGlobalAprsGrid():
	thisTag = "tagGlobalAprsGrid"
	thisBox = recByGlobalNetSectionBox
	displaySectionTitle(thisBox, "Received by Global APRS")
	globalAprsDataTable.displayTable(thisBox, thisTag)


def displayAprsTimeline():
	thisTag = "tagAprsTimeline"
	thisBox = aprsTimelineSectionBox
	canvasBox.delete(thisTag)
	# displaySectionTitle(thisBox, "Global APRS Timeline")

	daysInTimeline = 1
	orbitMarkerHi = 6
	markerHi = rs0issMarkerHi = rs0issMarkerShiftDown = 9

	timelineWid = thisBox.right - thisBox.left
	orbitsInTimeline = int(daysInTimeline * issOrbitsPerDay)
	minInTimeline = orbitsInTimeline * issMinsPerOrbit
	pixPerMin = float(timelineWid / minInTimeline)
	pixPerDay = float(timelineWid / daysInTimeline)
	pixPerOrbit = float (pixPerMin * issMinsPerOrbit)
	msgsPerDay = []

	now = ephem.now()  ### now is float

	for thisDay in range(0,daysInTimeline+1):
		msgsPerDay.append(0)
		if FALSE:
			print("initialized msg per day ", str(thisDay), " = ", str(msgsPerDay[thisDay]))

	for recmsg in range(0, len(globalAprsDataTable.dataTableData)):
		thisDateTime = dt13ToFloat(globalAprsDataTable.dataTableData[recmsg][allDataDtKeyCol])
		changeoftimemins = int((now - thisDateTime) * 24 * 60)
		pixelsbeforenow = int(changeoftimemins * pixPerMin)+1
		thisDayInt = int(changeoftimemins/(24*60))

		if thisDayInt <= daysInTimeline:
			thisTop = thisBox.top + charHi + orbitMarkerHi -2
			thisBottom = thisTop + markerHi
			if globalAprsDataTable.dataTableData[recmsg][4] != "RS0ISS":
				msgsPerDay[thisDayInt] += 1
				thisColor = aprsTimelineMark
			else:
				thisColor = aprsTimelineRs0issMark
				thisTop += rs0issMarkerShiftDown
				thisBottom += rs0issMarkerHi
			if FALSE:
				print("Sender = ", globalAprsDataTable.dataTableData[recmsg][4])
				print("msgs on day ",str(thisDayInt),": ",msgsPerDay[thisDayInt])
		if FALSE:
			print("\nNOW vs THISDATETIME as float")
			print("  now:         %f" % now)
			print("  thisdatetime %f" % thisDateTime)
			print("  change of time mins:", str(changeoftimemins))
			print(" pixels before now", pixelsbeforenow)

		# DISPLAY ON TIMELINE
		if (thisBox.right - pixelsbeforenow) >= thisBox.left:
			thisLeft = thisRight = thisBox.right - pixelsbeforenow

			displayAnyLine(thisLeft, thisTop, thisRight, thisBottom, thisColor, thisTag)

	# display orbits
	for orbits in range(0, orbitsInTimeline+1):
		thisLeftPix = thisBox.right - int(orbits * pixPerOrbit)
		thisTopPix = thisBox.top
		thisBottomPix = thisBox.top + orbitMarkerHi
		thisRightPix = thisLeftPix
		thisLabelMarkerColor = aprsTimelineOrbitsMarker
		displayAnyLine(thisLeftPix, thisTopPix, thisRightPix, thisBottomPix, thisLabelMarkerColor, thisTag)
	if FALSE: print("pix per orbit: ",pixPerOrbit)

	# display days
	for days in range(0, daysInTimeline + 1):
		thisLeftPix = thisBox.right - days * pixPerDay
		thisTopPix = thisBox.top
		thisBottomPix = thisBox.bottom
		thisRightPix = thisLeftPix
		thisText = str(0 - days) + " day"
		if days > 1: thisText += "s"
		thisText += (", " + str(msgsPerDay[days - 1]) + " msgs")
		thisText += (", " + str(round(float(1/pixPerMin), 1)) + " min/pix")
		thisTextColor = aprsTimelineLabel
		thisLabelMarkerColor = aprsTimelineLabelMarker
		thisBgColor = neutralBg
		displayAnyLine(thisLeftPix, thisTopPix, thisRightPix, thisBottomPix, thisLabelMarkerColor, thisTag)
		# displayAnyLine(thisLeftPix-1, thisTopPix, thisRightPix-1, thisBottomPix, thisLabelMarkerColor, thisTag)
		displayAnyText(thisLeftPix + 2, thisTopPix+orbitMarkerHi, thisText, thisTextColor, thisBgColor, thisTag)
		if FALSE:
			print("for day = ", str(days), "  msgsPerDay =", thisText)

###########################
#         TEST
###########################
def _________________________TEST():
	return

def testDataBase():
	# INTEGER, REAL, TEXT, BLOB, NULL
	print("BEGIN test data base")


	conn = sqlite3.connect("test4.db") # create or open connection to this data base
	c = conn.cursor() # define the cursor

### HAM STATIONS DATA TABLE #######################################################################
	if FALSE: # create new table, with primary key
		c.execute('CREATE TABLE hamStations (hamCallSign TEXT PRIMARY KEY, hamDecLat REAL, hamDecLon REAL)')

	if FALSE: # save all stns
		allStns = allGlobalDownlinkStns
		lastStn = len(allStns)
		if lastStn > 0:
			for stnNumber in range(0, lastStn):
				print("about to save ",allStns[stnNumber][0], allStns[stnNumber][1], allStns[stnNumber][2])
				try:
					c.execute("INSERT INTO hamStations VALUES (?,?,?)", (allStns[stnNumber][0],allStns[stnNumber][1], allStns[stnNumber][2]))
				except sqlite3.OperationalError:
					print('Operational error for ',allStns[stnNumber])
		print(" ")

	if FALSE: # display all data from table
		print("Display contents of data base (",len(allGlobalDownlinkStns)," stns):")
		cursor = c.execute("SELECT * FROM hamStations")
		for row in cursor:
			print (row[0], "\t", row[1], "\t", row[2])

		if FALSE:  # create new table, with primary key
			c.execute('CREATE TABLE hamStations (hamCallSign TEXT PRIMARY KEY, hamDecLat REAL, hamDecLon REAL)')

### ALL DATA REPORTS DATA TABLE #######################################################################

	print(globalAprsDataTable.dataTableData[0])
	print("number of reports: ",len(globalAprsDataTable.dataTableData))
	# aprsDataFormat = [['DTKEY', 'Priority', 'Date', '  Time', 'Sender', 'Receiver', 'Path', 'Message'],
	#				  ['13', '1', '7', '10', '10', '9', '25', '55']]
	# ['20171029135347', '1', 'Oct 29', '  9:53:47a', 'EA4FG', 'EA5AHQ-12', 'CQ,RS0ISS*,qAR,EA5AHQ-12',
	# 'hello from spain de ea4fg']
	print(aprsDataFormat[0][0])
	print(aprsDataFormat[0][1])


	if TRUE: # create new table, with primary key
		c.execute('CREATE TABLE globalAprsMsgs (DTKEY TEXT PRIMARY KEY, Priority TEXT, Date TEXT,\
				  Time TEXT, Sender TEXT, Receiver TEXT, Path TEXT, Message TEXT)')



	if FALSE:  # save all stns
		allStns = allGlobalDownlinkStns
		lastStn = len(allStns)
		if lastStn > 0:
			for stnNumber in range(0, lastStn):
				print("about to save ", allStns[stnNumber][0], allStns[stnNumber][1], allStns[stnNumber][2])
				try:
					c.execute("INSERT INTO hamStations VALUES (?,?,?)",
							  (allStns[stnNumber][0], allStns[stnNumber][1], allStns[stnNumber][2]))
				except sqlite3.OperationalError:
					print('Operational error for ', allStns[stnNumber])
		print(" ")

	if FALSE:  # display all data from table
		print("Display contents of data base (", len(allGlobalDownlinkStns), " stns):")
		cursor = c.execute("SELECT * FROM hamStations")
		for row in cursor:
			print(row[0], "\t", row[1], "\t", row[2])

		conn.commit()  # commit these changes
		conn.close()  # close the connection

		print("END test data base")

		conn.commit()  # commit these changes
		conn.close()  # close the connection

		print("END test data base")

# MULCH
	if FALSE: # immerse values method
		try:
			c.execute("INSERT INTO hamStations VALUES ('K26TH', 38.95883, -121.1105)")
		except sqlite3.IntegrityError:
			print('ERROR: ID already exists in PRIMARY KEY')


	if FALSE:  # use "format" methods
		table1Name = 'Table1Name'
		table1Col1Name = 'Table1Col1Name'
		table1Col1DataType = 'INTEGER'
		table1Col2Name = 'Table1Col2Name'
		table1Col2DataType = 'INTEGER'

		table2Name = 'Table2Name'
		table2Col1Name = 'Tabl2Col1Name'
		table2Col1DataType = 'INTEGER'
		table2Col2Name = 'Table2Col2Name'
		table2Col2DataType = 'INTEGER'
		table2Col3Name = 'Table2Col3Name'
		table2Col3DataType = 'INTEGER'

		defaultValue = 'Hello world'  # inserted into every row in this column

		# create new table
		c.execute('CREATE TABLE {tn} ({nf} {ft}) '\
	 		  .format(tn=table1Name, nf=table1Col1Name, ft=table1Col1DataType)) #tn=tablename, nf=new field, ft=fieldtype
		# Create a second table with 1 column as primary key
		c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY) '\
			  .format(tn=table2Name, nf=table2Col1Name, ft=table2Col1DataType)) #tn=tablename, nf=new field, ft=fieldtype
		# add a new column without a row value
		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
			.format(tn=table2Name, cn=table2Col2Name, ct=table2Col2DataType))
		# add a new column without a row value
		c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
			.format(tn=table2Name, cn=table2Col3Name, ct=table2Col3DataType, df=defaultValue))
		try:
			c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
				format(tn=table2Name, idf=table2Col1Name, cn= table2Col2Name))
		except sqlite3.IntegrityError:
			print('ERROR: ID already exists in PRIMARY KEY column {}'.format(table2Col1Name))
		try:
			c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
				format(tn=table2Name, idf=table2Col1Name, cn= table2Col2Name))
		except sqlite3.IntegrityError:
			print('ERROR: ID already exists in PRIMARY KEY column {}'.format(table2Col1Name))
		# insert an ID (if it does not exist yet) with a specific value in a second column
		c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')". \
			  	format(tn=table2Name, idf=table2Col1Name, cn=table2Col2Name))
		# pdates the newly inserted or pre-existing entry
		c.execute("UPDATE {tn} SET {cn}=('Hi World') WHERE {idf}=(123456)". \
			  format(tn=table2Name, cn=table2Col2Name, idf=table2Col1Name))


def testDemoTrickyStuff():
	# PYEPHEM - INITIALIZE #####################################################################

	# Create instance of stowObserver, initialize with local date
	stowObserver = ephem.Observer()  # create instance of class
	stowObserver.lat = localLatStr
	stowObserver.lon = localLonStr
	stowObserver.elev = localElev
	stowObserver.horizon = str(minVisDeg)
	# StowTimeZoneOffset = localTimeZoneOffset
	if FALSE:
		print("\nStow Observer set")
		print("  ", stowObserver)
		print("  lon:%s  lat:%s  elev:%s  now:%s" % (
			stowObserver.lon, stowObserver.lat, stowObserver.elev, stowObserver.date))

	# Create instance of iss, initialize with sample TLE
	iss = ephem.readtle("ISS",
						"1 25544U 98067A   17172.89442130  .00001906  00000-0  36110-4 0  9990",
						"2 25544  51.6433  14.8648 0004452 307.3885 252.6376 15.54069411 62481")
	if FALSE:
		print("\nTLE updated")
		print("  ISS all data: ", iss)

	# Compute (update) for ISS and stowObserver
	iss.compute(stowObserver)
	if FALSE:
		print("\nISS current location")
		print("  lon:%s  lat:%s  elev:%s" % (iss.sublong, iss.sublat, iss.elevation))

	# PYEPHEM - DATE & TIME FORMATS ################################################################

	#  stored as float decimal days  (with noon as x.0)
	#  can force to string or tuple as detailed below

	#  using stowObserver directly
	if FALSE:
		print("\nUsing stowObserver directly")
		print("  stowObserver.date:", stowObserver.date)
		print(stowObserver.date)

	# using thisDate as assigned (is this a pointer or a new instance?)
	thisDate = stowObserver.date
	if FALSE:
		print("\nUsing thisDate")
		print("  thisDate:", thisDate)
		print(thisDate)

	# changed date formats
	if FALSE:
		print("\nDate formats (using stowObserver)")
		print("  as float:", float(stowObserver.date))
		print("  as tuple:", stowObserver.date.tuple())  # does this work?
	if FALSE:
		print("\nDate formats (using thisDate)")
		print("  as float:", float(thisDate))
		print("  as tuple:", thisDate.tuple())

	# convert to local time
	if FALSE:
		print("\nChange format use datetime functions")
		print("  ctime:", ephem.localtime(stowObserver.date).ctime())

	# PYEPHEM - CHANGE DATE & TIME #################################################

	#  does this work in two ways?
	#       stowObserver.date  (see examples A-D)
	#       ephem.date  (see example E)

	if FALSE:
		print("\nSetting a specific date")

	stowObserver.date = ephem.now()
	iss.compute(stowObserver)
	if FALSE:
		print("  A. entered as NOW: ephem.now()")
		print("     lon:%s  lat:%s  elev:%s local observer dt:%s" % (
			iss.sublong, iss.sublat, iss.elevation, stowObserver.date))

	stowObserver.date = "2017/6/23 01:59:25"
	iss.compute(stowObserver)
	if FALSE:
		print("  B. entered as str: 2017/6/23 01:59:25")
		print("     lon:%s  lat:%s  elev:%s local observer dt:%s" % (
			iss.sublong, iss.sublat, iss.elevation, stowObserver.date))

	stowObserver.date = ((2017, 1, 10, 3, 16, 12))  # note double parens
	iss.compute(stowObserver)
	if FALSE:
		print("  C. entered as tuple: ((2017,1,10,3,16,12))")
		print("     lon:%s  lat:%s  elev:%s local observer dt:%s" % (
			iss.sublong, iss.sublat, iss.elevation, stowObserver.date))

	hour = 7
	stowObserver.date((2017, 7, 4, hour + 1, 56, 20))
	iss.compute(stowObserver)
	if FALSE:
		print("  D. entered as increment from now")
		print("     lon:%s  lat:%s  elev:%s local observer dt:%s" % (
			iss.sublong, iss.sublat, iss.elevation, stowObserver.date))

	ephem.date((2017, 7, 4, 7, 56, 20))  # does this also work
	iss.compute(stowObserver)
	if FALSE:
		print("  E. entered as ephem.date")
		print(
			"     lon:%s  lat:%s  elev:%s local observer dt:%s" % (iss.sublong, iss.sublat, iss.elevation, ephem.date))

	# PYEPHEM - CHANGE ISS LOCATION #################################################

	#  simply change the date (stowObserver.date or ephem.date), and ISS location moves
	#  or use next_pass (and its variations)

	# ISS location changed by date offset
	if FALSE:
		print("\nChanging to a later date")
	stowObserver.date += 1
	iss.compute(stowObserver)
	if FALSE:
		print("  A. stowObserver.date+=1")
		print("     lon:%s  lat:%s  elev:%s local observer dt:%s" % (
			iss.sublong, iss.sublat, iss.elevation, stowObserver.date))
	thisDate = ephem.now()  # this uses ephem, and also saves today and tomorrow
	today = ephem.date(thisDate)
	tomorrow = ephem.date(thisDate + 1)
	if FALSE:
		print("  B. ephem.date.date(d+=1), using today %s and tomorrrow %s" % (today, tomorrow))
		print(
			"     lon:%s  lat:%s  elev:%s local observer dt:%s" % (iss.sublong, iss.sublat, iss.elevation, ephem.date))

	# PYEPHEM - NEXT PASS FLYOVER #################################################

	# Next pass - calculate flyover time
	stowObserver.date = ephem.now()
	nextpass = stowObserver.next_pass(iss)
	if FALSE:
		print("\nNext Pass - all 6 fields (as str)")
		print("  rise_time:%s  rise_az:%s" % (nextpass[0], nextpass[1]))
		print("  max_time: %s  max_alt:%s" % (nextpass[2], nextpass[3]))
		print("  set_time: %s  set_az: %s" % (nextpass[4], nextpass[5]))

	# Next pass - changing the format
	if FALSE:
		print("\nNext pass - dt formats")
		print("  rise-time - default", nextpass[0])  # i think default is float decimal days
		print("  rise-time - string", str(nextpass[0]))
		print("  rise-time - float", str(float(nextpass[0])))

	# Next pass - Subsequent flyover time
	settime = float(nextpass[4])
	ephem.date = settime + 0.2
	nextpass = stowObserver.next_pass(iss)
	if FALSE:
		print("\nSubsequent Pass - all 6 fields (as str)")
		print("  rise_time:%s  rise_az:%s" % (nextpass[0], nextpass[1]))
		print("  max_time: %s  max_alt:%s" % (nextpass[2], nextpass[3]))
		print("  set_time: %s  set_az: %s" % (nextpass[4], nextpass[5]))

	# Compute difference between two times
	if FALSE:
		print("\nDifference between two times)")
		print("  A. Nextpass - set-rise", (nextpass[4] - nextpass[0]))
		("     convert to secs:", int((nextpass[4] - nextpass[0]) * 24 * 60 * 60))
		print("  B. ephem.date: today-tomorrow ephem.date(d+1)-ephem.date(d)")


###########################
#   ACTIONS ON CLICK
###########################
def __________________________ACTIONS_ON_CLICK():
	return

def updateEphemerisFromWeb():
	showProgressMsg("Get new ephemeris data: DOING")
	isstle = webGetIssEphem()
	iss = ephem.readtle(isstle[0], isstle[1], isstle[2])  # ? other steps?
	showProgressMsg("Get new ephemeris data: DONE")

def updatePrepNextMsg():
	showProgressMsg("update prep next msg: DOING")
	createNextMsgToSend()
	showProgressMsg("update prep next msg: DONE")

def updateSendCurrentMsg():
	showProgressMsg("update send current msg: DOING")
	sendCurrentMsg()
	showProgressMsg("update send current msg: DONE")

def quitProgram():
	exit()  # or sys.exit()?
	showProgressMsg("quit program: DONE")

def TESTupdateDisplaySampleLocalAprs():
	global localAprsDataTable
	localAprsDataTable.clearTable()
	dirName='./localRec/'
	for fileName in sorted(os.listdir(dirName)):
		if fileName.startswith("localRec"):
			print(fileName)
			dirFileName = dirName + fileName
			with open(dirFileName, 'r') as readFile:
				for aprsRaw in readFile:
					aprsData = parsAprsRawToAprsData(aprsRaw)
					if FALSE:
						print(aprsRaw)
						print(aprsData)
			localAprsDataTable.prependData(aprsData)
			displayLocalReceiveGrid()


#############################
#   display - CONTROL CENTER
#############################

def __________________________CONTROL_CENTER():
	return

def displayControlCenter(thisBox):
	thisTag = "tagControlCenter"
	displaySectionTitle(thisBox, "Control Center")

	# SELECT MSG TYPE - HEADING
	current_RowChar = 1
	current_width = 120
	xPos = thisBox.left
	yPos = thisBox.top + current_RowChar * charHi
	displayAnyRectangle(xPos, yPos,  #left, top
						thisBox.left + current_width, #right
						thisBox.top + (current_RowChar + 1) * charHi -1, # bottom
						promptBg, stdBoxOutline, thisTag)
	displayAnyText(xPos+1, yPos+1, "SELECT MSG TYPE: ", allTextFg, promptBg, thisTag)

	# SELECT MSG TYPE - OPTIONS (Radio Button)
	current_RowChar = 2
	current_ColChar = 3
	MODES = [("current email in queue", "current email action"),
			 ("insert this email", "insert email action"),
			 ("local beacon", "local beacon action"),
			 ("this custom message:", "custom message action")]
	v = StringVar()
	v.set("current email action")
	for text, mode in MODES:
		controlButton = Radiobutton(root, text=text, variable=v, value=mode)
		controlButton.place(x=thisBox.left + current_ColChar * charWid, y=thisBox.top + current_RowChar * charHi)
		current_RowChar += 1

	# FIRST NAME - Prompt and Entry
	bothRowChar = 3
	promptStartChar = 25
	promptWidthChar = 6
	entryWidthChar = 10
	nextStartChar = promptStartChar+promptWidthChar+entryWidthChar+2
	promptText = "FIRST:"
	firstname_entry = promptForTextInput(thisBox.left, thisBox.top,
										 bothRowChar, promptStartChar, promptWidthChar, entryWidthChar, promptText)

	# LAST NAME - Prompt and Entry
	bothRowChar = 3
	promptStartChar = nextStartChar
	promptWidthChar = 5
	entryWidthChar = 15
	nextStartChar = promptStartChar+promptWidthChar+entryWidthChar+2
	promptText = "LAST:"
	lastname_entry = promptForTextInput(thisBox.left, thisBox.top,
										bothRowChar, promptStartChar, promptWidthChar, entryWidthChar, promptText)

	# EMAIL - Prompt and Entry
	bothRowChar = 3
	promptStartChar = nextStartChar
	promptWidthChar = 6
	entryWidthChar = 24
	promptText = "EMAIL:"
	email_entry = promptForTextInput(thisBox.left, thisBox.top,
									 bothRowChar, promptStartChar, promptWidthChar, entryWidthChar, promptText)

	# CUSTOM MSG - Prompt and Entry
	bothRowChar = 5
	promptStartChar = 25
	promptWidthChar = 5
	entryWidthChar = 65
	promptText = "MSG:"
	custommsg = promptForTextInput(thisBox.left, thisBox.top,
								   bothRowChar, promptStartChar, promptWidthChar, entryWidthChar, promptText)

	# display NEXT MSG IN QUEUE
	thisRowChar = 7
	thisTextLen = 4
	displayAnyRectangle(thisBox.left,
						thisBox.top + thisRowChar * charHi - 1,
						thisBox.left + (thisTextLen + 1) * charWid - 1,
						thisBox.top + (thisRowChar + 1) * charHi - 1,
						promptBg, stdBoxOutline, thisTag)
	displayAnyText(thisBox.left + 1,thisBox.top + 1 + thisRowChar * charHi,"NEXT:",allTextFg, promptBg, thisTag)

	thisColChar = 5
	currentAPRSmsg = "KA1ARD>CQ,ARISS*::EMAIL    :MBowen@gmail.com Hello from ISS! SpaceStnExp.org/ham"
	displayAnyRectangle(thisBox.left + (thisColChar) * charWid - 1,
						thisBox.top + thisRowChar * charHi - 1,
						thisBox.right,
						thisBox.top + (thisRowChar + 1) * charHi - 1,
						highlightBg, stdBoxOutline, thisTag)
	displayAnyText(thisBox.left + thisColChar * charWid + 4,
				   thisBox.top + thisRowChar * charHi,
				   currentAPRSmsg,
				   allTextFg, highlightBg, thisTag)

	# CONTROL BUTTONS
	thisRowChar = 8
	thisRow2Char = 10
	thisRow3Char = 12
	thisRow4Char = 14
	buttonwidth = 200
	buttonRow1TopPix = thisBox.top + thisRowChar * charHi
	buttonRow2TopPix = thisBox.top + thisRow2Char * charHi
	buttonRow3TopPix = thisBox.top + thisRow3Char * charHi
	buttonRow4TopPix = thisBox.top + thisRow4Char * charHi
	# ROW 1
	Button(root, text="Create next msg", command=(lambda: updatePrepNextMsg())).place(
		x=thisBox.left + 0 * buttonwidth, y=buttonRow1TopPix)
	Button(root, text="Send Now", command=(lambda: updateSendCurrentMsg())).place(
		x=thisBox.left + 1 * buttonwidth, y=buttonRow1TopPix)
	Button(root, text="Automatic").place(
		x=thisBox.left + 2 * buttonwidth, y=buttonRow1TopPix)
	Button(root, text="Stop").place(
		x=thisBox.left + 3 * buttonwidth, y=buttonRow1TopPix)
	# ROW 2
	Button(root, text="Manual Refresh", command=(lambda: manualRefreshLoop())).place(
		x=thisBox.left + 0 * buttonwidth, y=buttonRow2TopPix)
	Button(root, text="Get data - ephemeris", command=(lambda: updateEphemerisFromWeb())).place(
		x=thisBox.left + 1 * buttonwidth, y=buttonRow2TopPix)
	Button(root, text="Receive now", command=(lambda: receiveNow())).place(
		x=thisBox.left + 2 * buttonwidth, y=buttonRow2TopPix)
	Button(root, text="Quit", command=(lambda: quitProgram())).place(
		x=thisBox.left + 3 * buttonwidth, y=buttonRow2TopPix)
	# ROW 3
	Button(root, text="read & display sample APRS", command=(lambda: TESTupdateDisplaySampleLocalAprs())).place(
		x=thisBox.left + 0 * buttonwidth, y=buttonRow3TopPix)


###########################
#   TIMED REFRESH
###########################
def __________________________TIMED_REFRESH():
	return

def processUpdate():
	global lastUpdate
	elapsedCheck = datetime.now() - lastUpdate

	showProgressMsg("entered processUpdate countdown: " + str(updateDelaySecs - int(elapsedCheck.total_seconds())))

	if elapsedCheck.total_seconds() > updateDelaySecs:
		# GET DATA - GLOBAL
		showProgressMsg("processUpdate: get new global APRS data: DOING")
		globalAprsClearAndRefreshDataTableFromWeb()
		# preCreateJsonForDataTable()

		# GET DATA - LOCAL RADIO
		showProgressMsg("processUpdate: get new local APRS data: DOING")
		checkAndGetLocalAprs()

		# UPDATE FLYOVER TIMES
		showProgressMsg("processUpdate: calculate flyovers: DOING")
		calculateDatatableFlyovers()

		# display FLYOVER
		showProgressMsg("processUpdae: display flyovers: DOING")
		displayFlyoverGrid()
		displayFlyoverTimelineBase(flyoverTimelineSectionBox)  ## delete?
		displayFlyoverTimeline()

		# display MAPS
		showProgressMsg("processUpdate: display maps: DOING")
		displayIssPathOnAllMaps()
		displayGlobalAprsOnAllMaps()
		displayAllRecStnOnAllMaps()
		displayIssNowOnAllMaps()

		# display GLOBAL APRS GRID
		showProgressMsg("processUpdate: display APRS grid: DOING")
		displayGlobalAprsGrid()
		displayAprsTimeline()

		lastUpdate = datetime.now()

def timedRefreshLoop():
	global updateDelaySecs
	global lastUpdate
	updateDelaySecs = 30

	showProgressMsg("entered timedRefreshLoop")

	lastUpdate = datetime.now() - timedelta(seconds=updateDelaySecs + 1)

	while TRUE:
		processUpdate()


###########################
#   MAIN PROGRAM
###########################
print("MAIN:  begin")

def __________________________MAIN_STARTUP_TKINTER():
	return

# CREATE MAIN WINDOW & SET UP GEOMETRY
root = Tk()
root.title("Hello from ISS")
rootgeomstr = (str(fullPageRightPix) + "x" + str(fullPageBottomPix) + "+0+0")
root.geometry(rootgeomstr)
canvasBox = Canvas(root, width=fullPageRightPix, height=fullPageBottomPix)
canvasBox.place(x=0, y=0)
canvasBox.update()

def _________________________MAIN_STARTUP_SCREEN_LAYOUT():
	return

# CREATE SECTION BOXES
flyoverTimesSectionBox = box(flyoverLeftPix, flyoverTopPix, flyoverRightPix, flyoverBottomPix)
flyoverTimelineSectionBox = box(flyoverTimelineLeftPix, flyoverTimelineTopPix, flyoverTimelineRightPix, flyoverTimelineBottomPix)
regMapSectionBox = box(regMapLeftPix, regMapTopPix, regMapRightPix, regMapBottomPix)
worldMapSectionBox = box(worldMapLeftPix, worldMapTopPix, worldMapRightPix, worldMapBottomPix)
sendToIssSectionBox = box(sendToIssLeftPix, sendToIssTopPix, sendToIssRightPix, sendToIssBottomPix)
controlCenterSectionBox = box(controlCenterLeftPix, controlCenterTopPix, controlCenterRightPix, controlCenterBottomPix)
recByLocalRadioSectionBox = box(recByLocalRadioLeftPix, recByLocalRadioTopPix, recByLocalRadioRightPix, recByLocalRadioBottomPix)
recByGlobalNetSectionBox = box(recByGlobalNetLeftPix, recByGlobalNetTopPix, recByGlobalNetRightPix, recByGlobalNetBottomPix)
actionMsgSectionBox = box(actionMsgLeftPix, actionMsgTopPix, actionMsgRightPix, actionMsgBottomPix)
aprsTimelineSectionBox = box(aprsTimelineLeftPix, aprsTimelineTopPix, aprsTimelineRightPix, aprsTimelineBottomPix)

# CREATE MAP SPECS
worldMapSpecs = mapSpecs(worldMapLeftPix, worldMapTopPix, worldMapRightPix, worldMapBottomPix,
						 worldMapLeftLonDeg, worldMapRightLonDeg, worldMapTopLatDeg, worldMapBottomLatDeg)
regMapSpecs = mapSpecs(regMapLeftPix, regMapTopPix, regMapRightPix, regMapBottomPix,
					   regMapLeftLonDeg, regMapRightLonDeg, regMapTopLatDeg, regMapBottomLatDeg)

# display Progress Msg Box
displayProgressMsgBase(actionMsgSectionBox)

def ________________________MAIN_STARTUP_DATA():
	return

# STARTUP - GET EPHEMERIS, INITIALIZE OBSERVER
if TRUE:
	showProgressMsg("MAIN:  Startup - Getting new TLE")
	isstle = webGetIssEphem()
	iss = ephem.readtle(isstle[0], isstle[1], isstle[2])
	localobserver = ephem.Observer()
	localobserver.lat = localLatStr
	localobserver.lon = localLonStr
	localobserver.elev = localElev
	localobserver.horizon = str(minVisDeg)

# STARTUP - CALCULATE FLYOVER TIMES   NOTE: this used to be part of display flyovers.  Should work fine here
if TRUE:
	showProgressMsg("MAIN:  Calculating flyovers")
	flyoversDataTable = dataTable(flyoversData,flyoversFormat)
	calculateDatatableFlyovers()

# STARTUP - GET BASELINE GLOBAL RECEIVED APRS
if TRUE:
	showProgressMsg("MAIN:  Startup - baseline global APRS msgs")
	globalAprsCreateDataTableFromJson()

# STARTUP - GET BASELINE EMAIL REQUESTS
if TRUE:
	showProgressMsg("MAIN:  Startup - baseline email requests")
	emailRequestsCreateDataTableFromJson()

# STARTUP - GET BASELINE LOCAL RADIO RECEIVED APRS
if TRUE:
	showProgressMsg("MAIN:  Startup - baseline local radio APRS msgs")
	localRadioAprsCreateDataTableFromJson()

# STARTUP - GET BASELINE downlink stations
if TRUE:
	showProgressMsg("MAIN:  Startup - baseline Downlink stns")
	downlinkStnsCreateReferenceDataFromJson()


def ________________________MAIN_STARTUP_DISPLAY_DATA():
	return

# DISPLAY - MAPS
if TRUE:
	showProgressMsg("MAIN:  displaying maps")
	displayRegMapBase(regMapSectionBox)
	displayWorldMapBase(worldMapSectionBox)
	displayReceptionRegionOnAllMaps()

	displayIssPathOnAllMaps()
	displayIssNowOnAllMaps()
	displayGlobalAprsOnAllMaps()
	displayAllRecStnOnAllMaps()

# DISPLAY - EMAIL REQUESTS
if TRUE:
	showProgressMsg("MAIN:  displaying grid: email requests")
	displayEmailRequestsGrid()


# DISPLAY - LOCAL RADIO RECEIVED APRS
if TRUE:
	showProgressMsg("MAIN:  displaying local receive")
	displayLocalReceiveGrid()


# DISPLAY - GLOBAL RECEIVED APRS
if TRUE:
	showProgressMsg("MAIN:  displaying Global APRS grid")
	displayGlobalAprsGrid()
	displayAprsTimelineBase(aprsTimelineSectionBox)
	displayAprsTimeline()

# DISPLAY - FLYOVER TIMES
if TRUE:
	showProgressMsg("MAIN:  displaying flyover times")
	displayFlyoverTimelineBase(flyoverTimelineSectionBox)
	displayFlyoverGrid()
	displayFlyoverTimeline()

# display CONTROL CENTER
def ________________________MAIN_STARTUP_CONTROL_CENTER():
	return

if TRUE:
	showProgressMsg("MAIN:  displaying control center")
	displayControlCenter(controlCenterSectionBox)

# TEST
if FALSE:
	testDemoTrickyStuff()

# TEST
if TRUE:
	testDataBase()

def ________________________MAIN_AUTO_UPDATE():
	return

if autoRefreshFullDisplay:
	showProgressMsg("MAIN:  Initiating timed display Loop")
	timedRefreshLoop()

showProgressMsg("MAIN:  Done, now in MAIN LOOP")

def ________________________MAIN_LOOP():
	return

root.mainloop()  # excecute main loop
