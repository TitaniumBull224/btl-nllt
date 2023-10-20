# Generated from d:/Program/XAMPP/htdocs/btl-nllt/assignment1/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
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
        4,1,61,506,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,100,8,1,1,2,1,2,1,2,1,2,3,2,106,8,2,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,117,8,3,1,4,1,4,1,4,1,4,
        3,4,123,8,4,1,5,1,5,1,5,3,5,128,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,142,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,152,8,7,1,8,1,8,3,8,156,8,8,1,8,1,8,3,8,160,8,8,1,9,1,9,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        3,12,178,8,12,1,12,1,12,1,12,1,12,3,12,184,8,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,193,8,12,1,12,1,12,3,12,197,8,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,3,13,207,8,13,1,14,1,14,1,14,1,14,
        3,14,213,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,
        3,17,225,8,17,1,18,1,18,1,18,1,18,1,18,3,18,232,8,18,1,19,1,19,1,
        19,1,19,1,19,3,19,239,8,19,1,20,1,20,1,20,1,20,1,20,3,20,246,8,20,
        1,21,1,21,1,21,1,21,1,21,1,21,5,21,254,8,21,10,21,12,21,257,9,21,
        1,22,1,22,1,22,1,22,1,22,1,22,5,22,265,8,22,10,22,12,22,268,9,22,
        1,23,1,23,1,23,1,23,1,23,1,23,5,23,276,8,23,10,23,12,23,279,9,23,
        1,24,1,24,1,24,3,24,284,8,24,1,25,1,25,1,25,3,25,289,8,25,1,26,1,
        26,1,26,1,26,1,26,1,26,3,26,297,8,26,1,27,1,27,1,27,1,27,1,27,1,
        27,3,27,305,8,27,1,27,3,27,308,8,27,1,27,1,27,1,27,1,27,1,27,3,27,
        315,8,27,5,27,317,8,27,10,27,12,27,320,9,27,1,28,1,28,1,28,3,28,
        325,8,28,1,28,1,28,1,28,3,28,330,8,28,1,28,3,28,333,8,28,1,29,1,
        29,1,29,1,29,3,29,339,8,29,1,30,1,30,1,30,1,30,1,30,1,30,3,30,347,
        8,30,1,31,1,31,1,32,1,32,1,32,1,32,1,32,3,32,356,8,32,1,33,1,33,
        1,33,1,33,1,33,3,33,363,8,33,1,33,1,33,1,34,1,34,1,34,1,34,3,34,
        371,8,34,1,35,1,35,1,35,1,35,3,35,377,8,35,1,36,1,36,1,36,1,36,1,
        36,3,36,384,8,36,1,37,1,37,1,37,1,37,3,37,390,8,37,1,38,1,38,1,39,
        1,39,1,39,1,39,3,39,398,8,39,1,40,1,40,1,40,3,40,403,8,40,1,40,1,
        40,1,40,1,40,1,40,1,40,3,40,411,8,40,1,40,1,40,1,40,1,40,1,40,3,
        40,418,8,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,1,40,3,40,435,8,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,3,40,444,8,40,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,
        42,1,42,1,42,1,42,5,42,458,8,42,10,42,12,42,461,9,42,1,43,1,43,1,
        43,1,43,1,43,1,43,3,43,469,8,43,1,43,3,43,472,8,43,1,43,1,43,1,43,
        1,43,1,43,3,43,479,8,43,5,43,481,8,43,10,43,12,43,484,9,43,1,44,
        1,44,1,44,3,44,489,8,44,1,44,1,44,1,44,3,44,494,8,44,1,44,3,44,497,
        8,44,1,45,1,45,1,45,1,45,1,45,3,45,504,8,45,1,45,0,6,42,44,46,54,
        84,86,46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,
        84,86,88,90,0,9,2,0,16,16,19,19,1,0,8,11,1,0,30,35,1,0,28,29,1,0,
        21,22,1,0,23,26,2,0,17,17,56,56,1,0,56,57,1,0,6,7,527,0,92,1,0,0,
        0,2,99,1,0,0,0,4,101,1,0,0,0,6,116,1,0,0,0,8,122,1,0,0,0,10,124,
        1,0,0,0,12,141,1,0,0,0,14,151,1,0,0,0,16,159,1,0,0,0,18,161,1,0,
        0,0,20,163,1,0,0,0,22,167,1,0,0,0,24,196,1,0,0,0,26,206,1,0,0,0,
        28,212,1,0,0,0,30,214,1,0,0,0,32,218,1,0,0,0,34,224,1,0,0,0,36,231,
        1,0,0,0,38,238,1,0,0,0,40,245,1,0,0,0,42,247,1,0,0,0,44,258,1,0,
        0,0,46,269,1,0,0,0,48,283,1,0,0,0,50,288,1,0,0,0,52,296,1,0,0,0,
        54,307,1,0,0,0,56,332,1,0,0,0,58,338,1,0,0,0,60,346,1,0,0,0,62,348,
        1,0,0,0,64,355,1,0,0,0,66,357,1,0,0,0,68,370,1,0,0,0,70,376,1,0,
        0,0,72,383,1,0,0,0,74,389,1,0,0,0,76,391,1,0,0,0,78,397,1,0,0,0,
        80,443,1,0,0,0,82,445,1,0,0,0,84,449,1,0,0,0,86,471,1,0,0,0,88,496,
        1,0,0,0,90,503,1,0,0,0,92,93,3,2,1,0,93,94,5,0,0,1,94,1,1,0,0,0,
        95,96,3,4,2,0,96,97,3,2,1,0,97,100,1,0,0,0,98,100,3,4,2,0,99,95,
        1,0,0,0,99,98,1,0,0,0,100,3,1,0,0,0,101,105,5,14,0,0,102,103,5,56,
        0,0,103,106,5,39,0,0,104,106,1,0,0,0,105,102,1,0,0,0,105,104,1,0,
        0,0,106,107,1,0,0,0,107,108,5,56,0,0,108,109,5,45,0,0,109,110,3,
        6,3,0,110,111,5,46,0,0,111,5,1,0,0,0,112,113,3,8,4,0,113,114,3,6,
        3,0,114,117,1,0,0,0,115,117,1,0,0,0,116,112,1,0,0,0,116,115,1,0,
        0,0,117,7,1,0,0,0,118,119,3,10,5,0,119,120,5,49,0,0,120,123,1,0,
        0,0,121,123,3,24,12,0,122,118,1,0,0,0,122,121,1,0,0,0,123,9,1,0,
        0,0,124,127,7,0,0,0,125,128,3,12,6,0,126,128,3,14,7,0,127,125,1,
        0,0,0,127,126,1,0,0,0,128,11,1,0,0,0,129,130,3,62,31,0,130,131,5,
        48,0,0,131,132,3,12,6,0,132,133,5,48,0,0,133,134,3,38,19,0,134,142,
        1,0,0,0,135,136,3,62,31,0,136,137,5,50,0,0,137,138,3,16,8,0,138,
        139,5,36,0,0,139,140,3,38,19,0,140,142,1,0,0,0,141,129,1,0,0,0,141,
        135,1,0,0,0,142,13,1,0,0,0,143,144,3,62,31,0,144,145,5,48,0,0,145,
        146,3,14,7,0,146,152,1,0,0,0,147,148,3,62,31,0,148,149,5,50,0,0,
        149,150,3,16,8,0,150,152,1,0,0,0,151,143,1,0,0,0,151,147,1,0,0,0,
        152,15,1,0,0,0,153,156,3,20,10,0,154,156,1,0,0,0,155,153,1,0,0,0,
        155,154,1,0,0,0,156,157,1,0,0,0,157,160,3,18,9,0,158,160,3,22,11,
        0,159,155,1,0,0,0,159,158,1,0,0,0,160,17,1,0,0,0,161,162,7,1,0,0,
        162,19,1,0,0,0,163,164,5,43,0,0,164,165,5,51,0,0,165,166,5,44,0,
        0,166,21,1,0,0,0,167,168,5,40,0,0,168,169,5,56,0,0,169,170,5,41,
        0,0,170,171,5,42,0,0,171,23,1,0,0,0,172,173,5,20,0,0,173,174,3,62,
        31,0,174,177,5,41,0,0,175,178,3,26,13,0,176,178,1,0,0,0,177,175,
        1,0,0,0,177,176,1,0,0,0,178,179,1,0,0,0,179,180,5,42,0,0,180,183,
        5,50,0,0,181,184,3,18,9,0,182,184,5,18,0,0,183,181,1,0,0,0,183,182,
        1,0,0,0,184,185,1,0,0,0,185,186,3,30,15,0,186,197,1,0,0,0,187,188,
        5,20,0,0,188,189,5,15,0,0,189,192,5,41,0,0,190,193,3,26,13,0,191,
        193,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,0,193,194,1,0,0,0,194,
        195,5,42,0,0,195,197,3,30,15,0,196,172,1,0,0,0,196,187,1,0,0,0,197,
        25,1,0,0,0,198,199,3,28,14,0,199,200,5,48,0,0,200,201,3,26,13,0,
        201,207,1,0,0,0,202,203,3,28,14,0,203,204,5,50,0,0,204,205,3,18,
        9,0,205,207,1,0,0,0,206,198,1,0,0,0,206,202,1,0,0,0,207,27,1,0,0,
        0,208,209,5,56,0,0,209,210,5,48,0,0,210,213,3,28,14,0,211,213,5,
        56,0,0,212,208,1,0,0,0,212,211,1,0,0,0,213,29,1,0,0,0,214,215,5,
        45,0,0,215,216,3,78,39,0,216,217,5,46,0,0,217,31,1,0,0,0,218,219,
        5,41,0,0,219,220,3,34,17,0,220,221,5,42,0,0,221,33,1,0,0,0,222,225,
        3,36,18,0,223,225,1,0,0,0,224,222,1,0,0,0,224,223,1,0,0,0,225,35,
        1,0,0,0,226,227,3,38,19,0,227,228,5,48,0,0,228,229,3,34,17,0,229,
        232,1,0,0,0,230,232,3,38,19,0,231,226,1,0,0,0,231,230,1,0,0,0,232,
        37,1,0,0,0,233,234,3,40,20,0,234,235,5,38,0,0,235,236,3,40,20,0,
        236,239,1,0,0,0,237,239,3,40,20,0,238,233,1,0,0,0,238,237,1,0,0,
        0,239,39,1,0,0,0,240,241,3,42,21,0,241,242,7,2,0,0,242,243,3,42,
        21,0,243,246,1,0,0,0,244,246,3,42,21,0,245,240,1,0,0,0,245,244,1,
        0,0,0,246,41,1,0,0,0,247,248,6,21,-1,0,248,249,3,44,22,0,249,255,
        1,0,0,0,250,251,10,2,0,0,251,252,7,3,0,0,252,254,3,44,22,0,253,250,
        1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,43,1,
        0,0,0,257,255,1,0,0,0,258,259,6,22,-1,0,259,260,3,46,23,0,260,266,
        1,0,0,0,261,262,10,2,0,0,262,263,7,4,0,0,263,265,3,46,23,0,264,261,
        1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,45,1,
        0,0,0,268,266,1,0,0,0,269,270,6,23,-1,0,270,271,3,48,24,0,271,277,
        1,0,0,0,272,273,10,2,0,0,273,274,7,5,0,0,274,276,3,48,24,0,275,272,
        1,0,0,0,276,279,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,47,1,
        0,0,0,279,277,1,0,0,0,280,281,5,27,0,0,281,284,3,48,24,0,282,284,
        3,50,25,0,283,280,1,0,0,0,283,282,1,0,0,0,284,49,1,0,0,0,285,286,
        5,22,0,0,286,289,3,50,25,0,287,289,3,52,26,0,288,285,1,0,0,0,288,
        287,1,0,0,0,289,51,1,0,0,0,290,291,3,54,27,0,291,292,5,43,0,0,292,
        293,3,38,19,0,293,294,5,44,0,0,294,297,1,0,0,0,295,297,3,54,27,0,
        296,290,1,0,0,0,296,295,1,0,0,0,297,53,1,0,0,0,298,299,6,27,-1,0,
        299,300,5,17,0,0,300,301,5,47,0,0,301,304,5,56,0,0,302,305,3,32,
        16,0,303,305,1,0,0,0,304,302,1,0,0,0,304,303,1,0,0,0,305,308,1,0,
        0,0,306,308,3,56,28,0,307,298,1,0,0,0,307,306,1,0,0,0,308,318,1,
        0,0,0,309,310,10,3,0,0,310,311,5,47,0,0,311,314,5,56,0,0,312,315,
        3,32,16,0,313,315,1,0,0,0,314,312,1,0,0,0,314,313,1,0,0,0,315,317,
        1,0,0,0,316,309,1,0,0,0,317,320,1,0,0,0,318,316,1,0,0,0,318,319,
        1,0,0,0,319,55,1,0,0,0,320,318,1,0,0,0,321,322,7,6,0,0,322,325,5,
        47,0,0,323,325,1,0,0,0,324,321,1,0,0,0,324,323,1,0,0,0,325,326,1,
        0,0,0,326,329,5,57,0,0,327,330,3,32,16,0,328,330,1,0,0,0,329,327,
        1,0,0,0,329,328,1,0,0,0,330,333,1,0,0,0,331,333,3,58,29,0,332,324,
        1,0,0,0,332,331,1,0,0,0,333,57,1,0,0,0,334,335,5,40,0,0,335,336,
        5,56,0,0,336,339,3,32,16,0,337,339,3,60,30,0,338,334,1,0,0,0,338,
        337,1,0,0,0,339,59,1,0,0,0,340,341,5,41,0,0,341,342,3,38,19,0,342,
        343,5,42,0,0,343,347,1,0,0,0,344,347,3,62,31,0,345,347,3,64,32,0,
        346,340,1,0,0,0,346,344,1,0,0,0,346,345,1,0,0,0,347,61,1,0,0,0,348,
        349,7,7,0,0,349,63,1,0,0,0,350,356,5,51,0,0,351,356,5,52,0,0,352,
        356,3,76,38,0,353,356,5,53,0,0,354,356,3,66,33,0,355,350,1,0,0,0,
        355,351,1,0,0,0,355,352,1,0,0,0,355,353,1,0,0,0,355,354,1,0,0,0,
        356,65,1,0,0,0,357,362,5,43,0,0,358,363,3,68,34,0,359,363,3,70,35,
        0,360,363,3,72,36,0,361,363,3,74,37,0,362,358,1,0,0,0,362,359,1,
        0,0,0,362,360,1,0,0,0,362,361,1,0,0,0,363,364,1,0,0,0,364,365,5,
        44,0,0,365,67,1,0,0,0,366,367,5,51,0,0,367,368,5,48,0,0,368,371,
        3,68,34,0,369,371,5,51,0,0,370,366,1,0,0,0,370,369,1,0,0,0,371,69,
        1,0,0,0,372,373,5,52,0,0,373,374,5,48,0,0,374,377,3,70,35,0,375,
        377,5,52,0,0,376,372,1,0,0,0,376,375,1,0,0,0,377,71,1,0,0,0,378,
        379,3,76,38,0,379,380,5,48,0,0,380,381,3,72,36,0,381,384,1,0,0,0,
        382,384,3,76,38,0,383,378,1,0,0,0,383,382,1,0,0,0,384,73,1,0,0,0,
        385,386,5,53,0,0,386,387,5,48,0,0,387,390,3,74,37,0,388,390,5,53,
        0,0,389,385,1,0,0,0,389,388,1,0,0,0,390,75,1,0,0,0,391,392,7,8,0,
        0,392,77,1,0,0,0,393,394,3,80,40,0,394,395,3,78,39,0,395,398,1,0,
        0,0,396,398,1,0,0,0,397,393,1,0,0,0,397,396,1,0,0,0,398,79,1,0,0,
        0,399,403,5,16,0,0,400,403,5,19,0,0,401,403,1,0,0,0,402,399,1,0,
        0,0,402,400,1,0,0,0,402,401,1,0,0,0,403,404,1,0,0,0,404,405,3,82,
        41,0,405,406,5,49,0,0,406,444,1,0,0,0,407,410,5,3,0,0,408,411,3,
        30,15,0,409,411,1,0,0,0,410,408,1,0,0,0,410,409,1,0,0,0,411,412,
        1,0,0,0,412,413,3,38,19,0,413,417,3,30,15,0,414,415,5,4,0,0,415,
        418,3,30,15,0,416,418,1,0,0,0,417,414,1,0,0,0,417,416,1,0,0,0,418,
        444,1,0,0,0,419,420,5,5,0,0,420,421,3,82,41,0,421,422,5,49,0,0,422,
        423,3,40,20,0,423,424,5,49,0,0,424,425,3,82,41,0,425,426,3,30,15,
        0,426,444,1,0,0,0,427,428,5,1,0,0,428,444,5,49,0,0,429,430,5,2,0,
        0,430,444,5,49,0,0,431,434,5,12,0,0,432,435,3,38,19,0,433,435,1,
        0,0,0,434,432,1,0,0,0,434,433,1,0,0,0,435,436,1,0,0,0,436,444,5,
        49,0,0,437,438,3,54,27,0,438,439,5,49,0,0,439,444,1,0,0,0,440,441,
        3,10,5,0,441,442,5,49,0,0,442,444,1,0,0,0,443,402,1,0,0,0,443,407,
        1,0,0,0,443,419,1,0,0,0,443,427,1,0,0,0,443,429,1,0,0,0,443,431,
        1,0,0,0,443,437,1,0,0,0,443,440,1,0,0,0,444,81,1,0,0,0,445,446,3,
        84,42,0,446,447,5,37,0,0,447,448,3,38,19,0,448,83,1,0,0,0,449,450,
        6,42,-1,0,450,451,3,86,43,0,451,459,1,0,0,0,452,453,10,2,0,0,453,
        454,5,43,0,0,454,455,3,38,19,0,455,456,5,44,0,0,456,458,1,0,0,0,
        457,452,1,0,0,0,458,461,1,0,0,0,459,457,1,0,0,0,459,460,1,0,0,0,
        460,85,1,0,0,0,461,459,1,0,0,0,462,463,6,43,-1,0,463,464,5,17,0,
        0,464,465,5,47,0,0,465,468,5,56,0,0,466,469,3,32,16,0,467,469,1,
        0,0,0,468,466,1,0,0,0,468,467,1,0,0,0,469,472,1,0,0,0,470,472,3,
        88,44,0,471,462,1,0,0,0,471,470,1,0,0,0,472,482,1,0,0,0,473,474,
        10,3,0,0,474,475,5,47,0,0,475,478,5,56,0,0,476,479,3,32,16,0,477,
        479,1,0,0,0,478,476,1,0,0,0,478,477,1,0,0,0,479,481,1,0,0,0,480,
        473,1,0,0,0,481,484,1,0,0,0,482,480,1,0,0,0,482,483,1,0,0,0,483,
        87,1,0,0,0,484,482,1,0,0,0,485,486,7,6,0,0,486,489,5,47,0,0,487,
        489,1,0,0,0,488,485,1,0,0,0,488,487,1,0,0,0,489,490,1,0,0,0,490,
        493,5,57,0,0,491,494,3,32,16,0,492,494,1,0,0,0,493,491,1,0,0,0,493,
        492,1,0,0,0,494,497,1,0,0,0,495,497,3,90,45,0,496,488,1,0,0,0,496,
        495,1,0,0,0,497,89,1,0,0,0,498,499,5,41,0,0,499,500,3,84,42,0,500,
        501,5,42,0,0,501,504,1,0,0,0,502,504,3,62,31,0,503,498,1,0,0,0,503,
        502,1,0,0,0,504,91,1,0,0,0,55,99,105,116,122,127,141,151,155,159,
        177,183,192,196,206,212,224,231,238,245,255,266,277,283,288,296,
        304,307,314,318,324,329,332,338,346,355,362,370,376,383,389,397,
        402,410,417,434,443,459,468,471,478,482,488,493,496,503
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
                      "VOID", "CONST", "FUNC", "PLUS", "MINUS", "MUL", "DIV_FLOAT", 
                      "DIV_INT", "MOD", "NEG", "AND", "OR", "EQ", "NEQ", 
                      "LT", "LTEQ", "GT", "GTEQ", "DECLARE", "ASSIGN", "CONCATE", 
                      "ARROW", "NEW", "LPN", "RPN", "LBK", "RBK", "LBR", 
                      "RBR", "DOT", "CM", "SM", "COL", "INT_LIT", "FLOAT_LIT", 
                      "STR_LIT", "BLOCK_COMMENT", "LINE_COMMENT", "ID", 
                      "AT_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecllist = 1
    RULE_classdecl = 2
    RULE_memberlist = 3
    RULE_member = 4
    RULE_attribute = 5
    RULE_attlistdecl = 6
    RULE_attlistnodecl = 7
    RULE_atttyp = 8
    RULE_typ = 9
    RULE_arraytyp = 10
    RULE_classtyp = 11
    RULE_method = 12
    RULE_paramlist = 13
    RULE_params = 14
    RULE_blockstmt = 15
    RULE_parenexpr = 16
    RULE_expressions = 17
    RULE_exprprime = 18
    RULE_exprstr = 19
    RULE_exprrel = 20
    RULE_exprlog = 21
    RULE_expradd = 22
    RULE_exprmul = 23
    RULE_exprnot = 24
    RULE_exprsign = 25
    RULE_exprindex = 26
    RULE_exprinst = 27
    RULE_exprstat = 28
    RULE_exprobj = 29
    RULE_exprparen = 30
    RULE_identifiers = 31
    RULE_literals = 32
    RULE_arrayliteral = 33
    RULE_arrint = 34
    RULE_arrfloat = 35
    RULE_arrbool = 36
    RULE_arrstr = 37
    RULE_boolliteral = 38
    RULE_statements = 39
    RULE_stmt = 40
    RULE_stmtassign = 41
    RULE_lhs = 42
    RULE_lhsinst = 43
    RULE_lhsstat = 44
    RULE_lhsparen = 45

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "attlistdecl", "attlistnodecl", 
                   "atttyp", "typ", "arraytyp", "classtyp", "method", "paramlist", 
                   "params", "blockstmt", "parenexpr", "expressions", "exprprime", 
                   "exprstr", "exprrel", "exprlog", "expradd", "exprmul", 
                   "exprnot", "exprsign", "exprindex", "exprinst", "exprstat", 
                   "exprobj", "exprparen", "identifiers", "literals", "arrayliteral", 
                   "arrint", "arrfloat", "arrbool", "arrstr", "boolliteral", 
                   "statements", "stmt", "stmtassign", "lhs", "lhsinst", 
                   "lhsstat", "lhsparen" ]

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
    PLUS=21
    MINUS=22
    MUL=23
    DIV_FLOAT=24
    DIV_INT=25
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
    ARROW=39
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
    INT_LIT=51
    FLOAT_LIT=52
    STR_LIT=53
    BLOCK_COMMENT=54
    LINE_COMMENT=55
    ID=56
    AT_ID=57
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
            self.state = 92
            self.classdecllist()
            self.state = 93
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.classdecl()
                self.state = 96
                self.classdecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
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

        def ARROW(self):
            return self.getToken(CSlangParser.ARROW, 0)

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
            self.state = 101
            self.match(CSlangParser.CLASS)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 102
                self.match(CSlangParser.ID)
                self.state = 103
                self.match(CSlangParser.ARROW)
                pass

            elif la_ == 2:
                pass


            self.state = 107
            self.match(CSlangParser.ID)
            self.state = 108
            self.match(CSlangParser.LBR)
            self.state = 109
            self.memberlist()
            self.state = 110
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
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.member()
                self.state = 113
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
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.attribute()
                self.state = 119
                self.match(CSlangParser.SM)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
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

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attlistdecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistdeclContext,0)


        def attlistnodecl(self):
            return self.getTypedRuleContext(CSlangParser.AttlistnodeclContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==16 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 125
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 126
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

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


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
        self.enterRule(localctx, 12, self.RULE_attlistdecl)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.identifiers()
                self.state = 130
                self.match(CSlangParser.CM)
                self.state = 131
                self.attlistdecl()
                self.state = 132
                self.match(CSlangParser.CM)
                self.state = 133
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.identifiers()
                self.state = 136
                self.match(CSlangParser.COL)
                self.state = 137
                self.atttyp()
                self.state = 138
                self.match(CSlangParser.DECLARE)
                self.state = 139
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

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


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
        self.enterRule(localctx, 14, self.RULE_attlistnodecl)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.identifiers()
                self.state = 144
                self.match(CSlangParser.CM)
                self.state = 145
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.identifiers()
                self.state = 148
                self.match(CSlangParser.COL)
                self.state = 149
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


        def arraytyp(self):
            return self.getTypedRuleContext(CSlangParser.ArraytypContext,0)


        def classtyp(self):
            return self.getTypedRuleContext(CSlangParser.ClasstypContext,0)


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
        self.enterRule(localctx, 16, self.RULE_atttyp)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [43]:
                    self.state = 153
                    self.arraytyp()
                    pass
                elif token in [8, 9, 10, 11]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 157
                self.typ()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.classtyp()
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
        self.enterRule(localctx, 18, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
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


    class ArraytypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraytyp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraytyp" ):
                listener.enterArraytyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraytyp" ):
                listener.exitArraytyp(self)




    def arraytyp(self):

        localctx = CSlangParser.ArraytypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arraytyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(CSlangParser.LBK)
            self.state = 164
            self.match(CSlangParser.INT_LIT)
            self.state = 165
            self.match(CSlangParser.RBK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClasstypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classtyp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClasstyp" ):
                listener.enterClasstyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClasstyp" ):
                listener.exitClasstyp(self)




    def classtyp(self):

        localctx = CSlangParser.ClasstypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_classtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(CSlangParser.NEW)
            self.state = 168
            self.match(CSlangParser.ID)
            self.state = 169
            self.match(CSlangParser.LPN)
            self.state = 170
            self.match(CSlangParser.RPN)
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

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


        def LPN(self):
            return self.getToken(CSlangParser.LPN, 0)

        def RPN(self):
            return self.getToken(CSlangParser.RPN, 0)

        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(CSlangParser.BlockstmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

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
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(CSlangParser.FUNC)
                self.state = 173
                self.identifiers()
                self.state = 174
                self.match(CSlangParser.LPN)
                self.state = 177
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [56]:
                    self.state = 175
                    self.paramlist()
                    pass
                elif token in [42]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 179
                self.match(CSlangParser.RPN)
                self.state = 180
                self.match(CSlangParser.COL)
                self.state = 183
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 9, 10, 11]:
                    self.state = 181
                    self.typ()
                    pass
                elif token in [18]:
                    self.state = 182
                    self.match(CSlangParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 185
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(CSlangParser.FUNC)
                self.state = 188
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 189
                self.match(CSlangParser.LPN)
                self.state = 192
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [56]:
                    self.state = 190
                    self.paramlist()
                    pass
                elif token in [42]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 194
                self.match(CSlangParser.RPN)
                self.state = 195
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


        def COL(self):
            return self.getToken(CSlangParser.COL, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


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
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.params()
                self.state = 199
                self.match(CSlangParser.CM)
                self.state = 200
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.params()
                self.state = 203
                self.match(CSlangParser.COL)
                self.state = 204
                self.typ()
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def params(self):
            return self.getTypedRuleContext(CSlangParser.ParamsContext,0)


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
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(CSlangParser.ID)
                self.state = 209
                self.match(CSlangParser.CM)
                self.state = 210
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(CSlangParser.ID)
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

        def statements(self):
            return self.getTypedRuleContext(CSlangParser.StatementsContext,0)


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
        self.enterRule(localctx, 30, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(CSlangParser.LBR)
            self.state = 215
            self.statements()
            self.state = 216
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

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


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
        self.enterRule(localctx, 32, self.RULE_parenexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(CSlangParser.LPN)
            self.state = 219
            self.expressions()
            self.state = 220
            self.match(CSlangParser.RPN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(CSlangParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressions" ):
                listener.enterExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressions" ):
                listener.exitExpressions(self)




    def expressions(self):

        localctx = CSlangParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressions)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 17, 22, 27, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
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

        def expressions(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionsContext,0)


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
        self.enterRule(localctx, 36, self.RULE_exprprime)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.exprstr()
                self.state = 227
                self.match(CSlangParser.CM)
                self.state = 228
                self.expressions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
        self.enterRule(localctx, 38, self.RULE_exprstr)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.exprrel()
                self.state = 234
                self.match(CSlangParser.CONCATE)
                self.state = 235
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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
        self.enterRule(localctx, 40, self.RULE_exprrel)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.exprlog(0)
                self.state = 241
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exprlog, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 252
                    self.expradd(0) 
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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


        def PLUS(self):
            return self.getToken(CSlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expradd, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.exprmul(0) 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def DIV_FLOAT(self):
            return self.getToken(CSlangParser.DIV_FLOAT, 0)

        def DIV_INT(self):
            return self.getToken(CSlangParser.DIV_INT, 0)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exprmul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 274
                    self.exprnot() 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_exprnot)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(CSlangParser.NEG)
                self.state = 281
                self.exprnot()
                pass
            elif token in [6, 7, 17, 22, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
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

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

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
        self.enterRule(localctx, 50, self.RULE_exprsign)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(CSlangParser.MINUS)
                self.state = 286
                self.exprsign()
                pass
            elif token in [6, 7, 17, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
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
        self.enterRule(localctx, 52, self.RULE_exprindex)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.exprinst(0)
                self.state = 291
                self.match(CSlangParser.LBK)
                self.state = 292
                self.exprstr()
                self.state = 293
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def exprstat(self):
            return self.getTypedRuleContext(CSlangParser.ExprstatContext,0)


        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exprinst, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 299
                self.match(CSlangParser.SELF)
                self.state = 300
                self.match(CSlangParser.DOT)
                self.state = 301
                self.match(CSlangParser.ID)
                self.state = 304
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 302
                    self.parenexpr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.state = 306
                self.exprstat()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprinst)
                    self.state = 309
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 310
                    self.match(CSlangParser.DOT)
                    self.state = 311
                    self.match(CSlangParser.ID)
                    self.state = 314
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 312
                        self.parenexpr()
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 320
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

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

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
        self.enterRule(localctx, 56, self.RULE_exprstat)
        self._la = 0 # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17, 56]:
                    self.state = 321
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==56):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 322
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [57]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 326
                self.match(CSlangParser.AT_ID)
                self.state = 329
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 327
                    self.parenexpr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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
        self.enterRule(localctx, 58, self.RULE_exprobj)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(CSlangParser.NEW)
                self.state = 335
                self.match(CSlangParser.ID)
                self.state = 336
                self.parenexpr()
                pass
            elif token in [6, 7, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


        def literals(self):
            return self.getTypedRuleContext(CSlangParser.LiteralsContext,0)


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
        self.enterRule(localctx, 60, self.RULE_exprparen)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(CSlangParser.LPN)
                self.state = 341
                self.exprstr()
                self.state = 342
                self.match(CSlangParser.RPN)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.identifiers()
                pass
            elif token in [6, 7, 43, 51, 52, 53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.literals()
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


    class IdentifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_identifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifiers" ):
                listener.enterIdentifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifiers" ):
                listener.exitIdentifiers(self)




    def identifiers(self):

        localctx = CSlangParser.IdentifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_identifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
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


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(CSlangParser.FLOAT_LIT, 0)

        def boolliteral(self):
            return self.getTypedRuleContext(CSlangParser.BoolliteralContext,0)


        def STR_LIT(self):
            return self.getToken(CSlangParser.STR_LIT, 0)

        def arrayliteral(self):
            return self.getTypedRuleContext(CSlangParser.ArrayliteralContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiterals" ):
                listener.enterLiterals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiterals" ):
                listener.exitLiterals(self)




    def literals(self):

        localctx = CSlangParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_literals)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(CSlangParser.INT_LIT)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(CSlangParser.FLOAT_LIT)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.boolliteral()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 353
                self.match(CSlangParser.STR_LIT)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 354
                self.arrayliteral()
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


    class ArrayliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBK(self):
            return self.getToken(CSlangParser.LBK, 0)

        def RBK(self):
            return self.getToken(CSlangParser.RBK, 0)

        def arrint(self):
            return self.getTypedRuleContext(CSlangParser.ArrintContext,0)


        def arrfloat(self):
            return self.getTypedRuleContext(CSlangParser.ArrfloatContext,0)


        def arrbool(self):
            return self.getTypedRuleContext(CSlangParser.ArrboolContext,0)


        def arrstr(self):
            return self.getTypedRuleContext(CSlangParser.ArrstrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrayliteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayliteral" ):
                listener.enterArrayliteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayliteral" ):
                listener.exitArrayliteral(self)




    def arrayliteral(self):

        localctx = CSlangParser.ArrayliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(CSlangParser.LBK)
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.state = 358
                self.arrint()
                pass
            elif token in [52]:
                self.state = 359
                self.arrfloat()
                pass
            elif token in [6, 7]:
                self.state = 360
                self.arrbool()
                pass
            elif token in [53]:
                self.state = 361
                self.arrstr()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 364
            self.match(CSlangParser.RBK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrint(self):
            return self.getTypedRuleContext(CSlangParser.ArrintContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrint" ):
                listener.enterArrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrint" ):
                listener.exitArrint(self)




    def arrint(self):

        localctx = CSlangParser.ArrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arrint)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(CSlangParser.INT_LIT)
                self.state = 367
                self.match(CSlangParser.CM)
                self.state = 368
                self.arrint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(CSlangParser.INT_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrfloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(CSlangParser.FLOAT_LIT, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrfloat(self):
            return self.getTypedRuleContext(CSlangParser.ArrfloatContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrfloat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrfloat" ):
                listener.enterArrfloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrfloat" ):
                listener.exitArrfloat(self)




    def arrfloat(self):

        localctx = CSlangParser.ArrfloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arrfloat)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(CSlangParser.FLOAT_LIT)
                self.state = 373
                self.match(CSlangParser.CM)
                self.state = 374
                self.arrfloat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(CSlangParser.FLOAT_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolliteral(self):
            return self.getTypedRuleContext(CSlangParser.BoolliteralContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrbool(self):
            return self.getTypedRuleContext(CSlangParser.ArrboolContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrbool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrbool" ):
                listener.enterArrbool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrbool" ):
                listener.exitArrbool(self)




    def arrbool(self):

        localctx = CSlangParser.ArrboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrbool)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.boolliteral()
                self.state = 379
                self.match(CSlangParser.CM)
                self.state = 380
                self.arrbool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.boolliteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_LIT(self):
            return self.getToken(CSlangParser.STR_LIT, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arrstr(self):
            return self.getTypedRuleContext(CSlangParser.ArrstrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arrstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrstr" ):
                listener.enterArrstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrstr" ):
                listener.exitArrstr(self)




    def arrstr(self):

        localctx = CSlangParser.ArrstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arrstr)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(CSlangParser.STR_LIT)
                self.state = 386
                self.match(CSlangParser.CM)
                self.state = 387
                self.arrstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(CSlangParser.STR_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_boolliteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolliteral" ):
                listener.enterBoolliteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolliteral" ):
                listener.exitBoolliteral(self)




    def boolliteral(self):

        localctx = CSlangParser.BoolliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_boolliteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
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


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def statements(self):
            return self.getTypedRuleContext(CSlangParser.StatementsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = CSlangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_statements)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 5, 6, 7, 12, 16, 17, 19, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.stmt()
                self.state = 394
                self.statements()
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

        def exprrel(self):
            return self.getTypedRuleContext(CSlangParser.ExprrelContext,0)


        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def exprinst(self):
            return self.getTypedRuleContext(CSlangParser.ExprinstContext,0)


        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


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
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 399
                    self.match(CSlangParser.VAR)
                    pass
                elif token in [19]:
                    self.state = 400
                    self.match(CSlangParser.CONST)
                    pass
                elif token in [17, 41, 56, 57]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 404
                self.stmtassign()
                self.state = 405
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(CSlangParser.IF)
                self.state = 410
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 408
                    self.blockstmt()
                    pass
                elif token in [6, 7, 17, 22, 27, 40, 41, 43, 51, 52, 53, 56, 57]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 412
                self.exprstr()
                self.state = 413
                self.blockstmt()
                self.state = 417
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 414
                    self.match(CSlangParser.ELSE)
                    self.state = 415
                    self.blockstmt()
                    pass
                elif token in [1, 2, 3, 5, 6, 7, 12, 16, 17, 19, 40, 41, 43, 46, 51, 52, 53, 56, 57]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 419
                self.match(CSlangParser.FOR)
                self.state = 420
                self.stmtassign()
                self.state = 421
                self.match(CSlangParser.SM)
                self.state = 422
                self.exprrel()
                self.state = 423
                self.match(CSlangParser.SM)
                self.state = 424
                self.stmtassign()
                self.state = 425
                self.blockstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.match(CSlangParser.BREAK)
                self.state = 428
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 429
                self.match(CSlangParser.CONTINUE)
                self.state = 430
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 431
                self.match(CSlangParser.RETURN)
                self.state = 434
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 7, 17, 22, 27, 40, 41, 43, 51, 52, 53, 56, 57]:
                    self.state = 432
                    self.exprstr()
                    pass
                elif token in [49]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 436
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 437
                self.exprinst(0)
                self.state = 438
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 440
                self.attribute()
                self.state = 441
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
            self.state = 445
            self.lhs(0)
            self.state = 446
            self.match(CSlangParser.ASSIGN)
            self.state = 447
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
            self.state = 450
            self.lhsinst(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 452
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 453
                    self.match(CSlangParser.LBK)
                    self.state = 454
                    self.exprstr()
                    self.state = 455
                    self.match(CSlangParser.RBK) 
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


    class LhsinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def lhsstat(self):
            return self.getTypedRuleContext(CSlangParser.LhsstatContext,0)


        def lhsinst(self):
            return self.getTypedRuleContext(CSlangParser.LhsinstContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 463
                self.match(CSlangParser.SELF)
                self.state = 464
                self.match(CSlangParser.DOT)
                self.state = 465
                self.match(CSlangParser.ID)
                self.state = 468
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 466
                    self.parenexpr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.state = 470
                self.lhsstat()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhsinst)
                    self.state = 473
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 474
                    self.match(CSlangParser.DOT)
                    self.state = 475
                    self.match(CSlangParser.ID)
                    self.state = 478
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        self.state = 476
                        self.parenexpr()
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

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
        self._la = 0 # Token type
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17, 56]:
                    self.state = 485
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==56):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 486
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [57]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 490
                self.match(CSlangParser.AT_ID)
                self.state = 493
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 491
                    self.parenexpr()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
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

        def identifiers(self):
            return self.getTypedRuleContext(CSlangParser.IdentifiersContext,0)


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
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(CSlangParser.LPN)
                self.state = 499
                self.lhs(0)
                self.state = 500
                self.match(CSlangParser.RPN)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.identifiers()
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
        self._predicates[21] = self.exprlog_sempred
        self._predicates[22] = self.expradd_sempred
        self._predicates[23] = self.exprmul_sempred
        self._predicates[27] = self.exprinst_sempred
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
                return self.precpred(self._ctx, 3)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def lhsinst_sempred(self, localctx:LhsinstContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




