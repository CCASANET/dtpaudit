#!/usr/bin/env python

import cndtp
import cnaudit
import csv


def findRows( patient, dtptable ):
    retlist = list()
    if patient.isAnonymous():
        print "Anonymous patient"
        return retlist
    for dtprow in dtptable:
        if patient.rowMatches( dtprow ): 
            retlist.append( dtprow )
    return retlist

basics = cndtp.TableBasic('dtpfiles/basic.csv')
follows = cndtp.TableFollow('dtpfiles/follow.csv')
visits = cndtp.TableVisit('dtpfiles/visit.csv')
arts = cndtp.TableART('dtpfiles/art.csv')
cd4s = cndtp.TableCD4('dtpfiles/lab_cd4.csv')
rnas = cndtp.TableRNA('dtpfiles/lab_rna.csv')

"""
Read list of patients to make HTML forms for
"""
patientids = list()
fh = open('dtpfiles/ids-for-audit.csv','r')
csv_reader = csv.reader(fh)
for x in csv_reader:
    newdict = dict()
    newdict['patient'] = x[0]
    newdict['site'] = x[1]
    patientids.append( newdict )
fh.close()

patients = list()
for patientid in patientids:
    thispatient = cndtp.DTPPatient()
    thisrowbasic = cndtp.RowBasic( patientid )
    thispatient.addRow( thisrowbasic )
    patients.append( thispatient )

# Uncomment for debugging
# patients = patients[:5]
for patient in patients:
    print "Looking for patient {0} {1}".format( patient._site, patient._patient )
    foundbasics = findRows( patient, basics )
    print "Found {0:d} rows in Basic, {1:d} added successfully".format( len( foundbasics ), patient.addRows( foundbasics ) )
    foundfollows = findRows( patient, follows )
    print "Found {0:d} rows in Follow, {1:d} added successfully".format( len( foundfollows ), patient.addRows( foundfollows ) )
    foundvisits = findRows( patient, visits )
    print "Found {0:d} rows in Visits, {1:d} added successfully".format( len( foundvisits ), patient.addRows( foundvisits ) )
    foundarts = findRows( patient, arts )
    print "Found {0:d} rows in ARTs, {1:d} added successfully".format( len( foundarts ), patient.addRows( foundarts ) )
    foundcd4s = findRows( patient, cd4s )
    print "Found {0:d} rows in CD4s, {1:d} added successfully".format( len( foundcd4s ), patient.addRows( foundcd4s ) )
    foundrnas = findRows( patient, rnas )
    print "Found {0:d} rows in RNAs, {1:d} added successfully".format( len( foundrnas ), patient.addRows( foundrnas ) )
    print
    patientHTML = cnaudit.DTPHTML( patient )
    patientHTML.makeFile()
