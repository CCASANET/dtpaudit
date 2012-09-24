import csv

DTPVerbose = True

class DTPSchema(object):
    BASIC = ( 
            'patient', 
            'site', 
            'male', 
            'birth_d', 
            'birth_d_a', 
            'mode', 
            'mode_oth', 
            'hivdiagnosis_d', 
            'hivdiagnosis_d_a', 
            'firstvis_d', 
            'firstvis_d_a', 
            'recart_y', 
            'recart_d', 
            'recart_d_a', 
            'enrol_d', 
            'enrol_d_a', 
            'aids_y', 
            'aids_d', 
            'aids_d_a', 
            'cdcstage', 
            'whostage',
            )
    FOLLOW = ( 
            'patient', 
            'site', 
            'death_y', 
            'death_d', 
            'drop_y', 
            'drop_d', 
            'drop_rs', 
            'death_r1', 
            'death_rc1', 
            'death_oth1', 
            'death_r2', 
            'death_rc2', 
            'death_oth2', 
            'death_r3', 
            'death_rc3',
            'death_oth3', 
            'l_alive_d', 
            )
    VISIT = (
            'patient', 
            'site', 
            'visit_d', 
            'location', 
            'whostage', 
            'cdcstage',
            )
    ART = (
            'patient', 
            'site', 
            'art_id', 
            'art_sd', 
            'art_sd_a', 
            'art_ed', 
            'art_ed_a', 
            'art_rs',
            'art_rs_oth', 
            )
    CD4 = (
            'patient', 
            'site', 
            'cd4_d', 
            'cd4_d_a', 
            'cd4_v', 
            'cd4_per',
            )
    RNA = (
            'patient', 
            'site', 
            'rna_d', 
            'rna_d_a', 
            'rna_v', 
            'rna_l', 
            'rna_u', 
            'rna_t',
            )

class DTPRow(object):
    _scheme = None
    def __init__(self,rowhash={}):
        schemevars = getattr( DTPSchema, self._scheme, () )
        for thisvar in schemevars:
            if rowhash.has_key( thisvar ):
                setattr( self, thisvar, rowhash[ thisvar ] )
            else:
                setattr( self, thisvar, None )

    def test(self):
        """
        Can override in subclasses
        True indicates a problem. Consider creating testing infrastructure.
        """
        if self.test_Unidentifiable():
            return True
        return False

    def test_Unidentifiable(self):
        if self.patient and self.site:
            return False
        else:
            return True

    def __str__(self):
        retstr = str(self.__class__)+"\n"
        retstr+= "Scheme = {0}\n".format(self._scheme)
        for x,y in vars(self).iteritems():
            retstr+= "\t{0}:\t{1}\n".format(x,y)
        retstr+= "\n"
        return retstr


class RowBasic(DTPRow):
    _scheme = 'BASIC'

class RowFollow(DTPRow):
    _scheme = 'FOLLOW'

class RowVisit(DTPRow):
    _scheme = 'VISIT'

class RowART(DTPRow):
    _scheme = 'ART'

class RowCD4(DTPRow):
    _scheme = 'CD4'

class RowRNA(DTPRow):
    _scheme = 'RNA'

class DTPTable(object):
    """
    Todo:
    add - check for schema
    iterate
    save
    map to patient
    """
    _numrows = None
    _rows = None
    _rowClass = None

    def __init__(self, filename=None):
        self._numrows = 0
        """For now implement as array of DTPRow"""
        self._rows = list()
        if filename is not None:
            self.readFile(filename)

    def append(self, newrow):
        if isinstance(newrow, self._rowClass):
            return self._rows.append( newrow )
        elif DTPVerbose:
            print "Attempting to add row of scheme={0} to table of scheme={1}".format(newrow._scheme, self._rowClass._scheme)
        return None

    def __getitem__(self, index):
        return self._rows[index]

    def __len__(self):
        return len(self._rows)

    def __iter__(self):
        return iter( self._rows )

    def makeRow(self, rowhash={} ):
        if self._rowClass and issubclass( self._rowClass, DTPRow ):
            return self._rowClass(rowhash)
        elif DTPVerbose:
            print "Attempting to create a row when the table's row class is not well defined"
        return None

    def readFile(self, filename):
        if DTPVerbose:
            print "Reading records into DTPTable"
            print "\tscheme = {0}".format(self._rowClass._scheme)
            print "\tsize before = {0:d}".format( len(self) )
        thisreader = DTPTableReader(filename)
        for thisrowhash in thisreader:
            thisrow = self.makeRow( thisrowhash )
            if DTPVerbose:
                if thisrow.test_Unidentifiable():
                    print "Found unidentifiable row, added anyway..."
            self.append(thisrow)
        thisreader.close()
        if DTPVerbose:
            print "Done reading records into DTPTable"
            print "\trows read = {0:d}".format(thisreader._counter)
            print "\tsize after = {0:d}".format( len(self) )
            print
        return thisreader._counter





