#!/usr/bin/python3
"""
Create a coincidence index of the characters and compute
the likelihood that the text is random.
- Joe Aczel
12/3/2020
"""

import collections
import matplotlib.pyplot as plt


def make_dict(in_text):
    """
    Create a counter of the string
    """
    my_dict = dict()
    for c in in_text:
        if c in [' ', '\n']:
            continue
        if c not in my_dict.keys():
            my_dict[c] = 1
        else:
            my_dict[c] += 1

    return my_dict


def make_bar_chart(character_count):
    """
    Make a bar chart
    """
    plt.bar(range(len(character_count)),
            list(character_count.values()),
            align='center')

    plt.xticks(range(len(character_count)),
               list(character_count.keys()))


def compute_coincidence_index(text_dictionary):
    """
    Compute the Coincidence Index
    http://alexbarter.com/statistics/index-of-coincidence/
    :param dictionary
    :ret float
    """
    count = 0
    count_minus_one = 0
    for c in text_dictionary.values():
        count += c
        count_minus_one += c * (c - 1)
    return count_minus_one / (count * (count - 1))


if __name__ == "__main__":

    text_1 = 'LRFKQ YUQFJ KXYQV NRTYS FRZRM ZLYGF'\
             'VEULQ FPDBH LQDQR RCRWD NXEUO QQEKL'\
             'AITGD PHCSP IJTHB SFYFV LADZP BFUDK'\
             'KLRWQ AOZMI XRPIF EFFEC LHBVF UKBYE'\
             'QFQOJ WIWOS ILEEZ TXWJL KNGBQ QMBXQ'\
             'CQPTK HHQRQ DWFCA YSSYO QCJOM WUFBD'\
             'FXUDZ HIFTA KCZVH SYBLO ETSWC RFHPX'\
             'PRBSS HSJXD FILEB XWBCT OAYAX ZFBJB'\
             'KRXIR IMQPZ WMSHL PJHTA ZHBUX HWADL'\
             'PTOYE ZIWKM GSOVQ ZGDIX RPDDZ PLCRW'\
             'NQWQE CYJYI BFIYK MJFQW LTVZK QTPVO'\
             'LPHCK CYUFD QMLGL IMKLF ZKTGY GDTIN'\
             'HCVPF DFBRP ZLKVS HWYWS HTDGM BQBKK'\
             'XCVGU MONMW VYTBY TNUQH MFJAQ TGNGC'\
             'WKUZY AMNER PHFMW EVHWL EZOHY EEHBR'

    text_2 = 'NUFTD WHFTW HFQUU VZXCX FFINA XMHMT'\
             'MHFHC XFFTZ AHXMT YUCXM HHAXN TFXNJ'\
             'HZTNX VATCU ZUNAH ATNTZ XDFTZ MUTAU'\
             'ZAXMH LXCNT NXACX WXMUN DVTNH OCTDH'\
             'YUCFQ UTRZH CXFFT ZATCX FFQHV MUHZD'\
             'UVZXD ATCHX YHFFT NXTRC XZMUF QUDHX'\
             'ZXCCX ZAUHJ XCHXD YUAAH MUNFT DWTVD'\
             'XZMTV ZNHZR VXRRH TXJTN AUDFH UZAHL'\
             'HFTWX XZFQU UDTYC XAAVA ATXFX CXAAU'\
             'CUFTW HFTTR ZHCXF FIZAT QXVZH ZACTM'\
             'VGHTZ ULTZM XWUZA XNUXW HTXJJ HDTFQ'\
             'UDYHU RXXRC XZMHN HZUUM TJUDX CXWOH'\
             'UZAXA XNXZX CCXGH TZUDY UDDTU JTNUZ'\
             'AHUCH DTZTM XAHDF HUZAH LHFHF QUMXZ'\
             'ZTVZH MUXMU NNXCR TWUZA TFVHR HCUCX'

    # Note: This is slightly higher than the general
    RANDOM_INDEX_OF_COINCIDENCE = 0.04
    # RANDOM_INDEX_OF_COINCIDENCE = 0.0385


    inp = input("Press 1 for Wax On, 2 for Wax-Off or your own string: ")
    if int(inp) == 1:
        my_string = text_1
        print(my_string)
    elif int(inp) == 2:
        my_string = text_2
        print(my_string)
    else:
        my_string = inp
    characters = make_dict(my_string)
    characters = collections.OrderedDict(sorted(characters.items()))
    make_bar_chart(characters)
    ci = compute_coincidence_index(characters)
    print("Coincidence Index of", ci)
    print("Random Index of Coincidence is", RANDOM_INDEX_OF_COINCIDENCE)
    if ci > RANDOM_INDEX_OF_COINCIDENCE:
        print("Text is most likely not random")
    else:
        print("Text is most likely random")
    plt.show()
