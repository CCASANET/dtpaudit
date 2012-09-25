import cndtp

class DTPHTML(object):
    _patient = None

    def __init__(self, patient):
        if isinstance( patient, cndtp.DTPPatient ):
            if not patient.isAnonymous(): 
                self._patient = patient
            else:
                print "Can't make HTML of an anonymous patient"
        else:
            print "Can't make HTML of object that is not DTPPatient"

    def makeFile(self):
        fh = open( 'auditforms/audit_{0}_{1}.html'.format( self._patient._site, self._patient._patient ), 'w' )
        fh.write( self._makeHeader() )
        fh.write( self._makeBody() )
        fh.close()

    def _makeHeader(self):
        retstring = '<html>\n<head>\n'
        retstring+= '\t<title>{0}_{1}</title>\n'.format( self._patient._site, self._patient._patient )
        retstring+= '\t<link rel="stylesheet" type="text/css" href="audit.css" />\n'
        retstring+= '</head>\n'
        return retstring

    def _makeBody(self):
        retstring = '<body>\n'
        retstring+= self._makeBasic()
        retstring+= self._makeFollow()
        retstring+= self._makeVisits()
        """
        retstring+= self._makeARTs()
        retstring+= self._makeCD4s()
        retstring+= self._makeRNAs()
        """
        retstring+= '</body>\n'
        retstring+= '</html>'
        return retstring

    def _makeBasic(self):
        retstring = ''
        retstring+= '<h1>BASIC</h1>\n'
        basic = self._patient.Basic
        if basic is None:
            retstring+= '<h2>No record in BASIC found</h2>\n'
            return retstring
        retstring+= '<table class="basic">\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'SITE', 'CENTER', 'PATIENT' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.site, 'Not prepared', basic.patient )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'MALE', 'BIRTH_D', 'BIRTH_D_A' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.male, basic.birth_d, basic.birth_d_a )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'MODE', 'MODE_OTH', '&nbsp;')
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.mode, basic.mode_oth, '&nbsp;' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'HIVDIAGNOSIS_D (_A)', 'FIRSTVIS_D (_A)', 'ENROL_D (_A)' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0} ({3})</td><td>{1} ({4})</td><td>{2} ({5})</td>'.format( basic.hivdiagnosis_d, basic.firstvis_d, basic.enrol_d, basic.hivdiagnosis_d_a, basic.firstvis_d_a, basic.enrol_d_a )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'AIDS_Y', 'AIDS_D', 'AIDS_D_A' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.aids_y, basic.aids_d, basic.aids_d_a )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'RECART_Y', 'RECART_D', 'RECART_D_A' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.recart_y, basic.recart_d, basic.recart_d_a )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'CDCSTAGE', 'WHOSTAGE', '&nbsp;' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.cdcstage, basic.whostage, '&nbsp;' )
        retstring+= '</tr>\n'
        retstring+= '</table>\n'
        retstring+= '<br />\n'
        return retstring

    def _makeFollow(self):
        retstring = ''
        retstring+= '<h1>FOLLOW</h1>\n'
        follow = self._patient.Follow
        if follow is None:
            retstring+= '<h2>No record in FOLLOW found</h2>\n'
            retstring+= '<br />\n'
            return retstring
        retstring+= '<table class="follow">\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DROP_Y', 'DROP_D', 'DROP_RS' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.drop_y, follow.drop_d, follow.drop_rs )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DEATH_Y', 'DEATH_D', 'L_ALIVE_D' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.death_y, follow.death_d, follow.l_alive_d )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DEATH_R1', 'DEATH_RC1', 'DEATH_OTH1' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.death_r1, follow.death_rc1, follow.death_oth1 )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DEATH_R2', 'DEATH_RC2', 'DEATH_OTH2' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.death_r2, follow.death_rc2, follow.death_oth2 )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DEATH_R3', 'DEATH_RC3', 'DEATH_OTH3' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.death_r3, follow.death_rc3, follow.death_oth3 )
        retstring+= '</tr>\n'
        retstring+= '</table>\n'
        retstring+= '<br />\n'
        return retstring

    def _makeVisits(self):
        retstring = ''
        retstring+= '<h1>VISIT</h1>\n'
        visits = self._patient.Visits
        if visits is None:
            retstring+='<h2>No records in VISIT found</h2>\n'
            retstring+='<br />'
            return retstring
        retstring+= '<table class="visit">\n'
        retstring+= '\t<tr>'
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th>'.format( '&nbsp;', 'VISIT_D', 'LOCATION', 'CDCSTAGE', 'WHOSTAGE' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for visit in visits:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td>'.format( rowcounter, visit.visit_d, visit.location, visit.cdcstage, visit.whostage )
            retstring+= '</tr>\n'

        retstring+= '</table>\n'
        retstring+= '<br />\n'
        return retstring

    def _makeARTs(self):
        retstring = ''
        retstring+= '<h1>ARTs</h1>\n'
        arts = self._patient.ARTs
        if arts is None:
            retstring+='<h2>No records in ART found</h2>\n'
            retstring+='<br />'
            return retstring
        retstring+= '<table class="art">\n'
        retstring+= '\t<tr>'
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th>'.format( '&nbsp;', 'Regimen', 'Start Date', 'End Date', 'Reason for Change' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for art in arts:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td>'.format( rowcounter, art.ART_ID, art.ART_SD, art.ART_ED, art.ART_RS )
            retstring+= '</tr>\n'

        retstring+= '</table>\n'
        retstring+= '<br />\n'
        return retstring

    def _makeCD4s(self):
        retstring = ''
        retstring+= '<h1>CD4s</h1>\n'
        cd4s = self._patient.CD4s
        if cd4s is None:
            retstring+='<h2>No records in CD4 found</h2>\n'
            retstring+='<br />'
            return retstring
        retstring+= '<table class="cd4">\n'
        retstring+= '\t<tr>'
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th>'.format( '&nbsp;', 'Date', 'Value' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for cd4 in cd4s:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1}</td><td>{2}</td>'.format( rowcounter, cd4.CD4_D, cd4.CD4_V )
            retstring+= '</tr>\n'

        retstring+= '</table>\n'
        retstring+= '<br />\n'
        return retstring

    def _makeRNAs(self):
        retstring = ''
        retstring+= '<h1>RNAs</h1>\n'
        rnas = self._patient.RNAs
        if rnas is None:
            retstring+='<h2>No records in RNA found</h2>\n'
            retstring+='<br />'
            return retstring
        retstring+= '<table class="rna">\n'
        retstring+= '\t<tr>'
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th>'.format( '&nbsp;', 'Date', 'Value' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for rna in rnas:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1}</td><td>{2}</td>'.format( rowcounter, rna.RNA_D, rna.RNA_V )
            retstring+= '</tr>\n'

        retstring+= '</table>\n'
        retstring+= '<br />\n'
        return retstring


