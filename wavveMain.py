# -*- coding: utf-8 -*-
__author__ = "NightRain"
__email__ = "kym1088@naver.com"
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
import os
import xbmcplugin , xbmcgui , xbmcaddon
import sys
import urlparse
import inputstreamhelper
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
__addon__ = xbmcaddon . Addon ( )
__language__ = __addon__ . getLocalizedString
__profile__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
__version__ = __addon__ . getAddonInfo ( 'version' )
__addonid__ = __addon__ . getAddonInfo ( 'id' )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
__cwd__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'path' ) )
__lib__ = os . path . join ( __cwd__ , 'resources' , 'lib' )
__data__ = os . path . join ( __cwd__ , 'resources' , 'data' )
sys . path . append ( __lib__ )
sys . path . append ( __data__ )
if 94 - 94: i1IIi % Oo0Ooo
o0oO0 = [
 { 'title' : '홈' , 'uicode' : 'GN1' , 'came' : 'home' }
 , { 'title' : '방송' , 'uicode' : 'GN2' , 'came' : 'broadcast' }
 , { 'title' : 'LIVE' , 'uicode' : 'GN3' , 'came' : 'live' }
 , { 'title' : '영화' , 'uicode' : 'GN4' , 'came' : 'movie' }
 , { 'title' : '해외시리즈' , 'uicode' : 'GN12' , 'came' : 'global' }

, { 'title' : '분류별 탐색 --- 방송(VOD)' , 'uicode' : 'GENRE' , 'came' : 'vodgenre' }
 , { 'title' : '분류별 탐색 --- 영화(Movie)' , 'uicode' : 'GENRE' , 'came' : 'moviegenre' }

, { 'title' : 'Watched' , 'uicode' : 'WATCH' , 'came' : '-' }
 , { 'title' : '검색' , 'uicode' : 'SEARCH' , 'came' : '-' }
 ]
oo00 = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
if 88 - 88: iII111i . oO0o % ooOoO0o
from wavveCore import *
if 66 - 66: iII111i
if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
def ooO00oOoo ( sting ) :
 try :
  O0OOo = xbmcgui . Dialog ( )
  O0OOo . notification ( __name__ , sting )
 except :
  None
  if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . IiII / IiII % IiII
  if 22 - 22: Ii1I . IiII
  if 41 - 41: I1Ii111 . ooOoO0o * IiII % i11iIiiIii
def o000o0o00o0Oo ( string , isDebug = False ) :
 try :
  oo = string . encode ( 'utf-8' , 'ignore' )
 except :
  oo = 'addonException: addon_log'
 if isDebug : IiII1I1i1i1ii = xbmc . LOGDEBUG
 else : IiII1I1i1i1ii = xbmc . LOGNOTICE
 xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , oo ) , level = IiII1I1i1i1ii )
 if 44 - 44: oO0o / Oo0Ooo - II111iiii - i11iIiiIii % I1Ii111
 if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
 if 31 - 31: OoO0O00 + II111iiii
 if 13 - 13: OOooOOo * oO0o * I1IiiI
def oOOOO ( title ) :
 i11iiII = None
 I1iiiiI1iII = xbmc . Keyboard ( )
 I1iiiiI1iII . setHeading ( title )
 xbmc . sleep ( 1000 )
 I1iiiiI1iII . doModal ( )
 if ( I1iiiiI1iII . isConfirmed ( ) ) :
  i11iiII = I1iiiiI1iII . getText ( )
 return i11iiII
 if 20 - 20: i1IIi + i11iIiiIii - Ii1I % OoO0O00 . OoooooooOO
 if 96 - 96: i1IIi . OoOoOO00 * OOooOOo % ooOoO0o
 if 60 - 60: oO0o * o0oOOo0O0Ooo % o0oOOo0O0Ooo % I11i * II111iiii + i1IIi
 if 64 - 64: oO0o - O0 / II111iiii / o0oOOo0O0Ooo / iIii1I11I1II1
def IiIIIiI1I1 ( ) :
 OoO000 = __addon__ . getSetting ( 'id' )
 IIiiIiI1 = __addon__ . getSetting ( 'pw' )
 iiIiIIi = __addon__ . getSetting ( 'selected_profile' )
 return ( OoO000 , IIiiIiI1 , iiIiIIi )
 if 65 - 65: OoOoOO00
 if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
 if 84 - 84: i11iIiiIii . o0oOOo0O0Ooo
def o0O00oooo ( ) :
 O00o = __addon__ . getSetting ( 'exclusion19' )
 if O00o == 'false' :
  return False
 else :
  return True
  if 61 - 61: iII111i . iIii1I11I1II1 * I1IiiI . ooOoO0o % Oo0Ooo
  if 72 - 72: OOooOOo
  if 63 - 63: Ii1I
def O00 ( credential ) :
 iII11i = xbmcgui . Window ( 10000 )
 iII11i . setProperty ( 'WavveCredential' , credential )
 if 97 - 97: I11i % I11i + II111iiii * iII111i
def o0o00o0 ( ) :
 iII11i = xbmcgui . Window ( 10000 )
 return iII11i . getProperty ( 'WavveCredential' )
 if 25 - 25: Oo0Ooo - IiII . OoooooooOO
 if 22 - 22: IiII + II111iiii % I1Ii111 . I11i . OoOoOO00
 if 76 - 76: OoOoOO00 - O0 % OOooOOo / I1ii11iIi11i / OoOoOO00
def oo0oooooO0 ( ) :
 i11Iiii = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for iI in i11Iiii . keys ( ) :
  i11Iiii [ iI ] = i11Iiii [ iI ] [ 0 ]
 return i11Iiii
 if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
 if 95 - 95: OoO0O00 % oO0o . O0
 if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
