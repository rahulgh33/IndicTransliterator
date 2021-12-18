# IndicTransliterator

Transliterates Devanagari text.
Includes:
- Harvard-Kyoto (HKandIASTTransliterator.py only)
- IAST
- Vedic pitch accent (VedicTransliterator.py only)
- Sanskrit punctuation (VedicTransliterator.py only)


Uses local text files as input and outputs something like this:
- (VedicTransliterator.py)
  - **Devanagari**: ॐ अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृत्विज॑म्। होता॑रं रत्न॒धात॑मम्॥१॥ 
अ॒ग्निः पूर्वे॑भि॒रृषि॑भि॒रीड्यो॒ नूत॑नैरु॒त। स दे॒वाँ एह व॑क्षति॥२॥ 
अ॒ग्निना॑ र॒यिम॑श्नव॒त्पोष॑मे॒व दि॒वेदि॑वे। य॒शसं॑ वी॒रव॑त्तमम्॥३॥ 
  - **IAST**: Oṃ àgnimī́ḻe pùrohítaṃ yàjñasyá dèvamṛtvijám. hotā́raṃ ratnàdhātámam|1| 
àgniḥ pūrvébhìrṛṣíbhìrīḍyò nūtánairùta. sa dèvāṃ eha vákṣati|2| 
àgninā́ ràyimáśnavàtpoṣámèva dìvedíve. yàśasaṃ vī̀raváttamam|3| 

- (HKandIASTTransliterator.py)
  - **Devanagari**: गणानां त्वा गणपतिं हवामहे 
कविं कवीनामुपमश्रवस्तमम् 
ज्येष्ठराजं ब्रह्मणां ब्रह्मणस्पत 
आ नः शृण्वन्नूतिभिः सीद सादनम् 
  - **Harvard Kyoto**: gaNAnAM tvA gaNapatiM havAmahe 
kaviM kavInAmupamazravastamam 
jyeSTharAjaM brahmaNAM brahmaNaspata 
Aa naH zRNvannUtibhiH sIda sAdanam 
  - **IAST**: gaṇānāṃ tvā gaṇapatiṃ havāmahe 
kaviṃ kavīnāmupamaśravastamam 
jyeṣṭharājaṃ brahmaṇāṃ brahmaṇaspata 
āa naḥ śṛṇvannūtibhiḥ sīda sādanam 

-What is "agnimile.txt"?
  - The first 3 lines of the rigveda. Includes pitch accent and punctuation, and thus is an example of a text file that can be used with VedicTransliterator.py

- What is "nasadiya.txt"
  - The "Hymn of Creation", a famous contemplative hymn in Rigveda (10:129) about the creation of the universe. Does not include pitch accent within the text file nor punctuation, example of a file that can be used with HKandIASTTransliterator.py
  
