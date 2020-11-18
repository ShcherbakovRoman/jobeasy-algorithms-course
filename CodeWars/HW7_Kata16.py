def conjugate(verb):
    conj_verbs = []
    ar_suffixes = ['o', 'as', 'a', 'amos', 'ais', 'an']
    er_suffixes = ['o', 'es', 'e', 'emos', 'eis', 'en']
    ir_suffixes = ['o', 'es', 'e', 'imos', 'is', 'en']
    verb_end = verb[-2] + verb[-1]
    verb_beg = verb[:-2]
    if verb_end == 'ar':
        for suffix in ar_suffixes:
            conj_verbs.append(verb_beg + suffix)
    elif verb_end == 'er':
        for suffix in er_suffixes:
            conj_verbs.append(verb_beg + suffix)
    else:
        for suffix in ir_suffixes:
            conj_verbs.append(verb_beg + suffix)
    dict = {verb: conj_verbs}
    return dict


'''
Test.describe("Basic tests")
Test.assert_equals(conjugate("caminar"), {"caminar": ["camino", "caminas", "camina", "caminamos", "caminais", "caminan"]})
Test.assert_equals(conjugate("comer"), {"comer": ["como", "comes", "come", "comemos", "comeis", "comen"]})
Test.assert_equals(conjugate("vivir"), {"vivir": ["vivo", "vives", "vive", "vivimos", "vivis", "viven"]})
'''