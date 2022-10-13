from typing import Final


class Languages:
    MULTITRAN: Final = {
        'english': 1, 'eng': 1, 'en': 1,
        'russian': 2, 'rus': 2, 'ru': 2,
        'german': 3, 'deu': 3, 'ger': 3, 'de': 3,
        'french': 4, 'fra': 4, 'fre': 4, 'fr': 4,
        'spanish': 5, 'esl': 5, 'spa': 5, 'es': 5,
        'hebrew': 6, 'heb': 6, 'he': 6,
        'serbian': 7, 'scc': 7, 'srp': 7, 'sr': 7,
        'croatian': 8, 'hrv': 8, 'scr': 8, 'hr': 8,
        'tatar': 9, 'tat': 9, 'tt': 9,
        'arabic': 10, 'ara': 10, 'ar': 10,
        'portuguese': 11, 'por': 11, 'pt': 11,
        'lithuanian': 12, 'lit': 12, 'lt': 12,
        'romanian': 13, 'ron': 13, 'rum': 13, 'ro': 13,
        'polish': 14, 'pol': 14, 'pl': 14,
        'bulgarian': 15, 'bul': 15, 'bg': 15,
        'czech': 16, 'ces': 16, 'cze': 16, 'cs': 16,
        'chinese': 17, 'zho': 17, 'chi': 17, 'zh': 17,
        'hindi': 18, 'hin': 18, 'hi': 18,
        'bengali': 19, 'ben': 19, 'bn': 19,
        'punjabi': 20, 'pan': 20, 'pa': 20,
        'vietnamese': 21, 'vie': 21, 'vi': 21,
        'danish': 22, 'dan': 22, 'da': 22,
        'italian': 23, 'ita': 23, 'it': 23,
        'dutch': 24, 'dut': 24, 'nld': 24, 'ndl': 24, 'nl': 24,
        'azerbaijani': 25, 'aze': 25, 'az': 25,
        'estonian': 26, 'est': 26, 'et': 26,
        'latvian': 27, 'lav': 27, 'lv': 27,
        'japanese': 28, 'jpn': 28, 'ja': 28,
        'swedish': 29, 'sve': 29, 'swe': 29, 'sv': 29,
        'norwegian': 30, 'nor': 30, 'no': 30,
        'afrikaans': 31, 'afr': 31, 'af': 31,
        'turkish': 32, 'tur': 32, 'tr': 32,
        'ukrainian': 33, 'ukr': 33, 'uk': 33,
        'esperanto': 34, 'epo': 34, 'eo': 34,
        'kalmyk': 35, 'xal': 35, 'kak': 35,
        'finnish': 36, 'fin': 36, 'fi': 36,
        'latin': 37, 'lat': 37, 'la': 37,
        'greek': 38, 'gre': 38, 'ell': 38, 'el': 38,
        'korean': 39, 'kor': 39, 'ko': 39,
        'georgian': 40, 'geo': 40, 'kat': 40, 'ka': 40,
        'armenian': 41, 'arm': 41, 'hye': 41, 'axm': 41, 'xcl': 41, 'hy': 41,
        'hungarian': 42, 'hun': 42, 'hu': 42,
        'kazakh': 43, 'kaz': 43, 'kk': 43,
        'kirghiz': 44, 'kir': 44, 'kyr': 44, 'ky': 44,
        'uzbek': 45, 'uzb': 45, 'uz': 45,
        'romany': 46, 'rom': 46,
        'albanian': 47, 'alb': 47, 'sqi': 47, 'sq': 47,
        'welsh': 48, 'cym': 48, 'wel': 48, 'cy': 48,
        'irish': 49, 'gle': 49, 'gai': 49, 'iri': 49,
        'icelandic': 50, 'ice': 50, 'isl': 50, 'is': 50,
        'kurdish': 51,
        'persian': 52, 'farsi': 52,
        'catalan': 53,
        'corsican': 54,
        'galician': 55,
        'mirandese': 56,
        'romansh': 57,
        'belarusian': 58,
        'ruthene': 59,
        'slovak': 60, 'slk': 60, 'slo': 60, 'sk': 60,
        'upper sorbian': 61,
        'lower sorbian': 62,
        'bosnian': 63,
        'montenegrin': 64,
        'macedonian': 65,
        'church slavonic': 66,
        'slovenian': 67, 'slv': 67, 'sl': 67,
        'basque': 68,
        'svan': 69,
        'mingrelian': 70,
        'abkhazian': 71,
        'adyghe': 72,
        'chechen': 73,
        'avar': 74,
        'ingush': 75,
        'crimean tatar': 76,
        'chuvash': 77,
        'maltese': 78, 'mlt': 78, 'mt': 78,
        'khmer': 79, 'nepali': 80, 'amharic': 81, 'assamese': 82, 'lao': 83, 'asturian': 84, 'odia': 85,
        'indonesian': 86, 'pashto': 87, 'quechua': 88, 'maori': 89, 'marathi': 90, 'tamil': 91, 'telugu': 92,
        'thai': 93, 'turkmen': 94, 'yoruba': 95, 'bosnian cyrillic': 96, 'chinese simplified': 97, 'chinese taiwan': 98,
        'filipino': 99, 'gujarati': 100, 'hausa': 101, 'igbo': 102, 'inuktitut': 103, 'isixhosa': 104, 'zulu': 105,
        'kannada': 106, 'kinyarwanda': 107, 'swahili': 108, 'konkani': 109, 'luxembourgish': 110, 'malayalam': 111,
        'wolof': 112, 'wayuu': 113, 'serbian latin': 114, 'tswana': 115, 'sinhala': 116, 'urdu': 117,
        'sesotho sa leboa': 118, 'norwegian nynorsk': 119, 'malay': 120, 'mongolian': 121, 'frisian': 122,
        'faroese': 123, 'friulian': 124, 'ladin': 125, 'sardinian': 126, 'occitan': 127, 'gaulish': 128, 'sylheti': 129,
        'sami': 130, 'breton': 131, 'cornish': 132, 'manx': 133, 'scottish gaelic': 134, 'yiddish': 135, 'tajik': 136,
        'tagalog': 137, 'soninke': 138, 'baoulé': 139, 'javanese': 140, 'wayana': 141, 'french guiana creole': 142,
        'mauritian creole': 143, 'seychellois creole': 144, 'guadeloupe creole': 145, 'rodriguan creole': 146,
        'haitian creole': 147, 'mandinka': 148, 'surigaonon': 149, 'adangme': 150, 'tok pisin': 151,
        'cameroonian creole': 152, 'suriname creole': 153, 'belizean creole': 154, 'virgin islands creole': 155,
        'fon': 156, 'kim': 157, 'ivatan': 158, 'gen': 159, 'marshallese': 160, 'wallisian': 161, 'old prussian': 162,
        'yom': 163, 'tokelauan': 164, 'zande': 165, 'yao': 166, 'waray': 167, 'walmajarri': 168, 'visayan': 169,
        'vili': 170, 'venda': 171, 'acehnese': 172, 'adjukru': 173, 'agutaynen': 174, 'afar': 175, 'acoli': 176,
        'afrihili': 177, 'ainu': 178, 'akan': 179, 'akkadian': 180, 'aleut': 181, 'southern altai': 182,
        'old english': 183, 'angika': 184, 'official aramaic': 185, 'aragonese': 186, 'mapudungun': 187,
        'arapaho': 188, 'arawak': 189, 'avestan': 190, 'awadhi': 191, 'aymara': 192, 'bashkir': 193, 'balochi': 194,
        'bambara': 195, 'balinese': 196, 'basaa': 197, 'beja': 198, 'bemba': 199, 'bhojpuri': 200, 'bikol': 201,
        'bini': 202, 'bislama': 203, 'siksika': 204, 'tibetan': 205, 'braj': 206, 'buriat': 207, 'buginese': 208,
        'burmese': 209, 'bilin': 210, 'caddo': 211, 'galibi carib': 212, 'cebuano': 213, 'chamorro': 214,
        'chibcha': 215, 'chagatai': 216, 'chuukese': 217, 'mari': 218, 'chinook jargon': 219, 'choctaw': 220,
        'chipewyan': 221, 'cherokee': 222, 'cheyenne': 223, 'coptic': 224, 'cree': 225, 'kashubian': 226,
        'dakota': 227, 'dargwa': 228, 'delaware': 229, 'slave': 230, 'dogrib': 231, 'dinka': 232, 'dhivehi': 233,
        'dogri': 234, 'duala': 235, 'middle dutch': 236, 'dyula': 237, 'dzongkha': 238, 'efik': 239, 'egyptian': 240,
        'ekajuk': 241, 'elamite': 242, 'middle english': 243, 'ewe': 244, 'ewondo': 245, 'fang': 246, 'fanti': 247,
        'fijian': 248, 'middle french': 249, 'old french': 250, 'eastern frisian': 251, 'fulah': 252, 'ga': 253,
        'gayo': 254, 'gbaya': 255, "ge'ez": 256, 'gilbertese': 257, 'middle high german': 258, 'old high german': 259,
        'gondi': 260, 'gorontalo': 261, 'gothic': 262, 'grebo': 263, 'ancient greek': 264, 'guarani': 265,
        'swiss german': 266, 'gwichʼin': 267, 'haida': 268, 'kikuyu': 269, 'hawaiian': 270, 'herero': 271,
        'hiligaynon': 272, 'hittite': 273, 'hmong': 274, 'hiri motu': 275, 'hupa': 276, 'iban': 277, 'ido': 278,
        'nuosu (sichuan yi)': 279, 'interlingue': 280, 'ilocano': 281, 'interlingua': 282, 'inupiaq': 283,
        'lojban': 284, 'judeo-persian': 285, 'judeo-arabic': 286, 'kara-kalpak': 287, 'kabyle': 288, 'kachin': 289,
        'kalaallisut': 290, 'kamba': 291, 'kashmiri': 292, 'kanuri': 293, 'kawi': 294, 'kabardian': 295, 'khasi': 296,
        'khotanese': 297, 'kimbundu': 298, 'komi': 299, 'kongo': 300, 'kosraean': 301, 'kpelle': 302,
        'karachay-balkar': 303, 'karelian': 304, 'kurukh': 305, 'kuanyama': 306, 'kumyk': 307, 'kutenai': 308,
        'lahnda': 309, 'lamba': 310, 'lezghian': 311, 'limburgan': 312, 'lingala': 313, 'mongo': 314, 'lozi': 315,
        'luba-lulua': 316, 'luba-katanga': 317, 'ganda': 318, 'luiseno': 319, 'lunda': 320, 'luo': 321, 'lushai': 322,
        'madurese': 323, 'magahi': 324, 'maithili': 325, 'makasar': 326, 'masai': 327, 'moksha': 328, 'mandar': 329,
        'mende': 330, 'middle irish': 331, "mi'kmaq": 332, 'minangkabau': 333, 'malagasy': 334, 'manchu': 335,
        'manipuri': 336, 'mohawk': 337, 'mossi': 338, 'creek': 339, 'marwari': 340, 'erzya': 341, 'neapolitan': 342,
        'nauru': 343, 'navajo': 344, 'south ndebele': 345, 'north ndebele': 346, 'ndonga': 347, 'low german': 348,
        'nepal bhasa': 349, 'nias': 350, 'niuean': 351, 'nogai': 352, 'old norse': 353, 'sandawe': 354, "n'ko": 355,
        'classical newari': 356, 'nyanja': 357, 'nyamwezi': 358, 'nyankole': 359, 'nyoro': 360, 'nzima': 361,
        'ojibwa': 362, 'oromo': 363, 'osage': 364, 'ossetian': 365, 'ottoman turkish': 366, 'pangasinan': 367,
        'pahlavi': 368, 'pampanga': 369, 'papiamento': 370, 'palauan': 371, 'old persian': 372, 'phoenician': 373,
        'pali': 374, 'pohnpeian': 375, 'old occitan': 376, 'rajasthani': 377, 'rapanui': 378, 'rarotongan': 379,
        'reunionese': 380, 'rundi': 381, 'macedo-romanian': 382, 'sango': 383, 'yakut': 384, 'samaritan aramaic': 385,
        'sanskrit': 386, 'sasak': 387, 'sicilian': 388, 'scots': 389, 'selkup': 390, 'old irish': 391, 'shan': 392,
        'sidamo': 393, 'southern sami': 394, 'northern sami': 395, 'lule sami': 396, 'inari sami': 397, 'samoan': 398,
        'skolt sami': 399, 'shona': 400, 'sindhi': 401, 'sogdian': 402, 'somali': 403, 'southern sotho': 404,
        'sranan tongo': 405, 'serer': 406, 'swati': 407, 'sukuma': 408, 'sundanese': 409, 'susu': 410, 'sumerian': 411,
        'santali': 412, 'syriac': 413, 'tahitian': 414, 'timne': 415, 'tonga': 416, 'tetum': 417, 'tigre': 418,
        'tigrinya': 419, 'tiv': 420, 'shilluk': 421, 'klingon': 422, 'tlingit': 423, 'tamashek': 424, 'carolinian': 425,
        'portuguese creole': 426, 'tuamotuan': 427, 'numèè': 428, 'gela': 429, 'comorian': 430, 'rennellese': 431,
        'emilian-romagnol': 432, 'mayan': 433, 'caribbean hindustani': 434, 'khakas': 435, 'kinga': 436,
        'kurmanji': 437, 'kwangali': 438, 'lango': 439, 'ligurian': 440, 'lombard': 441, 'luguru': 442, 'mamasa': 443,
        'mashi': 444, 'meru': 445, 'rotokas': 446, 'moldovan': 447, 'mongolian script': 448, 'nasioi': 449,
        'nyakyusa': 450, 'piedmontese': 451, 'pinyin': 452, 'sangu': 453, 'shambala': 454, 'shor': 455,
        'central atlas tamazight': 456, 'thai (transliteration)': 457, 'tsonga': 458, 'tuvan': 459, 'valencian': 460,
        'venetian': 461, 'walloon': 462, 'wanji': 463, 'zigula': 464, 'korean (transliteration)': 465,
        'mongolian (transliteration)': 466, 'assyrian': 467, 'kaguru': 468, 'kimakonde': 469, 'kirufiji': 470,
        'mbwera': 471, 'gronings': 472, 'hadza': 473, 'iraqw': 474, 'kami': 475, 'krio': 476, 'tweants': 477,
        'abaza': 478, 'украинский 1': 479
    }
    DEFAULT_OPTIONS: Final = {
        1: ('one', 'two', 'three', 'there'),
        2: ('один', 'два', 'три', 'там'),
        3: ('eins', 'zwei', 'drei', 'dort'),
        4: ('un', 'deux', 'trois', 'là'),
        5: ('uno', 'dos', 'tres', 'allí'),
        6: ('אחד', 'שתיים', 'שלוש', 'שם'),
        7: ('један', 'два', 'три', 'тамо'),
        8: ('jedan', 'dva', 'tri', 'tu'),
        9: ('бер', 'ике', 'өч', 'анда'),
        10: ('واحد', 'اثنين', 'ثلاثة', 'هناك'),
        11: ('um', 'dois', 'três', 'lá'),
        12: ('vienas', 'du', 'trys', 'ten'),
        13: ('unu', 'doi', 'trei', 'acolo'),
        14: ('jeden', 'dwa', 'trzy', 'tam'),
        15: ('едно', 'две', 'три', 'там'),
        16: ('jeden', 'dva', 'tři', 'tam'),
        17: ('一', '二', '三', '那裡'),
        18: ('एक', 'दो', 'तीन', 'वहां'),
        19: ('এক', 'দুই', 'তিন', 'সেখানে'),
        20: ('ਇੱਕ', 'ਦੋ', 'ਤਿੰਨ', 'ਉੱਥੇ'),
        21: ('một', 'hai', 'ba', 'đó'),
        22: ('en', 'to', 'tre', 'der'),
        23: ('uno', 'due', 'tre', 'là'),
        24: ('een', 'twee', 'drie', 'daar'),
        25: ('bir', 'iki', 'üç', 'orada'),
        26: ('üks', 'kaks', 'kolm', 'seal'),
        27: ('viens', 'divi', 'trīs', 'tur'),
        28: ('一', '二', '三', 'そこ'),
        29: ('en', 'två', 'tre', 'där'),
        30: ('en', 'to', 'tre', 'der'),
        31: ('een', 'twee', 'drie', 'daar'),
        32: ('bir', 'iki', 'üç', 'orada'),
        33: ('один', 'два', 'три', 'там'),
        34: ('unu', 'du', 'tri', 'tie'),
        35: ('негн', 'хойр', 'һурвн', 'тенд'),
        36: ('yksi', 'kaksi', 'kolme', 'siellä'),
        37: ('unus', 'duo', 'tres', 'ibi'),
        38: ('ένα', 'δύο', 'τρεις', 'εκεί'),
        39: ('하나', '둘', '셋', '거기'),
        40: ('ერთი', 'ორი', 'სამი', 'იქ'),
        41: ('մեկ', 'երկու', 'երեք', 'այնտեղ'),
        42: ('egy', 'kettő', 'három', 'ott'),
        43: ('бір', 'екі', 'үш', 'бар'),
        44: ('бир', 'эки', 'үч', 'бар'),
        45: ('bir', 'ikki', 'uch', 'u erda'),
        47: ('një', 'dy', 'tre', 'aty'),
        48: ('un', 'dau', 'tri', 'yno'),
        49: ('aon', 'dhá', 'trí', 'tá'),
        50: ('einn', 'tveir', 'þrír', 'þar'),
        60: ('jeden', 'dva', 'tri', 'tam'),
        67: ('ena', 'dva', 'tri', 'tam')
    }
