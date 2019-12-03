def answer(s):
    alp = 'abcdefghijklmnopqrstuvwxyz'

    dct = {}
    for k, ch in enumerate(alp):
        dct[ch] = len(alp)-k-1

    res = ''
    for ch in s:
        if ch in alp:
            rev_ch = alp[dct[ch.lower()]]
            res += (rev_ch, rev_ch.upper())[ch.isupper()]
        else:
            res += ch
    return res


print answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
print answer("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
