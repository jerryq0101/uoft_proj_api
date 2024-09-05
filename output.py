
first_year_calc = (["MAT135H1", "MAT136H1"],"MAT137Y1","MAT157Y1")

csc336h1_pre = [
    ("CSC148H1", "CSC111H1"),
    (
        {
            "code": "MAT133Y1",
            "min_req": "70%"
        },
        ["MAT135H1", "MAT136H1"],
        "MAT137Y1",
        "MAT157Y1",
    ),
    ("MAT223H1", "MAT240H1")
]
csc336h1_cor = []

# Special case: Pre not specifically required
csc148h1_pre = [
    "CSC108H1"
]
csc148h1_cor = []

csc108h1_pre = []
csc108h1_cor = []

csc111h1_pre = ["CSC110Y1"]
csc111h1_cor = []

csc110y1_pre = []
csc110y1_cor = []

mat133y1_pre = []
mat133y1_cor = []

mat135h1_pre = []
mat135h1_cor = []

mat136h1_pre = [
    "MAT135H1"
]
mat136h1_cor = []

mat137y1_pre = []
mat137y1_cor = []

mat157y1_pre = []
mat157y1_cor = []

mat223h1_pre = []
mat223h1_cor = []

mat240h1_pre = []
mat240h1_cor = [
    "MAT157Y1"
]

mat235y1_pre = [
    (   
        "MAT133Y1",
        ["MAT135H1", "MAT136H1"],
        "MAT137Y1",
        "MAT157Y1"
    )
]
mat235y1_cor = []

mat237y1_pre = [
    (
        [
            (
                "MAT133Y1",
                ["MAT135H1", "MAT136H1"]
            ),
            ("MAT138H1", "MAT246H1")
        ],
        "MAT137Y1",
        "MAT157Y1"
    ),
    (
        "MAT223H1",
        "MAT240H1"
    )
]
mat237y1_cor = []

mat138h1_pre = []
mat138h1_cor = []

mat246h1_pre = [
    (   
        "MAT133Y1",
        [
            "MAT135H1",
            "MAT136H1"
        ],
        "MAT137Y1",
    ),
    "MAT223H1",
]
mat246h1_cor = []

mat257y1_pre = [
    "MAT157Y1",
    "MAT247H1"
]
mat257y1_cor = []

mat247h1_pre = [
    "MAT240H1"
]
mat247h1_cor = [
    "MAT157Y1"
]

apm236h1_pre = [
    ("MAT221H1", "MAT223H1", "MAT240H1")
]
apm236h1_cor = []

mat221h1_pre = []
mat221h1_cor = []

mat224h1_pre = [
    (
        {
            "code": "MAT221H1",
            "min_req": "80%"
        },
        "MAT223H1",
        "MAT240H1"
    )
]
mat224h1_cor = []

mat247h1_pre = [
    "MAT240H1"
]
mat247h1_cor = [
    "MAT157Y1"
]

sta238h1_pre = [
    (
        "STA237H1",
        "STA247H1",
        "STA257H1"
    )
]
sta238h1_cor = [
    (
        "CSC108H1",
        "CSC110Y1",
        "CSC148H1"
    )
]

sta237h1_pre = [
    first_year_calc,
]
sta237h1_cor = [
    ("CSC108H1", "CSC110Y1", "CSC148H1")
]

sta247h1_pre = [
    first_year_calc,
    ("CSC111H1", "CSC148H1")
]
sta247h1_cor = []

sta257h1_pre = [
    ("MAT137Y1", "MAT157Y1")
]
sta257h1_cor = [
    ("MAT237Y1", "MAT257Y1"),
    ("MAT223H1", "MAT224H1", "MAT240H1")
]

sta248h1_pre = [
    ("STA237H1", "STA247H1", "STA257H1"),
    ("CSC111H1", "CSC148H1")
]
sta248h1_cor = []

sta261h1_pre = [
    "STA257H1"
]
sta261h1_cor = [
    ("MAT237Y1", "MAT257Y1"),
    ("MAT223H1", "MAT224H1", "MAT240H1")
]

sta302h1_pre = [
    ("STA238H1", "STA248H1", "STA255H1", "STA261H1", "ECO227Y1"),
    ("CSC108H1", "CSC110Y1", "CSC148H1"),
    ("MAT223H1", "MAT224H1", "MAT240H1")
]
sta302h1_cor = []

# Special Case (note:  ECO220Y1 may be taken as a co-requisite)
sta255h1_pre = [
    ("STA220H1", "STA221H1", "STA288H1", "ECO220Y1"),
    ({"code": "MAT133Y1", "min_req": "70%"},["MAT135H1", "MAT136H1"],"MAT137Y1","MAT157Y1")
]
sta255h1_cor = []

sta220h1_pre = []
sta220h1_cor = []

sta221h1_pre = [
    ("STA220H1", "PSY201H1", "GGR270H1", "EEB225H1")
]
sta221h1_cor = []

sta288h1_pre = [
    ("BIO230H1")
]
sta288h1_cor = []

bio230h1_pre = [
    "BIO130H1",
    (
        ["CHM135H1", "CHM136H1"],
        "CHM151Y1"
    )
]
bio230h1_cor = []

# Special Note: prerequisite SBI4U and SCH4U (Grade 12 University Preparation Biology and Chemistry) or permission of department. Please contact bio130@utoronto.ca for more information.
bio130h1_pre = []
bio130h1_cor = []

# Special Note: Prerequisite: Chemistry SCH4U, Mathematics MHF4U + MCV4U
chm135h1_pre = []
chm135h1_cor = [
    first_year_calc
]

chm136h1_pre = [
    "CHM135H1"
]
chm136h1_cor = [
    first_year_calc
]

# Special Note: Prerequisite: Chemistry SCH4U, Mathematics MHF4U + MCV4U; Physics SPH4U recommended
# Note for corerequisites: (PHY151H1,  PHY152H1) recommended, but may be required for further Chemistry courses
chm151y1_pre = [
]
chm151y1_cor = [
    first_year_calc,
    (
        ["PHY131H1", "PHY132H1"],
        ["PHY151H1", "PHY152H1"]
    )
]

phy131h1_pre = []
phy131h1_cor = [
    ("MAT135H1", "MAT137Y1", "MAT157Y1")
]

