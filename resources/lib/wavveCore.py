# -*- coding: utf-8 -*-
__author__ = "NightRain"
__email__ = "kym1088@naver.com"
if 64 - 64: i11iIiiIii
import urllib
import urllib2
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import cookielib
import re
import json
import sys
import urlparse
if 73 - 73: II111iiii
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
if 68 - 68: Ii1I / O0
if 46 - 46: O0 * II111iiii / IiII * Oo0Ooo * iII111i . I11i
if 62 - 62: i11iIiiIii - II111iiii % I1Ii111 - iIii1I11I1II1 . I1ii11iIi11i . II111iiii
if 61 - 61: oO0o / OoOoOO00 / iII111i * OoO0O00 . II111iiii
if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + IiII . I1Ii111
if 55 - 55: iIii1I11I1II1 - I1IiiI . Ii1I * IiII * i1IIi / iIii1I11I1II1
if 79 - 79: oO0o + I1Ii111 . ooOoO0o * IiII % I11i . I1IiiI
if 94 - 94: iII111i * Ii1I / IiII . i1IIi * iII111i
if 47 - 47: i1IIi % i11iIiiIii
if 20 - 20: ooOoO0o * II111iiii
oO0o0o0ooO0oO = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
if 52 - 52: II111iiii - i11iIiiIii % I1Ii111
if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
class iIiiI1 ( object ) :
 def __init__ ( self ) :
  if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
  self . MyCookie = cookielib . LWPCookieJar ( )
  if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
  self . Opener = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( self . MyCookie ) )
  self . Opener . addheaders = [ ( 'User-Agent' , oO0o0o0ooO0oO ) ]
  if 3 - 3: iII111i + O0
  urllib2 . install_opener ( self . Opener )
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
  if 78 - 78: OoO0O00
 def Request ( self , url , postdata = None ) :
  if postdata :
   Iii1I111 = self . Opener . open ( url , postdata )
  else :
   Iii1I111 = self . Opener . open ( url )
   if 60 - 60: oO0o * o0oOOo0O0Ooo % o0oOOo0O0Ooo % I11i * II111iiii + i1IIi
  OOoooooO = Iii1I111 . read ( )
  Iii1I111 . close ( )
  if 14 - 14: I11i % O0
  return OOoooooO
  if 41 - 41: i1IIi + I1Ii111 + OOooOOo - IiII
  if 77 - 77: Oo0Ooo . IiII % ooOoO0o
  if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