class TableBasic(DTPTable):
    _rowClass = RowBasic

class TableFollow(DTPTable):
    _rowClass = RowFollow

class TableVisit(DTPTable):
    _rowClass = RowVisit

class TableART(DTPTable):
    _rowClass = RowART

class TableCD4(DTPTable):
    _rowClass = RowCD4

class TableRNA(DTPTable):
    _rowClass = RowRNA



class DTPTableReader(object):
    _reader = None
    _filename = None
    _fhandle = None

    _lastRowHash = None;
    _counter = None;

    def __init__( self, filename ):
        self._filename = filename
        if DTPVerbose:
            print ('Opening file {0}\n'.format(self._filename))
        self._fhandle = open( self._filename, 'r')
        self._reader = csv.DictReader(self._fhandle)
        if DTPVerbose:
            print ('Fieldnames in file are:\n{0}\n\t'.format( '\n\t'.join( self._reader.fieldnames ) ) )
        self._counter = 0

    def __iter__( self ):
        return self

    def next( self ):
        self._lastRowHash = self._reader.next()
        """
        if no more records in the file, this method will raise a StopIteration exception, so records will not update (desired behavior)
        """
        self._counter = self._counter + 1
        return self._lastRowHash

    def close( self ):
        return self._fhandle.close()


class DTPPatient(object):
    """
    Assumes the global uniqueness is based on SITE + PATIENT combo
    Todo add visit
    """
    _patient = None
    _site = None

    Basic = None
    Follow = None
    Visits = None
    CD4s = None
    RNAs = None
    ARTs = None

    def isAnonymous(self):
        if self._patient and self._site:
            return False
        else:
            return True

    def addRows(self, newrows):
        """
        Convenience method, checks only at row level. Assumes newrows is
        iterable
        """
        truecounter = 0
        for newrow in newrows:
            addresult = self.addRow(newrow)
            if addresult:
                truecounter+=1
        return truecounter

    def addRow(self, newrow):
        """
        TODO
        Update to add confirmation to force update of existing rows
        Check automatically for SITE + PATIENT
        """
        if not isinstance(newrow, DTPRow):
            return False

        if newrow.test_Unidentifiable():
            print "Unidentifiable row, cannot add"
            return False

        if self.isAnonymous() and not isinstance(newrow, RowBasic):
            print "Can only add RowBasic to an anoymous patient"
            return False

        if isinstance(newrow, RowBasic):
            return self._addRow_Basic(newrow)
        elif isinstance(newrow, RowFollow):
            return self._addRow_Follow(newrow)
        elif isinstance(newrow, RowVisit):
            return self._addRow_Visit(newrow)
        elif isinstance(newrow, RowCD4):
            return self._addRow_CD4(newrow)
        elif isinstance(newrow, RowRNA):
            return self._addRow_RNA(newrow)
        elif isinstance(newrow, RowART):
            return self._addRow_ART(newrow)
        else:
            print "Unrecognized DTPRow type"
            return False

    def _addRow_Basic(self, newrow):
        if self.isAnonymous(): 
            self.Basic = newrow
            self._patient = newrow.patient
            self._site = newrow.site
            return True
        if not self.rowMatches(newrow):
            print "Basic row does not match the patient. Cannot add"
            return False
        self.Basic = newrow
        return True
        
    def _addRow_Follow(self, newrow):
        if not self.rowMatches(newrow):
            print "Follow row does not match the patient. Cannot add"
            return False
        self.Follow = newrow
        return True
        
    def _addRow_Visit(self, newrow):
        if not self.rowMatches(newrow):
            print "Visit row does not match the patient. Cannot add"
            return False
        if self.Visits is None:
            self.Visits = list()
        self.Visits.append( newrow )
        self.Visits.sort( key=lambda x: x.visit_d )
        return True

    def _addRow_CD4(self, newrow):
        if not self.rowMatches(newrow):
            print "CD4 row does not match the patient. Cannot add"
            return False
        if self.CD4s is None:
            self.CD4s = list()
        self.CD4s.append( newrow )
        self.CD4s.sort( key=lambda x: x.cd4_d )
        return True
        
    def _addRow_RNA(self, newrow):
        if not self.rowMatches(newrow):
            print "RNA row does not match the patient. Cannot add"
            return False
        if self.RNAs is None:
            self.RNAs = list()
        self.RNAs.append( newrow )
        self.RNAs.sort( key=lambda x: x.rna_d )
        return True
        
    def _addRow_ART(self, newrow):
        if not self.rowMatches(newrow):
            print "ART row does not match the patient. Cannot add"
            return False
        if self.ARTs is None:
            self.ARTs = list()
        self.ARTs.append( newrow )
        self.ARTs.sort( key=lambda x: x.art_sd )
        return True
        
    def rowMatches(self, newrow):
        if self._patient == newrow.patient and self._site == newrow.site:
            return True
        else:
            return False