phy132h1_pre = [
    ("PHY131H1", "PHY151H1")
]
phy132h1_cor = [
    ("MAT136H1", "MAT137Y1", "MAT157Y1")
]

# Special Note Prerequisite: MCV4U Calculus & Vectors / MCB4U Functions & Calculus; SPH4U Physics
phy151h1_pre = []
phy151h1_cor = [
    ("MAT137Y1", "MAT157Y1")
]

phy152h1_pre = [
    ("PHY131H1", "PHY151H1")
]
phy152h1_cor = [
    ("MAT137Y1", "MAT157Y1")
]

# Special note: cGPA > 3.0
bio255h1_pre = [
    "BIO130H1",
    (
        ["CHM135H1", "CHM136H1"],
        "CHM151Y1"
    )
]
bio255h1_cor = []

psy201h1_pre = [
    ("PSY100H1", "COG250Y1")
]
psy201h1_cor = []

psy100h1_pre = []
psy100h1_cor = []

cog250y1_pre = []
cog250y1_cor = []

ggr270h1_pre = []
ggr270h1_cor = []

eeb225h1_pre = [
    "BIO120H1"
]
eeb225h1_cor = []

# Special Note: Grade 12 Biology or equivalent. Students without high school Biology must consult the BIO120 Office (bio120@utoronto.ca)
bio120h1_pre = []
bio120h1_cor = []

eco220y1_pre = [
    (   
        [
            {
                "code": "ECO101H1",
                "min_req": "63%"
            },
            {
                "code": "ECO102H1",
                "min_req": "63%"
            }
        ],
        {
            "code": "ECO105Y1",
            "min_req": "80%"
        },
    ),
    ("MAT133Y1", ["MAT135H1", "MAT136H1"], "MAT137Y1", "MAT157Y1")
]
eco220y1_cor = []

eco101h1_pre = []
eco101h1_cor = []

eco102h1_pre = [
    "ECO101H1"
]
eco102h1_cor = []

eco105y1_pre = []
eco105y1_cor = []

# Special Note Corequisite: Recommended:  MAT223H1/  MAT240H1,  MAT235Y1/  MAT237Y1/  ECO210H1
eco227y1_pre = [
    [
        {
            "code": "ECO101H1",
            "min_req": "70%"
        },
        {
            "code": "ECO102H1",
            "min_req": "70%"
        }
    ],
    ({"code": "MAT133Y1", "min_req": "63%"}, [{"code": "MAT135H1", "min_req": "60%"}, {"code": "MAT136H1", "min_req": "60%"}], {"code": "MAT137Y1", "min_req": "55%"}, {"code": "MAT157Y1", "min_req": "55%"})
]
eco227y1_cor = []

eco210h1_pre = [
    [
        {
            "code": "ECO101H1",
            "min_req": "70%"
        },
        {
            "code": "ECO102H1",
            "min_req": "70%"
        }
    ],
    ({"code": "MAT133Y1", "min_req": "63%"}, [{"code": "MAT135H1", "min_req": "60%"}, {"code": "MAT136H1", "min_req": "60%"}], {"code": "MAT137Y1", "min_req": "55%"}, {"code": "MAT157Y1", "min_req": "55%"})
]
eco210h1_cor = []

# Special Note: Prerequisites (Note:  STA257H1,  MAT223H1/ MAT240H1,  MAT237Y1/ MAT257Y1 are very strongly recommended)
sta347h1_pre = [
    (
        {"code": "STA247H1", "min_req": "70%"},
        {"code": "STA255H1", "min_req": "70%"},
        {"code": "STA237H1", "min_req": "70%"},
        "STA257H1",
        "ECO227Y1"
    ),
    ("MAT223H1", "MAT224H1", "MAT240H1"),
    ("MAT235Y1", "MAT237Y1", "MAT257Y1")
]
sta347h1_cor = []

csc401h1_pre = [
    ("CSC207H1", "CSC209H1"),
    ("STA237H1", "STA247H1", "STA255H1")
]
csc401h1_cor = []

csc207h1_pre = [
    {"code": "CSC148H1", "min_req": "60%"},
    {"code": "CSC111H1", "min_req": "60%"}
]
csc207h1_cor = []

csc209h1_pre = [
    (
        "CSC207H1"
    )
]
csc209h1_cor = []

csc485h1_pre = [
    "CSC209H1",
    ("STA237H1", "STA247H1", "STA255H1", "STA257H1")
]
csc485h1_cor = []

csc320h1_pre = [
    ("CSC263H1", "CSC265H1"),
    ("MAT223H1", "MAT240H1"),
    ({"code": "MAT136H1", "min_req": "77%"},
     {"code": "MAT137Y1", "min_req": "73%"}, 
     {"code": "MAT157Y1", "min_req": "67%"},
     "MAT235Y1",
     "MAT237Y1",
     "MAT257Y1",
    )
]
csc320h1_cor = []

csc263h1_pre = [
    ("CSC236H1", "CSC240H1"),
    ("STA237H1", "STA247H1", "STA255H1", "STA257H1")
]
csc263h1_cor = []

csc236h1_pre = [
    (
        [
            {"code": "CSC148H1", "min_req": "60%"},
            {"code": "CSC165H1", "min_req": "60%"}
        ],
        {"code": "CSC111H1", "min_req": "60%"}
    )
]
csc236h1_cor = []

# Special Note, doesn't really require that corequisite
csc165h1_pre = []
csc165h1_cor = [
    "CSC108H1"
]

# Special Note, Prerequisite is not really needed, strong math background needed
csc240h1_pre = [
    ({"code": "CSC110Y1", "min_req": "70%"},
     {"code": "CSC165H1", "min_req": "85%"}
    )
]
csc240h1_cor = [
    ("CSC111H1", "CSC148H1"),
    ("MAT137Y1", "MAT157Y1")
]

# Notes: Students who have completed  CSC240H1 must enrol in  MAT377H1/  STA237H1/  STA247H1/  STA255H1/  STA257H1 concurrently with  CSC265H1, if they have not already completed one of those courses. Students who have completed additional 200- or 300-level Mathematics courses may submit a prerequisite waiver request for permission to complete the statistics requirement as a co-requisite or to consider other courses as appropriate preparation for  CSC265H1.
csc265h1_pre = [
    ({"code": "CSC240H1", "min_req": "70%"},
    {"code": "CSC236H1", "min_req": "85%"}),
    ("MAT337H1", "STA237H1", "STA247H1", "STA255H1", "STA257H1")
]
csc265h1_cor = []

