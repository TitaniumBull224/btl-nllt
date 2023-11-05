# Generated from d:/Program/XAMPP/htdocs/btl-nllt/assignment3/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
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
        4,1,61,494,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,106,8,1,
        1,2,1,2,1,2,3,2,111,8,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,
        122,8,3,1,4,1,4,1,4,1,4,3,4,128,8,4,1,5,1,5,3,5,132,8,5,1,6,1,6,
        1,6,3,6,137,8,6,1,7,1,7,1,7,3,7,142,8,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,156,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,166,8,9,1,10,1,10,1,10,3,10,171,8,10,1,10,1,10,1,11,1,11,
        1,12,1,12,1,12,1,12,3,12,181,8,12,1,12,1,12,1,12,1,12,3,12,187,8,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,195,8,12,1,12,1,12,3,12,199,
        8,12,1,13,1,13,1,13,1,13,1,13,3,13,206,8,13,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,3,15,217,8,15,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,18,1,18,3,18,229,8,18,1,19,1,19,1,19,1,19,1,19,
        3,19,236,8,19,1,20,1,20,1,20,1,20,1,20,3,20,243,8,20,1,21,1,21,1,
        21,1,21,1,21,3,21,250,8,21,1,22,1,22,1,22,1,22,1,22,1,22,5,22,258,
        8,22,10,22,12,22,261,9,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,269,
        8,23,10,23,12,23,272,9,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,280,
        8,24,10,24,12,24,283,9,24,1,25,1,25,1,25,3,25,288,8,25,1,26,1,26,
        1,26,3,26,293,8,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,301,8,27,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,311,8,28,1,28,1,28,1,
        28,3,28,316,8,28,5,28,318,8,28,10,28,12,28,321,9,28,1,29,1,29,3,
        29,325,8,29,1,29,1,29,3,29,329,8,29,1,29,3,29,332,8,29,1,30,1,30,
        1,30,1,30,3,30,338,8,30,1,31,1,31,1,31,1,31,1,31,3,31,345,8,31,1,
        32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,357,8,33,1,
        34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,3,36,367,8,36,1,37,1,37,1,
        37,1,37,1,37,3,37,374,8,37,1,38,1,38,1,38,1,38,3,38,380,8,38,1,39,
        1,39,3,39,384,8,39,1,39,1,39,1,39,1,39,3,39,390,8,39,1,39,1,39,1,
        39,1,39,1,39,1,39,1,39,1,39,1,39,3,39,401,8,39,1,39,1,39,1,39,1,
        39,1,39,1,39,1,39,1,39,1,39,3,39,412,8,39,1,39,1,39,1,39,1,39,1,
        39,1,39,1,39,3,39,421,8,39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,
        41,1,41,1,41,3,41,433,8,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,
        42,3,42,443,8,42,1,42,1,42,5,42,447,8,42,10,42,12,42,450,9,42,1,
        43,1,43,3,43,454,8,43,1,43,1,43,3,43,458,8,43,1,44,1,44,1,44,1,44,
        1,44,1,44,3,44,466,8,44,1,45,1,45,3,45,470,8,45,1,46,1,46,1,46,1,
        46,1,46,3,46,477,8,46,1,46,1,46,1,46,1,46,1,47,1,47,3,47,485,8,47,
        1,47,1,47,1,47,1,48,1,48,3,48,492,8,48,1,48,0,5,44,46,48,56,84,49,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,
        90,92,94,96,0,8,2,0,8,11,56,56,1,0,30,35,1,0,28,29,1,0,21,22,1,0,
        23,26,1,0,56,57,1,0,6,7,2,0,16,16,19,19,510,0,98,1,0,0,0,2,105,1,
        0,0,0,4,107,1,0,0,0,6,121,1,0,0,0,8,127,1,0,0,0,10,131,1,0,0,0,12,
        133,1,0,0,0,14,138,1,0,0,0,16,155,1,0,0,0,18,165,1,0,0,0,20,170,
        1,0,0,0,22,174,1,0,0,0,24,198,1,0,0,0,26,205,1,0,0,0,28,207,1,0,
        0,0,30,216,1,0,0,0,32,218,1,0,0,0,34,222,1,0,0,0,36,228,1,0,0,0,
        38,235,1,0,0,0,40,242,1,0,0,0,42,249,1,0,0,0,44,251,1,0,0,0,46,262,
        1,0,0,0,48,273,1,0,0,0,50,287,1,0,0,0,52,292,1,0,0,0,54,300,1,0,
        0,0,56,302,1,0,0,0,58,331,1,0,0,0,60,337,1,0,0,0,62,344,1,0,0,0,
        64,346,1,0,0,0,66,356,1,0,0,0,68,358,1,0,0,0,70,360,1,0,0,0,72,366,
        1,0,0,0,74,373,1,0,0,0,76,379,1,0,0,0,78,420,1,0,0,0,80,422,1,0,
        0,0,82,432,1,0,0,0,84,434,1,0,0,0,86,457,1,0,0,0,88,465,1,0,0,0,
        90,469,1,0,0,0,92,471,1,0,0,0,94,484,1,0,0,0,96,491,1,0,0,0,98,99,
        3,2,1,0,99,100,5,0,0,1,100,1,1,0,0,0,101,102,3,4,2,0,102,103,3,2,
        1,0,103,106,1,0,0,0,104,106,3,4,2,0,105,101,1,0,0,0,105,104,1,0,
        0,0,106,3,1,0,0,0,107,110,5,14,0,0,108,109,5,56,0,0,109,111,5,39,
        0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,5,56,
        0,0,113,114,5,45,0,0,114,115,3,6,3,0,115,116,5,46,0,0,116,5,1,0,
        0,0,117,118,3,8,4,0,118,119,3,6,3,0,119,122,1,0,0,0,120,122,1,0,
        0,0,121,117,1,0,0,0,121,120,1,0,0,0,122,7,1,0,0,0,123,124,3,10,5,
        0,124,125,5,49,0,0,125,128,1,0,0,0,126,128,3,24,12,0,127,123,1,0,
        0,0,127,126,1,0,0,0,128,9,1,0,0,0,129,132,3,12,6,0,130,132,3,14,
        7,0,131,129,1,0,0,0,131,130,1,0,0,0,132,11,1,0,0,0,133,136,5,16,
        0,0,134,137,3,16,8,0,135,137,3,18,9,0,136,134,1,0,0,0,136,135,1,
        0,0,0,137,13,1,0,0,0,138,141,5,19,0,0,139,142,3,16,8,0,140,142,3,
        18,9,0,141,139,1,0,0,0,141,140,1,0,0,0,142,15,1,0,0,0,143,144,3,
        64,32,0,144,145,5,48,0,0,145,146,3,16,8,0,146,147,5,48,0,0,147,148,
        3,40,20,0,148,156,1,0,0,0,149,150,3,64,32,0,150,151,5,50,0,0,151,
        152,3,20,10,0,152,153,5,36,0,0,153,154,3,40,20,0,154,156,1,0,0,0,
        155,143,1,0,0,0,155,149,1,0,0,0,156,17,1,0,0,0,157,158,3,64,32,0,
        158,159,5,48,0,0,159,160,3,18,9,0,160,166,1,0,0,0,161,162,3,64,32,
        0,162,163,5,50,0,0,163,164,3,20,10,0,164,166,1,0,0,0,165,157,1,0,
        0,0,165,161,1,0,0,0,166,19,1,0,0,0,167,168,5,43,0,0,168,169,5,51,
        0,0,169,171,5,44,0,0,170,167,1,0,0,0,170,171,1,0,0,0,171,172,1,0,
        0,0,172,173,3,22,11,0,173,21,1,0,0,0,174,175,7,0,0,0,175,23,1,0,
        0,0,176,177,5,20,0,0,177,178,3,64,32,0,178,180,5,41,0,0,179,181,
        3,26,13,0,180,179,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,
        5,42,0,0,183,186,5,50,0,0,184,187,3,20,10,0,185,187,5,18,0,0,186,
        184,1,0,0,0,186,185,1,0,0,0,187,188,1,0,0,0,188,189,3,32,16,0,189,
        199,1,0,0,0,190,191,5,20,0,0,191,192,5,15,0,0,192,194,5,41,0,0,193,
        195,3,26,13,0,194,193,1,0,0,0,194,195,1,0,0,0,195,196,1,0,0,0,196,
        197,5,42,0,0,197,199,3,32,16,0,198,176,1,0,0,0,198,190,1,0,0,0,199,
        25,1,0,0,0,200,201,3,28,14,0,201,202,5,48,0,0,202,203,3,26,13,0,
        203,206,1,0,0,0,204,206,3,28,14,0,205,200,1,0,0,0,205,204,1,0,0,
        0,206,27,1,0,0,0,207,208,3,30,15,0,208,209,5,50,0,0,209,210,3,20,
        10,0,210,29,1,0,0,0,211,212,3,64,32,0,212,213,5,48,0,0,213,214,3,
        30,15,0,214,217,1,0,0,0,215,217,3,64,32,0,216,211,1,0,0,0,216,215,
        1,0,0,0,217,31,1,0,0,0,218,219,5,45,0,0,219,220,3,76,38,0,220,221,
        5,46,0,0,221,33,1,0,0,0,222,223,5,41,0,0,223,224,3,36,18,0,224,225,
        5,42,0,0,225,35,1,0,0,0,226,229,3,38,19,0,227,229,1,0,0,0,228,226,
        1,0,0,0,228,227,1,0,0,0,229,37,1,0,0,0,230,231,3,40,20,0,231,232,
        5,48,0,0,232,233,3,38,19,0,233,236,1,0,0,0,234,236,3,40,20,0,235,
        230,1,0,0,0,235,234,1,0,0,0,236,39,1,0,0,0,237,238,3,42,21,0,238,
        239,5,38,0,0,239,240,3,42,21,0,240,243,1,0,0,0,241,243,3,42,21,0,
        242,237,1,0,0,0,242,241,1,0,0,0,243,41,1,0,0,0,244,245,3,44,22,0,
        245,246,7,1,0,0,246,247,3,44,22,0,247,250,1,0,0,0,248,250,3,44,22,
        0,249,244,1,0,0,0,249,248,1,0,0,0,250,43,1,0,0,0,251,252,6,22,-1,
        0,252,253,3,46,23,0,253,259,1,0,0,0,254,255,10,2,0,0,255,256,7,2,
        0,0,256,258,3,46,23,0,257,254,1,0,0,0,258,261,1,0,0,0,259,257,1,
        0,0,0,259,260,1,0,0,0,260,45,1,0,0,0,261,259,1,0,0,0,262,263,6,23,
        -1,0,263,264,3,48,24,0,264,270,1,0,0,0,265,266,10,2,0,0,266,267,
        7,3,0,0,267,269,3,48,24,0,268,265,1,0,0,0,269,272,1,0,0,0,270,268,
        1,0,0,0,270,271,1,0,0,0,271,47,1,0,0,0,272,270,1,0,0,0,273,274,6,
        24,-1,0,274,275,3,50,25,0,275,281,1,0,0,0,276,277,10,2,0,0,277,278,
        7,4,0,0,278,280,3,50,25,0,279,276,1,0,0,0,280,283,1,0,0,0,281,279,
        1,0,0,0,281,282,1,0,0,0,282,49,1,0,0,0,283,281,1,0,0,0,284,285,5,
        27,0,0,285,288,3,50,25,0,286,288,3,52,26,0,287,284,1,0,0,0,287,286,
        1,0,0,0,288,51,1,0,0,0,289,290,5,22,0,0,290,293,3,52,26,0,291,293,
        3,54,27,0,292,289,1,0,0,0,292,291,1,0,0,0,293,53,1,0,0,0,294,295,
        3,56,28,0,295,296,5,43,0,0,296,297,3,40,20,0,297,298,5,44,0,0,298,
        301,1,0,0,0,299,301,3,56,28,0,300,294,1,0,0,0,300,299,1,0,0,0,301,
        55,1,0,0,0,302,303,6,28,-1,0,303,304,3,58,29,0,304,319,1,0,0,0,305,
        310,10,2,0,0,306,307,5,43,0,0,307,308,3,40,20,0,308,309,5,44,0,0,
        309,311,1,0,0,0,310,306,1,0,0,0,310,311,1,0,0,0,311,312,1,0,0,0,
        312,313,5,47,0,0,313,315,5,56,0,0,314,316,3,34,17,0,315,314,1,0,
        0,0,315,316,1,0,0,0,316,318,1,0,0,0,317,305,1,0,0,0,318,321,1,0,
        0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,57,1,0,0,0,321,319,1,0,0,
        0,322,323,5,56,0,0,323,325,5,47,0,0,324,322,1,0,0,0,324,325,1,0,
        0,0,325,326,1,0,0,0,326,328,5,57,0,0,327,329,3,34,17,0,328,327,1,
        0,0,0,328,329,1,0,0,0,329,332,1,0,0,0,330,332,3,60,30,0,331,324,
        1,0,0,0,331,330,1,0,0,0,332,59,1,0,0,0,333,334,5,40,0,0,334,335,
        5,56,0,0,335,338,3,34,17,0,336,338,3,62,31,0,337,333,1,0,0,0,337,
        336,1,0,0,0,338,61,1,0,0,0,339,340,5,41,0,0,340,341,3,40,20,0,341,
        342,5,42,0,0,342,345,1,0,0,0,343,345,3,66,33,0,344,339,1,0,0,0,344,
        343,1,0,0,0,345,63,1,0,0,0,346,347,7,5,0,0,347,65,1,0,0,0,348,357,
        5,51,0,0,349,357,5,52,0,0,350,357,3,68,34,0,351,357,5,53,0,0,352,
        357,3,70,35,0,353,357,5,13,0,0,354,357,5,17,0,0,355,357,3,64,32,
        0,356,348,1,0,0,0,356,349,1,0,0,0,356,350,1,0,0,0,356,351,1,0,0,
        0,356,352,1,0,0,0,356,353,1,0,0,0,356,354,1,0,0,0,356,355,1,0,0,
        0,357,67,1,0,0,0,358,359,7,6,0,0,359,69,1,0,0,0,360,361,5,43,0,0,
        361,362,3,74,37,0,362,363,5,44,0,0,363,71,1,0,0,0,364,367,3,74,37,
        0,365,367,1,0,0,0,366,364,1,0,0,0,366,365,1,0,0,0,367,73,1,0,0,0,
        368,369,3,66,33,0,369,370,5,48,0,0,370,371,3,74,37,0,371,374,1,0,
        0,0,372,374,3,66,33,0,373,368,1,0,0,0,373,372,1,0,0,0,374,75,1,0,
        0,0,375,376,3,78,39,0,376,377,3,76,38,0,377,380,1,0,0,0,378,380,
        1,0,0,0,379,375,1,0,0,0,379,378,1,0,0,0,380,77,1,0,0,0,381,383,5,
        3,0,0,382,384,3,32,16,0,383,382,1,0,0,0,383,384,1,0,0,0,384,385,
        1,0,0,0,385,386,3,40,20,0,386,389,3,32,16,0,387,388,5,4,0,0,388,
        390,3,32,16,0,389,387,1,0,0,0,389,390,1,0,0,0,390,421,1,0,0,0,391,
        392,5,5,0,0,392,393,3,80,40,0,393,394,5,49,0,0,394,395,3,40,20,0,
        395,396,5,49,0,0,396,397,3,80,40,0,397,398,3,32,16,0,398,421,1,0,
        0,0,399,401,7,7,0,0,400,399,1,0,0,0,400,401,1,0,0,0,401,402,1,0,
        0,0,402,403,3,80,40,0,403,404,5,49,0,0,404,421,1,0,0,0,405,406,5,
        1,0,0,406,421,5,49,0,0,407,408,5,2,0,0,408,421,5,49,0,0,409,411,
        5,12,0,0,410,412,3,40,20,0,411,410,1,0,0,0,411,412,1,0,0,0,412,413,
        1,0,0,0,413,421,5,49,0,0,414,415,3,90,45,0,415,416,5,49,0,0,416,
        421,1,0,0,0,417,418,3,96,48,0,418,419,5,49,0,0,419,421,1,0,0,0,420,
        381,1,0,0,0,420,391,1,0,0,0,420,400,1,0,0,0,420,405,1,0,0,0,420,
        407,1,0,0,0,420,409,1,0,0,0,420,414,1,0,0,0,420,417,1,0,0,0,421,
        79,1,0,0,0,422,423,3,82,41,0,423,424,5,37,0,0,424,425,3,40,20,0,
        425,81,1,0,0,0,426,427,3,84,42,0,427,428,5,43,0,0,428,429,3,40,20,
        0,429,430,5,44,0,0,430,433,1,0,0,0,431,433,3,84,42,0,432,426,1,0,
        0,0,432,431,1,0,0,0,433,83,1,0,0,0,434,435,6,42,-1,0,435,436,3,86,
        43,0,436,448,1,0,0,0,437,442,10,2,0,0,438,439,5,43,0,0,439,440,3,
        40,20,0,440,441,5,44,0,0,441,443,1,0,0,0,442,438,1,0,0,0,442,443,
        1,0,0,0,443,444,1,0,0,0,444,445,5,47,0,0,445,447,5,56,0,0,446,437,
        1,0,0,0,447,450,1,0,0,0,448,446,1,0,0,0,448,449,1,0,0,0,449,85,1,
        0,0,0,450,448,1,0,0,0,451,452,5,56,0,0,452,454,5,47,0,0,453,451,
        1,0,0,0,453,454,1,0,0,0,454,455,1,0,0,0,455,458,5,57,0,0,456,458,
        3,88,44,0,457,453,1,0,0,0,457,456,1,0,0,0,458,87,1,0,0,0,459,460,
        5,41,0,0,460,461,3,82,41,0,461,462,5,42,0,0,462,466,1,0,0,0,463,
        466,5,17,0,0,464,466,3,64,32,0,465,459,1,0,0,0,465,463,1,0,0,0,465,
        464,1,0,0,0,466,89,1,0,0,0,467,470,3,92,46,0,468,470,3,94,47,0,469,
        467,1,0,0,0,469,468,1,0,0,0,470,91,1,0,0,0,471,476,3,56,28,0,472,
        473,5,43,0,0,473,474,3,40,20,0,474,475,5,44,0,0,475,477,1,0,0,0,
        476,472,1,0,0,0,476,477,1,0,0,0,477,478,1,0,0,0,478,479,5,47,0,0,
        479,480,5,56,0,0,480,481,3,34,17,0,481,93,1,0,0,0,482,483,5,56,0,
        0,483,485,5,47,0,0,484,482,1,0,0,0,484,485,1,0,0,0,485,486,1,0,0,
        0,486,487,5,57,0,0,487,488,3,34,17,0,488,95,1,0,0,0,489,492,3,12,
        6,0,490,492,3,14,7,0,491,489,1,0,0,0,491,490,1,0,0,0,492,97,1,0,
        0,0,53,105,110,121,127,131,136,141,155,165,170,180,186,194,198,205,
        216,228,235,242,249,259,270,281,287,292,300,310,315,319,324,328,
        331,337,344,356,366,373,379,383,389,400,411,420,432,442,448,453,
        457,465,469,476,484,491
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
    RULE_identifier = 32
    RULE_lit = 33
    RULE_boollit = 34
    RULE_arraylit = 35
    RULE_litlist = 36
    RULE_litprime = 37
    RULE_stmtlist = 38
    RULE_stmt = 39
    RULE_stmtassign = 40
    RULE_lhs = 41
    RULE_lhsinst = 42
    RULE_lhsstat = 43
    RULE_lhsparen = 44
    RULE_stmtinvoc = 45
    RULE_stmtinvocinst = 46
    RULE_stmtinvocstat = 47
    RULE_stmtdecl = 48

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "vardecl", "constdecl", "attlistdecl", 
                   "attlistnodecl", "atttyp", "typ", "method", "paramlist", 
                   "params", "param", "blockstmt", "parenexpr", "exprlist", 
                   "exprprime", "exprstr", "exprrel", "exprlog", "expradd", 
                   "exprmul", "exprnot", "exprsign", "exprindex", "exprinst", 
                   "exprstat", "exprobj", "exprparen", "identifier", "lit", 
                   "boollit", "arraylit", "litlist", "litprime", "stmtlist", 
                   "stmt", "stmtassign", "lhs", "lhsinst", "lhsstat", "lhsparen", 
                   "stmtinvoc", "stmtinvocinst", "stmtinvocstat", "stmtdecl" ]

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
            self.state = 98
            self.classdecllist()
            self.state = 99
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
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.classdecl()
                self.state = 102
                self.classdecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
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
            self.state = 107
            self.match(CSlangParser.CLASS)
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 108
                self.match(CSlangParser.ID)
                self.state = 109
                self.match(CSlangParser.LARROW)


            self.state = 112
            self.match(CSlangParser.ID)
            self.state = 113
            self.match(CSlangParser.LBR)
            self.state = 114
            self.memberlist()
            self.state = 115
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.member()
                self.state = 118
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
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.attribute()
                self.state = 124
                self.match(CSlangParser.SM)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.vardecl()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
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
            self.state = 133
            self.match(CSlangParser.VAR)
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 134
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 135
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
            self.state = 138
            self.match(CSlangParser.CONST)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 139
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 140
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
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.identifier()
                self.state = 144
                self.match(CSlangParser.CM)
                self.state = 145
                self.attlistdecl()
                self.state = 146
                self.match(CSlangParser.CM)
                self.state = 147
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.identifier()
                self.state = 150
                self.match(CSlangParser.COL)
                self.state = 151
                self.atttyp()
                self.state = 152
                self.match(CSlangParser.DECLARE)
                self.state = 153
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
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.identifier()
                self.state = 158
                self.match(CSlangParser.CM)
                self.state = 159
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.identifier()
                self.state = 162
                self.match(CSlangParser.COL)
                self.state = 163
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
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 167
                self.match(CSlangParser.LBK)
                self.state = 168
                self.match(CSlangParser.INTLIT)
                self.state = 169
                self.match(CSlangParser.RBK)


            self.state = 172
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
            self.state = 174
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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(CSlangParser.FUNC)
                self.state = 177
                self.identifier()
                self.state = 178
                self.match(CSlangParser.LPN)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56 or _la==57:
                    self.state = 179
                    self.paramlist()


                self.state = 182
                self.match(CSlangParser.RPN)
                self.state = 183
                self.match(CSlangParser.COL)
                self.state = 186
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 9, 10, 11, 43, 56]:
                    self.state = 184
                    self.atttyp()
                    pass
                elif token in [18]:
                    self.state = 185
                    self.match(CSlangParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 188
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(CSlangParser.FUNC)
                self.state = 191
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 192
                self.match(CSlangParser.LPN)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56 or _la==57:
                    self.state = 193
                    self.paramlist()


                self.state = 196
                self.match(CSlangParser.RPN)
                self.state = 197
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
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.params()
                self.state = 201
                self.match(CSlangParser.CM)
                self.state = 202
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
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
            self.state = 207
            self.param()
            self.state = 208
            self.match(CSlangParser.COL)
            self.state = 209
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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.identifier()
                self.state = 212
                self.match(CSlangParser.CM)
                self.state = 213
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
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
            self.state = 218
            self.match(CSlangParser.LBR)
            self.state = 219
            self.stmtlist()
            self.state = 220
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
            self.state = 222
            self.match(CSlangParser.LPN)
            self.state = 223
            self.exprlist()
            self.state = 224
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
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 13, 17, 22, 27, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
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
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.exprstr()
                self.state = 231
                self.match(CSlangParser.CM)
                self.state = 232
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
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
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.exprrel()
                self.state = 238
                self.match(CSlangParser.CONCATE)
                self.state = 239
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
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
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.exprlog(0)
                self.state = 245
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
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
            self.state = 252
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.expradd(0) 
                self.state = 261
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
            self.state = 263
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 267
                    self.exprmul(0) 
                self.state = 272
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
            self.state = 274
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 276
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 277
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 278
                    self.exprnot() 
                self.state = 283
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
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(CSlangParser.NEG)
                self.state = 285
                self.exprnot()
                pass
            elif token in [6, 7, 13, 17, 22, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
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
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(CSlangParser.SUB)
                self.state = 290
                self.exprsign()
                pass
            elif token in [6, 7, 13, 17, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.exprinst(0)
                self.state = 295
                self.match(CSlangParser.LBK)
                self.state = 296
                self.exprstr()
                self.state = 297
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
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
            self.state = 303
            self.exprstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprinst)
                    self.state = 305
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==43:
                        self.state = 306
                        self.match(CSlangParser.LBK)
                        self.state = 307
                        self.exprstr()
                        self.state = 308
                        self.match(CSlangParser.RBK)


                    self.state = 312
                    self.match(CSlangParser.DOT)
                    self.state = 313
                    self.match(CSlangParser.ID)
                    self.state = 315
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 314
                        self.parenexpr()

             
                self.state = 321
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

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56:
                    self.state = 322
                    self.match(CSlangParser.ID)
                    self.state = 323
                    self.match(CSlangParser.DOT)


                self.state = 326
                self.match(CSlangParser.ATID)
                self.state = 328
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 327
                    self.parenexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(CSlangParser.NEW)
                self.state = 334
                self.match(CSlangParser.ID)
                self.state = 335
                self.parenexpr()
                pass
            elif token in [6, 7, 13, 17, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
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
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(CSlangParser.LPN)
                self.state = 340
                self.exprstr()
                self.state = 341
                self.match(CSlangParser.RPN)
                pass
            elif token in [6, 7, 13, 17, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
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
        self.enterRule(localctx, 64, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
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
        self.enterRule(localctx, 66, self.RULE_lit)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.boollit()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.match(CSlangParser.STRLIT)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 352
                self.arraylit()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 353
                self.match(CSlangParser.NULL)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 354
                self.match(CSlangParser.SELF)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 8)
                self.state = 355
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
        self.enterRule(localctx, 68, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
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
        self.enterRule(localctx, 70, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(CSlangParser.LBK)
            self.state = 361
            self.litprime()
            self.state = 362
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
        self.enterRule(localctx, 72, self.RULE_litlist)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 13, 17, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
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
        self.enterRule(localctx, 74, self.RULE_litprime)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.lit()
                self.state = 369
                self.match(CSlangParser.CM)
                self.state = 370
                self.litprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
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
        self.enterRule(localctx, 76, self.RULE_stmtlist)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 5, 6, 7, 12, 13, 16, 17, 19, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.stmt()
                self.state = 376
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
        self.enterRule(localctx, 78, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(CSlangParser.IF)
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 382
                    self.blockstmt()


                self.state = 385
                self.exprstr()
                self.state = 386
                self.blockstmt()
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 387
                    self.match(CSlangParser.ELSE)
                    self.state = 388
                    self.blockstmt()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.match(CSlangParser.FOR)
                self.state = 392
                self.stmtassign()
                self.state = 393
                self.match(CSlangParser.SM)
                self.state = 394
                self.exprstr()
                self.state = 395
                self.match(CSlangParser.SM)
                self.state = 396
                self.stmtassign()
                self.state = 397
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16 or _la==19:
                    self.state = 399
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 402
                self.stmtassign()
                self.state = 403
                self.match(CSlangParser.SM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 405
                self.match(CSlangParser.BREAK)
                self.state = 406
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 407
                self.match(CSlangParser.CONTINUE)
                self.state = 408
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 409
                self.match(CSlangParser.RETURN)
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 231947475576037568) != 0):
                    self.state = 410
                    self.exprstr()


                self.state = 413
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 414
                self.stmtinvoc()
                self.state = 415
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 417
                self.stmtdecl()
                self.state = 418
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
        self.enterRule(localctx, 80, self.RULE_stmtassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.lhs()
            self.state = 423
            self.match(CSlangParser.ASSIGN)
            self.state = 424
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




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_lhs)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.lhsinst(0)
                self.state = 427
                self.match(CSlangParser.LBK)
                self.state = 428
                self.exprstr()
                self.state = 429
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.lhsinst(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_lhsinst, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.lhsstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhsinst)
                    self.state = 437
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 442
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==43:
                        self.state = 438
                        self.match(CSlangParser.LBK)
                        self.state = 439
                        self.exprstr()
                        self.state = 440
                        self.match(CSlangParser.RBK)


                    self.state = 444
                    self.match(CSlangParser.DOT)
                    self.state = 445
                    self.match(CSlangParser.ID) 
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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

        def ATID(self):
            return self.getToken(CSlangParser.ATID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

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
        self.enterRule(localctx, 86, self.RULE_lhsstat)
        self._la = 0 # Token type
        try:
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56:
                    self.state = 451
                    self.match(CSlangParser.ID)
                    self.state = 452
                    self.match(CSlangParser.DOT)


                self.state = 455
                self.match(CSlangParser.ATID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
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
        self.enterRule(localctx, 88, self.RULE_lhsparen)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.match(CSlangParser.LPN)
                self.state = 460
                self.lhs()
                self.state = 461
                self.match(CSlangParser.RPN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.match(CSlangParser.SELF)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
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
        self.enterRule(localctx, 90, self.RULE_stmtinvoc)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.stmtinvocinst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
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
        self.enterRule(localctx, 92, self.RULE_stmtinvocinst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.exprinst(0)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 472
                self.match(CSlangParser.LBK)
                self.state = 473
                self.exprstr()
                self.state = 474
                self.match(CSlangParser.RBK)


            self.state = 478
            self.match(CSlangParser.DOT)
            self.state = 479
            self.match(CSlangParser.ID)
            self.state = 480
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
        self.enterRule(localctx, 94, self.RULE_stmtinvocstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 482
                self.match(CSlangParser.ID)
                self.state = 483
                self.match(CSlangParser.DOT)


            self.state = 486
            self.match(CSlangParser.ATID)
            self.state = 487
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
        self.enterRule(localctx, 96, self.RULE_stmtdecl)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.vardecl()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
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
        self._predicates[42] = self.lhsinst_sempred
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
         

    def lhsinst_sempred(self, localctx:LhsinstContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