class iIi ( object ) :
 def __init__ ( self ) :
  self . SESSION = iIiiI1 ( )
  self . API_DOMAIN = 'https://apis.pooq.co.kr'
  self . APIKEY = 'E5F3E0D30947AA5440556471321BB6D9'
  self . CREDENTIAL = 'none'
  self . DEVICE = 'pc'
  self . DRM = 'wm'
  self . PARTNER = 'pooq'
  self . POOQZONE = 'none'
  self . REGION = 'kor'
  self . TARGETAGE = 'auto'
  self . CREDENTIAL = 'none'
  self . HTTPTAG = 'https://'
  self . LIST_LIMIT = 20
  self . EP_LIMIT = 10
  self . MV_LIMIT = 12
  self . guid = 'none'
  self . guidtimestamp = 'none'
  if 40 - 40: oO0o . OoOoOO00 . Oo0Ooo . i1IIi
 def SaveCredential ( self , credential ) :
  self . CREDENTIAL = credential
  if 33 - 33: Ii1I + II111iiii % i11iIiiIii . ooOoO0o - I1IiiI
 def LoadCredential ( self ) :
  return self . CREDENTIAL
  if 66 - 66: Ii1I - OoooooooOO * OoooooooOO . OOooOOo . I1ii11iIi11i
 def GetDefaultParams ( self ) :
  IiI1i11iii1 = { 'apikey' : self . APIKEY ,
 'credential' : self . CREDENTIAL ,
 'device' : self . DEVICE ,
 'drm' : self . DRM ,
 'partner' : self . PARTNER ,
 'pooqzone' : self . POOQZONE ,
 'region' : self . REGION ,
 'targetage' : self . TARGETAGE
 }
  return IiI1i11iii1
  if 96 - 96: O0 % oO0o % iIii1I11I1II1
 def makeurl ( self , domain , path , query = None ) :
  Oo00OOOOO = ''
  if domain :
   if re . search ( r'http[s]*://' , domain ) :
    Oo00OOOOO += domain
   else :
    Oo00OOOOO += 'http://%s' % domain
   if path :
    Oo00OOOOO += path
    if query : Oo00OOOOO += '?%s' % query
  return Oo00OOOOO
  if 85 - 85: ooOoO0o . iII111i - OoO0O00 % ooOoO0o % II111iiii
 def MakeServiceUrl ( self , path , params ) :
  if 81 - 81: OoO0O00 + II111iiii % iII111i * O0
  Oo00OOOOO = self . makeurl ( self . API_DOMAIN , path , urllib . urlencode ( params ) )
  return Oo00OOOOO
  if 89 - 89: oO0o + Oo0Ooo
 def GetGUID ( self , guid_str = 'POOQ' , guidType = 1 ) :
  if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
  def III1ii1iII ( media ) :
   from datetime import datetime
   oo0oooooO0 = datetime . now ( ) . strftime ( '%Y%m%d%H%M%S' )
   i11Iiii = iI ( 5 )
   I1i1I1II = i11Iiii + media + oo0oooooO0
   return I1i1I1II
   if 45 - 45: I1Ii111 . OoOoOO00
  def iI ( num ) :
   from random import randint
   oO = ""
   for ii1i1I1i in range ( 0 , num ) :
    o00oOO0 = str ( randint ( 1 , 5 ) )
    oO += o00oOO0
   return oO
   if 95 - 95: OOooOOo / OoooooooOO
  I1i1I1II = III1ii1iII ( guid_str )
  if 18 - 18: i11iIiiIii
  Ii11I = self . GetHash ( I1i1I1II )
  if guidType == 2 :
   Ii11I = '%s-%s-%s-%s-%s' % ( Ii11I [ : 8 ] , Ii11I [ 8 : 12 ] , Ii11I [ 12 : 16 ] , Ii11I [ 16 : 20 ] , Ii11I [ 20 : ] )
   if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
  return Ii11I
  if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
 def GetHash ( self , hash_str ) :
  import hashlib
  iii11 = hashlib . md5 ( )
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
  iii11 . update ( hash_str )
  return str ( iii11 . hexdigest ( ) )
  if 50 - 50: I1IiiI
 def CheckQuality ( self , sel_qt , qt_list ) :
  Ii1i11IIii1I = 0
  for OOOoO0O0o in qt_list :
   if sel_qt >= OOOoO0O0o : return OOOoO0O0o
   Ii1i11IIii1I = OOOoO0O0o
  return Ii1i11IIii1I
  if 55 - 55: OOooOOo + ooOoO0o . i1IIi - I1ii11iIi11i . O0 - ooOoO0o
  if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
 def GetCredential ( self , user_id , user_pw , user_pf ) :
  IiII1I11i1I1I = False
  try :
   oO0Oo = '/login'
   IiI1i11iii1 = self . GetDefaultParams ( )
   oOOoo0Oo = { 'id' : user_id
 , 'password' : user_pw
 , 'profile' : '0'
 , 'pushid' : ''
 , 'type' : 'general'
 }
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   if 78 - 78: I11i
   if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO , postdata = urllib . urlencode ( oOOoo0Oo ) )
   oO0OOoO0 = json . loads ( Iii1I111 )
   I111Ii111 = oO0OOoO0 [ 'credential' ]
   if 4 - 4: oO0o
   if 93 - 93: OoO0O00 % oO0o . OoO0O00 * I1Ii111 % Ii1I . II111iiii
   if user_pf != 0 :
    oOOoo0Oo = { 'id' : I111Ii111
 , 'password' : ''
 , 'profile' : str ( user_pf )
 , 'pushid' : ''
 , 'type' : 'credential'
 }
    if 38 - 38: o0oOOo0O0Ooo
    Iii1I111 = self . SESSION . Request ( Oo00OOOOO , postdata = urllib . urlencode ( oOOoo0Oo ) )
    oO0OOoO0 = json . loads ( Iii1I111 )
    I111Ii111 = oO0OOoO0 [ 'credential' ]
    if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
    if 26 - 26: iII111i
   if I111Ii111 : IiII1I11i1I1I = True
   if 91 - 91: OoO0O00 . I1ii11iIi11i + OoO0O00 - iII111i / OoooooooOO
   if 39 - 39: I1ii11iIi11i / ooOoO0o - II111iiii
  except Exception as OO00o :
   print ( OO00o )
   I111Ii111 = 'none'
   if 61 - 61: II111iiii * oO0o % Oo0Ooo
  self . SaveCredential ( I111Ii111 )
  return IiII1I11i1I1I
  if 64 - 64: I11i % iII111i - I1Ii111 - oO0o
 def GetIssue ( self ) :
  i1ii1iiI = False
  try :
   oO0Oo = '/guid/issue'
   IiI1i11iii1 = self . GetDefaultParams ( )
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   if 98 - 98: iII111i * iII111i / iII111i + I11i
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   if 34 - 34: ooOoO0o
   oO0OOoO0 = json . loads ( Iii1I111 )
   I1111I1iII11 = oO0OOoO0 [ 'guid' ]
   Oooo0O0oo00oO = oO0OOoO0 [ 'guidtimestamp' ]
   if I1111I1iII11 : i1ii1iiI = True
  except Exception as OO00o :
   print ( OO00o )
   I1111I1iII11 = 'none'
   Oooo0O0oo00oO = 'none'
   if 14 - 14: OoOoOO00 / IiII . OoOoOO00 . I11i % OoO0O00 * I11i
  self . guid = I1111I1iII11
  self . guidtimestamp = Oooo0O0oo00oO
  if 16 - 16: OoOoOO00 . ooOoO0o + i11iIiiIii
  return i1ii1iiI
  if 38 - 38: IiII * OOooOOo . o0oOOo0O0Ooo
 def GetGnList ( self , gn_str ) :
  ooo0OO = [ ]
  try :
   oO0Oo = '/cf/supermultisections/' + gn_str
   IiI1i11iii1 = self . GetDefaultParams ( )
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 21 - 21: I1IiiI * iIii1I11I1II1
   if not ( 'multisectionlist' in oO0OOoO0 ) : return None
   oooooOoo0ooo = oO0OOoO0 [ 'multisectionlist' ]
   if 6 - 6: I11i - Ii1I + iIii1I11I1II1 - I1Ii111 - i11iIiiIii
   if 79 - 79: OoOoOO00 - O0 * OoO0O00 + OoOoOO00 % O0 * O0
   for oOOo0 in oooooOoo0ooo :
    oo00O00oO = oOOo0 [ 'title' ]
    if len ( oo00O00oO ) == 0 : continue
    if 23 - 23: OoO0O00 + OoO0O00 . OOooOOo
    if re . search ( u'베너' , oo00O00oO ) : continue
    if 38 - 38: I1Ii111
    oo00O00oO = re . sub ( '\n|\!|\~|(@0@)|(@\^0@)' , '' , oo00O00oO )
    oo00O00oO = oo00O00oO . lstrip ( '#' )
    if 7 - 7: O0 . iII111i % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
    for I111IIIiIii in oOOo0 [ 'eventlist' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , I111IIIiIii ) :
      oO0000OOo00 = { 'title' : unicode ( oo00O00oO )
 , 'uicode' : re . sub ( r'uicode:' , '' , I111IIIiIii )
 }
      ooo0OO . append ( oO0000OOo00 )
      break
      if 27 - 27: I1IiiI % I1IiiI
  except Exception as OO00o :
   print ( OO00o )
   if 1 - 1: OoO0O00 - oO0o . I11i . OoO0O00 / Oo0Ooo + I11i
  return ooo0OO
  if 78 - 78: O0 . oO0o . II111iiii % OOooOOo
 def GetDeeplinkList ( self , gn_str , came_str , page_int ) :
  i1iIi = [ ]
  ooOOoooooo = II1I = 1
  O0i1II1Iiii1I11 = 'quick'
  IIII = iiIiI = ''
  o00oooO0Oo = False
  if 78 - 78: Ii1I % I1Ii111 + I1ii11iIi11i
  try :
   if 64 - 64: oO0o * O0 . I1IiiI + II111iiii
   oO0Oo = '/cf/deeplink/' + gn_str
   IiI1i11iii1 = self . GetDefaultParams ( )
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 6 - 6: OoOoOO00 / iII111i . IiII . IiII
   if not ( 'url' in oO0OOoO0 ) : return None
   OO00O0O = oO0OOoO0 [ 'url' ]
   if 33 - 33: O0 . IiII . I1IiiI
   if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
   if 29 - 29: I1ii11iIi11i + oO0o % O0
   oO0Oo = urlparse . urlsplit ( OO00O0O ) . path
   I1I11 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( OO00O0O ) . query ) )
   I1I11 [ 'came' ] = came_str
   I1I11 [ 'limit' ] = str ( self . LIST_LIMIT )
   if 'contenttype' in I1I11 : O0i1II1Iiii1I11 = I1I11 [ 'contenttype' ]
   if 34 - 34: I1IiiI . OOooOOo * I1ii11iIi11i + I1Ii111
   if page_int != 1 :
    I1I11 [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
    I1I11 [ 'page' ] = str ( page_int )
    if 31 - 31: iII111i % iII111i % I11i
   Oo00OOOOO = self . HTTPTAG + oO0Oo + '?' + urllib . urlencode ( I1I11 ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   if 69 - 69: OoO0O00 - Oo0Ooo + i1IIi / I1Ii111
   if 49 - 49: O0 . iII111i
   if 11 - 11: IiII * I1IiiI . iIii1I11I1II1 % OoooooooOO + iII111i
   if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
   if 54 - 54: OoOoOO00 % iII111i
   if 37 - 37: OoOoOO00 * Oo0Ooo / ooOoO0o - iII111i % II111iiii . oO0o
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 88 - 88: iII111i . II111iiii * II111iiii % I1Ii111
   if not ( 'cell_toplist' in oO0OOoO0 ) : return None
   if not ( 'celllist' in oO0OOoO0 [ 'cell_toplist' ] ) : return None
   iiIIiiIi1Ii11 = oO0OOoO0 [ 'cell_toplist' ] [ 'celllist' ]
   if 65 - 65: II111iiii . OOooOOo % I11i . i11iIiiIii + O0
   if 26 - 26: I11i - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
   for oOOo0 in iiIIiiIi1Ii11 :
    OO = iIiIIi1 = I1IIII1i = ''
    if 2 - 2: I11i + Ii1I - I1IiiI % o0oOOo0O0Ooo . iII111i
    OO = oOOo0 . get ( 'title_list' ) [ 0 ] . get ( 'text' )
    if ( len ( oOOo0 . get ( 'title_list' ) ) > 1 ) :
     if ( oOOo0 . get ( 'title_list' ) [ 1 ] . get ( 'text' ) . startswith ( '@' ) ) :
      for I1I1i1I in oOOo0 . get ( 'bottom_taglist' ) :
       if I1I1i1I == 'playy' or I1I1i1I == 'won' : iIiIIi1 = I1I1i1I
     else :
      iIiIIi1 = oOOo0 . get ( 'title_list' ) [ 1 ] . get ( 'text' )
      iIiIIi1 = re . sub ( r'(\$O\$)|(\&[a-z]{2}\;)' , '' , iIiIIi1 )
    if ( oOOo0 . get ( 'thumbnail' ) != '' ) : I1IIII1i = 'https://%s' % oOOo0 . get ( 'thumbnail' )
    if 30 - 30: OoooooooOO
    I1Ii1iI1 = oOOo0 [ 'event_list' ] [ 1 ] . get ( 'url' )
    oO0 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( I1Ii1iI1 ) . query ) )
    if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
    if re . search ( u'programid=\&' , I1Ii1iI1 ) and ( 'contentid' in oO0 ) :
     IIII = oO0 [ 'contentid' ]
     iiIiI = 'direct'
    elif ( 'contentid' in oO0 ) :
     IIII = oO0 [ 'contentid' ]
     iiIiI = 'contentid'
    elif ( 'programid' in oO0 ) :
     IIII = oO0 [ 'programid' ]
     iiIiI = 'programid'
    elif ( 'channelid' in oO0 ) :
     IIII = oO0 [ 'channelid' ]
     iiIiI = 'channelid'
    elif ( 'movieid' in oO0 ) :
     IIII = oO0 [ 'movieid' ]
     iiIiI = 'movieid'
     if O0i1II1Iiii1I11 == 'x' : O0i1II1Iiii1I11 = 'movie'
    else :
     IIII = '-'
     iiIiI = '-'
     if 55 - 55: OOooOOo . I1IiiI
    oO0000OOo00 = { 'title' : unicode ( OO )
 , 'subtitle' : unicode ( iIiIIi1 )
 , 'thumbnail' : I1IIII1i
 , 'uicode' : O0i1II1Iiii1I11
 , 'contentid' : IIII
 , 'contentidType' : iiIiI
 , 'viewage' : oOOo0 . get ( 'age' )
 }
    i1iIi . append ( oO0000OOo00 )
    if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
   ooOOoooooo = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'pagecount' ] )
   if oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] : II1I = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] )
   else : II1I = self . LIST_LIMIT
   if 100 - 100: I1Ii111 * O0
   if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
   o00oooO0Oo = ooOOoooooo > II1I
   if 79 - 79: O0
   if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
  except Exception as OO00o :
   print ( OO00o )
   if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  return ( i1iIi , o00oooO0Oo )
  if 57 - 57: OoO0O00 / ooOoO0o
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
 def GetEpisodeList ( self , contentid , contenttype , contentidType , page_int ) :
  I111I1Iiii1i = [ ]
  ooOOoooooo = II1I = 1
  o00oooO0Oo = False
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
   if contentidType == 'contentid' :
    oO0Oo = '/cf/vod/contents/' + contentid
    if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
    Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
    Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
    oO0OOoO0 = json . loads ( Iii1I111 )
    if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
    if not ( 'programid' in oO0OOoO0 ) : return None
    Oo = oO0OOoO0 [ 'programid' ]
    if 65 - 65: Ii1I - oO0o + oO0o + II111iiii
   else :
    Oo = contentid
    if 96 - 96: OOooOOo % O0 / O0
    if 44 - 44: oO0o / I11i / I11i
    if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
   oO0Oo = '/vod/programs-contents/' + Oo
   if 25 - 25: I1IiiI . I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / I1Ii111
   I1I11 = { 'limit' : self . EP_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . EP_LIMIT )
 , 'orderby' : 'new'
 }
   if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1I11 ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 73 - 73: OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
   if not ( 'list' in oO0OOoO0 ) : return None
   O0O = oO0OOoO0 [ 'list' ]
   if 80 - 80: Ii1I * o0oOOo0O0Ooo / o0oOOo0O0Ooo
   if 5 - 5: I1IiiI
   for oOOo0 in O0O :
    iIiIi11iI = oOOo0 . get ( 'programtitle' )
    Oo0O00O000 = '%s회, %s(%s)' % ( oOOo0 . get ( 'episodenumber' ) , oOOo0 . get ( 'releasedate' ) , oOOo0 . get ( 'releaseweekday' ) )
    if ( oOOo0 . get ( 'image' ) != '' ) : i11I1IiII1i1i = 'https://%s' % oOOo0 . get ( 'image' )
    if 95 - 95: i11iIiiIii
    iI1111iiii = unicode ( oOOo0 . get ( 'synopsis' ) )
    iI1111iiii = re . sub ( u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)' , '' , iI1111iiii )
    if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
    OooOo0ooo = { 'title' : unicode ( iIiIi11iI )
 , 'subtitle' : unicode ( Oo0O00O000 )
 , 'thumbnail' : i11I1IiII1i1i
 , 'uicode' : contenttype
 , 'contentid' : oOOo0 . get ( 'contentid' )
 , 'programid' : oOOo0 . get ( 'programid' )
 , 'synopsis' : iI1111iiii
 , 'viewage' : oOOo0 . get ( 'targetage' )
 }
    I111I1Iiii1i . append ( OooOo0ooo )
    if 71 - 71: I1Ii111 + Ii1I
   ooOOoooooo = int ( oO0OOoO0 [ 'pagecount' ] )
   if oO0OOoO0 [ 'count' ] : II1I = int ( oO0OOoO0 [ 'count' ] )
   else : II1I = self . EP_LIMIT
   if 28 - 28: OOooOOo
   o00oooO0Oo = ooOOoooooo > II1I
   if 38 - 38: ooOoO0o % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
  except Exception as OO00o :
   print ( OO00o )
   if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
  return ( I111I1Iiii1i , o00oooO0Oo )
  if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
 def GetMyviewList ( self , contenttype , page_int ) :
  I11I = [ ]
  ooOOoooooo = II1I = 1
  o00oooO0Oo = False
  if 50 - 50: I1Ii111 * i11iIiiIii * iIii1I11I1II1 - II111iiii * o0oOOo0O0Ooo * OoOoOO00
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 94 - 94: OoooooooOO + OoooooooOO . II111iiii + I11i / I1ii11iIi11i % Ii1I
   oO0Oo = '/myview/contents'
   if 18 - 18: iII111i * O0 - OoooooooOO % I1IiiI . II111iiii / i1IIi
   I1I11 = { 'contenttype' : contenttype
 , 'limit' : self . MV_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . MV_LIMIT )
 , 'orderby' : 'new'
 }
   if 76 - 76: I11i / OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1I11 ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 71 - 71: I1Ii111 . II111iiii
   if not ( 'list' in oO0OOoO0 [ 0 ] ) : return None
   oo0 = oO0OOoO0 [ 0 ] [ 'list' ]
   if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
   for oOOo0 in oo0 :
    if 25 - 25: O0 * I11i + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
    if contenttype == 'vod' :
     iIiIi11iI = oOOo0 . get ( 'programtitle' )
     Oo0O00O000 = '%s회, %s' % ( oOOo0 . get ( 'episodenumber' ) , oOOo0 . get ( 'releasedate' ) )
     IIII = oOOo0 . get ( 'contentid' )
     Oo = oOOo0 . get ( 'programid' )
     if 58 - 58: I1IiiI
    else :
     iIiIi11iI = oOOo0 . get ( 'title' )
     Oo0O00O000 = '%s' % ( oOOo0 . get ( 'releasedate' ) )
     IIII = Oo = oOOo0 . get ( 'movieid' )
     if 53 - 53: i1IIi
    if ( oOOo0 . get ( 'image' ) != '' ) : i11I1IiII1i1i = 'https://%s' % oOOo0 . get ( 'image' )
    if 59 - 59: o0oOOo0O0Ooo
    oOoO00O0 = { 'title' : unicode ( iIiIi11iI )
 , 'subtitle' : unicode ( Oo0O00O000 )
 , 'thumbnail' : i11I1IiII1i1i
 , 'uicode' : contenttype
 , 'contentid' : IIII
 , 'programid' : Oo
 , 'viewage' : oOOo0 . get ( 'targetage' )
 }
    if 75 - 75: I1IiiI . ooOoO0o . O0 * I1Ii111
    I11I . append ( oOoO00O0 )
    if 4 - 4: Ii1I % oO0o * OoO0O00
    if 100 - 100: I1Ii111 * OOooOOo + OOooOOo
   ooOOoooooo = int ( oO0OOoO0 [ 0 ] [ 'pagecount' ] )
   if oO0OOoO0 [ 0 ] [ 'count' ] : II1I = int ( oO0OOoO0 [ 0 ] [ 'count' ] )
   else : II1I = self . MV_LIMIT
   if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
   o00oooO0Oo = ooOOoooooo > II1I
   if 3 - 3: o0oOOo0O0Ooo % o0oOOo0O0Ooo
  except Exception as OO00o :
   print ( OO00o )
   if 83 - 83: II111iiii + I1Ii111
  return I11I , o00oooO0Oo
  if 73 - 73: iII111i
  if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . i11iIiiIii % I11i
 def GetSearchList ( self , search_key , genre , page_int , exclusion21 = False ) :
  i1iI = [ ]
  ooOOoooooo = II1I = 1
  o00oooO0Oo = False
  if 29 - 29: I1IiiI % OOooOOo - I1IiiI / OOooOOo . i1IIi
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 31 - 31: I1Ii111
   oO0Oo = '/cf/search/list.js'
   if 88 - 88: OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % iIii1I11I1II1 + Oo0Ooo
   I1I11 = { 'type' : 'program' if genre == 'vod' else 'movie'
 , 'keyword' : search_key
 , 'offset' : str ( ( page_int - 1 ) * self . LIST_LIMIT )
 , 'limit' : self . LIST_LIMIT
   , 'orderby' : 'score'
 , 'isplayymovie' : 'y'
 }
   if 76 - 76: I1IiiI * iII111i % I1Ii111
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1I11 ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
   if not ( 'celllist' in oO0OOoO0 [ 'cell_toplist' ] ) : return i1iI , o00oooO0Oo
   I1 = oO0OOoO0 [ 'cell_toplist' ] [ 'celllist' ]
   if 97 - 97: ooOoO0o
   if 48 - 48: i1IIi - I1Ii111
   for oOOo0 in I1 :
    if 56 - 56: o0oOOo0O0Ooo + II111iiii + OoOoOO00 - ooOoO0o . OoOoOO00
    iIiIi11iI = oOOo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( oOOo0 . get ( 'thumbnail' ) != '' ) : i11I1IiII1i1i = 'https://%s' % oOOo0 . get ( 'thumbnail' )
    if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
    for I111IIIiIii in oOOo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , I111IIIiIii ) :
      if genre == 'vod' :
       IIII = ''
       Oo = re . sub ( r'uicode:' , '' , I111IIIiIii )
      else :
       IIII = re . sub ( r'uicode:' , '' , I111IIIiIii )
       Oo = ''
       if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
      oOoO00O0 = { 'title' : unicode ( iIiIi11iI )
 , 'thumbnail' : i11I1IiII1i1i
 , 'uicode' : genre
 , 'contentid' : IIII
 , 'programid' : Oo
 , 'viewage' : oOOo0 . get ( 'age' )
 }
      if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
    if exclusion21 == False or oOOo0 . get ( 'age' ) != '21' :
     i1iI . append ( oOoO00O0 )
     if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
     if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
   ooOOoooooo = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'pagecount' ] )
   if oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] : II1I = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] )
   else : II1I = self . LIST_LIMIT
   if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
   o00oooO0Oo = ooOOoooooo > II1I
   if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
  except Exception as OO00o :
   print ( OO00o )
   if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
  return i1iI , o00oooO0Oo
  if 79 - 79: O0 * i11iIiiIii - IiII / IiII
  if 48 - 48: O0
 def GetGenreGroup ( self , maintype , subtype , exclusion21 = False ) :
  Oo0o0O00 = [ ]
  if 40 - 40: OoooooooOO
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
   oO0Oo = '/cf/filters'
   if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
   I1I11 = { 'type' : maintype }
   if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1I11 ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
   if not ( maintype in oO0OOoO0 ) : return None
   iIiIiIiI = oO0OOoO0 [ maintype ]
   if 30 - 30: I1Ii111 . ooOoO0o * I1ii11iIi11i
   if subtype == '-' :
    if 17 - 17: I1IiiI . O0 + OoO0O00
    for oOOo0 in iIiIiIiI :
     ii = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( oOOo0 . get ( 'url' ) ) . query ) )
     if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
     oOoO00O0 = { 'title' : oOOo0 . get ( 'text' )
 , 'genre' : oOOo0 . get ( 'id' )
 , 'subgenre' : '-'
 , 'adult' : oOOo0 . get ( 'adult' )
 , 'broadcastid' : ii . get ( 'broadcastid' )
 , 'contenttype' : ii . get ( 'contenttype' )
 , 'uiparent' : ii . get ( 'uiparent' )
 , 'uirank' : ii . get ( 'uirank' )
 , 'uitype' : ii . get ( 'uitype' )
 }
     if exclusion21 == False or oOoO00O0 . get ( 'adult' ) == 'n' :
      Oo0o0O00 . append ( oOoO00O0 )
      if 81 - 81: iII111i + IiII
   else :
    for oOOo0 in iIiIiIiI :
     if oOOo0 . get ( 'id' ) == subtype :
      for o0oo0 in oOOo0 [ 'sublist' ] :
       ii = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( o0oo0 . get ( 'url' ) ) . query ) )
       if 97 - 97: OoOoOO00 % I1ii11iIi11i
       oOoO00O0 = { 'title' : o0oo0 . get ( 'text' )
 , 'genre' : subtype
 , 'subgenre' : o0oo0 . get ( 'id' )
 , 'adult' : o0oo0 . get ( 'adult' )
 , 'broadcastid' : ii . get ( 'broadcastid' )
 , 'contenttype' : ii . get ( 'contenttype' )
 , 'uiparent' : ii . get ( 'uiparent' )
 , 'uirank' : ii . get ( 'uirank' )
 , 'uitype' : ii . get ( 'uitype' )
 }
       Oo0o0O00 . append ( oOoO00O0 )
      break
      if 25 - 25: Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  except Exception as OO00o :
   print ( OO00o )
   if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
  return Oo0o0O00
  if 41 - 41: i1IIi - I11i - Ii1I
  if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
 def GetGenreGroup_sub ( self , in_params ) :
  Oo0o0O00 = [ ]
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 44 - 44: II111iiii
   oO0Oo = '/cf/vod/newcontents'
   if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
   I1I11 = { 'WeekDay' : 'all'
 , 'limit' : '20'
 , 'offset' : '0'
 , 'orderby' : 'new'
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if 35 - 35: iIii1I11I1II1
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1I11 ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
   if not ( 'filter_item_list' in oO0OOoO0 [ 'filter' ] [ 'filterlist' ] [ 1 ] ) : return None
   iIiIiIiI = oO0OOoO0 [ 'filter' ] [ 'filterlist' ] [ 1 ] [ 'filter_item_list' ]
   if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
   for oOOo0 in iIiIiIiI :
    oOoO00O0 = { 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )

 , 'adult' : oOOo0 . get ( 'adult' )
 , 'title' : oOOo0 . get ( 'title' )
 , 'subgenre' : oOOo0 . get ( 'api_parameters' ) [ oOOo0 . get ( 'api_parameters' ) . find ( '=' ) + 1 : ]
 }
    Oo0o0O00 . append ( oOoO00O0 )
    if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  except Exception as OO00o :
   print ( OO00o )
   if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
  return Oo0o0O00
  if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
  if 71 - 71: O0 - iIii1I11I1II1
 def GetGenreList ( self , genre , in_params , page_int ) :
  Oo0o0O00 = [ ]
  ooOOoooooo = II1I = 1
  o00oooO0Oo = False
  if 12 - 12: OOooOOo / o0oOOo0O0Ooo
  try :
   IiI1i11iii1 = self . GetDefaultParams ( )
   if 42 - 42: Oo0Ooo
   I1I11 = { 'WeekDay' : 'all'
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'orderby' : 'new'
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
   if genre == 'vodgenre' :
    oO0Oo = '/cf/vod/newcontents'
    if 46 - 46: Oo0Ooo
    if in_params . get ( 'subgenre' ) != '-' :
     I1I11 [ 'subgenre' ] = in_params . get ( 'subgenre' )
   else :
    oO0Oo = '/cf/movie/contents'
    if 1 - 1: iII111i
    I1I11 [ 'price' ] = 'all'
    I1I11 [ 'orderby' ] = 'paid'
    if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
    if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
   I1I11 [ 'limit' ] = self . LIST_LIMIT
   I1I11 [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
   I1I11 [ 'page' ] = str ( page_int )
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
   if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( I1I11 ) + '&' + urllib . urlencode ( IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
   if not ( 'celllist' in oO0OOoO0 [ 'cell_toplist' ] ) : return None
   iIiIiIiI = oO0OOoO0 [ 'cell_toplist' ] [ 'celllist' ]
   if 17 - 17: i1IIi
   if 21 - 21: Oo0Ooo
   for oOOo0 in iIiIiIiI :
    iIiIi11iI = i11I1IiII1i1i = ''
    if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
    iIiIi11iI = oOOo0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
    if ( oOOo0 . get ( 'thumbnail' ) != '' ) : i11I1IiII1i1i = 'https://%s' % oOOo0 . get ( 'thumbnail' )
    if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
    for I111IIIiIii in oOOo0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , I111IIIiIii ) :
      oOoO00O0 = { 'title' : unicode ( iIiIi11iI )
 , 'uicode' : re . sub ( r'uicode:' , '' , I111IIIiIii )
 , 'thumbnail' : i11I1IiII1i1i
 , 'viewage' : oOOo0 . get ( 'age' )
 }
      if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
    Oo0o0O00 . append ( oOoO00O0 )
    if 54 - 54: i1IIi + II111iiii
    if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
   ooOOoooooo = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'pagecount' ] )
   if oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] : II1I = int ( oO0OOoO0 [ 'cell_toplist' ] [ 'count' ] )
   else : II1I = self . LIST_LIMIT
   if 5 - 5: Ii1I
   o00oooO0Oo = ooOOoooooo > II1I
   if 46 - 46: IiII
  except Exception as OO00o :
   print ( OO00o )
   if 45 - 45: ooOoO0o
  return Oo0o0O00 , o00oooO0Oo
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
 def GetStreamingURL ( self , contentid , contenttype , quality_int ) :
  i1iI1 = ii1 = I1IiiI1ii1i = O0o = ''
  oO0OoO00o = [ ]
  if 11 - 11: Oo0Ooo - I1IiiI * II111iiii . I1ii11iIi11i . oO0o
  try :
   if 61 - 61: iII111i % I1IiiI - o0oOOo0O0Ooo - II111iiii % O0
   if contenttype == 'channel' :
    oO0Oo = '/live/channels/' + contentid
    OoOOO00 = 'live'
   elif contenttype == 'movie' :
    oO0Oo = '/cf/movie/contents/' + contentid
    OoOOO00 = 'movie'
   else :
    oO0Oo = '/cf/vod/contents/' + contentid
    OoOOO00 = 'vod'
    if 94 - 94: IiII
   IiI1i11iii1 = self . GetDefaultParams ( )
   Oo00OOOOO = self . MakeServiceUrl ( oO0Oo , IiI1i11iii1 )
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 57 - 57: Ii1I % Ii1I * i11iIiiIii
   iiOOO0oOOoo = oO0OOoO0 [ 'qualities' ] [ 'list' ]
   if iiOOO0oOOoo == None : return None
   if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
   Oo000ooOOO = 'hls'
   if 'drms' in oO0OOoO0 :
    if oO0OOoO0 [ 'drms' ] :
     Oo000ooOOO = 'dash'
     if 31 - 31: iIii1I11I1II1 % I11i % ooOoO0o . Ii1I - I11i
   print ( Oo000ooOOO )
   if 17 - 17: Ii1I
   if 'type' in oO0OOoO0 :
    if oO0OOoO0 [ 'type' ] == 'onair' :
     OoOOO00 = 'onairvod'
     if 27 - 27: i11iIiiIii % II111iiii % I11i . O0 - Oo0Ooo + OoOoOO00
     if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
   for ooOOo00O00Oo in iiOOO0oOOoo :
    oO0OoO00o . append ( int ( ooOOo00O00Oo . get ( 'id' ) . rstrip ( 'p' ) ) )
    if 42 - 42: O0 / o0oOOo0O0Ooo + OoooooooOO * ooOoO0o % ooOoO0o
    if 7 - 7: iII111i / I1ii11iIi11i / i11iIiiIii
    if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
   OoOo = self . CheckQuality ( quality_int , oO0OoO00o )
   oO0Oo = '/streaming'
   I1I11 = { 'contentid' : contentid
 , 'contenttype' : OoOOO00
 , 'action' : Oo000ooOOO
 , 'quality' : str ( OoOo ) + 'p'
 , 'deviceModelId' : 'Windows 10'
 , 'guid' : self . GetGUID ( guidType = 2 )
 , 'lastplayid' : self . guid
 , 'authtype' : 'cookie'
 , 'isabr' : 'y'
 , 'ishevc' : 'n'
 }
   if 35 - 35: ooOoO0o * OOooOOo . I11i * o0oOOo0O0Ooo . OoOoOO00 / O0
   Oo00OOOOO = self . API_DOMAIN + oO0Oo + '?' + urllib . urlencode ( IiI1i11iii1 ) + '&' + urllib . urlencode ( I1I11 )
   if 100 - 100: I1Ii111 . o0oOOo0O0Ooo * Oo0Ooo % O0 * O0
   Iii1I111 = self . SESSION . Request ( Oo00OOOOO )
   oO0OOoO0 = json . loads ( Iii1I111 )
   if 14 - 14: I1ii11iIi11i . ooOoO0o + II111iiii / iII111i / I11i
   i1iI1 = oO0OOoO0 [ 'playurl' ]
   if i1iI1 == None : return None
   ii1 = oO0OOoO0 [ 'awscookie' ]
   I1IiiI1ii1i = oO0OOoO0 [ 'drm' ]
   if 'previewmsg' in oO0OOoO0 [ 'preview' ] : O0o = oO0OOoO0 [ 'preview' ] [ 'previewmsg' ]
   if 74 - 74: O0 / i1IIi
  except Exception as OO00o :
   print ( OO00o )
   if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
  i1iI1 = i1iI1 . replace ( 'pooq.co.kr' , 'wavve.com' )
  if 31 - 31: OoooooooOO . OOooOOo
  return ( i1iI1 , ii1 , I1IiiI1ii1i , O0o )
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
  if 100 - 100: OoO0O00
  if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
  if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
  if 45 - 45: I1Ii111
  if 83 - 83: OoOoOO00 . OoooooooOO
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