mat377h1_pre = [
    "MAT247H1",
    "MAT257Y1"
]
mat377h1_cor = []

csc420h1_pre = [
    ("CSC263H1", "CSC265H1"), 
    ([
        "MAT135H1",
        "MAT136H1"
    ],
        "MAT137Y1", "MAT157Y1", ["MAT194H1", "MAT195H1"]),
    ("MAT223H1", "MAT240H1"),
]
csc420h1_cor = []

mat194h1_pre = []
mat194h1_cor = []

mat195h1_pre = []
mat195h1_cor = []

# Check again
csc311h1_pre = [
    "CSC207H1",
    (
        "MAT235Y1",
        "MAT237Y1",
        "MAT257Y1",
        [
            {"code": "MAT135H1", "min_req": "77%"},
            {"code": "MAT136H1", "min_req": "77%"}
        ],
        {"code": "MAT137Y1", "min_req": "73%"},
        {"code": "MAT157Y1", "min_req": "67%"},
        [
            {"code": "MAT194H1", "min_req": "67%"},
            {"code": "MAT195H1", "min_req": "67%"}
        ]
    ),
    ("MAT223H1", "MAT240H1"),
    ("STA237H1", "STA247H1", "STA255H1", "STA257H1")
]
csc311h1_cor = []

csc413h1_pre = [
    ("CSC311H1", "STA314H1"),
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
    ("MAT223H1", "MAT240H1")
]
csc413h1_cor = []

sta314h1_pre = [
    "STA302H1",
    ("CSC108H1", "CSC110Y1", "CSC148H1"),
    ("MAT223H1", "MAT224H1", "MAT240H1"),
    ("MAT235Y1", "MAT237Y1", "MAT257Y1")
]
sta314h1_cor = []

csc412h1_pre = [
    ("CSC311H1", "STA314H1")
]
csc412h1_cor = []

sta414h1_pre = [
    ("STA314H1", "CSC311H1"),
    "STA302H1",
    ("CSC108H1", "CSC110Y1", "CSC148H1"),
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
    ("MAT223H1", "MAT224H1", "MAT240H1")
]
sta414h1_cor = []

csc304h1_pre = [
    ("STA247H1", "STA255H1", "STA257H1", "STA237H1", "PSY201H1", "ECO227Y1"),
    first_year_calc
]
csc304h1_cor = []

# Special Note, *CSC148H1 + ASMAJ1446A and completed >= 9 credits
# NOT SURE IF THIS ONE IS CORRECT Check again
csc384h1_pre = [
    ("CSC263H1", "CSC265H1", "CSC148H1"),
    ("STA220H1", "STA237H1", "STA247H1", "STA255H1", "STA257H1", "PSY201H1")
]
csc384h1_cor = []

csc486h1_pre = [
    "CSC384H1"
]
csc486h1_cor = []

csc324h1_pre = [
    ("CSC263H1", "CSC265H1")
]
csc324h1_cor = []

psy270h1_pre = [
    ("PSY100H1", "COG250Y1")
]
psy270h1_cor = []

phl232h1_pre = []
phl232h1_cor = []

# Special note Prerequisite: 8.0 credits, including  COG250Y1 or 1.5 credits in PHL
phl342h1_pre = []
phl342h1_cor = []

# Special Note Prerequisite: Any 0.5 credit in CSC/ ESC180H1/ ESC190H1/ APS105H1/ APS106H1
csc318h1_pre = []
csc318h1_cor = []

lin101h1_pre = []
lin101h1_cor = []

lin200h1_pre = []
lin200h1_cor = []

csc309h1_pre = [
    "CSC209H1"
]
csc309h1_cor = []

csc428h1_pre = [
    "CSC318H1",
    ("STA237H1", "STA247H1", "STA255H1", "STA257H1"),
    "CSC207H1"
]
csc428h1_cor = []

csc343h1_pre = [
    ("CSC111H1", "CSC165H1", "CSC240H1", [
        "MAT135H1",
        "MAT136H1"
    ], "MAT137Y1", "MAT157Y1"),
    "CSC207H1"
]
csc343h1_cor = []

csc367h1_pre = [
    "CSC258H1",
    "CSC209H1"
]
csc367h1_cor = []

# Check this again
csc258h1_pre = [
    {"code": "CSC148H1", "min_req": "60%"},
    (
        {"code": "CSC165H1", "min_req": "60%"},
        {"code": "CSC240H1", "min_req": "60%"},
        {"code": "CSC111H1", "min_req": "60%"},
    )
]
csc258h1_cor = []

csc369h1_pre = [
    "CSC209H1",
    "CSC258H1"
]
csc369h1_cor = []

csc457h1_pre = [
    "CSC373H1", 
    ("STA247H1", "STA255H1", "STA257H1", "STA237H1"),
]
csc457h1_cor = []

csc373h1_pre = [
    ("CSC263H1", "CSC265H1")
]
csc373h1_cor = []

csc458h1_pre = [
    "CSC209H1", "CSC258H1", 
    ("CSC263H1", "CSC265H1"),
    ("STA247H1", "STA255H1", "STA257H1", "STA237H1", "ECO227Y1")
]
csc458h1_cor = []

csc368h1_pre = [
    "CSC209H1",
    "CSC258H1"
]
csc368h1_cor = []

csc385h1_pre = [
    "CSC258H1",
    "CSC209H1"
]
csc385h1_cor = []

csc443h1_pre = [
    "CSC343H1",
    "CSC369H1", 
    "CSC373H1"
]
csc443h1_cor = []

csc469h1_pre = [
    "CSC369H1"
]
csc469h1_cor = []

csc488h1_pre = [
    "CSC258H1",
    "CSC324H1",
    ("CSC263H1", "CSC265H1")
]
csc488h1_cor = []

csc301h1_pre = [
    "CSC209H1",
    ("CSC263H1", "CSC265H1"),
]
csc301h1_cor = []

csc410h1_pre = [
    "CSC207H1", 
    ("CSC236H1", "CSC240H1"),
]
csc410h1_cor = []

