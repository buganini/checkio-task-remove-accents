# -*- coding: utf-8 -*-

"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": u"préfèrent",
            "answer": u"preferent",
        },
        {
            "input": u"loài trăn lớn",
            "answer": u"loai tran lon",
        },
        {
            "input": u"König",
            "answer": u"Konig",
        },
        {
            "input": u"完好無缺",
            "answer": u"完好無缺",
        },
    ],
    "Grave": [
        {
            "input": u"àèìǹòùẁỳÀÈÌǸÒÙẀỲ",
            "answer": u"aeinouwyAEINOUWY",
        },
    ],
    "Grave + Breve": [
        {
            "input": u"ằẰ",
            "answer": u"aA",
        },
    ],
    "Grave + Circum": [
        {
            "input": u"ầẦềỀồỒ",
            "answer": u"aAeEoO",
        },
    ],
    "Grave + Horn": [
        {
            "input": u"ờỜừỪ",
            "answer": u"oOuU",
        },
    ],
    "Double Grave": [
        {
            "input": u"ȁȅȉȍȑȕȀȄȈȌȐȔ",
            "answer": u"aeioruAEIORU",
        },
    ],
    "Acute": [
        {
            "input": u"áćéǵíḱĺḿńóṕŕśúẃýźÁĆÉǴÍḰĹḾŃÓṔŔŚÚẂÝŹ",
            "answer": u"acegiklmnoprsuwyzACEGIKLMNOPRSUWYZ",
        },
    ],
    "Acute + Breve": [
        {
            "input": u"ắẮ",
            "answer": u"aA",
        },
    ],
    "Acute + Circum": [
        {
            "input": u"ấẤếẾốỐ",
            "answer": u"aAeEoO",
        },
    ],
    "Acute + Horn": [
        {
            "input": u"ớỚứỨ",
            "answer": u"oOuU",
        },
    ],
    "Double Acute": [
        {
            "input": u"őűŐŰ",
            "answer": u"ouOU",
        },
    ],
    "Circum": [
        {
            "input": u"âĉêĝĥîĵôŝûŵŷẑÂĈÊĜĤÎĴÔŜÛŴŶẐ",
            "answer": u"aceghijosuwyzACEGHIJOSUWYZ",
        },
    ],
    "Caron": [
        {
            "input": u"ǎǍčČďĎěĚǧǦȟȞǐǏǰǩǨľĽňŇǒǑřŘšŠťŤǔǓžŽ",
            "answer": u"aAcCdDeEgGhHiIjkKlLnNoOrRsStTuUzZ",
        },
    ],
    "Breve": [
        {
            "input": u"ăĂĕĔğĞḫḪĭĬŏŎŭŬ",
            "answer": u"aAeEgGhHiIoOuU",
        },
    ],
    "Inverted Breve": [
        {
            "input": u"ȃȂȇȆȋȊȏȎȗȖȓȒ",
            "answer": u"aAeEiIoOuUrR",
        },
    ],
    "Tilde": [
        {
            "input": u"ãÃẽẼĩĨñÑõÕũŨṽṼỹỸ",
            "answer": u"aAeEiInNoOuUvVyY",
        },
    ],
    "Tilde + Breve": [
        {
            "input": u"ẵẴ",
            "answer": u"aA",
        },
    ],
    "Tilde + Circum": [
        {
            "input": u"ẫẪễỄỗỖ",
            "answer": u"aAeEoO",
        },
    ],
    "Tilde + Horn": [
        {
            "input": u"ỡỠữỮ",
            "answer": u"oOuU",
        },
    ],
    "Macron": [
        {
            "input": u"ĀāĒēḠḡĪīŌōŪūȲȳ",
            "answer": u"AaEeGgIiOoUuYy",
        },
    ],
    "Underline": [
        {
            "input": u"ḆḇḎḏẖḴḵḺḻṈṉṞṟṮṯẔẕ",
            "answer": u"BbDdhKkLlNnRrTtZz",
        },
    ],
    "Dieresis": [
        {
            "input": u"äëḧïöẗüẅẍÿÄËḦÏÖÜẄẌŸ",
            "answer": u"aehiotuwxyAEHIOUWXY",
        },
    ],
    "Ring": [
        {
            "input": u"åÅůŮẘẙ",
            "answer": u"aAuUwy",
        },
    ],
    "Dot": [
        {
            "input": u"ȧȦḃḂċĊḋḊėĖḟḞġĠḣḢİṁṀṅṄȯȮṗṖṙṘṡṠṫṪẇẆẋẊẏẎżŻ",
            "answer": u"aAbBcCdDeEfFgGhHImMnNoOpPrRsStTwWxXyYzZ",
        },
    ],
    "Under Dot": [
        {
            "input": u"ẠạḄḅḌḍẸẹḤḥỊịḲḳḶḷṂṃṆṇỌọṚṛṢṣṬṭỤụṾṿẈẉỴỵẒẓ",
            "answer": u"AaBbDdEeHhIiKkLlMmNnOoRrSsTtUuVvWwYyZz",
        },
    ],
    "Cedilla": [
        {
            "input": u"ąĄçÇḑḐęĘģĢḩḨįĮķĶļĻņŅǫǪŗŖşŞţŢųŲ",
            "answer": u"aAcCdDeEgGhHiIkKlLnNoOrRsStTuU",
        },
    ],
    "Hook": [
        {
            "input": u"ảẢẻẺỉỈỏỎủỦỷỶ",
            "answer": u"aAeEiIoOuUyY",
        },
    ],
    "Hook + Breve": [
        {
            "input": u"ẳẲ",
            "answer": u"aA",
        },
    ],
    "Hook + Circum": [
        {
            "input": u"ẩẨểỂổỔ",
            "answer": u"aAeEoO",
        },
    ],
    "Hook + Horn": [
        {
            "input": u"ởỞửỬ",
            "answer": u"oOuU",
        },
    ],
    "Under Dot + Breve": [
        {
            "input": u"ặẶ",
            "answer": u"aA",
        },
    ],
    "Under Dot + Circum": [
        {
            "input": u"ậẬệỆộỘ",
            "answer": u"aAeEoO",
        },
    ],
    "Under Dot + Horn": [
        {
            "input": u"ợỢựỰ",
            "answer": u"oOuU",
        },
    ],
    "Negative test": [
        {
            "input": u"蟒蛇",
            "answer": u"蟒蛇",
        },
        {
            "input": u"   ",
            "answer": u"   ",
        },
        {
            "input": u"!@#$%^&*()_+,./<>?",
            "answer": u"!@#$%^&*()_+,./<>?",
        },
    ]
}
