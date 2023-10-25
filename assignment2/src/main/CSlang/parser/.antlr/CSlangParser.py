# Generated from d:/Program/XAMPP/htdocs/btl-nllt/assignment2/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,501,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,108,8,1,1,2,1,2,1,2,3,2,113,8,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,3,3,124,8,3,1,4,1,4,1,4,1,4,3,4,130,8,4,1,5,1,5,3,5,134,8,
        5,1,6,1,6,1,6,3,6,139,8,6,1,7,1,7,1,7,3,7,144,8,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,158,8,8,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,168,8,9,1,10,1,10,1,10,3,10,173,8,10,1,10,1,10,
        1,11,1,11,1,12,1,12,1,12,1,12,3,12,183,8,12,1,12,1,12,1,12,1,12,
        3,12,189,8,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,197,8,12,1,12,1,
        12,3,12,201,8,12,1,13,1,13,1,13,1,13,1,13,3,13,208,8,13,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,3,15,219,8,15,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,18,1,18,3,18,231,8,18,1,19,1,19,1,19,
        1,19,1,19,3,19,238,8,19,1,20,1,20,1,20,1,20,1,20,3,20,245,8,20,1,
        21,1,21,1,21,1,21,1,21,3,21,252,8,21,1,22,1,22,1,22,1,22,1,22,1,
        22,5,22,260,8,22,10,22,12,22,263,9,22,1,23,1,23,1,23,1,23,1,23,1,
        23,5,23,271,8,23,10,23,12,23,274,9,23,1,24,1,24,1,24,1,24,1,24,1,
        24,5,24,282,8,24,10,24,12,24,285,9,24,1,25,1,25,1,25,3,25,290,8,
        25,1,26,1,26,1,26,3,26,295,8,26,1,27,1,27,1,27,1,27,1,27,1,27,3,
        27,303,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,313,8,28,
        1,28,1,28,1,28,3,28,318,8,28,5,28,320,8,28,10,28,12,28,323,9,28,
        1,29,1,29,3,29,327,8,29,1,30,1,30,1,30,1,30,3,30,333,8,30,1,31,1,
        31,1,31,1,31,1,31,3,31,340,8,31,1,32,1,32,3,32,344,8,32,1,32,1,32,
        3,32,348,8,32,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        3,34,360,8,34,1,35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,3,37,370,8,
        37,1,38,1,38,1,38,1,38,1,38,3,38,377,8,38,1,39,1,39,1,39,1,39,3,
        39,383,8,39,1,40,1,40,3,40,387,8,40,1,40,1,40,1,40,1,40,3,40,393,
        8,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,404,8,40,
        1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,415,8,40,1,40,
        1,40,1,40,1,40,1,40,1,40,1,40,3,40,424,8,40,1,41,1,41,1,41,1,41,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,5,42,438,8,42,10,42,12,42,
        441,9,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,451,8,43,1,
        43,1,43,1,43,3,43,456,8,43,5,43,458,8,43,10,43,12,43,461,9,43,1,
        44,1,44,3,44,465,8,44,1,45,1,45,1,45,1,45,1,45,1,45,3,45,473,8,45,
        1,46,1,46,3,46,477,8,46,1,47,1,47,1,47,1,47,1,47,3,47,484,8,47,1,
        47,1,47,1,47,1,47,1,48,1,48,3,48,492,8,48,1,48,1,48,1,48,1,49,1,
        49,3,49,499,8,49,1,49,0,6,44,46,48,56,84,86,50,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,0,8,
        2,0,8,11,56,56,1,0,30,35,1,0,28,29,1,0,21,22,1,0,23,26,1,0,56,57,
        1,0,6,7,2,0,16,16,19,19,516,0,100,1,0,0,0,2,107,1,0,0,0,4,109,1,
        0,0,0,6,123,1,0,0,0,8,129,1,0,0,0,10,133,1,0,0,0,12,135,1,0,0,0,
        14,140,1,0,0,0,16,157,1,0,0,0,18,167,1,0,0,0,20,172,1,0,0,0,22,176,
        1,0,0,0,24,200,1,0,0,0,26,207,1,0,0,0,28,209,1,0,0,0,30,218,1,0,
        0,0,32,220,1,0,0,0,34,224,1,0,0,0,36,230,1,0,0,0,38,237,1,0,0,0,
        40,244,1,0,0,0,42,251,1,0,0,0,44,253,1,0,0,0,46,264,1,0,0,0,48,275,
        1,0,0,0,50,289,1,0,0,0,52,294,1,0,0,0,54,302,1,0,0,0,56,304,1,0,
        0,0,58,326,1,0,0,0,60,332,1,0,0,0,62,339,1,0,0,0,64,343,1,0,0,0,
        66,349,1,0,0,0,68,359,1,0,0,0,70,361,1,0,0,0,72,363,1,0,0,0,74,369,
        1,0,0,0,76,376,1,0,0,0,78,382,1,0,0,0,80,423,1,0,0,0,82,425,1,0,
        0,0,84,429,1,0,0,0,86,442,1,0,0,0,88,464,1,0,0,0,90,472,1,0,0,0,
        92,476,1,0,0,0,94,478,1,0,0,0,96,491,1,0,0,0,98,498,1,0,0,0,100,
        101,3,2,1,0,101,102,5,0,0,1,102,1,1,0,0,0,103,104,3,4,2,0,104,105,
        3,2,1,0,105,108,1,0,0,0,106,108,3,4,2,0,107,103,1,0,0,0,107,106,
        1,0,0,0,108,3,1,0,0,0,109,112,5,14,0,0,110,111,5,56,0,0,111,113,
        5,39,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,
        5,56,0,0,115,116,5,45,0,0,116,117,3,6,3,0,117,118,5,46,0,0,118,5,
        1,0,0,0,119,120,3,8,4,0,120,121,3,6,3,0,121,124,1,0,0,0,122,124,
        1,0,0,0,123,119,1,0,0,0,123,122,1,0,0,0,124,7,1,0,0,0,125,126,3,
        10,5,0,126,127,5,49,0,0,127,130,1,0,0,0,128,130,3,24,12,0,129,125,
        1,0,0,0,129,128,1,0,0,0,130,9,1,0,0,0,131,134,3,12,6,0,132,134,3,
        14,7,0,133,131,1,0,0,0,133,132,1,0,0,0,134,11,1,0,0,0,135,138,5,
        16,0,0,136,139,3,16,8,0,137,139,3,18,9,0,138,136,1,0,0,0,138,137,
        1,0,0,0,139,13,1,0,0,0,140,143,5,19,0,0,141,144,3,16,8,0,142,144,
        3,18,9,0,143,141,1,0,0,0,143,142,1,0,0,0,144,15,1,0,0,0,145,146,
        3,66,33,0,146,147,5,48,0,0,147,148,3,16,8,0,148,149,5,48,0,0,149,
        150,3,40,20,0,150,158,1,0,0,0,151,152,3,66,33,0,152,153,5,50,0,0,
        153,154,3,20,10,0,154,155,5,36,0,0,155,156,3,40,20,0,156,158,1,0,
        0,0,157,145,1,0,0,0,157,151,1,0,0,0,158,17,1,0,0,0,159,160,3,66,
        33,0,160,161,5,48,0,0,161,162,3,18,9,0,162,168,1,0,0,0,163,164,3,
        66,33,0,164,165,5,50,0,0,165,166,3,20,10,0,166,168,1,0,0,0,167,159,
        1,0,0,0,167,163,1,0,0,0,168,19,1,0,0,0,169,170,5,43,0,0,170,171,
        5,51,0,0,171,173,5,44,0,0,172,169,1,0,0,0,172,173,1,0,0,0,173,174,
        1,0,0,0,174,175,3,22,11,0,175,21,1,0,0,0,176,177,7,0,0,0,177,23,
        1,0,0,0,178,179,5,20,0,0,179,180,3,66,33,0,180,182,5,41,0,0,181,
        183,3,26,13,0,182,181,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,
        185,5,42,0,0,185,188,5,50,0,0,186,189,3,20,10,0,187,189,5,18,0,0,
        188,186,1,0,0,0,188,187,1,0,0,0,189,190,1,0,0,0,190,191,3,32,16,
        0,191,201,1,0,0,0,192,193,5,20,0,0,193,194,5,15,0,0,194,196,5,41,
        0,0,195,197,3,26,13,0,196,195,1,0,0,0,196,197,1,0,0,0,197,198,1,
        0,0,0,198,199,5,42,0,0,199,201,3,32,16,0,200,178,1,0,0,0,200,192,
        1,0,0,0,201,25,1,0,0,0,202,203,3,28,14,0,203,204,5,48,0,0,204,205,
        3,26,13,0,205,208,1,0,0,0,206,208,3,28,14,0,207,202,1,0,0,0,207,
        206,1,0,0,0,208,27,1,0,0,0,209,210,3,30,15,0,210,211,5,50,0,0,211,
        212,3,20,10,0,212,29,1,0,0,0,213,214,3,66,33,0,214,215,5,48,0,0,
        215,216,3,30,15,0,216,219,1,0,0,0,217,219,3,66,33,0,218,213,1,0,
        0,0,218,217,1,0,0,0,219,31,1,0,0,0,220,221,5,45,0,0,221,222,3,78,
        39,0,222,223,5,46,0,0,223,33,1,0,0,0,224,225,5,41,0,0,225,226,3,
        36,18,0,226,227,5,42,0,0,227,35,1,0,0,0,228,231,3,38,19,0,229,231,
        1,0,0,0,230,228,1,0,0,0,230,229,1,0,0,0,231,37,1,0,0,0,232,233,3,
        40,20,0,233,234,5,48,0,0,234,235,3,38,19,0,235,238,1,0,0,0,236,238,
        3,40,20,0,237,232,1,0,0,0,237,236,1,0,0,0,238,39,1,0,0,0,239,240,
        3,42,21,0,240,241,5,38,0,0,241,242,3,42,21,0,242,245,1,0,0,0,243,
        245,3,42,21,0,244,239,1,0,0,0,244,243,1,0,0,0,245,41,1,0,0,0,246,
        247,3,44,22,0,247,248,7,1,0,0,248,249,3,44,22,0,249,252,1,0,0,0,
        250,252,3,44,22,0,251,246,1,0,0,0,251,250,1,0,0,0,252,43,1,0,0,0,
        253,254,6,22,-1,0,254,255,3,46,23,0,255,261,1,0,0,0,256,257,10,2,
        0,0,257,258,7,2,0,0,258,260,3,46,23,0,259,256,1,0,0,0,260,263,1,
        0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,45,1,0,0,0,263,261,1,0,
        0,0,264,265,6,23,-1,0,265,266,3,48,24,0,266,272,1,0,0,0,267,268,
        10,2,0,0,268,269,7,3,0,0,269,271,3,48,24,0,270,267,1,0,0,0,271,274,
        1,0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,47,1,0,0,0,274,272,1,
        0,0,0,275,276,6,24,-1,0,276,277,3,50,25,0,277,283,1,0,0,0,278,279,
        10,2,0,0,279,280,7,4,0,0,280,282,3,50,25,0,281,278,1,0,0,0,282,285,
        1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,49,1,0,0,0,285,283,1,
        0,0,0,286,287,5,27,0,0,287,290,3,50,25,0,288,290,3,52,26,0,289,286,
        1,0,0,0,289,288,1,0,0,0,290,51,1,0,0,0,291,292,5,22,0,0,292,295,
        3,52,26,0,293,295,3,54,27,0,294,291,1,0,0,0,294,293,1,0,0,0,295,
        53,1,0,0,0,296,297,3,56,28,0,297,298,5,43,0,0,298,299,3,40,20,0,
        299,300,5,44,0,0,300,303,1,0,0,0,301,303,3,56,28,0,302,296,1,0,0,
        0,302,301,1,0,0,0,303,55,1,0,0,0,304,305,6,28,-1,0,305,306,3,58,
        29,0,306,321,1,0,0,0,307,312,10,2,0,0,308,309,5,43,0,0,309,310,3,
        40,20,0,310,311,5,44,0,0,311,313,1,0,0,0,312,308,1,0,0,0,312,313,
        1,0,0,0,313,314,1,0,0,0,314,315,5,47,0,0,315,317,5,56,0,0,316,318,
        3,34,17,0,317,316,1,0,0,0,317,318,1,0,0,0,318,320,1,0,0,0,319,307,
        1,0,0,0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,1,0,0,0,322,57,1,
        0,0,0,323,321,1,0,0,0,324,327,3,64,32,0,325,327,3,60,30,0,326,324,
        1,0,0,0,326,325,1,0,0,0,327,59,1,0,0,0,328,329,5,40,0,0,329,330,
        5,56,0,0,330,333,3,34,17,0,331,333,3,62,31,0,332,328,1,0,0,0,332,
        331,1,0,0,0,333,61,1,0,0,0,334,335,5,41,0,0,335,336,3,40,20,0,336,
        337,5,42,0,0,337,340,1,0,0,0,338,340,3,68,34,0,339,334,1,0,0,0,339,
        338,1,0,0,0,340,63,1,0,0,0,341,342,5,56,0,0,342,344,5,47,0,0,343,
        341,1,0,0,0,343,344,1,0,0,0,344,345,1,0,0,0,345,347,5,57,0,0,346,
        348,3,34,17,0,347,346,1,0,0,0,347,348,1,0,0,0,348,65,1,0,0,0,349,
        350,7,5,0,0,350,67,1,0,0,0,351,360,5,51,0,0,352,360,5,52,0,0,353,
        360,3,70,35,0,354,360,5,53,0,0,355,360,3,72,36,0,356,360,5,13,0,
        0,357,360,5,17,0,0,358,360,3,66,33,0,359,351,1,0,0,0,359,352,1,0,
        0,0,359,353,1,0,0,0,359,354,1,0,0,0,359,355,1,0,0,0,359,356,1,0,
        0,0,359,357,1,0,0,0,359,358,1,0,0,0,360,69,1,0,0,0,361,362,7,6,0,
        0,362,71,1,0,0,0,363,364,5,43,0,0,364,365,3,76,38,0,365,366,5,44,
        0,0,366,73,1,0,0,0,367,370,3,76,38,0,368,370,1,0,0,0,369,367,1,0,
        0,0,369,368,1,0,0,0,370,75,1,0,0,0,371,372,3,68,34,0,372,373,5,48,
        0,0,373,374,3,76,38,0,374,377,1,0,0,0,375,377,3,68,34,0,376,371,
        1,0,0,0,376,375,1,0,0,0,377,77,1,0,0,0,378,379,3,80,40,0,379,380,
        3,78,39,0,380,383,1,0,0,0,381,383,1,0,0,0,382,378,1,0,0,0,382,381,
        1,0,0,0,383,79,1,0,0,0,384,386,5,3,0,0,385,387,3,32,16,0,386,385,
        1,0,0,0,386,387,1,0,0,0,387,388,1,0,0,0,388,389,3,40,20,0,389,392,
        3,32,16,0,390,391,5,4,0,0,391,393,3,32,16,0,392,390,1,0,0,0,392,
        393,1,0,0,0,393,424,1,0,0,0,394,395,5,5,0,0,395,396,3,82,41,0,396,
        397,5,49,0,0,397,398,3,40,20,0,398,399,5,49,0,0,399,400,3,82,41,
        0,400,401,3,32,16,0,401,424,1,0,0,0,402,404,7,7,0,0,403,402,1,0,
        0,0,403,404,1,0,0,0,404,405,1,0,0,0,405,406,3,82,41,0,406,407,5,
        49,0,0,407,424,1,0,0,0,408,409,5,1,0,0,409,424,5,49,0,0,410,411,
        5,2,0,0,411,424,5,49,0,0,412,414,5,12,0,0,413,415,3,40,20,0,414,
        413,1,0,0,0,414,415,1,0,0,0,415,416,1,0,0,0,416,424,5,49,0,0,417,
        418,3,92,46,0,418,419,5,49,0,0,419,424,1,0,0,0,420,421,3,98,49,0,
        421,422,5,49,0,0,422,424,1,0,0,0,423,384,1,0,0,0,423,394,1,0,0,0,
        423,403,1,0,0,0,423,408,1,0,0,0,423,410,1,0,0,0,423,412,1,0,0,0,
        423,417,1,0,0,0,423,420,1,0,0,0,424,81,1,0,0,0,425,426,3,84,42,0,
        426,427,5,37,0,0,427,428,3,40,20,0,428,83,1,0,0,0,429,430,6,42,-1,
        0,430,431,3,86,43,0,431,439,1,0,0,0,432,433,10,2,0,0,433,434,5,43,
        0,0,434,435,3,40,20,0,435,436,5,44,0,0,436,438,1,0,0,0,437,432,1,
        0,0,0,438,441,1,0,0,0,439,437,1,0,0,0,439,440,1,0,0,0,440,85,1,0,
        0,0,441,439,1,0,0,0,442,443,6,43,-1,0,443,444,3,88,44,0,444,459,
        1,0,0,0,445,450,10,2,0,0,446,447,5,43,0,0,447,448,3,40,20,0,448,
        449,5,44,0,0,449,451,1,0,0,0,450,446,1,0,0,0,450,451,1,0,0,0,451,
        452,1,0,0,0,452,453,5,47,0,0,453,455,5,56,0,0,454,456,3,34,17,0,
        455,454,1,0,0,0,455,456,1,0,0,0,456,458,1,0,0,0,457,445,1,0,0,0,
        458,461,1,0,0,0,459,457,1,0,0,0,459,460,1,0,0,0,460,87,1,0,0,0,461,
        459,1,0,0,0,462,465,3,64,32,0,463,465,3,90,45,0,464,462,1,0,0,0,
        464,463,1,0,0,0,465,89,1,0,0,0,466,467,5,41,0,0,467,468,3,84,42,
        0,468,469,5,42,0,0,469,473,1,0,0,0,470,473,5,17,0,0,471,473,3,66,
        33,0,472,466,1,0,0,0,472,470,1,0,0,0,472,471,1,0,0,0,473,91,1,0,
        0,0,474,477,3,94,47,0,475,477,3,96,48,0,476,474,1,0,0,0,476,475,
        1,0,0,0,477,93,1,0,0,0,478,483,3,56,28,0,479,480,5,43,0,0,480,481,
        3,40,20,0,481,482,5,44,0,0,482,484,1,0,0,0,483,479,1,0,0,0,483,484,
        1,0,0,0,484,485,1,0,0,0,485,486,5,47,0,0,486,487,5,56,0,0,487,488,
        3,34,17,0,488,95,1,0,0,0,489,490,5,56,0,0,490,492,5,47,0,0,491,489,
        1,0,0,0,491,492,1,0,0,0,492,493,1,0,0,0,493,494,5,57,0,0,494,495,
        3,34,17,0,495,97,1,0,0,0,496,499,3,12,6,0,497,499,3,14,7,0,498,496,
        1,0,0,0,498,497,1,0,0,0,499,99,1,0,0,0,53,107,112,123,129,133,138,
        143,157,167,172,182,188,196,200,207,218,230,237,244,251,261,272,
        283,289,294,302,312,317,321,326,332,339,343,347,359,369,376,382,
        386,392,403,414,423,439,450,455,459,464,472,476,483,491,498
    ]

