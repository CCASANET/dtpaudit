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
        retstring+= self._makeARTs()
        retstring+= self._makeCD4s()
        retstring+= self._makeRNAs()
        retstring+= self._makeCEs()
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
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.site, basic.center, basic.patient )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'MALE', 'BIRTH_D', 'BIRTH_D_A' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.male, basic.birth_d, basic.birth_d_a )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'MODE', 'MODE_OTH', '&nbsp;')
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.mode, basic.mode_oth, '&nbsp;' )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'HIVDIAGNOSIS_D (_A)', 'FIRSTVIS_D (_A)', 'ENROL_D (_A)' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0} ({3})</td><td>{1} ({4})</td><td>{2} ({5})</td>'.format( basic.hivdiagnosis_d, basic.firstvis_d, basic.enrol_d, basic.hivdiagnosis_d_a, basic.firstvis_d_a, basic.enrol_d_a )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'AIDS_Y', 'AIDS_D', 'AIDS_D_A' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.aids_y, basic.aids_d, basic.aids_d_a )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'RECART_Y', 'RECART_D', 'RECART_D_A' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.recart_y, basic.recart_d, basic.recart_d_a )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'CDCSTAGE', 'WHOSTAGE', '&nbsp;' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( basic.cdcstage, basic.whostage, '&nbsp;' )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
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
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DEATH_Y', 'DEATH_D', 'L_ALIVE_D' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.death_y, follow.death_d, follow.l_alive_d )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DEATH_R1', 'DEATH_RC1', 'DEATH_OTH1' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.death_r1, follow.death_rc1, follow.death_oth1 )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DEATH_R2', 'DEATH_RC2', 'DEATH_OTH2' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.death_r2, follow.death_rc2, follow.death_oth2 )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( 'DEATH_R3', 'DEATH_RC3', 'DEATH_OTH3' )
        retstring+= '</tr>\n'
        retstring+= '\t<tr>'
        retstring+= '<td>{0}</td><td>{1}</td><td>{2}</td>'.format( follow.death_r3, follow.death_rc3, follow.death_oth3 )
        retstring+= '</tr>\n'
        retstring+= self.makeEmptyRow(3)
        retstring+= self.makeEmptyRow(3)
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
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th><th>{5} ({6})</th><th>{7} ({8})</th>'.format( '&nbsp;', 'VISIT_D', 'LOCATION', 'CDCSTAGE', 'WHOSTAGE', 'WEIGHT', '_U', 'HEIGHT', '_U' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for visit in visits:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5} ({6})</td><td>{7} ({8})</td>'.format( rowcounter, visit.visit_d, visit.location, visit.cdcstage, visit.whostage, visit.weight, visit.weight_u, visit.height, visit.height_u )
            retstring+= '</tr>\n'
            retstring+= self.makeEmptyRow(7)
            retstring+= self.makeEmptyRow(7)
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
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th><th>{5}</th>'.format( '&nbsp;', 'ART_ID', 'ART_SD (_A)', 'ART_ED (_A)', 'ART_RS', 'ART_RS_OTH' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for art in arts:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1}</td><td>{2} ({3})</td><td>{4} ({5})</td><td>{6}</td><td>{7}</td>'.format( rowcounter, art.art_id, art.art_sd, art.art_sd_a, art.art_ed, art.art_ed_a, art.art_rs, art.art_rs_oth )
            retstring+= '</tr>\n'
            retstring+= self.makeEmptyRow(6)
            retstring+= self.makeEmptyRow(6)

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
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th>'.format( '&nbsp;', 'CD4_D (_A)', 'CD4_V', 'CD4_PER' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for cd4 in cd4s:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1} ({2})</td><td>{3}</td><td>{4}</td>'.format( rowcounter, cd4.cd4_d, cd4.cd4_d_a, cd4.cd4_v, cd4.cd4_per )
            retstring+= '</tr>\n'
            retstring+= self.makeEmptyRow(4)
            retstring+= self.makeEmptyRow(4)

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
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th><th>{5}</th>'.format( '&nbsp;', 'RNA_D (_A)', 'RNA_V', 'RNA_L', 'RNA_U', 'RNA_T' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for rna in rnas:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1} ({2})</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td>'.format( rowcounter, rna.rna_d, rna.rna_d_a, rna.rna_v, rna.rna_l, rna.rna_u, rna.rna_t )
            retstring+= '</tr>\n'
            retstring+= self.makeEmptyRow(6)
            retstring+= self.makeEmptyRow(6)

        retstring+= '</table>\n'
        retstring+= '<br />\n'
        return retstring

    def _makeCEs(self):
        retstring = ''
        retstring+= '<h1>CEs</h1>\n'
        ces = self._patient.CEs
        if ces is None:
            retstring+='<h2>No records in CE found</h2>\n'
            retstring+='<br />'
            return retstring
        retstring+= '<table class="ce">\n'
        retstring+= '\t<tr>'
        retstring+= '<th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th><th>{4}</th><th>{5}</th><th>{6}</th>'.format( '&nbsp;', 'CE_D (_A)', 'CE_ID', 'LOCAL_TABLE', 'LOCAL_ID', 'LOCAL_OTH', 'LOCAL_OTH1' )
        retstring+= '</tr>\n'
        rowcounter = 0
        for ce in ces:
            rowcounter+= 1
            retstring+= '\t<tr>'
            retstring+= '<td>{0:d}</td><td>{1} ({2})</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td>'.format( rowcounter, ce.ce_d, ce.ce_d_a, ce.ce_id, ce.local_table, ce.local_id, ce.local_oth, ce.local_oth1 )
            retstring+= '</tr>\n'
            retstring+= self.makeEmptyRow(7)
            retstring+= self.makeEmptyRow(7)

        retstring+= '</table>\n'
        retstring+= '<br />\n'
        return retstring

    def makeEmptyRow(self, numcells):
        retstring = '\t<tr>'
        cellstring = '<td>&nbsp;</td>' * int( numcells )
        retstring+= cellstring
        retstring+= '</tr>\n'
        return retstring
