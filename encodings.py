﻿''' Data from Py-documentation (7.2.3. Standard Encodings)
Arabic/Chinese/Japanese/Korean/... codepages are skipped
'''

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N

# Codec         Aliases                 Languages/Purpose
ENCODINGS = [
 ['mbcs',       'ANSI, dbcs',           _('Win only: Encode operand according to the ANSI codepage (CP_ACP)')]
,['cp866',      '866, IBM866',          _('Russian')]
,['cp1251',     'windows-1251',         _('Bulgarian, Belarusian, Macedonian, Russian, Serbian')]
,['ascii',      '646, us-ascii',        _('English')]
,['cp037',      'IBM037, IBM039',       _('English')]
,['cp424',      'EBCDIC-CP-HE, IBM424', _('Hebrew')]
,['cp437',      '437, IBM437',          _('English')]
,['cp500',      'EBCDIC-CP-BE, EBCDIC-CP-CH, IBM500', _('Western Europe')]
,['cp737',      '',                     _('Greek')]
,['cp775',      'IBM775',               _('Baltic languages')]
,['cp850',      '850, IBM850',          _('Western Europe')]
,['cp852',      '852, IBM852',          _('Central and Eastern Europe')]
,['cp855',      '855, IBM855',          _('Bulgarian, Belarusian, Macedonian, Russian, Serbian')]
,['cp856',      '',                     _('Hebrew')]
,['cp857',      '857, IBM857',          _('Turkish')]
,['cp858',      '858, IBM858',          _('Western Europe')]
,['cp860',      '860, IBM860',          _('Portuguese')]
,['cp861',      '861, CP-IS, IBM861',   _('Icelandic')]
,['cp862',      '862, IBM862',          _('Hebrew')]
,['cp863',      '863, IBM863',          _('Canadian')]
,['cp865',      '865, IBM865',          _('Danish, Norwegian')]
,['cp869',      '869, CP-GR, IBM869',   _('Greek')]
,['cp875',      '',                     _('Greek')]
,['cp1026',     'ibm1026',              _('Turkish')]
,['cp1140',     'ibm1140',              _('Western Europe')]
,['cp1250',     'windows-1250',         _('Central and Eastern Europe')]
,['cp1252',     'windows-1252',         _('Western Europe')]
,['cp1253',     'windows-1253',         _('Greek')]
,['cp1254',     'windows-1254',         _('Turkish')]
,['cp1255',     'windows-1255',         _('Hebrew')]
,['cp1257',     'windows-1257',         _('Baltic languages')]
,['cp65001',    '',                     _('Win only: Windows UTF-8 (CP_UTF8)')]
,['latin_1',    'iso-8859-1, iso8859-1, 8859, cp819, latin, latin1, L1', _('West Europe')]
,['iso8859_2',  'iso-8859-2, latin2, L2',   _('Central and Eastern Europe')]
,['iso8859_3',  'iso-8859-3, latin3, L3',   _('Esperanto, Maltese')]
,['iso8859_4',  'iso-8859-4, latin4, L4',   _('Baltic languages')]
,['iso8859_5',  'iso-8859-5, cyrillic',     _('Bulgarian, Belarusian, Macedonian, Russian, Serbian')]
,['iso8859_7',  'iso-8859-7, greek, greek8',_('Greek')]
,['iso8859_8',  'iso-8859-8, hebrew',       _('Hebrew')]
,['iso8859_9',  'iso-8859-9, latin5, L5',   _('Turkish')]
,['iso8859_10', 'iso-8859-10, latin6, L6',  _('Nordic languages')]
,['iso8859_13', 'iso-8859-13, latin7, L7',  _('Baltic languages')]
,['iso8859_14', 'iso-8859-14, latin8, L8',  _('Celtic languages')]
,['iso8859_15', 'iso-8859-15, latin9, L9',  _('Western Europe')]
,['iso8859_16', 'iso-8859-16, latin10, L10',_('South-Eastern Europe')]
,['koi8_r',     '',                     _('Russian')]
,['koi8_u',     '',                     _('Ukrainian')]
,['mac_cyrillic','maccyrillic',         _('Bulgarian, Belarusian, Macedonian, Russian, Serbian')]
,['mac_greek',  'macgreek',             _('Greek')]
,['mac_iceland','maciceland',           _('Icelandic')]
,['mac_latin2', 'maclatin2, maccentraleurope', _('Central and Eastern Europe')]
,['mac_roman',  'macroman, macintosh',  _('Western Europe')]
,['mac_turkish','macturkish',           _('Turkish')]
,['ptcp154',    'csptcp154, pt154, cp154, cyrillic-asian', _('Kazakh')]
,['utf_32',     'U32, utf32',           _('all languages')]
,['utf_32_be',  'UTF-32BE',             _('all languages')]
,['utf_32_le',  'UTF-32LE',             _('all languages')]
,['utf_16',     'U16, utf16',           _('all languages')]
,['utf_16_be',  'UTF-16BE',             _('all languages')]
,['utf_16_le',  'UTF-16LE',             _('all languages')]
,['utf_7',      'U7, unicode-1-1-utf-7',_('all languages')]
,['utf_8',      'U8, UTF, utf8',        _('all languages')]
,['utf_8_sig',  '',                     _('all languages')]
]
def get_encoding_names():
    return ['{}\t{}'.format(
						codec[0]
					 ,  ('({}) '.format(codec[1]) if codec[1]!='' else '')+codec[2]
                     )  
            for codec in ENCODINGS]
    #def get_encoding_names
