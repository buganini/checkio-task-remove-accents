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
        {
            "input": u"àèìǹòùẁỳÀÈÌǸÒÙẀỲ",
            "answer": u"aeinouwyAEINOUWY",
        },
        {
            "input": u"ằẰ",
            "answer": u"aA",
        },
        {
            "input": u"ầẦềỀồỒ",
            "answer": u"aAeEoO",
        },
        {
            "input": u"ờỜừỪ",
            "answer": u"oOuU",
        },
        {
            "input": u"ȁȅȉȍȑȕȀȄȈȌȐȔ",
            "answer": u"aeioruAEIORU",
        },
        {
            "input": u"áćéǵíḱĺḿńóṕŕśúẃýźÁĆÉǴÍḰĹḾŃÓṔŔŚÚẂÝŹ",
            "answer": u"acegiklmnoprsuwyzACEGIKLMNOPRSUWYZ",
        },
        {
            "input": u"ắẮ",
            "answer": u"aA",
        },
        {
            "input": u"ấẤếẾốỐ",
            "answer": u"aAeEoO",
        },
        {
            "input": u"ớỚứỨ",
            "answer": u"oOuU",
        },
        {
            "input": u"őűŐŰ",
            "answer": u"ouOU",
        },
        {
            "input": u"âĉêĝĥîĵôŝûŵŷẑÂĈÊĜĤÎĴÔŜÛŴŶẐ",
            "answer": u"aceghijosuwyzACEGHIJOSUWYZ",
        },
        {
            "input": u"ǎǍčČďĎěĚǧǦȟȞǐǏǰǩǨľĽňŇǒǑřŘšŠťŤǔǓžŽ",
            "answer": u"aAcCdDeEgGhHiIjkKlLnNoOrRsStTuUzZ",
        },
        {
            "input": u"ăĂĕĔğĞḫḪĭĬŏŎŭŬ",
            "answer": u"aAeEgGhHiIoOuU",
        },
        {
            "input": u"ȃȂȇȆȋȊȏȎȗȖȓȒ",
            "answer": u"aAeEiIoOuUrR",
        },
        {
            "input": u"ãÃẽẼĩĨñÑõÕũŨṽṼỹỸ",
            "answer": u"aAeEiInNoOuUvVyY",
        },
        {
            "input": u"ẵẴ",
            "answer": u"aA",
        },
    ],
    "Extra": [
        {
            "input": u"ẫẪễỄỗỖ",
            "answer": u"aAeEoO",
        },
        {
            "input": u"ỡỠữỮ",
            "answer": u"oOuU",
        },
        {
            "input": u"ĀāĒēḠḡĪīŌōŪūȲȳ",
            "answer": u"AaEeGgIiOoUuYy",
        },
        {
            "input": u"ḆḇḎḏẖḴḵḺḻṈṉṞṟṮṯẔẕ",
            "answer": u"BbDdhKkLlNnRrTtZz",
        },
        {
            "input": u"äëḧïöẗüẅẍÿÄËḦÏÖÜẄẌŸ",
            "answer": u"aehiotuwxyAEHIOUWXY",
        },
        {
            "input": u"åÅůŮẘẙ",
            "answer": u"aAuUwy",
        },
        {
            "input": u"ȧȦḃḂċĊḋḊėĖḟḞġĠḣḢİṁṀṅṄȯȮṗṖṙṘṡṠṫṪẇẆẋẊẏẎżŻ",
            "answer": u"aAbBcCdDeEfFgGhHImMnNoOpPrRsStTwWxXyYzZ",
        },
        {
            "input": u"ẠạḄḅḌḍẸẹḤḥỊịḲḳḶḷṂṃṆṇỌọṚṛṢṣṬṭỤụṾṿẈẉỴỵẒẓ",
            "answer": u"AaBbDdEeHhIiKkLlMmNnOoRrSsTtUuVvWwYyZz",
        },
        {
            "input": u"ąĄçÇḑḐęĘģĢḩḨįĮķĶļĻņŅǫǪŗŖşŞţŢųŲ",
            "answer": u"aAcCdDeEgGhHiIkKlLnNoOrRsStTuU",
        },
        {
            "input": u"ảẢẻẺỉỈỏỎủỦỷỶ",
            "answer": u"aAeEiIoOuUyY",
        },
        {
            "input": u"ẳẲ",
            "answer": u"aA",
        },
        {
            "input": u"ẩẨểỂổỔ",
            "answer": u"aAeEoO",
        },
        {
            "input": u"ởỞửỬ",
            "answer": u"oOuU",
        },
        {
            "input": u"ặẶ",
            "answer": u"aA",
        },
        {
            "input": u"ậẬệỆộỘ",
            "answer": u"aAeEoO",
        },
        {
            "input": u"ợỢựỰ",
            "answer": u"oOuU",
        },
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