class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'true'", "'false'", "'int'", "'float'", "'bool'", 
                     "'string'", "'return'", "'null'", "'class'", "'constructor'", 
                     "'var'", "'self'", "'void'", "'const'", "'func'", "'+'", 
                     "'-'", "'*'", "'/'", "'\\'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'='", "':='", "'^'", "'<-'", "'new'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", 
                      "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
                      "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                      "VOID", "CONST", "FUNC", "ADD", "SUB", "MUL", "DIVFLOAT", 
                      "DIVINT", "MOD", "NEG", "AND", "OR", "EQ", "NEQ", 
                      "LT", "LTEQ", "GT", "GTEQ", "DECLARE", "ASSIGN", "CONCATE", 
                      "LARROW", "NEW", "LPN", "RPN", "LBK", "RBK", "LBR", 
                      "RBR", "DOT", "CM", "SM", "COL", "INTLIT", "FLOATLIT", 
                      "STRLIT", "BLOCK_COMMENT", "LINE_COMMENT", "ID", "ATID", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecllist = 1
    RULE_classdecl = 2
    RULE_memberlist = 3
    RULE_member = 4
    RULE_attribute = 5
    RULE_vardecl = 6
    RULE_constdecl = 7
    RULE_attlistdecl = 8
    RULE_attlistnodecl = 9
    RULE_atttyp = 10
    RULE_typ = 11
    RULE_method = 12
    RULE_paramlist = 13
    RULE_params = 14
    RULE_param = 15
    RULE_blockstmt = 16
    RULE_parenexpr = 17
    RULE_exprlist = 18
    RULE_exprprime = 19
    RULE_exprstr = 20
    RULE_exprrel = 21
    RULE_exprlog = 22
    RULE_expradd = 23
    RULE_exprmul = 24
    RULE_exprnot = 25
    RULE_exprsign = 26
    RULE_exprindex = 27
    RULE_exprinst = 28
    RULE_exprstat = 29
    RULE_exprobj = 30
    RULE_exprparen = 31
    RULE_statpart = 32
    RULE_identifier = 33
    RULE_lit = 34
    RULE_boollit = 35
    RULE_arraylit = 36
    RULE_litlist = 37
    RULE_litprime = 38
    RULE_stmtlist = 39
    RULE_stmt = 40
    RULE_stmtassign = 41
    RULE_lhs = 42
    RULE_lhsinst = 43
    RULE_lhsstat = 44
    RULE_lhsparen = 45
    RULE_stmtinvoc = 46
    RULE_stmtinvocinst = 47
    RULE_stmtinvocstat = 48
    RULE_stmtdecl = 49

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "vardecl", "constdecl", "attlistdecl", 
                   "attlistnodecl", "atttyp", "typ", "method", "paramlist", 
                   "params", "param", "blockstmt", "parenexpr", "exprlist", 
                   "exprprime", "exprstr", "exprrel", "exprlog", "expradd", 
                   "exprmul", "exprnot", "exprsign", "exprindex", "exprinst", 
                   "exprstat", "exprobj", "exprparen", "statpart", "identifier", 
                   "lit", "boollit", "arraylit", "litlist", "litprime", 
                   "stmtlist", "stmt", "stmtassign", "lhs", "lhsinst", "lhsstat", 
                   "lhsparen", "stmtinvoc", "stmtinvocinst", "stmtinvocstat", 
                   "stmtdecl" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSE=4
    FOR=5
    TRUE=6
    FALSE=7
    INT=8
    FLOAT=9
    BOOL=10
    STRING=11
    RETURN=12
    NULL=13
    CLASS=14
    CONSTRUCTOR=15
    VAR=16
    SELF=17
    VOID=18
    CONST=19
    FUNC=20
    ADD=21
    SUB=22
    MUL=23
    DIVFLOAT=24
    DIVINT=25
    MOD=26
    NEG=27
    AND=28
    OR=29
    EQ=30
    NEQ=31
    LT=32
    LTEQ=33
    GT=34
    GTEQ=35
    DECLARE=36
    ASSIGN=37
    CONCATE=38
    LARROW=39
    NEW=40
    LPN=41
    RPN=42
    LBK=43
    RBK=44
    LBR=45
    RBR=46
    DOT=47
    CM=48
    SM=49
    COL=50
    INTLIT=51
    FLOATLIT=52
    STRLIT=53
    BLOCK_COMMENT=54
    LINE_COMMENT=55
    ID=56
    ATID=57
    WS=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecllist(self):
            return self.getTypedRuleContext(CSlangParser.ClassdecllistContext,0)


        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.classdecllist()
            self.state = 101
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(CSlangParser.ClassdeclContext,0)


        def classdecllist(self):
            return self.getTypedRuleContext(CSlangParser.ClassdecllistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classdecllist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassdecllist" ):
                listener.enterClassdecllist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassdecllist" ):
                listener.exitClassdecllist(self)




    def classdecllist(self):

        localctx = CSlangParser.ClassdecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecllist)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.classdecl()
                self.state = 104
                self.classdecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.classdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def LBR(self):
            return self.getToken(CSlangParser.LBR, 0)

        def memberlist(self):
            return self.getTypedRuleContext(CSlangParser.MemberlistContext,0)


        def RBR(self):
            return self.getToken(CSlangParser.RBR, 0)

        def LARROW(self):
            return self.getToken(CSlangParser.LARROW, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassdecl" ):
                listener.enterClassdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassdecl" ):
                listener.exitClassdecl(self)




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(CSlangParser.CLASS)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 110
                self.match(CSlangParser.ID)
                self.state = 111
                self.match(CSlangParser.LARROW)


            self.state = 114
            self.match(CSlangParser.ID)
            self.state = 115
            self.match(CSlangParser.LBR)
            self.state = 116
            self.memberlist()
            self.state = 117
            self.match(CSlangParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(CSlangParser.MemberContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(CSlangParser.MemberlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_memberlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberlist" ):
                listener.enterMemberlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberlist" ):
                listener.exitMemberlist(self)




    def memberlist(self):

        localctx = CSlangParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memberlist)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.member()
                self.state = 120
                self.memberlist()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def method(self):
            return self.getTypedRuleContext(CSlangParser.MethodContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember" ):
                listener.enterMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember" ):
                listener.exitMember(self)




    def member(self):

        localctx = CSlangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.attribute()
                self.state = 126
                self.match(CSlangParser.SM)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(CSlangParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = CSlangParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.vardecl()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.constdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def attlistdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistdeclContext,0)


        def attlistnodecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistnodeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_vardecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl" ):
                listener.enterVardecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl" ):
                listener.exitVardecl(self)




    def vardecl(self):

        localctx = CSlangParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(CSlangParser.VAR)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 136
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 137
                self.attlistnodecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attlistdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistdeclContext,0)


        def attlistnodecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistnodeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstdecl" ):
                listener.enterConstdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstdecl" ):
                listener.exitConstdecl(self)




    def constdecl(self):

        localctx = CSlangParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CSlangParser.CONST)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 141
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 142
                self.attlistnodecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttlistdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def attlistdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistdeclContext,0)


        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


        def DECLARE(self):
            return self.getToken(CSlangParser.DECLARE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attlistdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttlistdecl" ):
                listener.enterAttlistdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttlistdecl" ):
                listener.exitAttlistdecl(self)




    def attlistdecl(self):

        localctx = CSlangParser.AttlistdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attlistdecl)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.identifier()
                self.state = 146
                self.match(CSlangParser.CM)
                self.state = 147
                self.attlistdecl()
                self.state = 148
                self.match(CSlangParser.CM)
                self.state = 149
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.identifier()
                self.state = 152
                self.match(CSlangParser.COL)
                self.state = 153
                self.atttyp()
                self.state = 154
                self.match(CSlangParser.DECLARE)
                self.state = 155
                self.exprstr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttlistnodeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def attlistnodecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistnodeclContext,0)


        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attlistnodecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttlistnodecl" ):
                listener.enterAttlistnodecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttlistnodecl" ):
                listener.exitAttlistnodecl(self)




    def attlistnodecl(self):

        localctx = CSlangParser.AttlistnodeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attlistnodecl)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.identifier()
                self.state = 160
                self.match(CSlangParser.CM)
                self.state = 161
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.identifier()
                self.state = 164
                self.match(CSlangParser.COL)
                self.state = 165
                self.atttyp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtttypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_atttyp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtttyp" ):
                listener.enterAtttyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtttyp" ):
                listener.exitAtttyp(self)




    def atttyp(self):

        localctx = CSlangParser.AtttypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atttyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 169
                self.match(CSlangParser.LBK)
                self.state = 170
                self.match(CSlangParser.INTLIT)
                self.state = 171
                self.match(CSlangParser.RBK)


            self.state = 174
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594037931776) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(CSlangParser.FUNC)
                self.state = 179
                self.identifier()
                self.state = 180
                self.match(CSlangParser.LPN)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56 or _la==57:
                    self.state = 181
                    self.paramlist()


                self.state = 184
                self.match(CSlangParser.RPN)
                self.state = 185
                self.match(CSlangParser.COL)
                self.state = 188
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 9, 10, 11, 43, 56]:
                    self.state = 186
                    self.atttyp()
                    pass
                elif token in [18]:
                    self.state = 187
                    self.match(CSlangParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 190
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(CSlangParser.FUNC)
                self.state = 193
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 194
                self.match(CSlangParser.LPN)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56 or _la==57:
                    self.state = 195
                    self.paramlist()


                self.state = 198
                self.match(CSlangParser.RPN)
                self.state = 199
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(CSlangParser.ParamsContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamlist" ):
                listener.enterParamlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamlist" ):
                listener.exitParamlist(self)




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramlist)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.params()
                self.state = 203
                self.match(CSlangParser.CM)
                self.state = 204
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(CSlangParser.ParamContext,0)


        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def atttyp(self):
            return self.getTypedRuleContext(CSlangParser.AtttypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = CSlangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.param()
            self.state = 210
            self.match(CSlangParser.COL)
            self.state = 211
            self.atttyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def param(self):
            return self.getTypedRuleContext(CSlangParser.ParamContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.identifier()
                self.state = 214
                self.match(CSlangParser.CM)
                self.state = 215
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBR(self):
            return self.getToken(CSlangParser.LBR, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def RBR(self):
            return self.getToken(CSlangParser.RBR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_blockstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockstmt" ):
                listener.enterBlockstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockstmt" ):
                listener.exitBlockstmt(self)




    def blockstmt(self):

        localctx = CSlangParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(CSlangParser.LBR)
            self.state = 221
            self.stmtlist()
            self.state = 222
            self.match(CSlangParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(CSlangParser.ExprlistContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_parenexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenexpr" ):
                listener.enterParenexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenexpr" ):
                listener.exitParenexpr(self)




    def parenexpr(self):

        localctx = CSlangParser.ParenexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parenexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(CSlangParser.LPN)
            self.state = 225
            self.exprlist()
            self.state = 226
            self.match(CSlangParser.RPN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(CSlangParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprlist" ):
                listener.enterExprlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprlist" ):
                listener.exitExprlist(self)




    def exprlist(self):

        localctx = CSlangParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprlist)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 13, 17, 22, 27, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.exprprime()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def exprprime(self):
            return self.getTypedRuleContext(CSlangParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprprime" ):
                listener.enterExprprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprprime" ):
                listener.exitExprprime(self)




    def exprprime(self):

        localctx = CSlangParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprprime)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.exprstr()
                self.state = 233
                self.match(CSlangParser.CM)
                self.state = 234
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.exprstr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprrel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprrelContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprrelContext,i)


        def CONCATE(self):
            return self.getToken(CSlangParser.CONCATE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprstr" ):
                listener.enterExprstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprstr" ):
                listener.exitExprstr(self)




    def exprstr(self):

        localctx = CSlangParser.ExprstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exprstr)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.exprrel()
                self.state = 240
                self.match(CSlangParser.CONCATE)
                self.state = 241
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.exprrel()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprrelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlog(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprlogContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprlogContext,i)


        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CSlangParser.NEQ, 0)

        def LT(self):
            return self.getToken(CSlangParser.LT, 0)

        def LTEQ(self):
            return self.getToken(CSlangParser.LTEQ, 0)

        def GT(self):
            return self.getToken(CSlangParser.GT, 0)

        def GTEQ(self):
            return self.getToken(CSlangParser.GTEQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprrel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprrel" ):
                listener.enterExprrel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprrel" ):
                listener.exitExprrel(self)




    def exprrel(self):

        localctx = CSlangParser.ExprrelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exprrel)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.exprlog(0)
                self.state = 247
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.exprlog(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expradd(self):
            return self.getTypedRuleContext(CSlangParser.ExpraddContext,0)


        def exprlog(self):
            return self.getTypedRuleContext(CSlangParser.ExprlogContext,0)


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprlog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprlog" ):
                listener.enterExprlog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprlog" ):
                listener.exitExprlog(self)



    def exprlog(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprlogContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exprlog, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.expradd(0) 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpraddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprmul(self):
            return self.getTypedRuleContext(CSlangParser.ExprmulContext,0)


        def expradd(self):
            return self.getTypedRuleContext(CSlangParser.ExpraddContext,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expradd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpradd" ):
                listener.enterExpradd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpradd" ):
                listener.exitExpradd(self)



    def expradd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExpraddContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expradd, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 269
                    self.exprmul(0) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprmulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprnot(self):
            return self.getTypedRuleContext(CSlangParser.ExprnotContext,0)


        def exprmul(self):
            return self.getTypedRuleContext(CSlangParser.ExprmulContext,0)


        def MUL(self):
            return self.getToken(CSlangParser.MUL, 0)

        def DIVFLOAT(self):
            return self.getToken(CSlangParser.DIVFLOAT, 0)

        def DIVINT(self):
            return self.getToken(CSlangParser.DIVINT, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprmul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprmul" ):
                listener.enterExprmul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprmul" ):
                listener.exitExprmul(self)



    def exprmul(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprmulContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exprmul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 280
                    self.exprnot() 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprnotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEG(self):
            return self.getToken(CSlangParser.NEG, 0)

        def exprnot(self):
            return self.getTypedRuleContext(CSlangParser.ExprnotContext,0)


        def exprsign(self):
            return self.getTypedRuleContext(CSlangParser.ExprsignContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprnot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprnot" ):
                listener.enterExprnot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprnot" ):
                listener.exitExprnot(self)




    def exprnot(self):

        localctx = CSlangParser.ExprnotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exprnot)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(CSlangParser.NEG)
                self.state = 287
                self.exprnot()
                pass
            elif token in [6, 7, 13, 17, 22, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.exprsign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def exprsign(self):
            return self.getTypedRuleContext(CSlangParser.ExprsignContext,0)


        def exprindex(self):
            return self.getTypedRuleContext(CSlangParser.ExprindexContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprsign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprsign" ):
                listener.enterExprsign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprsign" ):
                listener.exitExprsign(self)




    def exprsign(self):

        localctx = CSlangParser.ExprsignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exprsign)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(CSlangParser.SUB)
                self.state = 292
                self.exprsign()
                pass
            elif token in [6, 7, 13, 17, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.exprindex()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprindexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exprindex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprindex" ):
                listener.enterExprindex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprindex" ):
                listener.exitExprindex(self)




    def exprindex(self):

        localctx = CSlangParser.ExprindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exprindex)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.exprinst(0)
                self.state = 297
                self.match(CSlangParser.LBK)
                self.state = 298
                self.exprstr()
                self.state = 299
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.exprinst(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprstat(self):
            return self.getTypedRuleContext(CSlangParser.ExprstatContext,0)


        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprinst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprinst" ):
                listener.enterExprinst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprinst" ):
                listener.exitExprinst(self)



    def exprinst(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprinstContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exprinst, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.exprstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprinst)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==43:
                        self.state = 308
                        self.match(CSlangParser.LBK)
                        self.state = 309
                        self.exprstr()
                        self.state = 310
                        self.match(CSlangParser.RBK)


                    self.state = 314
                    self.match(CSlangParser.DOT)
                    self.state = 315
                    self.match(CSlangParser.ID)
                    self.state = 317
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 316
                        self.parenexpr()

             
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statpart(self):
            return self.getTypedRuleContext(CSlangParser.StatpartContext,0)


        def exprobj(self):
            return self.getTypedRuleContext(CSlangParser.ExprobjContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprstat" ):
                listener.enterExprstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprstat" ):
                listener.exitExprstat(self)




    def exprstat(self):

        localctx = CSlangParser.ExprstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exprstat)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.statpart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.exprobj()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprobjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def exprparen(self):
            return self.getTypedRuleContext(CSlangParser.ExprparenContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprobj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprobj" ):
                listener.enterExprobj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprobj" ):
                listener.exitExprobj(self)




    def exprobj(self):

        localctx = CSlangParser.ExprobjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exprobj)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(CSlangParser.NEW)
                self.state = 329
                self.match(CSlangParser.ID)
                self.state = 330
                self.parenexpr()
                pass
            elif token in [6, 7, 13, 17, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.exprparen()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprparenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def lit(self):
            return self.getTypedRuleContext(CSlangParser.LitContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprparen

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprparen" ):
                listener.enterExprparen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprparen" ):
                listener.exitExprparen(self)




    def exprparen(self):

        localctx = CSlangParser.ExprparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exprparen)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(CSlangParser.LPN)
                self.state = 335
                self.exprstr()
                self.state = 336
                self.match(CSlangParser.RPN)
                pass
            elif token in [6, 7, 13, 17, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatpartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statpart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatpart" ):
                listener.enterStatpart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatpart" ):
                listener.exitStatpart(self)




    def statpart(self):

        localctx = CSlangParser.StatpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 341
                self.match(CSlangParser.ID)
                self.state = 342
                self.match(CSlangParser.DOT)


            self.state = 345
            self.match(CSlangParser.ATID)
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 346
                self.parenexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = CSlangParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            _la = self._input.LA(1)
            if not(_la==56 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(CSlangParser.BoollitContext,0)


        def STRLIT(self):
            return self.getToken(CSlangParser.STRLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(CSlangParser.ArraylitContext,0)


        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLit" ):
                listener.enterLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLit" ):
                listener.exitLit(self)




    def lit(self):

        localctx = CSlangParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_lit)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.boollit()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.match(CSlangParser.STRLIT)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                self.arraylit()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 356
                self.match(CSlangParser.NULL)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 357
                self.match(CSlangParser.SELF)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 8)
                self.state = 358
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoollitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_boollit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoollit" ):
                listener.enterBoollit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoollit" ):
                listener.exitBoollit(self)




    def boollit(self):

        localctx = CSlangParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def litprime(self):
            return self.getTypedRuleContext(CSlangParser.LitprimeContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraylit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraylit" ):
                listener.enterArraylit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraylit" ):
                listener.exitArraylit(self)




    def arraylit(self):

        localctx = CSlangParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(CSlangParser.LBK)
            self.state = 364
            self.litprime()
            self.state = 365
            self.match(CSlangParser.RBK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def litprime(self):
            return self.getTypedRuleContext(CSlangParser.LitprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_litlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitlist" ):
                listener.enterLitlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitlist" ):
                listener.exitLitlist(self)




    def litlist(self):

        localctx = CSlangParser.LitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_litlist)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 13, 17, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.litprime()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(CSlangParser.LitContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def litprime(self):
            return self.getTypedRuleContext(CSlangParser.LitprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_litprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitprime" ):
                listener.enterLitprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitprime" ):
                listener.exitLitprime(self)




    def litprime(self):

        localctx = CSlangParser.LitprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_litprime)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.lit()
                self.state = 372
                self.match(CSlangParser.CM)
                self.state = 373
                self.litprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtlist" ):
                listener.enterStmtlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtlist" ):
                listener.exitStmtlist(self)




    def stmtlist(self):

        localctx = CSlangParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmtlist)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 5, 6, 7, 12, 13, 16, 17, 19, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.stmt()
                self.state = 379
                self.stmtlist()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def blockstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.BlockstmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.BlockstmtContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def stmtassign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtassignContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtassignContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SM)
            else:
                return self.getToken(CSlangParser.SM, i)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def stmtinvoc(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocContext,0)


        def stmtdecl(self):
            return self.getTypedRuleContext(CSlangParser.StmtdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(CSlangParser.IF)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 385
                    self.blockstmt()


                self.state = 388
                self.exprstr()
                self.state = 389
                self.blockstmt()
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 390
                    self.match(CSlangParser.ELSE)
                    self.state = 391
                    self.blockstmt()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(CSlangParser.FOR)
                self.state = 395
                self.stmtassign()
                self.state = 396
                self.match(CSlangParser.SM)
                self.state = 397
                self.exprstr()
                self.state = 398
                self.match(CSlangParser.SM)
                self.state = 399
                self.stmtassign()
                self.state = 400
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16 or _la==19:
                    self.state = 402
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 405
                self.stmtassign()
                self.state = 406
                self.match(CSlangParser.SM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 408
                self.match(CSlangParser.BREAK)
                self.state = 409
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 410
                self.match(CSlangParser.CONTINUE)
                self.state = 411
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 412
                self.match(CSlangParser.RETURN)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 231947475576037568) != 0):
                    self.state = 413
                    self.exprstr()


                self.state = 416
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 417
                self.stmtinvoc()
                self.state = 418
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 420
                self.stmtdecl()
                self.state = 421
                self.match(CSlangParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtassign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtassign" ):
                listener.enterStmtassign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtassign" ):
                listener.exitStmtassign(self)




    def stmtassign(self):

        localctx = CSlangParser.StmtassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmtassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.lhs(0)
            self.state = 426
            self.match(CSlangParser.ASSIGN)
            self.state = 427
            self.exprstr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhsinst(self):
            return self.getTypedRuleContext(CSlangParser.LhsinstContext,0)


        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhs" ):
                listener.enterLhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhs" ):
                listener.exitLhs(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.lhsinst(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 432
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 433
                    self.match(CSlangParser.LBK)
                    self.state = 434
                    self.exprstr()
                    self.state = 435
                    self.match(CSlangParser.RBK) 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LhsinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhsstat(self):
            return self.getTypedRuleContext(CSlangParser.LhsstatContext,0)


        def lhsinst(self):
            return self.getTypedRuleContext(CSlangParser.LhsinstContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhsinst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhsinst" ):
                listener.enterLhsinst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhsinst" ):
                listener.exitLhsinst(self)



    def lhsinst(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.LhsinstContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_lhsinst, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.lhsstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhsinst)
                    self.state = 445
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 450
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==43:
                        self.state = 446
                        self.match(CSlangParser.LBK)
                        self.state = 447
                        self.exprstr()
                        self.state = 448
                        self.match(CSlangParser.RBK)


                    self.state = 452
                    self.match(CSlangParser.DOT)
                    self.state = 453
                    self.match(CSlangParser.ID)
                    self.state = 455
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        self.state = 454
                        self.parenexpr()

             
                self.state = 461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LhsstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statpart(self):
            return self.getTypedRuleContext(CSlangParser.StatpartContext,0)


        def lhsparen(self):
            return self.getTypedRuleContext(CSlangParser.LhsparenContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhsstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhsstat" ):
                listener.enterLhsstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhsstat" ):
                listener.exitLhsstat(self)




    def lhsstat(self):

        localctx = CSlangParser.LhsstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_lhsstat)
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.statpart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.lhsparen()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsparenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhsparen

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhsparen" ):
                listener.enterLhsparen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhsparen" ):
                listener.exitLhsparen(self)




    def lhsparen(self):

        localctx = CSlangParser.LhsparenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lhsparen)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(CSlangParser.LPN)
                self.state = 467
                self.lhs(0)
                self.state = 468
                self.match(CSlangParser.RPN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(CSlangParser.SELF)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtinvocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtinvocinst(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocinstContext,0)


        def stmtinvocstat(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocstatContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtinvoc" ):
                listener.enterStmtinvoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtinvoc" ):
                listener.exitStmtinvoc(self)




    def stmtinvoc(self):

        localctx = CSlangParser.StmtinvocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmtinvoc)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.stmtinvocinst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.stmtinvocstat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtinvocinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def exprstr(self):
            return self.getTypedRuleContext(CSlangParser.ExprstrContext,0)


        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvocinst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtinvocinst" ):
                listener.enterStmtinvocinst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtinvocinst" ):
                listener.exitStmtinvocinst(self)




    def stmtinvocinst(self):

        localctx = CSlangParser.StmtinvocinstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmtinvocinst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.exprinst(0)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 479
                self.match(CSlangParser.LBK)
                self.state = 480
                self.exprstr()
                self.state = 481
                self.match(CSlangParser.RBK)


            self.state = 485
            self.match(CSlangParser.DOT)
            self.state = 486
            self.match(CSlangParser.ID)
            self.state = 487
            self.parenexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtinvocstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvocstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtinvocstat" ):
                listener.enterStmtinvocstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtinvocstat" ):
                listener.exitStmtinvocstat(self)




    def stmtinvocstat(self):

        localctx = CSlangParser.StmtinvocstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmtinvocstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 489
                self.match(CSlangParser.ID)
                self.state = 490
                self.match(CSlangParser.DOT)


            self.state = 493
            self.match(CSlangParser.ATID)
            self.state = 494
            self.parenexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(CSlangParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtdecl" ):
                listener.enterStmtdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtdecl" ):
                listener.exitStmtdecl(self)




    def stmtdecl(self):

        localctx = CSlangParser.StmtdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmtdecl)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.vardecl()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.constdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.exprlog_sempred
        self._predicates[23] = self.expradd_sempred
        self._predicates[24] = self.exprmul_sempred
        self._predicates[28] = self.exprinst_sempred
        self._predicates[42] = self.lhs_sempred
        self._predicates[43] = self.lhsinst_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprlog_sempred(self, localctx:ExprlogContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expradd_sempred(self, localctx:ExpraddContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exprmul_sempred(self, localctx:ExprmulContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exprinst_sempred(self, localctx:ExprinstContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def lhsinst_sempred(self, localctx:LhsinstContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