# Special Note: CSC209 may be omitted if proficient in C or C++
csc417h1_pre = [
    ("MAT237Y1", "MAT237Y1", "MAT257Y1"),
    ("MAT223H1", "MAT240H1"),
    "CSC209H1"
]
csc417h1_cor = []

csc317h1_pre = [
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
    ("MAT223H1", "MAT240H1"),
    "CSC209H1"
]
csc317h1_cor = []

# Special Note: CSC209 may be omitted if proficient in C or C++
csc419h1_pre = [
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
    ("MAT223H1", "MAT240H1"),
    "CSC209H1"
]
csc419h1_cor = []

apm462h1_pre = [
    (["MAT223H1", "MAT224H1"], "MAT247H1"),
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
]
apm462h1_cor = []

phy385h1_pre = [
    "PHY250H1",
    "PHY224H1", 
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
]
phy385h1_cor = []

phy250h1_pre = [
    ("PHY131H1", "PHY151H1"),
    ("PHY132H1", "PHY152H1"),
    (
        ["MAT135H1", "MAT136H1"],
        "MAT137Y1",
        "MAT157Y1"
    )
]
phy250h1_cor = [
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
]

phy224h1_pre = [
    ("PHY131H1", "PHY151H1"),
    ("PHY132H1", "PHY152H1"),
    (
        ["MAT135H1", "MAT136H1"],
        "MAT137Y1",
        "MAT157Y1"
    )
]
phy224h1_cor = [
    ("PHY231H1", "PHY250H1", "PHY252H1", "PHY254H1", "PHY256H1")
]

phy231h1_pre = [
    ("PHY131H1", "PHY151H1"),
    ("PHY132H1", "PHY152H1"),
    (
        ["MAT135H1", "MAT136H1"],
        "MAT137Y1",
        "MAT157Y1"
    )
]
phy231h1_cor = []

phy252h1_pre = [
    ("PHY131H1", "PHY151H1"),
    ("PHY132H1", "PHY152H1"),
    (
        ["MAT135H1", "MAT136H1"],
        "MAT137Y1",
        "MAT157Y1"
    )
]
phy252h1_cor = [
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
]

phy254h1_pre = [
    ("PHY131H1", "PHY151H1"),
    ("PHY132H1", "PHY152H1"),
    (
        ["MAT135H1", "MAT136H1"],
        "MAT137Y1",
        "MAT157Y1"
    )
]
phy254h1_cor = [
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
]

# Special Note: + Corequisite ( MAT223H1/  MAT240H1 recommended)
phy256h1_pre = [
    ("PHY131H1", "PHY151H1"),
    ("PHY132H1", "PHY152H1"),
    (
        ["MAT135H1", "MAT136H1"],
        "MAT137Y1",
        "MAT157Y1"
    )
]
phy256h1_cor = [
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
]

psl440y1_pre = [
    ("PSL300H1", "PSY290H1")
]
psl440y1_cor = []

psl300h1_pre = []
psl300h1_cor = []

psy290h1_pre = [
    ("PSY100H1", "COG250Y1")
]
psy290h1_cor = []

psy280h1_pre = [
    ("PSY100H1", "COG250Y1")
]
psy280h1_cor = []

# Special Note Prerequisite: 0.5 credit in CSC
csc300h1_pre = []
csc300h1_cor = []

csc404h1_pre = [
    ("CSC301H1", "CSC317H1", "CSC318H1", "CSC384H1", "CSC417H1", "CSC419H1")
]
csc404h1_cor = []

csc303h1_pre = [
    ("CSC263H1", "CSC265H1"),
    ("STA247H1", "STA255H1", "STA257H1", "ECO227Y1", "STA237H1"),
    ("MAT223H1", "MAT240H1")
]
csc303h1_cor = []

mus300h1_pre = []
mus300h1_cor = []

cin212h1_pre = []
cin212h1_cor = []

# Special Note: Prerequisite: At least 10.0 credits, including  CIN105Y1,  CIN201Y1
cin432h1_pre = [
    "CIN105Y1", "CIN201Y1"
]
cin432h1_cor = [
    "CIN301Y1"
]

cin105y1_pre = []
cin105y1_cor = []

cin201y1_pre = [
    "CIN105Y1"
]
cin201y1_cor = []

cin301y1_pre = [
    "CIN105Y1",
    "CIN201Y1"
]
cin301y1_cor = []

# Special Note: Prerequisite: 1.0 ENG credit or any 4.0 credits
eng235h1_pre = []
eng235h1_cor = []

# Check if this one is correct
eco326h1_pre = [
    ({"code": "ECO200Y1", "min_req": "70%"}, "ECO204Y1", "ECO206Y1"),
    (
        {"code": "ECO220Y1", "min_req": "70%"},
        "ECO227Y1",
        [{"code": "STA237H1", "min_req": "70%"}, {"code": "STA238H1", "min_req": "70%"}],
        [{"code": "STA247H1", "min_req": "70%"}, {"code": "STA248H1", "min_req": "70%"}],
        ["STA257H1", "STA261H1"]
    )
]
eco326h1_cor = []

eco200y1_pre = [
    ([{"code": "ECO101H1", "min_req": "63%"}, {"code": "ECO102H1", "min_req": "63%"}],
     {"code": "ECO105Y1", "min_req": "80%"},
     ),
    ("MAT133Y1", ["MAT135H1", "MAT136H1"],"MAT137Y1","MAT157Y1")
]
eco200y1_cor = []

eco204y1_pre = [
    [
        {
            "code": "ECO101H1",
            "min_req": "63%"
        },
        {
            "code": "ECO102H1",
            "min_req": "63%"
        }
    ],
    (
        {
            "code": "MAT133Y1",
            "min_req": "63%"
        },
        [
            {
                "code": "MAT135H1",
                "min_req": "60%"
            },
            {
                "code": "MAT136H1",
                "min_req": "60%"
            }
        ],
        {
            "code": "MAT137Y1",
            "min_req": "55%"
        },
        {
            "code": "MAT157Y1",
            "min_req": "55%"
        }
    )
]
eco204y1_cor = []