def o00oOO0 ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 if 95 - 95: OOooOOo / OoooooooOO
 iIo00O = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
 if sublabel : Iii111II = '%s < %s >' % ( label , sublabel )
 else : Iii111II = label
 if not img : img = 'DefaultFolder.png'
 if 9 - 9: OoO0O00
 i11 = xbmcgui . ListItem ( Iii111II , thumbnailImage = img )
 if infoLabels : i11 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : i11 . setProperty ( 'IsPlayable' , 'true' )
 if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
 xbmcplugin . addDirectoryItem ( ii11i1 , iIo00O , i11 , isFolder )
 if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 if 42 - 42: Ii1I + oO0o
 if 76 - 76: I1Ii111 - OoO0O00
def oOooOOo00Oo0O ( ) :
 try :
  O00oO = [ 1080 , 720 , 480 , 360 ]
  if 39 - 39: IiII - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
  OoOOOOO = int ( __addon__ . getSetting ( 'selected_quality' ) )
  return O00oO [ OoOOOOO ]
 except :
  None
  if 33 - 33: I1ii11iIi11i % i1IIi
 return 1080
 if 78 - 78: I11i
 if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
 if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
 if 16 - 16: I1IiiI * oO0o % IiII
def Oo000o ( ) :
 ( I11IiI1I11i1i , iI1ii1Ii , oooo000 ) = IiIIIiI1I1 ( )
 if 16 - 16: I1ii11iIi11i + OoO0O00 - II111iiii
 if 85 - 85: OoOoOO00 + i1IIi
 if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
 if 75 - 75: oO0o
 if 50 - 50: Ii1I / Oo0Ooo - oO0o - I11i % iII111i - oO0o
 if not ( I11IiI1I11i1i and iI1ii1Ii ) :
  O0OOo = xbmcgui . Dialog ( )
  OOO0o = O0OOo . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if OOO0o == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 30 - 30: iIii1I11I1II1 / ooOoO0o - I1Ii111 - II111iiii % iII111i
   if 49 - 49: I1IiiI % ooOoO0o . ooOoO0o . I11i * ooOoO0o
 if not O0oOO0 . GetCredential ( I11IiI1I11i1i , iI1ii1Ii , oooo000 ) :
  ooO00oOoo ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  sys . exit ( )
  if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
  if 92 - 92: iII111i . I1Ii111
 for i1i in o0oO0 :
  Iii111II = i1i . get ( 'title' )
  if 50 - 50: IiII
  if i1i . get ( 'uicode' ) == 'GENRE' :
   i11I1iIiII = { 'mode' : 'GENRE'
 , 'uicode' : i1i . get ( 'came' )
   , 'genre' : '-'
 , 'subgenre' : '-'
   }
  elif i1i . get ( 'uicode' ) == 'WATCH' :
   i11I1iIiII = { 'mode' : 'WATCH'
 , 'genre' : '-'
 }
  elif i1i . get ( 'uicode' ) == 'SEARCH' :
   i11I1iIiII = { 'mode' : 'SEARCH'
 , 'genre' : '-'
 }
  else :
   i11I1iIiII = { 'mode' : 'GNB_LIST'
 , 'uicode' : i1i . get ( 'uicode' )
 , 'came' : i1i . get ( 'came' )
 }
   if 96 - 96: Oo0Ooo
  Ii1I1IIii1II = True
  if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
  if i1i . get ( 'uicode' ) == 'XXX' :
   i11I1iIiII [ 'mode' ] = 'XXX'
   Ii1I1IIii1II = False
   if 21 - 21: I1IiiI * iIii1I11I1II1
  o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = Ii1I1IIii1II , params = i11I1iIiII )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 )
 if 91 - 91: IiII
 if 15 - 15: II111iiii
 O00 ( O0oOO0 . LoadCredential ( ) )
 if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
 if 5 - 5: o0oOOo0O0Ooo * ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
 if 91 - 91: O0
