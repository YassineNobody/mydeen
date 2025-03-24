import pytest
from mydeen import MyDeen, TypedMetaSurah


def test_mydeen_language_normalization():
    mydeen = MyDeen('fr')
    assert mydeen.language == 'fr'

    quran = mydeen.meta_surahs()
    al_fatihaa: TypedMetaSurah = quran.get("1")[0]

    assert al_fatihaa['position'] == 1
    assert 'url_quran' in al_fatihaa
    assert mydeen.language in al_fatihaa['url_quran']