eco206y1_pre = [
    [
        {
            "code": "ECO101H1",
            "min_req": "63%"
        },
        {
            "code": "ECO102H1",
            "min_req": "63%"
        }
    ],
    (
        {
            "code": "MAT133Y1",
            "min_req": "63%"
        },
        [
            {
                "code": "MAT135H1",
                "min_req": "60%"
            },
            {
                "code": "MAT136H1",
                "min_req": "60%"
            }
        ],
        {
            "code": "MAT137Y1",
            "min_req": "55%"
        },
        {
            "code": "MAT157Y1",
            "min_req": "55%"
        }
    )
]
eco206y1_cor = []

rsm482h1_pre = [
    ("ECO204Y1", "ECO206Y1")
]
rsm482h1_cor = []

soc204h1_pre = [
    "SOC100H1", "SOC150H1"
]
soc204h1_cor = []

soc100h1_pre = []
soc100h1_cor = []

soc150h1_pre = ["SOC100H1"]
soc150h1_cor = []

csc302h1_pre = [
    "CSC301H1",
]
csc302h1_cor = []

csc316h1_pre = [
    "CSC207H1",
]
csc316h1_cor = []

# Special Note Prerequisite: 2.5 credits at the 300-level or higher
csc318h1_pre = []
csc318h1_cor = []

sta313h1_pre = [
    ("CSC108H1", "CSC110Y1", "CSC148H1"),
    ("STA238H1", "STA248H1", "STA261H1", "ECO227Y1"),
]
sta313h1_cor = []

# Special Note Prerequisite: Completion of 4.0 credits
env281h1_pre = []
env281h1_cor = []

# Special Note Prerequisite: Completion of 9.0 credits
env381h1_pre = []
env381h1_cor = []

# Special Note Prerequisite: 4.0 credits
ire260h1_pre = []
ire260h1_cor = []

cog260h1_pre = [
    ("CSC108H1", "CSC148H1"),
]
cog260h1_cor = [
    "COG250Y1"
]

cog341h1_pre = [
    "COG250Y1",
    ("PSY270H1", "PHL342H1")
]
cog341h1_cor = []

cog343h1_pre = [
    "COG260H1",
    "CSC148H1",
    ("STA220H1", "PSY201H1")
]
cog343h1_cor = []

cog344h1_pre = [
    "COG250Y1",
    (
        "LIN232H1", 
        "LIN241H1",
        "JLP315H1",
        "JLP374H1",
    )
]
cog344h1_cor = []

lin232h1_pre = [
    "LIN101H1"
]
lin232h1_cor = []

lin102h1_pre = []
lin102h1_cor = []

lin241h1_pre = [
    "LIN102H1"
]
lin241h1_cor = []

# Special Note Prerequisite: 1.0 credit at the 200+ level in LIN/JAL/JUP/PSL/PSY/COG
jlp315h1_pre = []
jlp315h1_cor = []

# Special Note Prerequisite: 1.0 credit from  LIN228H1,  LIN229H1,  LIN232H1,  LIN241H1,  PSY260H1,  PSY270H1,  PSY280H1,  PSY290H1,  COG250Y1
jlp374h1_pre = []
jlp374h1_cor = []

lin228h1_pre = []
lin228h1_cor = []

lin229h1_pre = [
    "LIN101H1", "LIN228H1"
]
lin229h1_cor = []

psy260h1_pre = [
    ("PSY100H1", "COG250Y1")
]
psy260h1_cor = []

csc436h1_pre = [
    "CSC336H1"
]
csc436h1_cor = []

# Special NOte + Exposure to PDEs for MAT244 and MAT267 thing 
csc446h1_pre = [
    {
        "code": "CSC336H1",
        "min_req": "75%"
    },
    ("MAT237Y1", "MAT257Y1"),
    ("APM346H1", "MAT351Y1", ("MAT244H1", "MAT267H1"))
]
csc446h1_cor = []

apm346h1_pre = [
    ("MAT235Y1", "MAT237Y1", "MAT257Y1"),
    ("MAT244H1", "MAT267H1")
]
apm346h1_cor = []

mat244h1_pre = [
    (
        (("MAT133Y1", "MAT135H1"), "MAT136H1"),
        "MAT137Y1", "MAT157Y1"
    ),
    ("MAT223H1",
    "MAT240H1")
]
mat244h1_cor = ["MAT235Y1", "MAT237Y1", "MAT257Y1"]

mat267h1_pre = [
    "MAT157Y1",
    "MAT247H1"
]
mat267h1_cor = ["MAT257Y1"]

mat351y1_pre = [
    ("MAT257Y1", {"code": "MAT237Y1", "min_req": "85%"}),
    "MAT267H1"
]
mat351y1_cor = []

# Special Note: Prerequisite csc209 can be replaced if proficient in c, C++ or fortran
csc456h1_pre = [
    ("CSC436H1", {"code": "CSC336H1", "min_req": "75%"}),
    "CSC209H1"
]
csc456h1_cor = []


csc466h1_pre = [
    "CSC336H1", 
    ("MAT223H1", "MAT240H1"),
    ("MAT235Y1", "MAT237Y1", "MAT257Y1")
]
csc466h1_cor = []

mat334h1_pre = [
    ("MAT223H1", "MAT240H1"),
    ("MAT235Y1", "MAT237Y1", "MAT257Y1")
]
mat334h1_cor = []

mat354h1_pre = [
    "MAT257Y1"
]
mat354h1_cor = []

mat337h1_pre = [
    "MAT257Y1", 
]
mat337h1_cor = []

mat357h1_pre = [
    "MAT257Y1"
]
mat357h1_cor = []

csc308h1_pre = [
    "CSC207H1"
]
csc308h1_cor = []

# Special Note (Project course) Prerequisite: 1.5 credits of 300+ level CSC courses.
csc490h1_pre = []
csc490h1_cor = []

# Special Note (Project Course) Corequisite: CSC454H1/ CSC2527H (Grad school level courses)
csc491h1_pre = []
csc491h1_cor = []

# Special Note (Project Course) Prerequisite: 1.5 credits of 300+ level CSC courses.
csc494h1_pre = []
csc494h1_cor = []

# Special Note (Project Course) Prerequisite: CSC494H1. 1.5 credits of 300+ level CSC courses.
csc495h1_pre = []
csc495h1_cor = []

# Special Note (Project course) Prerequisite: 1.5 credits of 300+ level CSC courses.
csc494y1_pre = []
csc494y1_cor = []


csc463h1_pre = [
    ("CSC236H1", "CSC240H1")
]
csc463h1_cor = []

