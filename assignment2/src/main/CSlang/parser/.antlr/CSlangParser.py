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
        4,1,61,465,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,100,8,1,1,2,1,2,1,2,3,2,105,8,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,116,8,3,1,4,1,4,1,4,1,4,3,4,
        122,8,4,1,5,1,5,1,5,3,5,127,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,141,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,
        151,8,7,1,8,1,8,1,8,3,8,156,8,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,
        10,3,10,166,8,10,1,10,1,10,1,10,1,10,3,10,172,8,10,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,180,8,10,1,10,1,10,3,10,184,8,10,1,11,1,11,1,
        11,1,11,1,11,3,11,191,8,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,3,13,202,8,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        16,1,16,3,16,214,8,16,1,17,1,17,1,17,1,17,1,17,3,17,221,8,17,1,18,
        1,18,1,18,1,18,1,18,3,18,228,8,18,1,19,1,19,1,19,1,19,1,19,3,19,
        235,8,19,1,20,1,20,1,20,1,20,1,20,1,20,5,20,243,8,20,10,20,12,20,
        246,9,20,1,21,1,21,1,21,1,21,1,21,1,21,5,21,254,8,21,10,21,12,21,
        257,9,21,1,22,1,22,1,22,1,22,1,22,1,22,5,22,265,8,22,10,22,12,22,
        268,9,22,1,23,1,23,1,23,3,23,273,8,23,1,24,1,24,1,24,3,24,278,8,
        24,1,25,1,25,1,25,1,25,1,25,1,25,3,25,286,8,25,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,3,26,295,8,26,5,26,297,8,26,10,26,12,26,300,9,
        26,1,27,1,27,3,27,304,8,27,1,28,1,28,1,28,1,28,3,28,310,8,28,1,29,
        1,29,1,29,1,29,1,29,3,29,317,8,29,1,30,1,30,3,30,321,8,30,1,30,1,
        30,3,30,325,8,30,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,3,32,337,8,32,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,3,35,347,
        8,35,1,36,1,36,1,36,1,36,1,36,3,36,354,8,36,1,37,1,37,1,37,1,37,
        3,37,360,8,37,1,38,3,38,363,8,38,1,38,1,38,1,38,1,38,1,38,3,38,370,
        8,38,1,38,1,38,1,38,1,38,3,38,376,8,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,392,8,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,3,38,401,8,38,1,39,1,39,1,39,1,39,
        1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,5,40,415,8,40,10,40,12,40,
        418,9,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,427,8,41,5,41,429,
        8,41,10,41,12,41,432,9,41,1,42,1,42,3,42,436,8,42,1,43,1,43,1,43,
        1,43,1,43,1,43,3,43,444,8,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,
        3,44,453,8,44,5,44,455,8,44,10,44,12,44,458,9,44,1,45,1,45,1,45,
        3,45,463,8,45,1,45,0,7,40,42,44,52,80,82,88,46,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,0,8,2,0,16,16,19,
        19,2,0,8,11,56,56,1,0,30,35,1,0,28,29,1,0,21,22,1,0,23,26,1,0,56,
        57,1,0,6,7,480,0,92,1,0,0,0,2,99,1,0,0,0,4,101,1,0,0,0,6,115,1,0,
        0,0,8,121,1,0,0,0,10,123,1,0,0,0,12,140,1,0,0,0,14,150,1,0,0,0,16,
        155,1,0,0,0,18,159,1,0,0,0,20,183,1,0,0,0,22,190,1,0,0,0,24,192,
        1,0,0,0,26,201,1,0,0,0,28,203,1,0,0,0,30,207,1,0,0,0,32,213,1,0,
        0,0,34,220,1,0,0,0,36,227,1,0,0,0,38,234,1,0,0,0,40,236,1,0,0,0,
        42,247,1,0,0,0,44,258,1,0,0,0,46,272,1,0,0,0,48,277,1,0,0,0,50,285,
        1,0,0,0,52,287,1,0,0,0,54,303,1,0,0,0,56,309,1,0,0,0,58,316,1,0,
        0,0,60,320,1,0,0,0,62,326,1,0,0,0,64,336,1,0,0,0,66,338,1,0,0,0,
        68,340,1,0,0,0,70,346,1,0,0,0,72,353,1,0,0,0,74,359,1,0,0,0,76,400,
        1,0,0,0,78,402,1,0,0,0,80,406,1,0,0,0,82,419,1,0,0,0,84,435,1,0,
        0,0,86,443,1,0,0,0,88,445,1,0,0,0,90,462,1,0,0,0,92,93,3,2,1,0,93,
        94,5,0,0,1,94,1,1,0,0,0,95,96,3,4,2,0,96,97,3,2,1,0,97,100,1,0,0,
        0,98,100,3,4,2,0,99,95,1,0,0,0,99,98,1,0,0,0,100,3,1,0,0,0,101,104,
        5,14,0,0,102,103,5,56,0,0,103,105,5,39,0,0,104,102,1,0,0,0,104,105,
        1,0,0,0,105,106,1,0,0,0,106,107,5,56,0,0,107,108,5,45,0,0,108,109,
        3,6,3,0,109,110,5,46,0,0,110,5,1,0,0,0,111,112,3,8,4,0,112,113,3,
        6,3,0,113,116,1,0,0,0,114,116,1,0,0,0,115,111,1,0,0,0,115,114,1,
        0,0,0,116,7,1,0,0,0,117,118,3,10,5,0,118,119,5,49,0,0,119,122,1,
        0,0,0,120,122,3,20,10,0,121,117,1,0,0,0,121,120,1,0,0,0,122,9,1,
        0,0,0,123,126,7,0,0,0,124,127,3,12,6,0,125,127,3,14,7,0,126,124,
        1,0,0,0,126,125,1,0,0,0,127,11,1,0,0,0,128,129,3,62,31,0,129,130,
        5,48,0,0,130,131,3,12,6,0,131,132,5,48,0,0,132,133,3,36,18,0,133,
        141,1,0,0,0,134,135,3,62,31,0,135,136,5,50,0,0,136,137,3,16,8,0,
        137,138,5,36,0,0,138,139,3,36,18,0,139,141,1,0,0,0,140,128,1,0,0,
        0,140,134,1,0,0,0,141,13,1,0,0,0,142,143,3,62,31,0,143,144,5,48,
        0,0,144,145,3,14,7,0,145,151,1,0,0,0,146,147,3,62,31,0,147,148,5,
        50,0,0,148,149,3,16,8,0,149,151,1,0,0,0,150,142,1,0,0,0,150,146,
        1,0,0,0,151,15,1,0,0,0,152,153,5,43,0,0,153,154,5,51,0,0,154,156,
        5,44,0,0,155,152,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,
        3,18,9,0,158,17,1,0,0,0,159,160,7,1,0,0,160,19,1,0,0,0,161,162,5,
        20,0,0,162,163,3,62,31,0,163,165,5,41,0,0,164,166,3,22,11,0,165,
        164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,168,5,42,0,0,168,
        171,5,50,0,0,169,172,3,16,8,0,170,172,5,18,0,0,171,169,1,0,0,0,171,
        170,1,0,0,0,172,173,1,0,0,0,173,174,3,28,14,0,174,184,1,0,0,0,175,
        176,5,20,0,0,176,177,5,15,0,0,177,179,5,41,0,0,178,180,3,22,11,0,
        179,178,1,0,0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,182,5,42,0,0,
        182,184,3,28,14,0,183,161,1,0,0,0,183,175,1,0,0,0,184,21,1,0,0,0,
        185,186,3,24,12,0,186,187,5,48,0,0,187,188,3,22,11,0,188,191,1,0,
        0,0,189,191,3,24,12,0,190,185,1,0,0,0,190,189,1,0,0,0,191,23,1,0,
        0,0,192,193,3,26,13,0,193,194,5,50,0,0,194,195,3,16,8,0,195,25,1,
        0,0,0,196,197,3,62,31,0,197,198,5,48,0,0,198,199,3,26,13,0,199,202,
        1,0,0,0,200,202,3,62,31,0,201,196,1,0,0,0,201,200,1,0,0,0,202,27,
        1,0,0,0,203,204,5,45,0,0,204,205,3,74,37,0,205,206,5,46,0,0,206,
        29,1,0,0,0,207,208,5,41,0,0,208,209,3,32,16,0,209,210,5,42,0,0,210,
        31,1,0,0,0,211,214,3,34,17,0,212,214,1,0,0,0,213,211,1,0,0,0,213,
        212,1,0,0,0,214,33,1,0,0,0,215,216,3,36,18,0,216,217,5,48,0,0,217,
        218,3,34,17,0,218,221,1,0,0,0,219,221,3,36,18,0,220,215,1,0,0,0,
        220,219,1,0,0,0,221,35,1,0,0,0,222,223,3,38,19,0,223,224,5,38,0,
        0,224,225,3,38,19,0,225,228,1,0,0,0,226,228,3,38,19,0,227,222,1,
        0,0,0,227,226,1,0,0,0,228,37,1,0,0,0,229,230,3,40,20,0,230,231,7,
        2,0,0,231,232,3,40,20,0,232,235,1,0,0,0,233,235,3,40,20,0,234,229,
        1,0,0,0,234,233,1,0,0,0,235,39,1,0,0,0,236,237,6,20,-1,0,237,238,
        3,42,21,0,238,244,1,0,0,0,239,240,10,2,0,0,240,241,7,3,0,0,241,243,
        3,42,21,0,242,239,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,
        1,0,0,0,245,41,1,0,0,0,246,244,1,0,0,0,247,248,6,21,-1,0,248,249,
        3,44,22,0,249,255,1,0,0,0,250,251,10,2,0,0,251,252,7,4,0,0,252,254,
        3,44,22,0,253,250,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,
        1,0,0,0,256,43,1,0,0,0,257,255,1,0,0,0,258,259,6,22,-1,0,259,260,
        3,46,23,0,260,266,1,0,0,0,261,262,10,2,0,0,262,263,7,5,0,0,263,265,
        3,46,23,0,264,261,1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,
        1,0,0,0,267,45,1,0,0,0,268,266,1,0,0,0,269,270,5,27,0,0,270,273,
        3,46,23,0,271,273,3,48,24,0,272,269,1,0,0,0,272,271,1,0,0,0,273,
        47,1,0,0,0,274,275,5,22,0,0,275,278,3,48,24,0,276,278,3,50,25,0,
        277,274,1,0,0,0,277,276,1,0,0,0,278,49,1,0,0,0,279,280,3,52,26,0,
        280,281,5,43,0,0,281,282,3,36,18,0,282,283,5,44,0,0,283,286,1,0,
        0,0,284,286,3,52,26,0,285,279,1,0,0,0,285,284,1,0,0,0,286,51,1,0,
        0,0,287,288,6,26,-1,0,288,289,3,54,27,0,289,298,1,0,0,0,290,291,
        10,2,0,0,291,292,5,47,0,0,292,294,5,56,0,0,293,295,3,30,15,0,294,
        293,1,0,0,0,294,295,1,0,0,0,295,297,1,0,0,0,296,290,1,0,0,0,297,
        300,1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,53,1,0,0,0,300,298,
        1,0,0,0,301,304,3,60,30,0,302,304,3,56,28,0,303,301,1,0,0,0,303,
        302,1,0,0,0,304,55,1,0,0,0,305,306,5,40,0,0,306,307,5,56,0,0,307,
        310,3,30,15,0,308,310,3,58,29,0,309,305,1,0,0,0,309,308,1,0,0,0,
        310,57,1,0,0,0,311,312,5,41,0,0,312,313,3,36,18,0,313,314,5,42,0,
        0,314,317,1,0,0,0,315,317,3,64,32,0,316,311,1,0,0,0,316,315,1,0,
        0,0,317,59,1,0,0,0,318,319,5,56,0,0,319,321,5,47,0,0,320,318,1,0,
        0,0,320,321,1,0,0,0,321,322,1,0,0,0,322,324,5,57,0,0,323,325,3,30,
        15,0,324,323,1,0,0,0,324,325,1,0,0,0,325,61,1,0,0,0,326,327,7,6,
        0,0,327,63,1,0,0,0,328,337,5,51,0,0,329,337,5,52,0,0,330,337,3,66,
        33,0,331,337,5,53,0,0,332,337,3,68,34,0,333,337,5,13,0,0,334,337,
        5,17,0,0,335,337,3,62,31,0,336,328,1,0,0,0,336,329,1,0,0,0,336,330,
        1,0,0,0,336,331,1,0,0,0,336,332,1,0,0,0,336,333,1,0,0,0,336,334,
        1,0,0,0,336,335,1,0,0,0,337,65,1,0,0,0,338,339,7,7,0,0,339,67,1,
        0,0,0,340,341,5,43,0,0,341,342,3,72,36,0,342,343,5,44,0,0,343,69,
        1,0,0,0,344,347,3,72,36,0,345,347,1,0,0,0,346,344,1,0,0,0,346,345,
        1,0,0,0,347,71,1,0,0,0,348,349,3,64,32,0,349,350,5,48,0,0,350,351,
        3,72,36,0,351,354,1,0,0,0,352,354,3,64,32,0,353,348,1,0,0,0,353,
        352,1,0,0,0,354,73,1,0,0,0,355,356,3,76,38,0,356,357,3,74,37,0,357,
        360,1,0,0,0,358,360,1,0,0,0,359,355,1,0,0,0,359,358,1,0,0,0,360,
        75,1,0,0,0,361,363,7,0,0,0,362,361,1,0,0,0,362,363,1,0,0,0,363,364,
        1,0,0,0,364,365,3,78,39,0,365,366,5,49,0,0,366,401,1,0,0,0,367,369,
        5,3,0,0,368,370,3,28,14,0,369,368,1,0,0,0,369,370,1,0,0,0,370,371,
        1,0,0,0,371,372,3,36,18,0,372,375,3,28,14,0,373,374,5,4,0,0,374,
        376,3,28,14,0,375,373,1,0,0,0,375,376,1,0,0,0,376,401,1,0,0,0,377,
        378,5,5,0,0,378,379,3,78,39,0,379,380,5,49,0,0,380,381,3,36,18,0,
        381,382,5,49,0,0,382,383,3,78,39,0,383,384,3,28,14,0,384,401,1,0,
        0,0,385,386,5,1,0,0,386,401,5,49,0,0,387,388,5,2,0,0,388,401,5,49,
        0,0,389,391,5,12,0,0,390,392,3,36,18,0,391,390,1,0,0,0,391,392,1,
        0,0,0,392,393,1,0,0,0,393,401,5,49,0,0,394,395,3,88,44,0,395,396,
        5,49,0,0,396,401,1,0,0,0,397,398,3,10,5,0,398,399,5,49,0,0,399,401,
        1,0,0,0,400,362,1,0,0,0,400,367,1,0,0,0,400,377,1,0,0,0,400,385,
        1,0,0,0,400,387,1,0,0,0,400,389,1,0,0,0,400,394,1,0,0,0,400,397,
        1,0,0,0,401,77,1,0,0,0,402,403,3,80,40,0,403,404,5,37,0,0,404,405,
        3,36,18,0,405,79,1,0,0,0,406,407,6,40,-1,0,407,408,3,82,41,0,408,
        416,1,0,0,0,409,410,10,2,0,0,410,411,5,43,0,0,411,412,3,36,18,0,
        412,413,5,44,0,0,413,415,1,0,0,0,414,409,1,0,0,0,415,418,1,0,0,0,
        416,414,1,0,0,0,416,417,1,0,0,0,417,81,1,0,0,0,418,416,1,0,0,0,419,
        420,6,41,-1,0,420,421,3,84,42,0,421,430,1,0,0,0,422,423,10,2,0,0,
        423,424,5,47,0,0,424,426,5,56,0,0,425,427,3,30,15,0,426,425,1,0,
        0,0,426,427,1,0,0,0,427,429,1,0,0,0,428,422,1,0,0,0,429,432,1,0,
        0,0,430,428,1,0,0,0,430,431,1,0,0,0,431,83,1,0,0,0,432,430,1,0,0,
        0,433,436,3,60,30,0,434,436,3,86,43,0,435,433,1,0,0,0,435,434,1,
        0,0,0,436,85,1,0,0,0,437,438,5,41,0,0,438,439,3,80,40,0,439,440,
        5,42,0,0,440,444,1,0,0,0,441,444,5,17,0,0,442,444,3,62,31,0,443,
        437,1,0,0,0,443,441,1,0,0,0,443,442,1,0,0,0,444,87,1,0,0,0,445,446,
        6,44,-1,0,446,447,3,90,45,0,447,456,1,0,0,0,448,449,10,2,0,0,449,
        450,5,47,0,0,450,452,5,56,0,0,451,453,3,30,15,0,452,451,1,0,0,0,
        452,453,1,0,0,0,453,455,1,0,0,0,454,448,1,0,0,0,455,458,1,0,0,0,
        456,454,1,0,0,0,456,457,1,0,0,0,457,89,1,0,0,0,458,456,1,0,0,0,459,
        463,3,60,30,0,460,463,5,17,0,0,461,463,3,62,31,0,462,459,1,0,0,0,
        462,460,1,0,0,0,462,461,1,0,0,0,463,91,1,0,0,0,48,99,104,115,121,
        126,140,150,155,165,171,179,183,190,201,213,220,227,234,244,255,
        266,272,277,285,294,298,303,309,316,320,324,336,346,353,359,362,
        369,375,391,400,416,426,430,435,443,452,456,462
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
    RULE_attlistdecl = 6
    RULE_attlistnodecl = 7
    RULE_atttyp = 8
    RULE_typ = 9
    RULE_method = 10
    RULE_paramlist = 11
    RULE_params = 12
    RULE_param = 13
    RULE_blockstmt = 14
    RULE_parenexpr = 15
    RULE_exprlist = 16
    RULE_exprprime = 17
    RULE_exprstr = 18
    RULE_exprrel = 19
    RULE_exprlog = 20
    RULE_expradd = 21
    RULE_exprmul = 22
    RULE_exprnot = 23
    RULE_exprsign = 24
    RULE_exprindex = 25
    RULE_exprinst = 26
    RULE_exprstat = 27
    RULE_exprobj = 28
    RULE_exprparen = 29
    RULE_statpart = 30
    RULE_identifier = 31
    RULE_lit = 32
    RULE_boollit = 33
    RULE_arraylit = 34
    RULE_litlist = 35
    RULE_litprime = 36
    RULE_stmtlist = 37
    RULE_stmt = 38
    RULE_stmtassign = 39
    RULE_lhs = 40
    RULE_lhsinst = 41
    RULE_lhsstat = 42
    RULE_lhsparen = 43
    RULE_stmtinvoc = 44
    RULE_stmtinvocstat = 45

    ruleNames =  [ "program", "classdecllist", "classdecl", "memberlist", 
                   "member", "attribute", "attlistdecl", "attlistnodecl", 
                   "atttyp", "typ", "method", "paramlist", "params", "param", 
                   "blockstmt", "parenexpr", "exprlist", "exprprime", "exprstr", 
                   "exprrel", "exprlog", "expradd", "exprmul", "exprnot", 
                   "exprsign", "exprindex", "exprinst", "exprstat", "exprobj", 
                   "exprparen", "statpart", "identifier", "lit", "boollit", 
                   "arraylit", "litlist", "litprime", "stmtlist", "stmt", 
                   "stmtassign", "lhs", "lhsinst", "lhsstat", "lhsparen", 
                   "stmtinvoc", "stmtinvocstat" ]

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
            self.state = 101
            self.match(CSlangParser.CLASS)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 102
                self.match(CSlangParser.ID)
                self.state = 103
                self.match(CSlangParser.LARROW)


            self.state = 106
            self.match(CSlangParser.ID)
            self.state = 107
            self.match(CSlangParser.LBR)
            self.state = 108
            self.memberlist()
            self.state = 109
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
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.member()
                self.state = 112
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.attribute()
                self.state = 118
                self.match(CSlangParser.SM)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
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
            self.state = 123
            _la = self._input.LA(1)
            if not(_la==16 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 124
                self.attlistdecl()
                pass

            elif la_ == 2:
                self.state = 125
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
        self.enterRule(localctx, 12, self.RULE_attlistdecl)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.identifier()
                self.state = 129
                self.match(CSlangParser.CM)
                self.state = 130
                self.attlistdecl()
                self.state = 131
                self.match(CSlangParser.CM)
                self.state = 132
                self.exprstr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.identifier()
                self.state = 135
                self.match(CSlangParser.COL)
                self.state = 136
                self.atttyp()
                self.state = 137
                self.match(CSlangParser.DECLARE)
                self.state = 138
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
        self.enterRule(localctx, 14, self.RULE_attlistnodecl)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.identifier()
                self.state = 143
                self.match(CSlangParser.CM)
                self.state = 144
                self.attlistnodecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.identifier()
                self.state = 147
                self.match(CSlangParser.COL)
                self.state = 148
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
        self.enterRule(localctx, 16, self.RULE_atttyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 152
                self.match(CSlangParser.LBK)
                self.state = 153
                self.match(CSlangParser.INTLIT)
                self.state = 154
                self.match(CSlangParser.RBK)


            self.state = 157
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
        self.enterRule(localctx, 18, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
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
        self.enterRule(localctx, 20, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(CSlangParser.FUNC)
                self.state = 162
                self.identifier()
                self.state = 163
                self.match(CSlangParser.LPN)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56 or _la==57:
                    self.state = 164
                    self.paramlist()


                self.state = 167
                self.match(CSlangParser.RPN)
                self.state = 168
                self.match(CSlangParser.COL)
                self.state = 171
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 9, 10, 11, 43, 56]:
                    self.state = 169
                    self.atttyp()
                    pass
                elif token in [18]:
                    self.state = 170
                    self.match(CSlangParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 173
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(CSlangParser.FUNC)
                self.state = 176
                self.match(CSlangParser.CONSTRUCTOR)
                self.state = 177
                self.match(CSlangParser.LPN)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==56 or _la==57:
                    self.state = 178
                    self.paramlist()


                self.state = 181
                self.match(CSlangParser.RPN)
                self.state = 182
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
        self.enterRule(localctx, 22, self.RULE_paramlist)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.params()
                self.state = 186
                self.match(CSlangParser.CM)
                self.state = 187
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
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
        self.enterRule(localctx, 24, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.param()
            self.state = 193
            self.match(CSlangParser.COL)
            self.state = 194
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
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.identifier()
                self.state = 197
                self.match(CSlangParser.CM)
                self.state = 198
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
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
        self.enterRule(localctx, 28, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(CSlangParser.LBR)
            self.state = 204
            self.stmtlist()
            self.state = 205
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
        self.enterRule(localctx, 30, self.RULE_parenexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(CSlangParser.LPN)
            self.state = 208
            self.exprlist()
            self.state = 209
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
        self.enterRule(localctx, 32, self.RULE_exprlist)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 13, 17, 22, 27, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
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
        self.enterRule(localctx, 34, self.RULE_exprprime)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.exprstr()
                self.state = 216
                self.match(CSlangParser.CM)
                self.state = 217
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
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
        self.enterRule(localctx, 36, self.RULE_exprstr)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.exprrel()
                self.state = 223
                self.match(CSlangParser.CONCATE)
                self.state = 224
                self.exprrel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
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
        self.enterRule(localctx, 38, self.RULE_exprrel)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.exprlog(0)
                self.state = 230
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 231
                self.exprlog(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exprlog, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.expradd(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprlogContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprlog)
                    self.state = 239
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 240
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 241
                    self.expradd(0) 
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expradd, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.exprmul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExpraddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expradd)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 252
                    self.exprmul(0) 
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exprmul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.exprnot()
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprmulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprmul)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.exprnot() 
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
        self.enterRule(localctx, 46, self.RULE_exprnot)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(CSlangParser.NEG)
                self.state = 270
                self.exprnot()
                pass
            elif token in [6, 7, 13, 17, 22, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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
        self.enterRule(localctx, 48, self.RULE_exprsign)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(CSlangParser.SUB)
                self.state = 275
                self.exprsign()
                pass
            elif token in [6, 7, 13, 17, 40, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
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
        self.enterRule(localctx, 50, self.RULE_exprindex)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.exprinst(0)
                self.state = 280
                self.match(CSlangParser.LBK)
                self.state = 281
                self.exprstr()
                self.state = 282
                self.match(CSlangParser.RBK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exprinst, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.exprstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprinst)
                    self.state = 290
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 291
                    self.match(CSlangParser.DOT)
                    self.state = 292
                    self.match(CSlangParser.ID)
                    self.state = 294
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        self.state = 293
                        self.parenexpr()

             
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_exprstat)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.statpart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
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
        self.enterRule(localctx, 56, self.RULE_exprobj)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(CSlangParser.NEW)
                self.state = 306
                self.match(CSlangParser.ID)
                self.state = 307
                self.parenexpr()
                pass
            elif token in [6, 7, 13, 17, 41, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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
        self.enterRule(localctx, 58, self.RULE_exprparen)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(CSlangParser.LPN)
                self.state = 312
                self.exprstr()
                self.state = 313
                self.match(CSlangParser.RPN)
                pass
            elif token in [6, 7, 13, 17, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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
        self.enterRule(localctx, 60, self.RULE_statpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 318
                self.match(CSlangParser.ID)
                self.state = 319
                self.match(CSlangParser.DOT)


            self.state = 322
            self.match(CSlangParser.ATID)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 323
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
        self.enterRule(localctx, 62, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
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
        self.enterRule(localctx, 64, self.RULE_lit)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
                self.boollit()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 331
                self.match(CSlangParser.STRLIT)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 332
                self.arraylit()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 333
                self.match(CSlangParser.NULL)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 334
                self.match(CSlangParser.SELF)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 8)
                self.state = 335
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
        self.enterRule(localctx, 66, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
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
        self.enterRule(localctx, 68, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(CSlangParser.LBK)
            self.state = 341
            self.litprime()
            self.state = 342
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
        self.enterRule(localctx, 70, self.RULE_litlist)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 13, 17, 43, 51, 52, 53, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
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
        self.enterRule(localctx, 72, self.RULE_litprime)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.lit()
                self.state = 349
                self.match(CSlangParser.CM)
                self.state = 350
                self.litprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
        self.enterRule(localctx, 74, self.RULE_stmtlist)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 5, 12, 16, 17, 19, 41, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.stmt()
                self.state = 356
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

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def stmtinvoc(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocContext,0)


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
        self.enterRule(localctx, 76, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16 or _la==19:
                    self.state = 361
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 364
                self.stmtassign()
                self.state = 365
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(CSlangParser.IF)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 368
                    self.blockstmt()


                self.state = 371
                self.exprstr()
                self.state = 372
                self.blockstmt()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 373
                    self.match(CSlangParser.ELSE)
                    self.state = 374
                    self.blockstmt()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.match(CSlangParser.FOR)
                self.state = 378
                self.stmtassign()
                self.state = 379
                self.match(CSlangParser.SM)
                self.state = 380
                self.exprstr()
                self.state = 381
                self.match(CSlangParser.SM)
                self.state = 382
                self.stmtassign()
                self.state = 383
                self.blockstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.match(CSlangParser.BREAK)
                self.state = 386
                self.match(CSlangParser.SM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 387
                self.match(CSlangParser.CONTINUE)
                self.state = 388
                self.match(CSlangParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 389
                self.match(CSlangParser.RETURN)
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 231947475576037568) != 0):
                    self.state = 390
                    self.exprstr()


                self.state = 393
                self.match(CSlangParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 394
                self.stmtinvoc(0)
                self.state = 395
                self.match(CSlangParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 397
                self.attribute()
                self.state = 398
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
        self.enterRule(localctx, 78, self.RULE_stmtassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.lhs(0)
            self.state = 403
            self.match(CSlangParser.ASSIGN)
            self.state = 404
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.lhsinst(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 410
                    self.match(CSlangParser.LBK)
                    self.state = 411
                    self.exprstr()
                    self.state = 412
                    self.match(CSlangParser.RBK) 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_lhsinst, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.lhsstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.LhsinstContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhsinst)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    self.match(CSlangParser.DOT)
                    self.state = 424
                    self.match(CSlangParser.ID)
                    self.state = 426
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        self.state = 425
                        self.parenexpr()

             
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_lhsstat)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.statpart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
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
        self.enterRule(localctx, 86, self.RULE_lhsparen)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(CSlangParser.LPN)
                self.state = 438
                self.lhs(0)
                self.state = 439
                self.match(CSlangParser.RPN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.match(CSlangParser.SELF)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
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

        def stmtinvocstat(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocstatContext,0)


        def stmtinvoc(self):
            return self.getTypedRuleContext(CSlangParser.StmtinvocContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def parenexpr(self):
            return self.getTypedRuleContext(CSlangParser.ParenexprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtinvoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtinvoc" ):
                listener.enterStmtinvoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtinvoc" ):
                listener.exitStmtinvoc(self)



    def stmtinvoc(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.StmtinvocContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_stmtinvoc, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.stmtinvocstat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 456
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.StmtinvocContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stmtinvoc)
                    self.state = 448
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 449
                    self.match(CSlangParser.DOT)
                    self.state = 450
                    self.match(CSlangParser.ID)
                    self.state = 452
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        self.state = 451
                        self.parenexpr()

             
                self.state = 458
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StmtinvocstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statpart(self):
            return self.getTypedRuleContext(CSlangParser.StatpartContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


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
        self.enterRule(localctx, 90, self.RULE_stmtinvocstat)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.statpart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.match(CSlangParser.SELF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.identifier()
                pass


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
        self._predicates[20] = self.exprlog_sempred
        self._predicates[21] = self.expradd_sempred
        self._predicates[22] = self.exprmul_sempred
        self._predicates[26] = self.exprinst_sempred
        self._predicates[40] = self.lhs_sempred
        self._predicates[41] = self.lhsinst_sempred
        self._predicates[44] = self.stmtinvoc_sempred
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
         

    def stmtinvoc_sempred(self, localctx:StmtinvocContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