def oOOo0 ( args ) :
 if 54 - 54: O0 - IiII % OOooOOo
 O0oOO0 . SaveCredential ( o0o00o0 ( ) )
 if 77 - 77: OoOoOO00 / I1IiiI / OoO0O00 + OoO0O00 . OOooOOo
 ii1ii11IIIiiI = O0oOO0 . GetGnList ( args . get ( 'uicode' ) )
 if 67 - 67: I11i * oO0o * I1ii11iIi11i + OOooOOo / i1IIi
 if 11 - 11: Ii1I + iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
 if 83 - 83: I11i / I1IiiI
 if 34 - 34: IiII
 for oOo in ii1ii11IIIiiI :
  Iii111II = oOo . get ( 'title' )
  i11I1iIiII = { 'mode' : 'GN_LIST' if oOo . get ( 'uicode' ) != 'CY1' else 'GN_MYVIEW'
  , 'uicode' : oOo . get ( 'uicode' )
 , 'came' : args . get ( 'came' )
 , 'page' : '1'
 }
  if 75 - 75: I1IiiI + Oo0Ooo
  o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
 if len ( ii1ii11IIIiiI ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 73 - 73: O0 - OoooooooOO . OOooOOo - OOooOOo / OoOoOO00
 if 45 - 45: iIii1I11I1II1 % OoO0O00
 if 29 - 29: OOooOOo + Oo0Ooo . i11iIiiIii - i1IIi / iIii1I11I1II1
 if 26 - 26: I11i . OoooooooOO
def I11i1ii1 ( args ) :
 Iii111II = 'VOD 시청내역'
 i11I1iIiII = { 'mode' : 'MYVIEW_LIST'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
 o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
 if 87 - 87: I11i - iIii1I11I1II1 + I1IiiI . iII111i
 Iii111II = '영화 시청내역'
 i11I1iIiII [ 'uicode' ] = 'movie'
 o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
 if 62 - 62: O0 * i1IIi * o0oOOo0O0Ooo - I1IiiI + I1IiiI
 xbmcplugin . endOfDirectory ( ii11i1 )
 if 34 - 34: iIii1I11I1II1 - o0oOOo0O0Ooo
 if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
 if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
 if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
def oo0o00O ( args ) :
 if 51 - 51: Ii1I - OoO0O00 * iII111i
 O0oOO0 . SaveCredential ( o0o00o0 ( ) )
 if 66 - 66: OoooooooOO + O0
 I1IiiIIIi = args . get ( 'uicode' )
 i1Iii1i1I = int ( args . get ( 'page' ) )
 OOoO00 , IiI111111IIII = O0oOO0 . GetMyviewList ( I1IiiIIIi , i1Iii1i1I )
 if 37 - 37: I1Ii111 / OoOoOO00
 for i1 in OOoO00 :
  Iii111II = i1 . get ( 'title' )
  I1iI1iIi111i = i1 . get ( 'subtitle' )
  iiIi1IIi1I = i1 . get ( 'thumbnail' )
  if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
  O0ooO0Oo00o = { }
  O0ooO0Oo00o [ 'plot' ] = Iii111II
  if 77 - 77: iIii1I11I1II1 * OoO0O00
  if I1IiiIIIi == 'vod' :
   i11I1iIiII = { 'mode' : 'DEEP_LIST'
 , 'contentid' : i1 . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : Iii111II
   , 'subtitle' : I1iI1iIi111i
   , 'thumbnail' : iiIi1IIi1I
   , 'viewage' : i1 . get ( 'viewage' )
 }
   Ii1I1IIii1II = True
   if 95 - 95: I1IiiI + i11iIiiIii
  else :
   i11I1iIiII = { 'mode' : 'MOVIE'
 , 'contentid' : i1 . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : Iii111II
   , 'subtitle' : I1iI1iIi111i
   , 'thumbnail' : iiIi1IIi1I
   , 'viewage' : i1 . get ( 'viewage' )
 }
   Ii1I1IIii1II = False
   if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
  if i1 . get ( 'viewage' ) == '21' : I1iI1iIi111i += ' (%s)' % ( i1 . get ( 'viewage' ) )
  if 80 - 80: II111iiii
  o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = iiIi1IIi1I , infoLabels = O0ooO0Oo00o , isFolder = Ii1I1IIii1II , params = i11I1iIiII )
  if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
 if IiI111111IIII :
  if 53 - 53: II111iiii
  i11I1iIiII [ 'mode' ] = 'MYVIEW_LIST'
  i11I1iIiII [ 'uicode' ] = I1IiiIIIi
  i11I1iIiII [ 'page' ] = str ( i1Iii1i1I + 1 )
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  I1iI1iIi111i = str ( i1Iii1i1I + 1 )
  o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
  if 31 - 31: OoO0O00
 if len ( OOoO00 ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
 if 25 - 25: OoO0O00
 if 62 - 62: OOooOOo + O0
 if 98 - 98: o0oOOo0O0Ooo
 if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
def OoO0o ( args ) :
 if 78 - 78: oO0o % O0 % Ii1I
 O0oOO0 . SaveCredential ( o0o00o0 ( ) )
 if 46 - 46: OoooooooOO . i11iIiiIii
 OOo0oO00ooO00 = args . get ( 'mode' )
 oOO0O00oO0Ooo = args . get ( 'uicode' )
 oO0Oo0O0o = args . get ( 'genre' )
 OO = args . get ( 'subgenre' )
 if 37 - 37: ooOoO0o % oO0o . i11iIiiIii % Ii1I . Oo0Ooo
 if oO0Oo0O0o == '-' :
  I11I1IIII = O0oOO0 . GetGenreGroup ( oOO0O00oO0Ooo , oO0Oo0O0o , exclusion21 = o0O00oooo ( ) )
 else :
  iIIIiiI1i1 = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 }
  I11I1IIII = O0oOO0 . GetGenreGroup_sub ( iIIIiiI1i1 )
  if 50 - 50: IiII
  if 46 - 46: O0 + iII111i % I1IiiI / o0oOOo0O0Ooo . IiII * I11i
 for OOooo0oOO0O in I11I1IIII :
  Iii111II = OOooo0oOO0O . get ( 'title' )
  if 62 - 62: I1IiiI
  i11I1iIiII = { 'mode' : OOo0oO00ooO00
 , 'uicode' : oOO0O00oO0Ooo
  , 'genre' : OOooo0oOO0O . get ( 'genre' )
 , 'subgenre' : OOooo0oOO0O . get ( 'subgenre' )
 , 'adult' : OOooo0oOO0O . get ( 'adult' )
 , 'page' : '1'
 , 'broadcastid' : OOooo0oOO0O . get ( 'broadcastid' )
 , 'contenttype' : OOooo0oOO0O . get ( 'contenttype' )
 , 'uiparent' : OOooo0oOO0O . get ( 'uiparent' )
 , 'uirank' : OOooo0oOO0O . get ( 'uirank' )
 , 'uitype' : OOooo0oOO0O . get ( 'uitype' )
 }
  if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  if oOO0O00oO0Ooo == 'moviegenre' or OOooo0oOO0O . get ( 'subgenre' ) != '-' :
   i11I1iIiII [ 'mode' ] = 'GENRE_LIST'
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  else :
   if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
   None
   if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
  if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
 if len ( I11I1IIII ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 63 - 63: OoOoOO00 * iII111i
 if 69 - 69: O0 . OoO0O00
 if 49 - 49: I1IiiI - I11i
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
def oooOo0OOOoo0 ( args ) :
 if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
 O0oOO0 . SaveCredential ( o0o00o0 ( ) )
 if 73 - 73: OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
 oOO0O00oO0Ooo = args . get ( 'uicode' )
 i1Iii1i1I = int ( args . get ( 'page' ) )
 if 99 - 99: ooOoO0o . Ii1I + I1Ii111 + OoooooooOO % o0oOOo0O0Ooo
 i11I1iIiII = { 'adult' : args . get ( 'adult' )
 , 'broadcastid' : args . get ( 'broadcastid' )
 , 'contenttype' : args . get ( 'contenttype' )
 , 'genre' : args . get ( 'genre' )
 , 'subgenre' : args . get ( 'subgenre' )
 , 'uiparent' : args . get ( 'uiparent' )
 , 'uirank' : args . get ( 'uirank' )
 , 'uitype' : args . get ( 'uitype' )
 }
 if args . get ( 'genre' ) == args . get ( 'subgenre' ) :
  i11I1iIiII [ 'subgenre' ] = 'all'
  if 51 - 51: iIii1I11I1II1
 I11I1IIII , IiI111111IIII = O0oOO0 . GetGenreList ( oOO0O00oO0Ooo , i11I1iIiII , i1Iii1i1I )
 if 34 - 34: oO0o + I1IiiI - oO0o
 if 17 - 17: II111iiii % iII111i + I11i - iII111i / OOooOOo + ooOoO0o
 if 59 - 59: OOooOOo % OoOoOO00 . Ii1I * I1ii11iIi11i % I11i
 for OOooo0oOO0O in I11I1IIII :
  Iii111II = OOooo0oOO0O . get ( 'title' )
  iiIi1IIi1I = OOooo0oOO0O . get ( 'thumbnail' )
  if 59 - 59: oO0o - iII111i
  O0ooO0Oo00o = { }
  O0ooO0Oo00o [ 'plot' ] = Iii111II
  if 15 - 15: I1Ii111 . i11iIiiIii . OoooooooOO / OoO0O00 % Ii1I
  if oOO0O00oO0Ooo == 'vodgenre' :
   OooooOOoo0 = { 'mode' : 'DEEP_LIST'
 , 'contentid' : OOooo0oOO0O . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : Iii111II
   , 'subtitle' : ''
   , 'thumbnail' : iiIi1IIi1I
   , 'viewage' : OOooo0oOO0O . get ( 'viewage' )
 }
   Ii1I1IIii1II = True
   if 35 - 35: I11i % OOooOOo - oO0o
  else :
   OooooOOoo0 = { 'mode' : 'MOVIE'
 , 'contentid' : OOooo0oOO0O . get ( 'uicode' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : Iii111II
   , 'subtitle' : ''
   , 'thumbnail' : iiIi1IIi1I
   , 'viewage' : OOooo0oOO0O . get ( 'viewage' )
 }
   if 20 - 20: i1IIi - ooOoO0o
   Ii1I1IIii1II = False
   if 30 - 30: I11i / I1IiiI
  if OooooOOoo0 . get ( 'viewage' ) == '21' : Iii111II += ' (%s)' % ( OooooOOoo0 . get ( 'viewage' ) )
  if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
  o00oOO0 ( Iii111II , sublabel = '' , img = iiIi1IIi1I , infoLabels = O0ooO0Oo00o , isFolder = Ii1I1IIii1II , params = OooooOOoo0 )
  if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
 if IiI111111IIII :
  if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
  i11I1iIiII [ 'mode' ] = 'GENRE_LIST'
  i11I1iIiII [ 'uicode' ] = oOO0O00oO0Ooo
  i11I1iIiII [ 'page' ] = str ( i1Iii1i1I + 1 )
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  I1iI1iIi111i = str ( i1Iii1i1I + 1 )
  o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
  if 72 - 72: Ii1I
 if len ( I11I1IIII ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
 if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
 if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
 if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
def i1I1i111Ii ( args ) :
 if 67 - 67: I1IiiI . i1IIi
 O0oOO0 . SaveCredential ( o0o00o0 ( ) )
 if 27 - 27: ooOoO0o % I1IiiI
 oOO0O00oO0Ooo = args . get ( 'uicode' )
 o0oooOO00 = args . get ( 'came' )
 i1Iii1i1I = int ( args . get ( 'page' ) )
 if 32 - 32: I1Ii111
 if 30 - 30: iIii1I11I1II1 / I11i . OoO0O00 - o0oOOo0O0Ooo
 if 48 - 48: i1IIi - Ii1I / O0 * OoO0O00
 ooOOOooO , IiI111111IIII = O0oOO0 . GetDeeplinkList ( oOO0O00oO0Ooo , o0oooOO00 , i1Iii1i1I )
 if 12 - 12: O0 - o0oOOo0O0Ooo
 for oOoO00O0 in ooOOOooO :
  Iii111II = oOoO00O0 . get ( 'title' )
  I1iI1iIi111i = oOoO00O0 . get ( 'subtitle' )
  iiIi1IIi1I = oOoO00O0 . get ( 'thumbnail' )
  OOIi1iI111II1I1 = oOoO00O0 . get ( 'uicode' )
  if 91 - 91: OOooOOo % OOooOOo - I1IiiI
  i11I1iIiII = { 'uicode' : OOIi1iI111II1I1
  , 'came' : o0oooOO00
 , 'contentid' : oOoO00O0 . get ( 'contentid' )
 , 'contentidType' : oOoO00O0 . get ( 'contentidType' )
 , 'page' : '1'
 , 'title' : Iii111II
  , 'subtitle' : I1iI1iIi111i
  , 'thumbnail' : iiIi1IIi1I
  , 'viewage' : oOoO00O0 . get ( 'viewage' )
 }
  if 18 - 18: I11i - i11iIiiIii / II111iiii . OOooOOo
  if OOIi1iI111II1I1 == 'channel' :
   i11I1iIiII [ 'mode' ] = 'LIVE'
  elif OOIi1iI111II1I1 == 'movie' :
   i11I1iIiII [ 'mode' ] = 'MOVIE'
  else :
   i11I1iIiII [ 'mode' ] = 'DEEP_LIST'
   if 55 - 55: i1IIi % II111iiii + I11i * iIii1I11I1II1
   if 81 - 81: IiII % i1IIi . iIii1I11I1II1
  O0ooO0Oo00o = { }
  O0ooO0Oo00o [ 'plot' ] = '%s\n%s' % ( Iii111II , I1iI1iIi111i )
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
  if oOoO00O0 . get ( 'viewage' ) == '21' : I1iI1iIi111i += ' (%s)' % ( oOoO00O0 . get ( 'viewage' ) )
  if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
  if OOIi1iI111II1I1 in [ 'channel' , 'movie' ] :
   Ii1I1IIii1II = False
  elif i11I1iIiII [ 'contentidType' ] == 'direct' :
   Ii1I1IIii1II = False
   i11I1iIiII [ 'mode' ] = 'VOD'
  else :
   Ii1I1IIii1II = True
   if 31 - 31: OOooOOo
   if 23 - 23: I1Ii111 . IiII
  o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = iiIi1IIi1I , infoLabels = O0ooO0Oo00o , isFolder = Ii1I1IIii1II , params = i11I1iIiII )
  if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
 if IiI111111IIII :
  if 42 - 42: Oo0Ooo
  i11I1iIiII [ 'mode' ] = 'GN_LIST'
  i11I1iIiII [ 'uicode' ] = oOO0O00oO0Ooo
  i11I1iIiII [ 'page' ] = str ( i1Iii1i1I + 1 )
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  I1iI1iIi111i = str ( i1Iii1i1I + 1 )
  o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
  if 76 - 76: I1IiiI * iII111i % I1Ii111
 if len ( ooOOOooO ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
 if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
 if 34 - 34: I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / I1Ii111 / I1ii11iIi11i
def oOoOOo0O ( args ) :
 if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
 O0oOO0 . SaveCredential ( o0o00o0 ( ) )
 if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
 oOOoo0000O0o0 = args . get ( 'contentid' )
 II1III = args . get ( 'contentidType' )
 I1IiiIIIi = args . get ( 'uicode' )
 if 1 - 1: o0oOOo0O0Ooo . ooOoO0o / iII111i . OOooOOo
 i1Iii1i1I = int ( args . get ( 'page' ) )
 if 81 - 81: O0 . OoooooooOO . iII111i - Oo0Ooo / OoO0O00 + I1ii11iIi11i
 o0O00oOOoo , IiI111111IIII = O0oOO0 . GetEpisodeList ( oOOoo0000O0o0 , I1IiiIIIi , II1III , i1Iii1i1I )
 if 18 - 18: Ii1I + IiII - O0
 for o00O in o0O00oOOoo :
  Iii111II = o00O . get ( 'title' )
  I1iI1iIi111i = o00O . get ( 'subtitle' )
  iiIi1IIi1I = o00O . get ( 'thumbnail' )
  i11I1iIiII = { 'mode' : 'VOD'
 , 'uicode' : o00O . get ( 'uicode' )
  , 'contentid' : o00O . get ( 'contentid' )
 , 'programid' : o00O . get ( 'programid' )
 , 'title' : Iii111II
  , 'subtitle' : I1iI1iIi111i
  , 'thumbnail' : iiIi1IIi1I
  , 'viewage' : o00O . get ( 'viewage' )
 }
  if 5 - 5: I1Ii111
  if o00O . get ( 'viewage' ) == '21' : I1iI1iIi111i += ' (%s)' % ( o00O . get ( 'viewage' ) )
  if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
  ii1 = { }
  ii1 [ 'plot' ] = o00O . get ( 'synopsis' )
  if 39 - 39: Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * iII111i + I1IiiI
  if 77 - 77: Ii1I + II111iiii . OoOoOO00 * I1Ii111 + OOooOOo + OOooOOo
  o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = iiIi1IIi1I , infoLabels = ii1 , isFolder = False , params = i11I1iIiII )
  if 9 - 9: I11i % OoooooooOO . oO0o % I11i
 if IiI111111IIII :
  if 32 - 32: i11iIiiIii
  i11I1iIiII [ 'mode' ] = 'DEEP_LIST'
  i11I1iIiII [ 'uicode' ] = I1IiiIIIi
  i11I1iIiII [ 'contentid' ] = oOOoo0000O0o0
  i11I1iIiII [ 'contentidType' ] = II1III
  i11I1iIiII [ 'page' ] = str ( i1Iii1i1I + 1 )
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  I1iI1iIi111i = str ( i1Iii1i1I + 1 )
  o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
  if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
 if len ( o0O00oOOoo ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 41 - 41: Oo0Ooo
 if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
 if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
def ii ( args ) :
 if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
 O0oOO0 . SaveCredential ( o0o00o0 ( ) )
 if 81 - 81: iII111i + IiII
 oOOoo0000O0o0 = args . get ( 'contentid' )
 I1IiiIIIi = args . get ( 'uicode' )
 o0oo0 = oOooOOo00Oo0O ( )
 if 97 - 97: OoOoOO00 % I1ii11iIi11i
 o000o0o00o0Oo ( oOOoo0000O0o0 + ' - ' + I1IiiIIIi , False )
 iIiIII1I1I1 , i11IIIiI11 , III11I1 , IIi1IIIi = O0oOO0 . GetStreamingURL ( oOOoo0000O0o0 , I1IiiIIIi , o0oo0 )
 if 99 - 99: Ii1I + OoO0O00 * II111iiii . o0oOOo0O0Ooo - I1ii11iIi11i
 if 58 - 58: Ii1I + o0oOOo0O0Ooo - I1IiiI
 i1i1ii = '%s|Cookie=%s' % ( iIiIII1I1I1 , i11IIIiI11 )
 o000o0o00o0Oo ( i1i1ii , False )
 if 46 - 46: OoOoOO00 + OoO0O00
 o0o0O = xbmcgui . ListItem ( path = i1i1ii )
 if 68 - 68: ooOoO0o
 if III11I1 :
  if 25 - 25: I1ii11iIi11i . ooOoO0o
  if 24 - 24: oO0o / i11iIiiIii + oO0o
  I1i11i = III11I1 [ 'customdata' ]
  IiIi = III11I1 [ 'drmhost' ]
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
  OOooo = 'mpd'
  iIIiIiI1I1 = 'com.widevine.alpha'
  if 56 - 56: I1IiiI . O0 + Oo0Ooo
  i1II1I1Iii1 = inputstreamhelper . Helper ( OOooo , drm = iIIiIiI1I1 )
  if 30 - 30: OoooooooOO - OoOoOO00
  if i1II1I1Iii1 . check_inputstream ( ) :
   if 75 - 75: iIii1I11I1II1 - Ii1I . Oo0Ooo % i11iIiiIii % I11i
   if I1IiiIIIi == 'movie' :
    O00II1I11i = 'https://www.wavve.com/player/movie?movieid=%s' % oOOoo0000O0o0
   else :
    O00II1I11i = 'https://www.wavve.com/player/vod?programid=%s&page=1' % oOOoo0000O0o0
    if 82 - 82: I11i + OoooooooOO - i1IIi . i1IIi
   iIi1i = { 'content-type' : 'application/octet-stream'
 , 'origin' : 'https://www.wavve.com'
 , 'pallycon-customdata' : I1i11i
 , 'referer' : O00II1I11i
 , 'sec-fetch-mode' : 'cors'

   , 'sec-fetch-site' : 'cross-site'
 , 'user-agent' : oo00
 }
   I1i11111i1i11 = IiIi + '|' + urllib . urlencode ( iIi1i ) + '|R{SSM}|'
   if 77 - 77: I1ii11iIi11i + OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
   o0o0O . setProperty ( 'inputstreamaddon' , i1II1I1Iii1 . inputstream_addon )
   o0o0O . setProperty ( 'inputstream.adaptive.manifest_type' , OOooo )
   o0o0O . setProperty ( 'inputstream.adaptive.license_type' , iIIiIiI1I1 )
   if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
   o0o0O . setProperty ( 'inputstream.adaptive.license_key' , I1i11111i1i11 )
   o0o0O . setProperty ( 'inputstream.adaptive.stream_headers' , 'Cookie=%s' % i11IIIiI11 )
   if 54 - 54: i1IIi + II111iiii
 xbmcplugin . setResolvedUrl ( ii11i1 , True , o0o0O )
 if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
 if IIi1IIIi :
  ooO00oOoo ( IIi1IIIi . encode ( 'utf-8' ) )
 else :
  if '/preview.' in urlparse . urlsplit ( iIiIII1I1I1 ) . path : ooO00oOoo ( __language__ ( 30401 ) . encode ( 'utf8' ) )
  if 5 - 5: Ii1I
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) and args . get ( 'viewage' ) != '21' :
  i11I1iIiII = { 'code' : args . get ( 'programid' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'contentid' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'subtitle' : args . get ( 'subtitle' )
 }
  iIi1i1iIi1iI ( args . get ( 'mode' ) . lower ( ) , i11I1iIiII )
  if 26 - 26: OoooooooOO * I1IiiI + OOooOOo
  if 24 - 24: i11iIiiIii % iIii1I11I1II1 + OOooOOo / i11iIiiIii
  if 70 - 70: OoO0O00 * O0 . I11i + I1IiiI . IiII
  if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - OoO0O00 - I11i
def o00oo0 ( args ) :
 oO0Oo0O0o = args . get ( 'genre' )
 if 59 - 59: I1IiiI * II111iiii . O0
 if oO0Oo0O0o == '-' :
  Iii111II = 'VOD 시청내역'
  i11I1iIiII = { 'mode' : 'WATCH'
 , 'genre' : 'vod'
 }
  o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
  if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
  Iii111II = '영화 시청내역'
  i11I1iIiII [ 'genre' ] = 'movie'
  o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
  if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
  xbmcplugin . endOfDirectory ( ii11i1 )
  if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
 else :
  i1OO0oOOoo = oOOO00o000o ( oO0Oo0O0o )
  if 9 - 9: oO0o + I11i / I11i
  for Ii1I11ii1i in i1OO0oOOoo :
   O0iIiIIIIIii = dict ( urlparse . parse_qsl ( Ii1I11ii1i ) )
   if 58 - 58: o0oOOo0O0Ooo / IiII . OoOoOO00 / OoooooooOO + I1Ii111
   Iii111II = O0iIiIIIIIii . get ( 'title' ) . strip ( )
   I1iI1iIi111i = O0iIiIIIIIii . get ( 'subtitle' ) . strip ( )
   if I1iI1iIi111i == 'None' : I1iI1iIi111i = ''
   iiIi1IIi1I = O0iIiIIIIIii . get ( 'img' )
   if 86 - 86: I11i * I1IiiI + I11i + II111iiii
   O0ooO0Oo00o = { }
   O0ooO0Oo00o [ 'plot' ] = '%s\n%s' % ( Iii111II , I1iI1iIi111i )
   if 8 - 8: I1Ii111 - iII111i / ooOoO0o
   if oO0Oo0O0o == 'vod' :
    i11I1iIiII = { 'mode' : 'DEEP_LIST'
 , 'contentid' : O0iIiIIIIIii . get ( 'code' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 }
    Ii1I1IIii1II = True
   else :
    i11I1iIiII = { 'mode' : 'MOVIE'
 , 'contentid' : O0iIiIIIIIii . get ( 'code' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 }
    Ii1I1IIii1II = False
    if 96 - 96: OoOoOO00
   o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = iiIi1IIi1I , infoLabels = O0ooO0Oo00o , isFolder = Ii1I1IIii1II , params = i11I1iIiII )
   if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
  O0ooO0Oo00o = { 'plot' : '시청목록을 삭제합니다.' }
  Iii111II = '*** 시청목록 삭제 ***'
  i11I1iIiII = { 'mode' : 'MYVIEW_REMOVE'
 , 'genre' : oO0Oo0O0o
 }
  if 20 - 20: i1IIi % OoO0O00 . I1IiiI / IiII * i11iIiiIii * OOooOOo
  o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = O0ooO0Oo00o , isFolder = False , params = i11I1iIiII )
  if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / ooOoO0o . O0 % I1Ii111
  xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
  if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
  if 74 - 74: O0 / i1IIi
  if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
  if 31 - 31: OoooooooOO . OOooOOo
def O0iII1 ( args ) :
 Iii111II = 'VOD 검색'
 i11I1iIiII = { 'mode' : 'SEARCH_LIST'
 , 'genre' : 'vod'
 , 'page' : '1'
 }
 o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
 if 27 - 27: OoO0O00 . I11i + OoOoOO00 / iIii1I11I1II1 % iII111i . ooOoO0o
 Iii111II = '영화 검색'
 i11I1iIiII [ 'genre' ] = 'movie'
 o00oOO0 ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
 if 14 - 14: oO0o + I1ii11iIi11i - iII111i / O0 . I1Ii111
 xbmcplugin . endOfDirectory ( ii11i1 )
 if 45 - 45: I1Ii111
 if 83 - 83: OoOoOO00 . OoooooooOO
 if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
 if 62 - 62: OoO0O00 / I1ii11iIi11i
def ii1O000OOO0OOo ( args ) :
 if 32 - 32: Ii1I * O0
 O0oOO0 . SaveCredential ( o0o00o0 ( ) )
 if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
 I1IiiIIIi = args . get ( 'genre' )
 i1Iii1i1I = int ( args . get ( 'page' ) )
 if 92 - 92: ooOoO0o
 if 'search_key' in args :
  II11iI111i1 = args . get ( 'search_key' )
 else :
  II11iI111i1 = oOOOO ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not II11iI111i1 : return
  if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
 iIi1 , IiI111111IIII = O0oOO0 . GetSearchList ( II11iI111i1 , I1IiiIIIi , i1Iii1i1I , exclusion21 = o0O00oooo ( ) )
 if 21 - 21: I11i
 for OoO00 in iIi1 :
  Iii111II = OoO00 . get ( 'title' )
  iiIi1IIi1I = OoO00 . get ( 'thumbnail' )
  if 85 - 85: Oo0Ooo * Oo0Ooo * I1IiiI . OoooooooOO . Ii1I * ooOoO0o
  O0ooO0Oo00o = { }
  O0ooO0Oo00o [ 'plot' ] = Iii111II
  if 65 - 65: OOooOOo * I1Ii111
  if I1IiiIIIi == 'vod' :
   i11I1iIiII = { 'mode' : 'DEEP_LIST'
 , 'contentid' : OoO00 . get ( 'programid' )
 , 'contentidType' : 'programid'
 , 'uicode' : 'vod'
 , 'page' : '1'
 , 'title' : Iii111II
   , 'subtitle' : ''
   , 'thumbnail' : iiIi1IIi1I
   , 'viewage' : OoO00 . get ( 'viewage' )
 }
   Ii1I1IIii1II = True
   if 79 - 79: OoooooooOO - I1IiiI
  else :
   i11I1iIiII = { 'mode' : 'MOVIE'
 , 'contentid' : OoO00 . get ( 'contentid' )
 , 'contentidType' : 'contentid'
 , 'uicode' : 'movie'
 , 'page' : '1'
 , 'title' : Iii111II
   , 'subtitle' : ''
   , 'thumbnail' : iiIi1IIi1I
   , 'viewage' : OoO00 . get ( 'viewage' )
 }
   if 69 - 69: I11i
   if 95 - 95: ooOoO0o + i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - iIii1I11I1II1
   Ii1I1IIii1II = False
   if 75 - 75: OoooooooOO * IiII
  if i11I1iIiII . get ( 'viewage' ) == '21' : Iii111II += ' (%s)' % ( i11I1iIiII . get ( 'viewage' ) )
  if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  o00oOO0 ( Iii111II , sublabel = '' , img = iiIi1IIi1I , infoLabels = O0ooO0Oo00o , isFolder = Ii1I1IIii1II , params = i11I1iIiII )
  if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
 if IiI111111IIII :
  if 69 - 69: O0
  i11I1iIiII [ 'mode' ] = 'SEARCH_LIST'
  i11I1iIiII [ 'genre' ] = I1IiiIIIi
  i11I1iIiII [ 'page' ] = str ( i1Iii1i1I + 1 )
  i11I1iIiII [ 'search_key' ] = II11iI111i1
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  I1iI1iIi111i = str ( i1Iii1i1I + 1 )
  o00oOO0 ( Iii111II , sublabel = I1iI1iIi111i , img = '' , infoLabels = None , isFolder = True , params = i11I1iIiII )
  if 85 - 85: ooOoO0o / O0
 if len ( iIi1 ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 )
 if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
 if 62 - 62: I1Ii111 . IiII . OoooooooOO
 if 11 - 11: OOooOOo / I11i
 if 73 - 73: i1IIi / i11iIiiIii
 if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
def oOOO00o000o ( genre ) :
 try :
  oOOoOo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( oOOoOo , 'r' ) as ooOooo0 :
   oO0OO0 = ooOooo0 . readlines ( )
 except :
  oO0OO0 = [ ]
  if 82 - 82: IiII - IiII + OoOoOO00
 return oO0OO0
 if 8 - 8: o0oOOo0O0Ooo % iII111i * oO0o % Ii1I . ooOoO0o / ooOoO0o
 if 81 - 81: OoO0O00
 if 99 - 99: oO0o * II111iiii * I1Ii111
 if 92 - 92: Oo0Ooo
def iIi1i1iIi1iI ( genre , in_params ) :
 try :
  oOOoOo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  iI11I = oOOO00o000o ( genre )
  if 53 - 53: iIii1I11I1II1 + Ii1I - I1Ii111
  with open ( oOOoOo , 'w' ) as ooOooo0 :
   OoO = urllib . urlencode ( in_params )
   OoO = OoO . encode ( 'utf-8' ) + '\n'
   ooOooo0 . write ( OoO )
   if 35 - 35: OoOoOO00 + i11iIiiIii - II111iiii
   Ii1ii111i1 = 0
   for i1i1i1I in iI11I :
    oOoo000 = dict ( urlparse . parse_qsl ( i1i1i1I ) )
    if in_params . get ( 'code' ) != oOoo000 . get ( 'code' ) :
     ooOooo0 . write ( i1i1i1I )
     Ii1ii111i1 += 1
     if Ii1ii111i1 >= 50 : break
 except :
  None
  if 87 - 87: OoooooooOO - o0oOOo0O0Ooo / IiII . i11iIiiIii * OoooooooOO
  if 84 - 84: OoOoOO00 / I11i * iII111i / oO0o - i11iIiiIii . Oo0Ooo
  if 60 - 60: I1ii11iIi11i * I1IiiI
  if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
def i1i1IIii1i1 ( genre ) :
 try :
  oOOoOo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % genre ) )
  with open ( oOOoOo , 'w' ) as ooOooo0 :
   ooOooo0 . write ( '' )
 except :
  None
  if 65 - 65: I1IiiI + OoOoOO00 / OOooOOo
  if 83 - 83: o0oOOo0O0Ooo . iII111i - Oo0Ooo
  if 65 - 65: iIii1I11I1II1 / ooOoO0o . IiII - II111iiii
  if 72 - 72: iIii1I11I1II1 / IiII % iII111i % OOooOOo - I11i % OOooOOo
def oOo0Oo0 ( args ) :
 oO0Oo0O0o = args . get ( 'genre' )
 if 23 - 23: I1Ii111 % o0oOOo0O0Ooo % iII111i * IiII
 O0OOo = xbmcgui . Dialog ( )
 OOO0o = O0OOo . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if OOO0o == False : sys . exit ( )
 if 19 - 19: iIii1I11I1II1
 i1i1IIii1i1 ( oO0Oo0O0o )
 if 26 - 26: OoooooooOO % I1IiiI % Oo0Ooo . I1IiiI % Ii1I
 xbmc . executebuiltin ( "Container.Refresh" )
 if 34 - 34: IiII / OoOoOO00
 if 87 - 87: O0 * o0oOOo0O0Ooo * Oo0Ooo * II111iiii
 if 6 - 6: i1IIi . I1ii11iIi11i + OoOoOO00 * I11i / OoOoOO00 % oO0o
 if 18 - 18: II111iiii . OoooooooOO % OoOoOO00 % Ii1I
 if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
 if 2 - 2: OoooooooOO % OOooOOo
 if 63 - 63: I1IiiI % iIii1I11I1II1
 if 39 - 39: iII111i / II111iiii / I1ii11iIi11i % I1IiiI
 if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
 if 59 - 59: OOooOOo + i11iIiiIii
 if 88 - 88: i11iIiiIii - ooOoO0o
O0oOO0 = iIi ( )
ii11i1 = int ( sys . argv [ 1 ] )
if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
if 30 - 30: OoOoOO00
i11I1iIiII = oo0oooooO0 ( )
OOo0oO00ooO00 = i11I1iIiII . get ( 'mode' , None )
if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
if OOo0oO00ooO00 is None :
 Oo000o ( )
 O00 ( O0oOO0 . LoadCredential ( ) )
 if 26 - 26: II111iiii * OoOoOO00
 if 10 - 10: II111iiii . iII111i
 if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
 if 88 - 88: iII111i
 if 19 - 19: II111iiii * IiII + Ii1I
 if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
 if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
 if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - ooOoO0o
elif OOo0oO00ooO00 == 'GNB_LIST' :
 oOOo0 ( i11I1iIiII )
 if 67 - 67: I11i - OOooOOo . i1IIi
elif OOo0oO00ooO00 == 'GN_LIST' :
 i1I1i111Ii ( i11I1iIiII )
 if 35 - 35: iII111i + ooOoO0o - oO0o . iII111i . IiII
elif OOo0oO00ooO00 == 'DEEP_LIST' :
 I1IiiIIIi = i11I1iIiII . get ( 'uicode' , None )
 if 87 - 87: OoOoOO00
 if I1IiiIIIi in [ 'quick' , 'vod' , 'program' , 'x' ] :
  oOoOOo0O ( i11I1iIiII )
  if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
 else : None
 if 50 - 50: OoO0O00 . i11iIiiIii - oO0o . oO0o
elif OOo0oO00ooO00 in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 ii ( i11I1iIiII )
 xbmc . sleep ( 200 )
 if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
elif OOo0oO00ooO00 == 'GN_MYVIEW' :
 I11i1ii1 ( i11I1iIiII )
 if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
elif OOo0oO00ooO00 == 'MYVIEW_LIST' :
 oo0o00O ( i11I1iIiII )
 if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1 . I11i % oO0o . OoooooooOO
elif OOo0oO00ooO00 == 'GENRE' :
 OoO0o ( i11I1iIiII )
 if 94 - 94: Ii1I + iIii1I11I1II1 % OoO0O00
elif OOo0oO00ooO00 == 'GENRE_LIST' :
 oooOo0OOOoo0 ( i11I1iIiII )
 if 93 - 93: Ii1I - OOooOOo + iIii1I11I1II1 * o0oOOo0O0Ooo + I1Ii111 . iII111i
elif OOo0oO00ooO00 == 'WATCH' :
 o00oo0 ( i11I1iIiII )
 if 49 - 49: OoooooooOO * I11i - Oo0Ooo . oO0o
elif OOo0oO00ooO00 == 'MYVIEW_REMOVE' :
 oOo0Oo0 ( i11I1iIiII )
 if 89 - 89: ooOoO0o + Ii1I * ooOoO0o / ooOoO0o
elif OOo0oO00ooO00 == 'SEARCH' :
 O0iII1 ( i11I1iIiII )
 if 46 - 46: OoO0O00
elif OOo0oO00ooO00 == 'SEARCH_LIST' :
 ii1O000OOO0OOo ( i11I1iIiII )
 if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
else :
 None
 if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
 if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
 if 68 - 68: OoooooooOO % II111iiii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