csc310h1_pre = [
    (
        {"code": "CSC148H1", "min_req": "60%"},
        {"code": "CSC111H1", "min_req": "60%"}
    ),
    (
        "CSC263H1",
        "CSC265H1"
    ),
    (
        "MAT223H1",
        "MAT240H1"
    )
]
csc310h1_cor = []

csc438h1_pre = [
    (
        "CSC463H1",
        "CSC373H1",
        "MAT247H1"
     )
]
csc438h1_cor = []

mat309h1_pre = [
    (
        "MAT257Y1",
        [
            (
                "MAT223H1",
                "MAT240H1",
            ),
            ("MAT235Y1","MAT237Y1"),
            ("MAT246H1", "MAT157Y1", "CSC236H1", "CSC240H1")
        ]
    )
]
mat309h1_cor = []

csc448h1_pre = [
    ("CSC236H1", "CSC240H1"),
    ("CSC263H1", "CSC265H1"),
]
csc448h1_cor = []

csc473h1_pre = [
    "CSC373H1",
    ("MAT223H1", "MAT240H1"),
]
csc473h1_cor = []

mat332h1_pre = [
    ("MAT224H1", "MAT247H1")
]
mat332h1_cor = []

mat344h1_pre = [
    ("MAT223H1", "MAT240H1")
]
mat344h1_cor = []

# Additional courses - I should do like a note for special non-course requirements, to have people visit the actual site
csc454h1_pre = []
csc454h1_cor = []

output_titles_dict = {'CSC336H1': 'CSC336H1: Numerical Methods', 'CSC148H1': 'CSC148H1: Introduction to Computer Science', 'CSC108H1': 'CSC108H1: Introduction to Computer Programming', 'CSC111H1': 'CSC111H1: Foundations of Computer Science II', 'CSC110Y1': 'CSC110Y1: Foundations of Computer Science I', 'MAT133Y1': 'MAT133Y1: Calculus and Linear Algebra for Commerce', 'MAT135H1': 'MAT135H1: Calculus I', 'MAT136H1': 'MAT136H1: Calculus II', 'MAT137Y1': 'MAT137Y1: Calculus with Proofs', 'MAT157Y1': 'MAT157Y1: Analysis I', 'MAT223H1': 'MAT223H1: Linear Algebra I', 'MAT240H1': 'MAT240H1: Algebra I', 'MAT235Y1': 'MAT235Y1: Multivariable Calculus', 'MAT237Y1': 'MAT237Y1: Multivariable Calculus with Proofs', 'MAT138H1': 'MAT138H1: Introduction to Proofs', 'MAT246H1': 'MAT246H1: Concepts in Abstract Mathematics', 'MAT257Y1': 'MAT257Y1: Analysis II', 'MAT247H1': 'MAT247H1: Algebra II', 'APM236H1': 'APM236H1: Applications of Linear Programming', 'MAT221H1': 'MAT221H1: Applied Linear Algebra', 'MAT224H1': 'MAT224H1: Linear Algebra II', 'STA238H1': 'STA238H1: Probability, Statistics and Data Analysis II', 'STA237H1': 'STA237H1: Probability, Statistics and Data Analysis I', 'STA247H1': 'STA247H1: Probability with Computer Applications', 'STA257H1': 'STA257H1: Probability and Statistics I', 'STA248H1': 'STA248H1: Statistics for Computer Scientists', 'STA261H1': 'STA261H1: Probability and Statistics II', 'STA302H1': 'STA302H1: Methods of Data Analysis I', 'STA255H1': 'STA255H1: Statistical Theory', 'STA220H1': 'STA220H1: The Practice of Statistics I', 'STA221H1': 'STA221H1: The Practice of Statistics II', 'STA288H1': 'STA288H1: Statistics and Scientific Inquiry in the Life Sciences', 'BIO230H1': 'BIO230H1: From Genes to Organisms', 'BIO130H1': 'BIO130H1: Molecular and Cell Biology', 'CHM135H1': 'CHM135H1: Chemistry: Physical Principles', 'CHM136H1': 'CHM136H1: Introductory Organic Chemistry I', 'CHM151Y1': 'CHM151Y1: Chemistry: The Molecular Science', 'PHY131H1': 'PHY131H1: Introduction to Physics I', 'PHY132H1': 'PHY132H1: Introduction to Physics II', 'PHY151H1': 'PHY151H1: Foundations of Physics I', 'PHY152H1': 'PHY152H1: Foundations of Physics II', 'BIO255H1': 'BIO255H1: From Genes to Organisms with Advanced Laboratory', 'PSY201H1': 'PSY201H1: Statistics I', 'PSY100H1': 'PSY100H1: Introductory Psychology', 'COG250Y1': 'COG250Y1: Introduction to Cognitive Science', 'GGR270H1': 'GGR270H1: Introductory Analytical Methods', 'EEB225H1': 'EEB225H1: Biostatistics for Biological Sciences', 'BIO120H1': 'BIO120H1: Adaptation and Biodiversity', 'ECO220Y1': 'ECO220Y1: Introduction to Data Analysis and Applied Econometrics', 'ECO101H1': 'ECO101H1: Principles of Microeconomics', 'ECO102H1': 'ECO102H1: Principles of Macroeconomics', 'ECO105Y1': 'ECO105Y1: Principles of Economics for Non-Specialists', 'ECO227Y1': 'ECO227Y1: Foundations of Econometrics', 'ECO210H1': 'ECO210H1: Mathematical Methods for Economic Theory', 'STA347H1': 'STA347H1: Probability', 'CSC401H1': 'CSC401H1: Natural Language Computing', 'CSC207H1': 'CSC207H1: Software Design', 'CSC209H1': 'CSC209H1: Software Tools and Systems Programming', 'CSC485H1': 'CSC485H1: Computational Linguistics', 'CSC320H1': 'CSC320H1: Introduction to Visual Computing', 'CSC263H1': 'CSC263H1: Data Structures and Analysis', 'CSC236H1': 'CSC236H1: Introduction to the Theory of Computation', 'CSC165H1': 'CSC165H1: Mathematical Expression and Reasoning for Computer Science', 'CSC240H1': 'CSC240H1: Enriched Introduction to the Theory of Computation', 'CSC265H1': 'CSC265H1: Enriched Data Structures and Analysis', 'MAT377H1': 'MAT377H1: Mathematical Probability Theory', 'CSC420H1': 'CSC420H1: Introduction to Image Understanding', 'MAT194H1': 'MAT194H1: Mathematical Personalities', 'MAT195H1': 'MAT195H1: Mathematics as an Interdisciplinary Pursuit', 'CSC311H1': 'CSC311H1: Introduction to Machine Learning', 'CSC413H1': 'CSC413H1: Neural Networks and Deep Learning', 'STA314H1': 'STA314H1: Statistical Methods for Machine Learning I', 'CSC412H1': 'CSC412H1: Probabilistic Learning and Reasoning', 'STA414H1': 'STA414H1: Statistical Methods for Machine Learning II', 'CSC304H1': 'CSC304H1: Algorithmic Game Theory and Mechanism Design', 'CSC384H1': 'CSC384H1: Introduction to Artificial Intelligence', 'CSC486H1': 'CSC486H1: Knowledge Representation and Reasoning', 'CSC324H1': 'CSC324H1: Principles of Programming Languages', 'PSY270H1': 'PSY270H1: Introduction to Cognitive Psychology', 'PHL232H1': 'PHL232H1: Knowledge and Reality', 'PHL342H1': 'PHL342H1: Minds and Machines', 'CSC318H1': 'CSC318H1: The Design of Interactive Computational Media', 'LIN101H1': 'LIN101H1: Introduction to Linguistics: Sound Structure', 'LIN200H1': 'LIN200H1: Introduction to Language', 'CSC309H1': 'CSC309H1: Programming on the Web', 'CSC428H1': 'CSC428H1: Human-Computer Interaction', 'CSC343H1': 'CSC343H1: Introduction to Databases', 'CSC367H1': 'CSC367H1: Parallel Programming', 'CSC258H1': 'CSC258H1: Computer Organization', 'CSC369H1': 'CSC369H1: Operating Systems', 'CSC457H1': 'CSC457H1: Principles of Computer Networks', 'CSC373H1': 'CSC373H1: Algorithm Design, Analysis & Complexity', 'CSC458H1': 'CSC458H1: Computer Networking Systems', 'CSC368H1': 'CSC368H1: Computer Architecture', 'CSC385H1': 'CSC385H1: Microprocessor Systems', 'CSC443H1': 'CSC443H1: Database System Technology', 'CSC469H1': 'CSC469H1: Operating Systems Design and Implementation', 'CSC488H1': 'CSC488H1: Compilers and Interpreters', 'CSC301H1': 'CSC301H1: Introduction to Software Engineering', 'CSC410H1': 'CSC410H1: Software Testing and Verification', 'CSC417H1': 'CSC417H1: Physics-Based Animation', 'CSC317H1': 'CSC317H1: Computer Graphics', 'CSC419H1': 'CSC419H1: Geometry Processing', 'APM462H1': 'APM462H1: Nonlinear Optimization', 'PHY385H1': 'PHY385H1: Introductory Optics', 'PHY250H1': 'PHY250H1: Electricity and Magnetism', 'PHY224H1': 'PHY224H1: Practical Physics I', 'PHY231H1': 'PHY231H1: Physics of Living Systems', 'PHY252H1': 'PHY252H1: Thermal Physics', 'PHY254H1': 'PHY254H1: Classical Mechanics', 'PHY256H1': 'PHY256H1: Introduction to Quantum Physics', 'PSL440Y1': 'PSL440Y1: Neuroscience: Systems and Behaviour', 'PSL300H1': 'PSL300H1: Human Physiology I', 'PSY290H1': 'PSY290H1: Behavioural Neuroscience', 'PSY280H1': 'PSY280H1: Introduction to Sensation and Perception', 'CSC300H1': 'CSC300H1: Computers and Society', 'CSC404H1': 'CSC404H1: Introduction to Video Game Design', 'CSC303H1': 'CSC303H1: Social and Information Networks', 'MUS300H1': 'MUS300H1: Music, Media and Technology', 'CIN212H1': 'CIN212H1: Cinema and Sensation I: Action/Spectacle', 'CIN432H1': 'CIN432H1: Advanced Study in Cinema as Social and Cultural Practice', 'CIN105Y1': 'CIN105Y1: Introduction to Film Study', 'CIN201Y1': 'CIN201Y1: Film Cultures I: Art and Industry', 'CIN301Y1': 'CIN301Y1: Film Cultures II: Politics and Global Media', 'ENG235H1': 'ENG235H1: The Graphic Novel', 'ECO326H1': 'ECO326H1: Advanced Microeconomics - Game Theory', 'ECO200Y1': 'ECO200Y1: Microeconomic Theory', 'ECO204Y1': 'ECO204Y1: Microeconomic Theory and Applications (for Commerce)', 'ECO206Y1': 'ECO206Y1: Microeconomic Theory', 'RSM482H1': 'RSM482H1: Game Theory for Business Strategy', 'SOC204H1': 'SOC204H1: Introduction to Qualitative Methods in Sociology', 'SOC100H1': 'SOC100H1: Introduction to Sociology I: Sociological Perspectives', 'SOC150H1': 'SOC150H1: Introduction to Sociology II: Sociological Inquiries', 'CSC302H1': 'CSC302H1: Engineering Large Software Systems', 'CSC316H1': 'CSC316H1: Data Visualization: Foundations and Advanced Programming', 'CSC454H1': 'CSC454H1: The Business of Software', 'STA313H1': 'STA313H1: Data Visualization', 'ENV281H1': 'ENV281H1: Special Topics in Environment', 'ENV381H1': 'ENV381H1: Special Topics in Environment', 'IRE260H1': 'IRE260H1: Organizational Behaviour', 'COG260H1': 'COG260H1: Data, Computation, and the Mind', 'COG341H1': 'COG341H1: Issues in Cognitive Science I: Attention, Perception, and Consciousness', 'COG343H1': 'COG343H1: Issues in Cognitive Science III: Computational Cognition', 'COG344H1': 'COG344H1: Issues in Cognitive Science IV: Language and Communication', 'LIN232H1': 'LIN232H1: Syntactic Patterns in Language', 'LIN102H1': 'LIN102H1: Introduction to Linguistics: Sentence Structure and Meaning', 'LIN241H1': 'LIN241H1: Introduction to Semantics', 'JLP315H1': 'JLP315H1: Language Acquisition', 'JLP374H1': 'JLP374H1: Psychology of Language', 'LIN228H1': 'LIN228H1: Phonetics', 'LIN229H1': 'LIN229H1: Phonological Patterns in Language', 'PSY260H1': 'PSY260H1: Introduction to Learning and Plasticity', 'CSC436H1': 'CSC436H1: Numerical Algorithms', 'CSC446H1': 'CSC446H1: Computational Methods for Partial Differential Equations', 'APM346H1': 'APM346H1: Partial Differential Equations', 'MAT244H1': 'MAT244H1: Introduction to Ordinary Differential Equations', 'MAT267H1': 'MAT267H1: Advanced Ordinary Differential Equations', 'MAT351Y1': 'MAT351Y1: Partial Differential Equations', 'CSC456H1': 'CSC456H1: High-Performance Scientific Computing', 'CSC466H1': 'CSC466H1: Numerical Methods for Optimization Problems', 'MAT334H1': 'MAT334H1: Complex Variables', 'MAT354H1': 'MAT354H1: Complex Analysis I', 'MAT337H1': 'MAT337H1: Introduction to Real Analysis', 'MAT357H1': 'MAT357H1: Foundations of Real Analysis', 'CSC308H1': 'CSC308H1: Technology Leadership', 'CSC490H1': 'CSC490H1: Capstone Design Project', 'CSC491H1': 'CSC491H1: Capstone Design Project', 'CSC494H1': 'CSC494H1: Computer Science Project', 'CSC495H1': 'CSC495H1: Computer Science Project', 'CSC494Y1': 'CSC494Y1: Computer Science Project', 'CSC463H1': 'CSC463H1: Computational Complexity and Computability', 'CSC310H1': 'CSC310H1: Information Theory', 'CSC438H1': 'CSC438H1: Computability and Logic', 'MAT309H1': 'MAT309H1: Introduction to Mathematical Logic', 'CSC448H1': 'CSC448H1: Formal Languages and Automata', 'CSC473H1': 'CSC473H1: Advanced Algorithm Design', 'MAT332H1': 'MAT332H1: Introduction to Graph Theory', 'MAT344H1': 'MAT344H1: Introduction to Combinatorics'}
output_codes = ['CSC336H1', 'CSC148H1', 'CSC108H1', 'CSC111H1', 'CSC110Y1', 'MAT133Y1', 'MAT135H1', 'MAT136H1', 'MAT137Y1', 'MAT157Y1', 'MAT223H1', 'MAT240H1', 'MAT235Y1', 'MAT237Y1', 'MAT138H1', 'MAT246H1', 'MAT257Y1', 'MAT247H1', 'APM236H1', 'MAT221H1', 'MAT224H1', 'STA238H1', 'STA237H1', 'STA247H1', 'STA257H1', 'STA248H1', 'STA261H1', 'STA302H1', 'STA255H1', 'STA220H1', 'STA221H1', 'STA288H1', 'BIO230H1', 'BIO130H1', 'CHM135H1', 'CHM136H1', 'CHM151Y1', 'PHY131H1', 'PHY132H1', 'PHY151H1', 'PHY152H1', 'BIO255H1', 'PSY201H1', 'PSY100H1', 'COG250Y1', 'GGR270H1', 'EEB225H1', 'BIO120H1', 'ECO220Y1', 'ECO101H1', 'ECO102H1', 'ECO105Y1', 'ECO227Y1', 'ECO210H1', 'STA347H1', 'CSC401H1', 'CSC207H1', 'CSC209H1', 'CSC485H1', 'CSC320H1', 'CSC263H1', 'CSC236H1', 'CSC165H1', 'CSC240H1', 'CSC265H1', 'MAT377H1', 'CSC420H1', 'MAT194H1', 'MAT195H1', 'CSC311H1', 'CSC413H1', 'STA314H1', 'CSC412H1', 'STA414H1', 'CSC304H1', 'CSC384H1', 'CSC486H1', 'CSC324H1', 'PSY270H1', 'PHL232H1', 'PHL342H1', 'CSC318H1', 'LIN101H1', 'LIN200H1', 'CSC309H1', 'CSC428H1', 'CSC343H1', 'CSC367H1', 'CSC258H1', 'CSC369H1', 'CSC457H1', 'CSC373H1', 'CSC458H1', 'CSC368H1', 'CSC385H1', 'CSC443H1', 'CSC469H1', 'CSC488H1', 'CSC301H1', 'CSC410H1', 'CSC417H1', 'CSC317H1', 'CSC419H1', 'APM462H1', 'PHY385H1', 'PHY250H1', 'PHY224H1', 'PHY231H1', 'PHY252H1', 'PHY254H1', 'PHY256H1', 'PSL440Y1', 'PSL300H1', 'PSY290H1', 'PSY280H1', 'CSC300H1', 'CSC404H1', 'CSC303H1', 'MUS300H1', 'CIN212H1', 'CIN432H1', 'CIN105Y1', 'CIN201Y1', 'CIN301Y1', 'ENG235H1', 'ECO326H1', 'ECO200Y1', 'ECO204Y1', 'ECO206Y1', 'RSM482H1', 'SOC204H1', 'SOC100H1', 'SOC150H1', 'CSC302H1', 'CSC316H1', 'CSC454H1', 'STA313H1', 'ENV281H1', 'ENV381H1', 'IRE260H1', 'COG260H1', 'COG341H1', 'COG343H1', 'COG344H1', 'LIN232H1', 'LIN102H1', 'LIN241H1', 'JLP315H1', 'JLP374H1', 'LIN228H1', 'LIN229H1', 'PSY260H1', 'CSC436H1', 'CSC446H1', 'APM346H1', 'MAT244H1', 'MAT267H1', 'MAT351Y1', 'CSC456H1', 'CSC466H1', 'MAT334H1', 'MAT354H1', 'MAT337H1', 'MAT357H1', 'CSC308H1', 'CSC490H1', 'CSC491H1', 'CSC494H1', 'CSC495H1', 'CSC494Y1', 'CSC463H1', 'CSC310H1', 'CSC438H1', 'MAT309H1', 'CSC448H1', 'CSC473H1', 'MAT332H1', 'MAT344H1']