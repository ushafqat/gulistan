import json
import os

batch_02 = {
  "batch_info": {
    "batch_id": 2,
    "pages_pdf": [11, 20],
    "pages_book": [9, 18],
    "title_ur": "دیباچہ: سببِ تالیف و آغازِ گلستان (صفحات ۹ تا ۱۸)",
    "title_en": "Dibacha: Cause of Composition & Creation of the Gulistan (Pages 9 to 18)"
  },
  "sections": [
    {
      "section_id": "dibacha_mystical_contemplation",
      "title_ur": "دیباچہ: حیرتِ عشق و مجلسِ مراقبہ",
      "title_en": "Dibacha: Mystical Bewilderment & Silent Contemplation",
      "pdf_page": 11,
      "book_page": 9,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p11_01",
          "book_page": 9,
          "pdf_page": 11,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "گَرْ کَسِے وَصْفِ اَوْ زِ مَنْ پُرْسَدْ",
          "persian_m2": "بِیْدِلْ اَزْ بﮯ نِشَاں چَہ گُوْیَدْ بَازْ",
          "urdu_m1": "اگر کوئی اُس کی تعریف مجھ سے پوچھے",
          "urdu_m2": "تو بے دل بے پتہ کے بارے میں آخر کیا کہے",
          "english_trans": "If someone were to ask of me His description: / What, after all, can one who has lost his heart say of the Traceless One?",
          "footnotes": [
            "یعنی میں عاشقِ حیران ہوں اور وہ بے نشان، تو حیران عاشق بے نشان کا کیا پتا بتا سکتا ہے۔",
            "لفظ 'باز' یہاں پر زائد اور محض تکمیلِ وزن کے لیے معلوم ہوتا ہے۔"
          ],
          "study": {
            "notes_en": "Saadi encapsulates the classic apophatic paradox of mystical union: the lover who has dissolved his ego ('bī-dil', heartless/in ecstasy) cannot communicate the attributes of the Infinite God ('bē-nishān', signless, uncircumscribable).",
            "notes_ur": "'بیدل' سے مراد وہ عاشق ہے جس کا دل قابو میں نہ رہا ہو یا جو وارفتگی اور محویت کے عالم میں ہو۔ 'بے نشاں' خدا کی ذاتِ پاک کے لیے لایا گیا ہے جو کسی خاص مادی نشان یا مکان سے ماورا ہے۔",
            "vocabulary": [
              {
                "persian": "وَصْف",
                "grammar": "اسم (عربی)",
                "meaning_en": "attribute, description, praise",
                "meaning_ur": "صفت، تعریف و توصیف",
                "urdu_cognates": "وصف، اوصاف، موصوف"
              },
              {
                "persian": "بِیْدِل",
                "grammar": "صفتِ مرکب",
                "meaning_en": "heartless, lost in love, ecstatically bewildered",
                "meaning_ur": "بے دل، والہ و شیدا",
                "urdu_cognates": "بیدل، بیدلی"
              },
              {
                "persian": "بﮯ نِشَاں",
                "grammar": "صفتِ مرکب",
                "meaning_en": "traceless, boundless, signless",
                "meaning_ur": "بے پتہ، جس کا کوئی ظاہری نشان نہ ہو",
                "urdu_cognates": "بے نشان، نشان"
              }
            ]
          }
        },
        {
          "id": "entry_p11_02",
          "book_page": 9,
          "pdf_page": 11,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "عَاشِقَاں کُشْتَگَانِ مَعْشُوْقَنْد",
          "persian_m2": "بَرْ نَیَایَدْ زِ کُشْتَگَاں آواز",
          "urdu_m1": "عاشق، معشوق کے مارے ہوئے ہیں",
          "urdu_m2": "مُرے ہوؤں کی آواز نہیں نکلتی",
          "english_trans": "True lovers are the slain of the Beloved: / And never does a cry arise from the dead!",
          "footnotes": [],
          "study": {
            "notes_en": "One of Saadi's most famous maxims. The slain lover represents complete *fana* (annihilation of self in Divine contemplation). Speech belongs only to the living ego; once annihilated, all claims cease.",
            "notes_ur": "سعدی کا لازوال شعر ہے۔ 'کشتگاں' سے مراد وہ شہدائے محبت ہیں جو معشوق کے جلووں کے سامنے اپنی ہستی مٹا چکے ہوں۔ مردہ زبان نہیں رکھتا، اسی طرح سچے عارف پر جب تجلیاتِ الٰہی کا غلبہ ہوتا ہے تو اس کے پاس بولنے کے لیے الفاظ نہیں رہتے۔",
            "vocabulary": [
              {
                "persian": "کُشْتَگَان",
                "grammar": "اسمِ مفعول جمع",
                "meaning_en": "the slain, the dead",
                "meaning_ur": "مقتولین، مارے ہوئے لوگ",
                "urdu_cognates": "کشتہ (جیسے کشتۂ عشق)"
              },
              {
                "persian": "بَرْ نَیَایَد",
                "grammar": "فعلِ مضارع منفی",
                "meaning_en": "does not arise / come forth",
                "meaning_ur": "نہیں نکلتی، بلند نہیں ہوتی",
                "urdu_cognates": "برآمد ہونا"
              }
            ]
          }
        },
        {
          "id": "entry_p11_03",
          "book_page": 9,
          "pdf_page": 11,
          "type": "prose",
          "persian": "یَکِے اَزْ صَاحِبْ دِلَاں بِجَیْبِ مَرَاقَبَہ فُرُوْ بُرْدَہ بُوْد وَ دَرْ بَحْرِ مُکَاشَفَہ مُسْتَغْرِقْ شُدَہ ، حَالِے کِہ اَزَاں مُعَامِلَتْ بَازْ آمَدْ یَکِے اَزْ مُحِبَّاں گُفْت : اَزِیْں بُوْسْتَاں کِہ بُوْدِیْ چَہ تُحْفَہ کَرَامَتْ کَرْدِیْ اَصْحَابْ رَا ؟ گُفْت : بَخَاطِر دَاشْتَمْ کِہ چُوْں بَدِرَخْتِ گُلْ بَرَسَمْ دَامَنِے پُرْ کُنَمْ ہَدِیَۂ اَصْحَابْ رَا ، چُوْں بَرَسِیْدَمْ بُوْئے گُلْ چُنَاں مَسْتْ کَرْد کِہ دَامَنَمْ اَزْ دَسْتْ بَرَفْت ۔",
          "urdu_interlinear": "ایک صاحبِ دل مراقبہ کے گریبان میں سر ڈالے ہوئے تھا اور کشف کے سمندر میں ڈوبا ہوا ، جب اس حالت سے واپس لوٹا ایک دوست نے کہا : اس باغ سے جس میں تو تھا کیا تحفہ لایا اس نے ساتھیوں سے کہا : میرا یہ خیال تھا کہ جب پھول کے درخت کے پاس پہنچوں گا تو دوستوں کے تحفہ کے لئے دامن بھر لوں گا ، جب میں پہنچا تو پھول کی خوشبو نے مجھے ایسا مست کر دیا کہ دامن میرے ہاتھ سے چھوٹ گیا ۔",
          "english_trans": "One of the enlightened mystics had bowed his head into the collar of deep meditation and was submerged in the ocean of divine unveiling. When he returned from that state, one of his companions asked: 'From this garden in which thou hast been, what gift hast thou bestowed upon thy companions?' He answered: 'I had intended that when I reached the rosebush, I would fill my skirt with roses as a gift for my friends. But when I arrived, the scent of the roses so intoxicated me that the skirt slipped from my hands!'",
          "footnotes": [
            "مراقبہ: گردن جھکانا، یعنی دنیا و مافیہا سے غافل ہو کر دل کو یادِ خدا میں مشغول کرنا۔"
          ],
          "study": {
            "notes_en": "The famous rose-basket allegory: mystical experience is ineffable. The spiritual traveller intends to bring back tangible descriptions for his brethren, but upon encountering the immediate Presence, sensory perception and conceptual faculties are overwhelmed.",
            "notes_ur": "'جیبِ مراقبہ' یعنی مراقبے کا گریبان۔ صوفیہ جب دھیان میں بیٹھتے ہیں تو گردن سینے اور گریبان کی طرف جھکا لیتے ہیں۔ سعدی کا یہ خوبصورت تمثیلی واقعہ تصوف کی دنیا میں وجدان اور بے خودی کی سب سے بلیغ مثال مانا جاتا ہے۔",
            "vocabulary": [
              {
                "persian": "صَاحِبْ دِل",
                "grammar": "صفتِ مرکب",
                "meaning_en": "mystic, enlightened person, sage",
                "meaning_ur": "اہلِ دل، صوفی، باخدا انسان",
                "urdu_cognates": "صاحبِ دل"
              },
              {
                "persian": "جَیْب",
                "grammar": "اسم (عربی)",
                "meaning_en": "collar, pocket, breast of garment",
                "meaning_ur": "گریبان (جیسے چاکِ جیب)",
                "urdu_cognates": "جیب، گریبان"
              },
              {
                "persian": "مُکَاشَفَہ",
                "grammar": "اسم (عربی)",
                "meaning_en": "unveiling, spiritual revelation",
                "meaning_ur": "کشف و الہام، باطنی حقیقت کا کھلنا",
                "urdu_cognates": "مکاشفہ، کشف"
              },
              {
                "persian": "مُسْتَغْرِق",
                "grammar": "اسمِ فاعل (عربی)",
                "meaning_en": "submerged, deeply absorbed",
                "meaning_ur": "ڈوبا ہوا، محو",
                "urdu_cognates": "مستغرق، غرق"
              },
              {
                "persian": "دَامَنَمْ اَزْ دَسْتْ بَرَفْت",
                "grammar": "محاورہ",
                "meaning_en": "the skirt slipped from my hand (I lost control)",
                "meaning_ur": "دامن ہاتھ سے چھوٹ گیا (بے خود ہو گیا)",
                "urdu_cognates": "دامن ہاتھ سے چھوٹنا"
              }
            ]
          }
        },
        {
          "id": "entry_p11_04",
          "book_page": 9,
          "pdf_page": 11,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "اے مُرْغِ سَحَرْ عِشْقْ زِ پَرْوَانَہ بَیَامُوْز",
              "persian_m2": "کَاں سُوْخْتَہ رَا جَاں شُد وَ آواز نَیَامَدْ",
              "urdu_m1": "اے صبح کے پرند عشق پروانے سے سیکھ",
              "urdu_m2": "کہ اُس دل جلے کی جان چلی گئی اور آواز نہ نکلی"
            },
            {
              "persian_m1": "اِیْں مُدَّعِیَاں دَرْ طَلَبَشْ بﮯ خَبَرَانَنْد",
              "persian_m2": "کَاں رَا کِہ خَبَرْ شُد خَبَرَشْ بَازْ نَیَامَدْ",
              "urdu_m1": "یہ اُس کی طلب میں ڈینگیں مارنے والے بے خبر ہیں",
              "urdu_m2": "کیونکہ جس کو خبر ہو گئی پھر اُس کی خبر نہ آئی"
            }
          ],
          "english_trans": "O morning bird! Learn true love from the moth, / For that scorched creature surrendered its life without a whimper! / These pretenders are utterly ignorant in their seeking, / For he who truly receives the news never returns to tell of it!",
          "footnotes": [],
          "study": {
            "notes_en": "The nightingale ('murgh-e sahar') weeps loudly in complaint, yet survives. The moth enters the flame in silence and perishes. The ultimate gnosis is silent: 'He who knows, does not speak; he who speaks, does not know.'",
            "notes_ur": "فارسی و اردو شاعری کا ایک ضرب المثل قطعہ۔ بلبل صبح کے وقت فریاد اور نالہ کرتی ہے مگر زندہ رہتی ہے، جبکہ پروانہ شمع پر نثار ہو کر بغیر کسی آہ و فغاں کے جان دے دیتا ہے۔ سعدی فرماتے ہیں کہ دعوے کرنے والے بے خبر ہیں، کیونکہ جسے حقیقت کی خبر ہو گئی وہ خود بے خود ہو گیا۔",
            "vocabulary": [
              {
                "persian": "مُرْغِ سَحَر",
                "grammar": "مرکب اضافی",
                "meaning_en": "morning bird (the nightingale)",
                "meaning_ur": "صبح کا پرندہ (بلبل)",
                "urdu_cognates": "مرغ، سحر"
              },
              {
                "persian": "سُوْخْتَہ",
                "grammar": "اسمِ مفعول",
                "meaning_en": "burnt, consumed, ardent lover",
                "meaning_ur": "جلا ہوا، سوختہ",
                "urdu_cognates": "سوختہ، دل سوختہ"
              },
              {
                "persian": "مُدَّعِیَاں",
                "grammar": "اسمِ فاعل جمع (عربی)",
                "meaning_en": "claimants, pretenders",
                "meaning_ur": "دعوے دار، ڈینگیں مارنے والے",
                "urdu_cognates": "مدعی، مدعیان"
              }
            ]
          }
        },
        {
          "id": "entry_p11_05",
          "book_page": 9,
          "pdf_page": 11,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "اے بَرْتَر اَزْ خَیَالْ وَ قِیَاسْ وَ گُمَانْ وَ وَہْمْ",
              "persian_m2": "وَزْ ہَرْ چَہ گُفْتَہ اَنْد وَ شَنِیْدِیْم وَ خِوَانْدَہ اِیْم",
              "urdu_m1": "اے وہ ذات جو خیال، قیاس، گمان اور وہم سے بالا تر ہے",
              "urdu_m2": "اور اُس سے بھی جو لوگوں نے کہا ہے اور ہم نے سنا اور پڑھا ہے"
            },
            {
              "persian_m1": "دَفْتَرْ تَمَامْ گَشْت وَ بَپَایَاں رَسِیْد عُمْر",
              "persian_m2": "مَا ہَمْچُنَاں دَرْ اَوَّلِ وَصْفِ تَوْ مَانْدَہ اِیْم",
              "urdu_m1": "دفتر ختم ہو گیا اور عمر آخر ہوئی",
              "urdu_m2": "اور ہم اُسی طرح تیری ابتدائی تعریف میں لگے ہوئے ہیں"
            }
          ],
          "english_trans": "O Thou Who art exalted far beyond imagination, conjecture, doubt, and fancy, / And beyond all that men have spoken, or we have heard, or read! / The book has reached its end and life has drawn to its close, / Yet we remain standing at the very threshold of praising Thee!",
          "footnotes": [
            "دفتر سے مراد یہاں کتابِ حمد ہے، یعنی تعریف و توصیف کے تمام اوراق ختم ہو گئے۔"
          ],
          "study": {
            "notes_en": "This transcendent quatrain spans pages 9 and 10 of the lithograph. It gathers the four faculties of human perception (khayāl, qiyās, gumān, wahm) and sets God above all human speech, hearing, and texts. Even a whole lifetime spent in hymnody leaves one only at the first syllable of Divine praise.",
            "notes_ur": "انسان کی چاروں فکری قوتیں (خیال، قیاس، گمان اور وہم) باری تعالیٰ کی حقیقت کا ادراک نہیں کر سکتیں۔ سعدی فرماتے ہیں کہ زندگی تمام ہو گئی اور حمد و ستائش کے تمام دفتر ختم ہو گئے مگر ہم ابھی تیری صفت کے پہلے ہی درجے میں حیران کھڑے ہیں۔",
            "vocabulary": [
              {
                "persian": "بَرْتَر",
                "grammar": "صفتِ تفضیلی",
                "meaning_en": "higher, far exalted",
                "meaning_ur": "بلند تر، بالا تر",
                "urdu_cognates": "برتر، برتری"
              },
              {
                "persian": "قِیَاس",
                "grammar": "اسم (عربی)",
                "meaning_en": "analogical deduction, inference",
                "meaning_ur": "اندازہ، عقل کا قیاس",
                "urdu_cognates": "قیاس، قیاسات"
              },
              {
                "persian": "دَفْتَر",
                "grammar": "اسم",
                "meaning_en": "register, volume, scroll",
                "meaning_ur": "کتاب، رجسٹر، اوراق کا مجموعہ",
                "urdu_cognates": "دفتر"
              }
            ]
          }
        }
      ]
    },
    {
      "section_id": "madah_atabak",
      "title_ur": "ذِکْرِ مَحَامِدِ پَادْشَاہِ اِسْلَامْ اَتَابَکْ اَبُوْ بَکْرِ بْنِ سَعْدِ بْنِ زَنْگِیْؒ",
      "title_en": "In Praise of the Sovereign of Islam, Atabak Abu Bakr ibn Sa'd ibn Zangi",
      "pdf_page": 12,
      "book_page": 10,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p12_01",
          "book_page": 10,
          "pdf_page": 12,
          "type": "prose",
          "persian": "ذِکْرِ جَمِیْلِ سَعْدِیْ کِہ دَرْ اَفْوَاہِ عَوَامْ اُفْتَادَہ اَسْت ، وَ صِیْتِ سُخَنَشْ کِہ دَرْ بَسِیْطِ زَمِیْنْ رَفْتَہ ، وَ قَصَبُ الْجَیْبِ حَدِیْثَشْ کِہ ہَمْچُوْ شَکَر مِیْ خُوْرَنْد ، وَ رُقْعَۂ مُنْشَآتَشْ کِہ ہَمْچُوْ کَاغَذِ زَرْ مِیْبَرَنْد ، بَرْ کَمَالِ فَضْلْ وَ بَلَاغَتِ اَوْ حَمْلْ نَتُوَاں کَرْد ، بَلْکِہ خُدَاوَنْدِ جَہَاں ، وَ قُطْبِ دَائِرَۂ زَمَاں ، وَ قَائِمْ مَقَامِ سُلَیْمَاں ، وَ نَاصِرِ اَہْلِ اِیْمَاں ، اَتَابَکِ اَعْظَمْ ، مُظَفَّرُ الدُّنْیَا وَ الدِّیْنْ اَبُوْ بَکْرِ بْنِ سَعْدِ زَنْگِیْ ، ظِلُّ اللہِ تَعَالٰی فِیْ اَرْضِہٖ ، رَبِّ ارْضَ عَنْہُ وَ اَرْضِہٖ ، بِعَیْنِ عِنَایَتْ نَظَرْ کَرْدَہ اَسْت وَ تَحْسِیْنِ بَلِیْغْ فَرْمُوْدَہ وَ اِرَادَتِ صَادِقْ نَمُوْدَہ ، لَاجَرَمْ کَافَّۂ اَنَامْ اَزْ خَوَاصْ وَ عَوَامْ بَہ مَحَبَّتِ اَوْ گِرَائِیْدَہ اَنْد ، وَ النَّاسُ عَلٰی دِیْنِ مُلُوْکِہِمْ ۔",
          "urdu_interlinear": "سعدی کا ذکرِ خیر جو عوام کی زبانوں پر ہے اور اس کے کلام کا شہرہ جو روئے زمین پر ہے اور اُس کی بات کے گنے جس کو لوگ شکر کی طرح کھاتے ہیں اور اُس کی انشا پردازی کے کاغذ جس کو سونے کے پتر کی طرح لے جاتے ہیں اس کی بزرگی اور بلاغت کے کمال پر محمول نہیں کیا جا سکتا بلکہ جہان کے بادشاہ ، اور زمانہ کے دائرہ کے قطب ، اور حضرت سلیمانؑ کے قائم مقام اور اہلِ ایمان کے مددگار ، اتابک اعظم ، دین اور دنیا کا فتح مند ، ابوبکر بن سعد زنگی نے جو اللہ کی سرزمین میں اس کا سایہ ہے (اے خدا تو اس سے راضی ہو اور اس کو راضی کر) مہربانی کی نگاہ ڈال دی ہے اور بہت زیادہ تعریف فرمائی ہے اور سچی عقیدت ظاہر کی ہے ، لامحالہ عوام اور خواص تمام مخلوق اُس کی محبت کی طرف مائل ہو گئی ہے ۔ اور لوگ اپنے بادشاہ کے مذہب پر ہوتے ہیں ۔",
          "english_trans": "The good name of Saadi that has fallen upon the tongues of the multitude, the fame of his speech that has spread across the expanse of the earth, the sugarcane of his discourse that men devour like sugar, and the leaves of his compositions that they carry away like sheets of gold—none of this can be attributed to the perfection of his own merit and eloquence! Rather, it is because the Sovereign of the World, the Pivot of the Sphere of Time, the Successor to Solomon, Protector of the Faithful, the Greatest Atabeg, Champion of the World and the Faith, Abu Bakr ibn Sa'd ibn Zangi—Shadow of God Exalted in His earth! May my Lord be pleased with him and grant him contentment!—has looked upon him with the eye of gracious favor, bestowed lavish praise, and manifested sincere affection. Consequently, all humanity, elite and commoners alike, have inclined towards his love, for 'People follow the faith of their kings.'",
          "footnotes": [
            "قصب الجیب: قصب گنے اور بانس کو کہتے ہیں، مراد ہے گنے کی طرح میٹھا کلام۔",
            "اتابک: بضمِ باء اتالیق کو کہتے ہیں یعنی شاہی مربی و اتالیق۔",
            "خدا اُس کی قبر کو نورانی کرے اور اس سے راضی ہو۔"
          ],
          "study": {
            "notes_en": "Classical panegyric humility: Saadi attributes his immense global fame not to his own literary genius, but to the patronage and esteem of the Salghurid ruler of Fars, Atabeg Abu Bakr ibn Sa'd (reigned 1231–1260 CE), under whose peaceful rule Shiraz flourished while the rest of the Islamic world was ravaged by the Mongol invasion.",
            "notes_ur": "سعدی کی کسرِ نفسی دیکھیے کہ اپنی عالمی شہرت اور قبولِ عام کو اپنی بلاغت کا کمال قرار دینے کے بجائے اتابک ابوبکر بن سعد زنگی کی قدردانی کا نتیجہ قرار دیتے ہیں۔ 'کاغذِ زر' سے مراد وہ کاغذ ہے جس پر سونے کا پانی چڑھایا جاتا تھا یا جو انتہائی قیمتی ہو۔ عربی مقولہ 'الناس علی دین ملوکہم' (لوگ اپنے بادشاہوں کے طور طریقوں پر چلتے ہیں) کو بر محل نقل کیا ہے۔",
            "vocabulary": [
              {
                "persian": "صِیْت",
                "grammar": "اسم (عربی)",
                "meaning_en": "fame, renown, good reputation",
                "meaning_ur": "شہرہ، نیک نامی، شہرت",
                "urdu_cognates": "صیت (کتبِ لغت)"
              },
              {
                "persian": "بَسِیْطِ زَمِیْن",
                "grammar": "مرکب اضافی",
                "meaning_en": "the vast expanse of the earth",
                "meaning_ur": "زمین کا وسیع تختہ، روئے زمین",
                "urdu_cognates": "بسیط، وسعت"
              },
              {
                "persian": "قَصَبُ الْجَیْب",
                "grammar": "مرکب اضافی",
                "meaning_en": "sweet reed, sugarcane",
                "meaning_ur": "شیریں گنا، مصری",
                "urdu_cognates": "قصب، قصبہ"
              },
              {
                "persian": "مُنْشَآت",
                "grammar": "اسمِ مفعول جمع (عربی)",
                "meaning_en": "epistles, literary essays, compositions",
                "meaning_ur": "تحریریں، مضامین، انشا پردازی",
                "urdu_cognates": "منشآت، انشا"
              }
            ]
          }
        },
        {
          "id": "entry_p13_01",
          "book_page": 11,
          "pdf_page": 13,
          "type": "stanza",
          "header_persian": "رُبَاعِیْ",
          "header_urdu": "رباعی",
          "lines": [
            {
              "persian_m1": "زَاں گِہ کِہ تُرَا بَر مَنِ مِسْکِیْنْ نَظَرَسْت",
              "persian_m2": "آثَارَمْ اَزْ آفْتَابْ مَشْہُوْر تَرَسْت",
              "urdu_m1": "جب سے تیری مجھ مسکین پر نظر ہے",
              "urdu_m2": "میرے نشانات آفتاب سے زیادہ مشہور ہیں"
            },
            {
              "persian_m1": "گَرْ خُوْدْ ہَمَہ عَیْبْ بَا بَدِیْں بَنْدَہ دُرُسْت",
              "persian_m2": "ہَرْ عَیْبْ کِہ سُلْطَاں بَہ پَسَنْدَدْ ہُنَرَسْت",
              "urdu_m1": "اگر سب عیب ہی عیب اس خادم میں ہیں",
              "urdu_m2": "جو عیب کہ بادشاہ پسند کرے وہ ہنر ہے"
            }
          ],
          "english_trans": "Since Thy glance of favor fell upon humble me, / My literary works have shone more famed than the sun itself! / Even if this servant be compounded wholly of defects, / Whatever defect the Sultan approves is esteemed an art!",
          "footnotes": [],
          "study": {
            "notes_en": "Royal favor transforms base metal into gold: Saadi plays on the courtly convention that whatever the beloved or the king approves, even if flawed in common eyes, becomes the standard of excellence.",
            "notes_ur": "شاہی سرپرستی کی مدح میں رباعی: 'آثارم از آفتاب مشہور ترست' (میرے آثار سورج سے زیادہ روشن ہیں)۔ دوسرا مصرعہ فارسی کا ضرب المثل شعر ہے کہ جس بات کو حاکمِ وقت یا معشوق پسند کر لے وہ خامی ہونے کے باوجود ہنر سمجھی جاتی ہے۔",
            "vocabulary": [
              {
                "persian": "آثَار",
                "grammar": "اسم جمع (عربی)",
                "meaning_en": "works, footprints, writings",
                "meaning_ur": "نشانات، تصانیف، کتب",
                "urdu_cognates": "آثار، اثر"
              },
              {
                "persian": "ہُنَر",
                "grammar": "اسم",
                "meaning_en": "virtue, skill, artistic excellence",
                "meaning_ur": "کمال، خوبی، فن",
                "urdu_cognates": "ہنر، باہنر، ہنرمند"
              }
            ]
          }
        },
        {
          "id": "entry_p13_02",
          "book_page": 11,
          "pdf_page": 13,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "گِلے خُوْشْبُوْئے دَرْ حَمَّامْ رُوْزے",
              "persian_m2": "رَسِیْد اَزْ دَسْتِ مَحْبُوْبے بَدَسْتَمْ",
              "urdu_m1": "ایک دن حمام میں ایک خوشبودار مٹی",
              "urdu_m2": "میرے ہاتھ میں ایک محبوب کے ہاتھ سے آئی"
            },
            {
              "persian_m1": "بَدُوْ گُفْتَمْ کِہ مُشْکِیْ یَا عَبِیْرِیْ",
              "persian_m2": "کِہ اَزْ بُوْئے دِلْ آوِیْزِ تَوْ مَسْتَمْ",
              "urdu_m1": "میں نے اُس سے کہا کہ تو مشک ہے یا عبیر ہے",
              "urdu_m2": "کیونکہ میں تیری دل کش خوشبو سے مست ہوں"
            },
            {
              "persian_m1": "بِگُفْتَا مَنْ گِلے نَاچِیْز بُوْدَمْ",
              "persian_m2": "وَ لِیْکِنْ مُدَّتِے بَا گُلْ نِشَسْتَمْ",
              "urdu_m1": "اُس نے کہا میں ایک ناچیز مٹی تھی",
              "urdu_m2": "لیکن ایک زمانے تک میں پھول کے ساتھ رہی"
            },
            {
              "persian_m1": "جَمَالِ ہَمْنِشِیْں دَرْ مَنْ اَثَرْ کَرْد",
              "persian_m2": "وَگَرْ نَہ مَنْ ہَمَاں خَاکَمْ کِہ ہَسْتَمْ",
              "urdu_m1": "ساتھی کے حسن نے مجھ میں اثر کیا",
              "urdu_m2": "ورنہ میں تو وہی مٹی کی مٹی ہوں"
            }
          ],
          "english_trans": "One day in the bathhouse, a piece of scented clay / Reached my hand from the hand of a beloved. / I said to it: 'Art thou musk or ambergris? / For I am intoxicated by thy heart-ravishing fragrance!' / It replied: 'I was but a worthless piece of clay, / But for a season I sat in company with the rose! / The beauty of my companion worked its influence within me, / Else am I still that very humble dust that I ever was!'",
          "footnotes": [
            "اس حکایت کے بیان سے مصنف کا مقصد یہ ہے کہ صحبت کا اثر ہوتا ہے اور اچھی بری صحبت سے اچھے اور برے نتیجے پیدا ہوتے ہیں",
            "عبیر ایک مرکب خوشبو کا نام ہے جو صندل گلاب مشک اور زعفران وغیرہ سے تیار ہوتی ہے۔"
          ],
          "study": {
            "notes_en": "One of the most celebrated allegories in world literature on the power of company (*suhbat*). In traditional Persian baths, fragrant Fuller's earth (*gil-e sarshūy*) scented with rose petals was used to cleanse the hair and body. Saadi uses it as an allegory of moral transformation through proximity to the righteous.",
            "notes_ur": "فارسی ادب کا یہ لازوال شاہکار قطعہ حسنِ صحبت کی تاثیر کا بے مثل ترجمان ہے۔ قدیم زمانے میں حماموں میں سر دھونے کے لیے خاص خوشبودار مٹی استعمال ہوتی تھی جو پھولوں کے ساتھ رکھی جاتی تھی۔ مٹی کا اعتراف کہ 'جمالِ ہمنشیں در من اثر کرد' اخلاقیات اور تربیت کی بنیادی حقیقت کو ظاہر کرتا ہے۔",
            "vocabulary": [
              {
                "persian": "گِل",
                "grammar": "اسم",
                "meaning_en": "clay, mud, earth",
                "meaning_ur": "مٹی، گِل",
                "urdu_cognates": "گل، گلِ سرشوی"
              },
              {
                "persian": "عَبِیْر",
                "grammar": "اسم (عربی)",
                "meaning_en": "ambergris, aromatic compound perfume",
                "meaning_ur": "ایک مرکب خوشبو (صندل، زعفران، مشک)",
                "urdu_cognates": "عبیر (جیسے عبیر و عنبر)"
              },
              {
                "persian": "دِلْ آوِیْز",
                "grammar": "صفتِ فاعلی مرکب",
                "meaning_en": "heart-captivating, enchanting",
                "meaning_ur": "دلکش، دل کو کھینچنے والا",
                "urdu_cognates": "دلاویز، دلاویزی"
              },
              {
                "persian": "ہَمْنِشِیْں",
                "grammar": "صفتِ مرکب / اسم",
                "meaning_en": "companion, associate",
                "meaning_ur": "ساتھی، پاس بیٹھنے والا",
                "urdu_cognates": "ہمنشیں، ہمنشینی"
              }
            ]
          }
        },
        {
          "id": "entry_p13_03",
          "book_page": 11,
          "pdf_page": 13,
          "type": "quran",
          "arabic": "اَللّٰھُمَّ مَتِّعِ الْمُسْلِمِیْنَ بِطُوْلِ حَیَاتِہٖ ، وَ ضَاعِفْ ثَوَابَ جَمِیْلِہٖ وَ حَسَنَاتِہٖ ، وَ ارْفَعْ دَرَجَ اَوْدَائِہٖ وَ وُلَاتِہٖ ، وَ دَمِّرْ عَلٰی اَعْدَائِہٖ وَ شَنَاتِہٖ ، بِمَا تُتْلٰی فِی الْقُرْآنِ مِنْ آیَاتِہٖ ، وَ آمِنْ بَلْدَہٗ یَا رَبِّ وَ احْفَظْ وَلَدَہٗ ۔",
          "urdu_interlinear": "اے اللہ اس کی زندگی کی درازی سے مسلمانوں کو نفع بخش اور اس کے اچھے کاموں کا ثواب دو گنا عنایت فرما اور اس کے دوستوں اور یاروں کے مراتب بلند کر اور اس کے دشمنوں اور بدخواہوں کو ہلاک کر قرآن کی ان آیتوں کی برکت سے جن کی تلاوت کی گئی ہو اور اس کے ملک کو پُر امن رکھ اور اس کے لڑکے کی حفاظت فرما ۔",
          "english_trans": "O Allah! Benefit the Muslims through the length of his days; multiply the recompense of his noble deeds and virtues; elevate the stations of his beloved friends and governors; destroy his enemies and detractors through the efficacy of what is recited from the verses of the Quran; keep his realm secure, O Lord, and protect his progeny!",
          "footnotes": [],
          "study": {
            "notes_en": "A formal Arabic liturgical benediction (*du'ā-ye dawlat*) invoking divine protection upon Shiraz and the royal lineage.",
            "notes_ur": "عربی دعا میں مسجع و مقفٰی عبارت کے ساتھ اتابک ابوبکر اور اس کے ولی عہد شہزادہ سعد کے لیے دعائے خیر اور شیراز کے امن کی التجا کی گئی ہے۔",
            "vocabulary": []
          }
        },
        {
          "id": "entry_p14_01",
          "book_page": 12,
          "pdf_page": 14,
          "type": "stanza",
          "header_persian": "شعر (عربی)",
          "header_urdu": "اشعارِ عربی",
          "lines": [
            {
              "persian_m1": "لَقَدْ سَعِدَ الدُّنْیَا بِہٖ دَامَ سَعْدُہٗ",
              "persian_m2": "وَ اَیَّدَہُ الْمَوْلٰی بِاَلْوِیَةِ النَّصْرِ",
              "urdu_m1": "اس کی ذات سے دنیا نیک بخت ہوئی اس کی سعادت ہمیشہ رہے",
              "urdu_m2": "اور مولیٰ مدد کے جھنڈوں سے اس کی تائید فرمائے"
            },
            {
              "persian_m1": "کَذٰلِکَ تَنْشَأُ لِیْنَةٌ ھُوَ عِرْقُھَا",
              "persian_m2": "وَ حُسْنُ نَبَاتِ الْاَرْضِ مِنْ کَرَمِ الْبَذْرِ",
              "urdu_m1": "اسی طرح نشوو نما پاتی ہیں وہ شاخیں جن کی وہ جڑ ہے",
              "urdu_m2": "اور زمین کی پیداوار کی خوبی بیج کی اچھائی کی وجہ سے ہے"
            }
          ],
          "english_trans": "Truly the world has attained felicity through him—may his auspicious fortune endure! / And may the Sovereign Lord aid him with the banners of victory! / Thus grows the noble palm-branch when he is its nourishing root, / And the excellence of the earth's harvest springs from the nobility of the seed!",
          "footnotes": [],
          "study": {
            "notes_en": "Arabic verses celebrating the dynastic continuity of the Salghurids: the virtue of the offspring ('līnah' - young palm tree) derives from the excellence of the ancestral root.",
            "notes_ur": "عربی کے دو بلیغ اشعار جن میں تمثیلی انداز میں بیان کیا گیا ہے کہ درخت کا پھلنا پھولنا اس کی عمدہ جڑ اور اچھے بیج کا مرہونِ منت ہے۔",
            "vocabulary": []
          }
        },
        {
          "id": "entry_p14_02",
          "book_page": 12,
          "pdf_page": 14,
          "type": "prose",
          "persian": "اِیْزَدِ تَعَالٰی وَ تَقَدَّسَ خِطَّۂ پَاکِ شِیْرَازْ رَا بَہ ہَیْبَتِ حَاکِمَانِ عَادِلْ وَ بَہ ہِمَّتِ عَالِمَانِ عَامِلْ تَا زَمَانِ قِیَامَتْ دَر اَمَانِ سَلَامَتْ نِگَہْدَارَدْ ۔",
          "urdu_interlinear": "خدائے بلند اور پاک شیراز کے پاک علاقہ کو منصف حاکموں کی ہیبت اور عمل کرنے والے عالموں کی توجہ سے قیامت تک سلامتی کے امن میں رکھے ۔",
          "english_trans": "May God—Exalted and Hallowed be He!—preserve the pure territory of Shiraz in the sanctuary of peace until the Day of Resurrection, through the awe of just rulers and the lofty resolve of practicing scholars!",
          "footnotes": [
            "خطہ: وہ علاقہ یا خطہ زمین جو کسی شہر اور اس کے گرد و نواح پر مشتمل ہو۔"
          ],
          "study": {
            "notes_en": "Saadi's famous prayer for his beloved home city of Shiraz. The dual pillars of civic peace are declared to be: the awe (*haybat*) of just rulers, and the spiritual aspiration (*himmat*) of practicing scholars.",
            "notes_ur": "شیراز کے لیے شیخ سعدی کی قلبی دعا: عدلِ حکام اور عملِ علماء۔ یہ دو بنیادی ستون ہیں جن پر کسی بھی اسلامی معاشرے کا امن و سکون قائم رہتا ہے۔",
            "vocabulary": [
              {
                "persian": "خِطَّہ",
                "grammar": "اسم (عربی)",
                "meaning_en": "territory, region, district",
                "meaning_ur": "علاقہ، سرزمین",
                "urdu_cognates": "خطہ (جیسے خطۂ ارض)"
              },
              {
                "persian": "ہَیْبَت",
                "grammar": "اسم (عربی)",
                "meaning_en": "awe, majestic authority",
                "meaning_ur": "دبدبہ، رعب، جلال",
                "urdu_cognates": "ہیبت، ہیبت ناک"
              }
            ]
          }
        },
        {
          "id": "entry_p14_03",
          "book_page": 12,
          "pdf_page": 14,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "اِقْلِیْمِ پَارْسْ رَا غَمْ اَزْ آسِیْبِ دَہْر نِیْسْت",
              "persian_m2": "تَا بَر سَرِشْ بُوَدْ چُوْ تُوْئے سَایَۂ خُدَا",
              "urdu_m1": "پارس کے علاقہ کو زمانہ کے حوادث کا غم نہیں ہے",
              "urdu_m2": "جب تک اس کے سر پر اے سایۂ خدا تجھ جیسا موجود ہے"
            },
            {
              "persian_m1": "اِمْرُوْز کَسْ نِشَاں نَدَہَدْ دَرْ بَسِیْطِ خَاکْ",
              "persian_m2": "مَانَنْدِ آسْتَانِ دَرَتْ مَامَنِ رِضَا",
              "urdu_m1": "آج کوئی شخص بھی روئے زمین پر کسی ایسی جگہ کا پتہ نہیں بتاتا",
              "urdu_m2": "جو تیرے در کی چوکھٹ کی طرح خوشنودی کا ٹھکانہ ہو"
            },
            {
              "persian_m1": "بَر تُسْتْ پَاسِ خَاطِرِ بَیْچَارَگَانْ وَ شُکْر",
              "persian_m2": "بَر مَا وَ بَر خُدَائے جَہَاں آفَرِیْں جَزَا",
              "urdu_m1": "تجھ پر غریبوں کے دل کی پاسداری اور ہم پر شکر ادا کرنا ہے",
              "urdu_m2": "اور اللہ پر اُس کا بدلہ ہے"
            },
            {
              "persian_m1": "یَا رَبْ زِ بَادِ فِتْنَہ نِگَہْدَار خَاکِ پَارْس",
              "persian_m2": "چَنْدَانْکِہ خَاکْ رَا بُوَدْ وَ بَادْ رَا بَقَا",
              "urdu_m1": "اے خدا فارس کی سر زمین کو فتنہ کی ہوا سے اُس وقت",
              "urdu_m2": "تک بچا تا جب تک مٹی اور ہوا کو بقا ہے"
            }
          ],
          "english_trans": "The realm of Fars has no dread of the afflictions of time, / So long as upon its head stands the Shadow of God like unto thee! / Today no man on the broad expanse of dust can point / To a sanctuary of contentment like the threshold of thy door! / Upon thee lies the care of the hearts of the helpless; upon us, gratitude; / And upon the World-Creator God, the reward! / O Lord! Preserve the soil of Fars from the gale of turmoil, / So long as soil has endurance and wind has breath!",
          "footnotes": [],
          "study": {
            "notes_en": "Historical context: While the Mongols devastated Nishapur, Baghdad, and Central Asia, the province of Fars remained an oasis of arts, letters, and security due to the diplomatic prudence of Atabeg Abu Bakr.",
            "notes_ur": "تاتاریوں کے قتلِ عام کے پر آشوب دور میں خطۂ فارس امن کا گہوارہ بنا رہا۔ سعدی کا یہ پرخلوص قطعہ امن کی قدردانی کا اعتراف ہے کہ جب تک زمین اور ہوا باقی ہے خدا فارس کو فتنوں سے محفوظ رکھے۔",
            "vocabulary": [
              {
                "persian": "آسِیْبِ دَہْر",
                "grammar": "مرکب اضافی",
                "meaning_en": "afflictions / misfortunes of time",
                "meaning_ur": "زمانہ کے حوادث و مصائب",
                "urdu_cognates": "آسیب، دہر"
              },
              {
                "persian": "مَامَن",
                "grammar": "اسمِ ظرف (عربی)",
                "meaning_en": "place of safety, sanctuary",
                "meaning_ur": "امن کی جگہ، پناہ گاہ",
                "urdu_cognates": "مأمن، امن"
              }
            ]
          }
        }
      ]
    },
    {
      "section_id": "sabab_talif_kitab",
      "title_ur": "دَرْ سَبَبِ تَالِیْفِ کِتَابْ (کتاب کی تصنیف کا سبب)",
      "title_en": "On the Cause of Composing the Book",
      "pdf_page": 14,
      "book_page": 12,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p14_04",
          "book_page": 12,
          "pdf_page": 14,
          "type": "prose",
          "persian": "یَکْ شَبْ تَاَمُّلِ اَیَّامِ گُذَشْتَہ مِیْ کَرْدَمْ ، وَ بَرْ عُمْرِ تَلَفْ کَرْدَہ تَاَسُّفْ مِیْ خُوْرْدَمْ ، وَ سَنْگْلَاخِ دِلْ رَا بَاَلْمَاسِ آبِ دِیْدَہ مِیْ سُفْتَمْ ، وَ اِیْں بَیْتْہَا مُنَاسِبِ حَالِ خُوْد مِیْ گُفْتَمْ :",
          "urdu_interlinear": "ایک رات میں گزرے ہوئے دنوں کے بارے میں سوچ رہا تھا اور برباد کی ہوئی زندگی پر افسوس کر رہا تھا اور دل کے پتھر کو آنسوؤں کے ہیرے سے چھید رہا تھا اور اپنے مناسبِ حال یہ شعر پڑھ رہا تھا :",
          "english_trans": "One night I was reflecting upon the days that had gone by, grieving over a lifetime squandered, and piercing the stony bedrock of my heart with the diamond of tears, repeating these verses suited to my condition:",
          "footnotes": [],
          "study": {
            "notes_en": "A dramatic turning point: Saadi depicts the dark night of the soul. Notice the gem-cutting metaphor: 'سنگلاخِ دل' (the stony quarry of the heart) pierced by 'الماسِ آبِ دیدہ' (the diamond of tears, tears as hard and piercing as diamond drill-bits).",
            "notes_ur": "سعدی کی نثری نقاشی دیکھیے: 'سنگلاخِ دل را بالماسِ آبِ دیدہ می سفتم' (دل کے پتھر کو آنسوؤں کے ہیرے سے چھید رہا تھا)۔ سفتن کے معنی موتی وغیرہ پرونا یا سوراخ کرنا۔ یہ خود احتسابی دیباچے کا سب سے موثر حصہ ہے۔",
            "vocabulary": [
              {
                "persian": "سَنْگْلَاخ",
                "grammar": "اسمِ ظرف / صفت",
                "meaning_en": "stony ground, rocky terrain",
                "meaning_ur": "پتھریلی زمین، سنگلاخ",
                "urdu_cognates": "سنگلاخ (جیسے سنگلاخ زمین)"
              },
              {
                "persian": "سُفْتَمْ",
                "grammar": "فعلِ ماضی (از سفتن)",
                "meaning_en": "I pierced / bored / drilled",
                "meaning_ur": "میں نے چھیدا، پرویا",
                "urdu_cognates": "سفتہ (جیسے درِّ ناسفتہ)"
              }
            ]
          }
        },
        {
          "id": "entry_p15_01",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "مَثْنَوِیْ",
          "header_urdu": "مثنوی",
          "persian_m1": "ہَرْ دَمْ اَزْ عُمْر مِیْ رَوَدْ نَفَسِے",
          "persian_m2": "چُوْں نِگَہ مِیْ کُنَمْ نَمَانْد بَسِے",
          "urdu_m1": "ہر آن زندگی کا ایک سانس جا رہا ہے",
          "urdu_m2": "جب میں غور کرتا ہوں تو اب زیادہ باقی نہیں ہے",
          "english_trans": "With every moment a breath of life departs; / When I look closely, not much remains!",
          "footnotes": [],
          "study": {
            "notes_en": "The ticking clock of human existence. 'Dam' and 'nafas' mirror each other in rhythm and urgency.",
            "notes_ur": "زندگی ہر گھڑی ایک سانس کی صورت میں رخصت ہو رہی ہے، اور جب انسان غور کرتا ہے تو پاتا ہے کہ عمر کی پونجی بہت کم رہ گئی ہے۔",
            "vocabulary": [
              {
                "persian": "نَمَانْد بَسِے",
                "grammar": "جملہ فعلی",
                "meaning_en": "not much remains",
                "meaning_ur": "زیادہ باقی نہیں رہا",
                "urdu_cognates": "بسیار، بس"
              }
            ]
          }
        },
        {
          "id": "entry_p15_02",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "اے کِہ پَنْجَاہْ رَفْت وَ دَرْ خِوَابِیْ",
          "persian_m2": "مَگَرْ اِیْں پَنْجْرُوْز دَرْ یَابِیْ",
          "urdu_m1": "اے وہ شخص کہ پچاس سال گزر گئے اور تو خواب میں ہے",
          "urdu_m2": "شاید ان پانچ روز سے فائدہ اٹھا لے",
          "english_trans": "O thou whose fifty years are gone while thou art yet asleep! / Perchance thou mayest seize these remaining five days!",
          "footnotes": [
            "دریافتن: حاصل کرنا، یعنی بقیہ مختصر مہلت سے فائدہ اٹھانا۔"
          ],
          "study": {
            "notes_en": "Saadi's famous autobiographical benchmark: he was around 50 years of age when composing the *Gulistan* (c. 1258 CE / 656 AH). The contrast between 'panjāh' (50) and 'panj-rōz' (5 fleeting days) emphasizes urgency.",
            "notes_ur": "اس شعر سے معلوم ہوتا ہے کہ گلستان کی تصنیف کے وقت سعدی کی عمر پچاس سال کے لگ بھگ تھی۔ پچاس سال کے خوابِ غفلت کے مقابلے میں عمر کے آخری چند دنوں کو غنیمت سمجھنے کی نصیحت ہے۔",
            "vocabulary": [
              {
                "persian": "پَنْجْرُوْز",
                "grammar": "اسمِ مرکب",
                "meaning_en": "five days (metaphor for transient life)",
                "meaning_ur": "پانچ دن، مختصر مہلتِ حیات",
                "urdu_cognates": "پانچ روزہ زندگی"
              }
            ]
          }
        },
        {
          "id": "entry_p15_03",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "خَجِلْ آں کَسْ کِہ رَفْت وَ کَارْ نَسَاخْت",
          "persian_m2": "کُوْسِ رِحْلَتْ زَدَنْد وَ بَارْ نَسَاخْت",
          "urdu_m1": "وہ بہت شرمندہ ہے جو چل دیا اور کوئی کام نہ بنایا",
          "urdu_m2": "لوگوں نے کوچ کا نقارہ بجا دیا اور اس نے سامان نہ باندھا",
          "english_trans": "Shame on him who departed without completing his work! / The drum of departure sounded, and he had not packed his load!",
          "footnotes": [
            "بار نساخت: یعنی زادِ راہ اور سامانِ سفر درست نہ کیا۔"
          ],
          "study": {
            "notes_en": "'Kōs-e rihlat': the heavy kettle-drum sounded by caravans at dawn to signal imminent departure. The traveler who sleeps through it is left behind in the desert.",
            "notes_ur": "'کوسِ رحلت' یعنی کوچ کا بڑا نقارہ۔ قافلے کی روانگی سے پہلے جب نقارہ بجتا تھا تو سب مسافر اپنا سامان اونٹوں پر باندھ لیتے تھے۔ جو غفلت میں سوتا رہا وہ بغیر زادِ راہ کے منزل سے محروم رہ گیا۔",
            "vocabulary": [
              {
                "persian": "خَجِل",
                "grammar": "صفت (عربی)",
                "meaning_en": "ashamed, mortified",
                "meaning_ur": "شرمندہ، پشیمان",
                "urdu_cognates": "خجل، خجالت"
              },
              {
                "persian": "کُوْسِ رِحْلَت",
                "grammar": "مرکب اضافی",
                "meaning_en": "drum of departure",
                "meaning_ur": "کوچ کا نقارہ",
                "urdu_cognates": "کوس، رحلت"
              }
            ]
          }
        },
        {
          "id": "entry_p15_04",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "خِوَابِ نُوْشِیْں بَامْدَادِ رَحِیْل",
          "persian_m2": "بَازْ دَارَدْ پَیَادَہ رَا زِ سَبِیْل",
          "urdu_m1": "کوچ کی صبح کو میٹھی نیند",
          "urdu_m2": "مسافر کو راستہ چلنے سے باز رکھتی ہے",
          "english_trans": "Sweet slumber on the morning of departure / Holds back the foot-traveler from the highway!",
          "footnotes": [],
          "study": {
            "notes_en": "Procrastination and sweet sleep in youth paralyze the spiritual traveller until the highway is empty and the sun sets.",
            "notes_ur": "'خوابِ نوشیں' یعنی میٹھی اور پر لطف نیند۔ سفر کی صبح کی غفلت انسان کو راستے سے محروم کر دیتی ہے۔",
            "vocabulary": [
              {
                "persian": "نُوْشِیْں",
                "grammar": "صفت",
                "meaning_en": "sweet, nectar-like",
                "meaning_ur": "شیریں، میٹھا",
                "urdu_cognates": "نوشیں، نوش"
              },
              {
                "persian": "سَبِیْل",
                "grammar": "اسم (عربی)",
                "meaning_en": "way, path, road",
                "meaning_ur": "راستہ، شاہراہ",
                "urdu_cognates": "سبیل، فی سبیل اللہ"
              }
            ]
          }
        },
        {
          "id": "entry_p15_05",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "ہَرْ کِہ آمَدْ عِمَارَتِے نَوْ سَاخْت",
          "persian_m2": "رَفْت وَ مَنْزِلْ بَدِیْگَرَے پَرْدَاخْت",
          "urdu_m1": "جو آیا اُس نے ایک نئی عمارت بنائی",
          "urdu_m2": "وہ چلا گیا اور عمارت دوسرے کیلئے خالی کر گیا",
          "english_trans": "Everyone who arrived built a new edifice, / Then departed, vacating the mansion for another!",
          "footnotes": [],
          "study": {
            "notes_en": "The illusion of earthly permanence: worldly builders labor over palaces only to hand the keys to another.",
            "notes_ur": "دنیا کی ناپائیداری کا ایسا نقشہ جو ہر دور کے لیے سچا ہے: انسان محل تعمیر کرتا ہے مگر رہ نہیں پاتا اور دوسرے کے لیے خالی کر جاتا ہے۔",
            "vocabulary": [
              {
                "persian": "پَرْدَاخْت",
                "grammar": "فعلِ ماضی (از پرداختن)",
                "meaning_en": "vacated, cleared out, attended to",
                "meaning_ur": "خالی کر دیا، چھوڑ گیا",
                "urdu_cognates": "پرداخت"
              }
            ]
          }
        },
        {
          "id": "entry_p15_06",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "وَاں دِگَرْ پُخْت ہَمْچُنِیْں ہَوَسِے",
          "persian_m2": "وِیْں عِمَارَتْ بَسَرْ نَبُرْد کَسِے",
          "urdu_m1": "اُس دوسرے نے بھی ایسی ہی ہوس پکائی",
          "urdu_m2": "اور اس عمارت کو کوئی پورا نہ کر سکا",
          "english_trans": "And that other nurtured the very same craving, / Yet this edifice no mortal has ever completed!",
          "footnotes": [],
          "study": {
            "notes_en": "'پختن ہوس': to cook/nurture a passion or ambition. Worldly ambition is an infinite house that no mortal ever finishes building before death intervenes.",
            "notes_ur": "'ہوس پختن' فارسی کا محاورہ ہے یعنی دل میں آرزو اور حرص کو پالنا۔ یہ دنیا ایسا ادھورا محل ہے جسے کوئی مکمل نہیں کر سکا۔",
            "vocabulary": [
              {
                "persian": "بَسَرْ نَبُرْد",
                "grammar": "فعلِ مرکب منفی",
                "meaning_en": "did not finish / bring to completion",
                "meaning_ur": "پورا نہ کر سکا، تکمیل تک نہ پہنچا سکا",
                "urdu_cognates": "بسر لے جانا"
              }
            ]
          }
        },
        {
          "id": "entry_p15_07",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "یَارِ نَاپَائِدَار دُوْسْتْ مَدَار",
          "persian_m2": "دُوْسْتِیْ رَا نَشَایَدْ اِیْں غَدَّار",
          "urdu_m1": "غیر مستقل یار سے دوستی نہ کر",
          "urdu_m2": "یہ غدار دوستی کے لائق نہیں ہے",
          "english_trans": "Take not an unfaithful friend for thy confidant; / This treacherous world is not worthy of thy friendship!",
          "footnotes": [],
          "study": {
            "notes_en": "'Yār-e nā-pāydār': personification of the fickle, treacherous world (*dunyā*).",
            "notes_ur": "دنیا کو بے وفا اور غدار دوست سے تشبیہ دی گئی ہے جو عین ضرورت کے وقت ساتھ چھوڑ دیتا ہے۔",
            "vocabulary": [
              {
                "persian": "نَاپَائِدَار",
                "grammar": "صفتِ مرکب",
                "meaning_en": "transient, unstable, inconstant",
                "meaning_ur": "بے ثبات، غیر مستقل",
                "urdu_cognates": "ناپائیدار، پائیداری"
              },
              {
                "persian": "غَدَّار",
                "grammar": "صفتِ مبالغہ (عربی)",
                "meaning_en": "treacherous, traitorous",
                "meaning_ur": "دغا باز، بے وفا",
                "urdu_cognates": "غدار، غداری"
              }
            ]
          }
        },
        {
          "id": "entry_p15_08",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "مَادَّۂ عَیْشِ آدَمِیْ شِکَمْ اَسْت",
          "persian_m2": "تَا بِتَدْرِیْج مِیْ رَوَدْ چَہ غَمْ اَسْت",
          "urdu_m1": "آدمی کی زندگی کا سرمایہ پیٹ ہے",
          "urdu_m2": "جب تک اس کی رفتار درمیانہ ہو کیا فکر ہے",
          "english_trans": "The foundation of man's bodily livelihood is the belly; / So long as it functions moderately, what anxiety is there?",
          "footnotes": [],
          "study": {
            "notes_en": "Somatic physiology in medieval medicine: the gut's digestive rhythm governs human health.",
            "notes_ur": "قدیم طب کے مطابق انسان کی صحت کا دارو مدار معدے کے اعتدال پر ہے۔",
            "vocabulary": [
              {
                "persian": "شِکَم",
                "grammar": "اسم",
                "meaning_en": "belly, stomach",
                "meaning_ur": "پیٹ، شکم",
                "urdu_cognates": "شکم، شکم پرور"
              }
            ]
          }
        },
        {
          "id": "entry_p15_09",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "گَرْ بَہ بَنْدَدْ چُنَاں کِہ نَگْشَایَدْ",
          "persian_m2": "گَرْ دِلْ اَزْ عُمْر بَر کَنَدْ شَایَدْ",
          "urdu_m1": "اگر اس میں ایسا بند پڑ جائے جو نہ کھلے",
          "urdu_m2": "تو زندگی سے اگر دل ہٹا لے تو مناسب ہے",
          "english_trans": "If it should become bound so that it opens not, / It were fitting if the heart severed its ties with life;",
          "footnotes": [],
          "study": {
            "notes_en": "Referencing severe intestinal obstruction (constipation/colic) in classical medicine.",
            "notes_ur": "پیٹ کے بند پڑ جانے کی تکلیف کا بیان کہ انسان جینے سے مایوس ہو جائے۔",
            "vocabulary": []
          }
        },
        {
          "id": "entry_p15_10",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "وَرْ کُشَایَدْ چُنَاں کِہ نَتْوَاں بَسْت",
          "persian_m2": "گُوْ بِشُوْ اَزْ حَیَاتِ دُنْیَا دَسْت",
          "urdu_m1": "اور اگر ایسا کھل پڑے جو روکا نہ جا سکے",
          "urdu_m2": "تو کہہ دو کہ دنیا کی زندگی سے ہاتھ دھو لے",
          "english_trans": "And if it should open so that it cannot be stanched, / Say to him: 'Wash thy hands of this earthly life!'",
          "footnotes": [],
          "study": {
            "notes_en": "'دست شستن': to wash one's hands of something, give up all hope. The human constitution is fragile.",
            "notes_ur": "'دست شستن' فارسی اور اردو دونوں میں مایوس ہونے اور دستبردار ہونے کے لیے آتا ہے۔",
            "vocabulary": []
          }
        },
        {
          "id": "entry_p15_11",
          "book_page": 13,
          "pdf_page": 15,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "چَار طَبْعِ مُخَالِفْ وَ سَرْکَشْ",
          "persian_m2": "چَنْدْ رُوْزے بَوَنْد بَاہَمْ خُوْشْ",
          "urdu_m1": "چار طبیعتیں جو باہمی مخالف اور سرکش ہوں",
          "urdu_m2": "وہ چند ہی دن آپس میں خوش رہ سکتی ہیں",
          "english_trans": "Four opposing and rebellious humors / Can dwell together harmoniously for but a few days;",
          "footnotes": [
            "چار طبع سے چار عنصر (خاک، پانی، ہوا، آگ) یا چار اخلاط (خون، بلغم، صفراء، سوداء) مراد ہیں۔"
          ],
          "study": {
            "notes_en": "Humoral pathology (Galenic/Avicennian): blood, phlegm, yellow bile, black bile (or the four elements). Their harmony constitutes life; their inevitable discord causes dissolution.",
            "notes_ur": "طبِ یونانی کے چار اخلاط یا چاروں عناصر باہم متضاد ہیں اور ان کا چند روزہ اجتماع ہی انسانی زندگی کہلاتا ہے۔",
            "vocabulary": [
              {
                "persian": "سَرْکَش",
                "grammar": "صفت",
                "meaning_en": "rebellious, unruly",
                "meaning_ur": "باغی، ضدی",
                "urdu_cognates": "سرکش، سرکشی"
              }
            ]
          }
        },
        {
          "id": "entry_p16_01",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "گَرْ یَکِے زِیْں چَہَار شُد غَالِبْ",
          "persian_m2": "جَانِ شِیْرِیْں بَرَایَدْ اَزْ قَالِبْ",
          "urdu_m1": "اگر ان چار میں سے ایک غالب ہو گئی",
          "urdu_m2": "تو میٹھی جان قالب سے باہر آ جاتی ہے",
          "english_trans": "If but one of these four gains mastery, / Sweet life departs from the physical frame!",
          "footnotes": [],
          "study": {
            "notes_en": "When humoral equilibrium is disrupted, the soul (*jān-e shīrīn*) exits the mortal vessel (*qālib*).",
            "notes_ur": "'قالب' بدن اور مٹی کے پتلے کو کہتے ہیں۔ جب ایک خلط غالب آ جائے تو جان جسم سے جدا ہو جاتی ہے۔",
            "vocabulary": [
              {
                "persian": "قَالِب",
                "grammar": "اسم (عربی)",
                "meaning_en": "mold, body, frame",
                "meaning_ur": "بدن، جسم کا ڈھانچہ",
                "urdu_cognates": "قالب، قلب"
              }
            ]
          }
        },
        {
          "id": "entry_p16_02",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "لَاجَرَمْ مَرْدِ عَارِفِ کَامِلْ",
          "persian_m2": "نَہ نَہَدْ بَرْ حَیَاتِ دُنْیَا دِلْ",
          "urdu_m1": "لامحالہ پورا جان کار انسان",
          "urdu_m2": "دنیا کی زندگی سے دل نہیں لگاتا",
          "english_trans": "Inevitably, therefore, the fully enlightened sage / Never attaches his heart to this earthly life!",
          "footnotes": [],
          "study": {
            "notes_en": "Knowing the precarious nature of the body, the true gnosis-bearer remains detached.",
            "notes_ur": "عارفِ کامل جسمانی زندگی کی نزاکت اور ناپائیداری کو دیکھ کر فانی دنیا سے دل نہیں لگاتا۔",
            "vocabulary": []
          }
        },
        {
          "id": "entry_p16_03",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "نِیْکْ وَ بَدْ چُوْں ہَمِے بَبَایَدْ مُرْد",
          "persian_m2": "خُنُکْ آں کَسْ کِہ گُوْئے نِیْکِیْ بُرْد",
          "urdu_m1": "نیک اور بد جب سبھی کو مرنا ہے",
          "urdu_m2": "تو وہ اچھا ہے جو نیکی میں بازی لے گیا",
          "english_trans": "Since good and wicked alike must inevitably die, / Blessed is he who carried off the ball of goodness in the polo field of life!",
          "footnotes": [],
          "study": {
            "notes_en": "'Gōy burdan': polo metaphor. To carry away the wooden ball (*gōy*) with the mallet (*chawgān*) meant winning the game. Here: winning the championship of virtue.",
            "notes_ur": "'گوئے نیکی بردن': چوگان (پولو) کا استعارہ۔ چوگان کے کھیل میں گیند کو لے اڑنا بازی جیتنا کہلاتا ہے۔ جب موت سب کے لیے ہے تو مبارکباد کا مستحق وہ ہے جو نیکی کی بازی جیت گیا۔",
            "vocabulary": [
              {
                "persian": "خُنُک",
                "grammar": "صفت / اسمِ صوت",
                "meaning_en": "blessed, happy, fortunate",
                "meaning_ur": "خوش نصیب، مبارک",
                "urdu_cognates": "خنک، خنکی"
              },
              {
                "persian": "گُوْئے",
                "grammar": "اسم",
                "meaning_en": "ball (in polo)",
                "meaning_ur": "گیند (چوگان کی)",
                "urdu_cognates": "گوئے سبقت لے جانا"
              }
            ]
          }
        },
        {
          "id": "entry_p16_04",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "بَرْگِ عَیْشِے بَگُوْرِ خِوِیْشْ فِرِسْت",
          "persian_m2": "کَسْ نَیَارَدْ زِ پَسْ تُوْ پِیْشْ فِرِسْت",
          "urdu_m1": "اپنی قبر میں زندگی کا سامان بھیج دے",
          "urdu_m2": "بعد میں کوئی نہیں لائے گا تو پہلے سے بھیج دے",
          "english_trans": "Send provision for comfort to thy own grave beforehand! / None will bring it after thee; dispatch it ahead in thine own lifetime!",
          "footnotes": [],
          "study": {
            "notes_en": "Provisions (*barg*) for the afterlife must be earned and sent while alive through charity and devotion; relying on heirs to do good deeds after death is folly.",
            "notes_ur": "سعدی کا مشہور شعر ہے: اپنی قبر کا سامان خود اپنی زندگی میں نیکیوں کی صورت میں آگے بھیج دو، کیونکہ تمہارے بعد کوئی تمہاری خاطر مشقت نہیں اٹھائے گا۔",
            "vocabulary": [
              {
                "persian": "بَرْگِ عَیْش",
                "grammar": "مرکب اضافی",
                "meaning_en": "provision for ease / comfort",
                "meaning_ur": "آرام اور خوشحالی کا سامان",
                "urdu_cognates": "برگ و ساز"
              }
            ]
          }
        },
        {
          "id": "entry_p16_05",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "عُمْر بَرْفْ اَسْت وَ آفْتَابِ تَمُوْز",
          "persian_m2": "اَنْدَکِے مَانْد وَ خِوَاجَہ غِرَّہ ہَنُوْز",
          "urdu_m1": "عمر برف کی طرح ہے اور سورج تموز کے مہینہ کا ہو",
          "urdu_m2": "تھوڑی رہی ہے اور جناب ابھی تک غافل ہیں",
          "english_trans": "Life is like snow, and the sun is the scorching sun of midsummer! / But a little of it remains, yet the master is heedless still!",
          "footnotes": [
            "خواجہ سردار اور معزز آدمی کو کہتے ہیں، لیکن یہاں پر طنزاً و تنبیہاً لایا گیا ہے۔"
          ],
          "study": {
            "notes_en": "A world-famous metaphor: life melting like a block of ice under the blazing July sun ('āftāb-e tamūz'). 'Khwājah' (gentleman/master) is addressed with affectionate irony.",
            "notes_ur": "عمر کی رفتار کی سب سے لرزہ خیز تمثیل: سخت گرمی کے مہینے میں دھوپ میں رکھی ہوئی برف جو ہر پل پگھل رہی ہو، اور انسان اپنی غفلت میں مگن ہو۔",
            "vocabulary": [
              {
                "persian": "تَمُوْز",
                "grammar": "اسم (سریانی/عربی)",
                "meaning_en": "midsummer (July, hottest month)",
                "meaning_ur": "سخت گرمی کا مہینہ (جولائی)",
                "urdu_cognates": "تموز"
              },
              {
                "persian": "غِرَّہ",
                "grammar": "صفت (عربی)",
                "meaning_en": "heedless, deluded, proud",
                "meaning_ur": "غافل، مغرور، دھوکے میں پڑا ہوا",
                "urdu_cognates": "غرہ، غرور"
              }
            ]
          }
        },
        {
          "id": "entry_p16_06",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "اے تُرَا دَسْتْ رَفْتَہ دَرْ بَازَار",
          "persian_m2": "تَرْسَمَتْ پُرْ نَیَاوَرِیْ دَسْتَار",
          "urdu_m1": "اے وہ جو خالی ہاتھ بازار میں چلا گیا",
          "urdu_m2": "مجھے ڈر ہے تو دستار بھر کر نہ لائے گا",
          "english_trans": "O thou who hast gone empty-handed into the marketplace! / I fear thou wilt not bring back thy turban filled with goods!",
          "footnotes": [
            "پر نیاوری دستار: یعنی بازار سے کچھ خرید نہ سکے گا اور خالی ہاتھ واپس آئے گا۔"
          ],
          "study": {
            "notes_en": "Entering the marketplace of the world without the coin of obedience means returning empty-handed.",
            "notes_ur": "جو شخص بازار میں خالی جیب جائے وہ سودا خرید کر اپنی پگڑی کے پلو میں کیسے باندھ سکتا ہے۔",
            "vocabulary": []
          }
        },
        {
          "id": "entry_p16_07",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "ہَرْ کِہ مَزْرُوْعِ خُوْد بَخُوْرْد بَخِیْد",
          "persian_m2": "وَقْتِ خِرْمَنْشْ خُوْشَہ بَایَدْ چِیْد",
          "urdu_m1": "جو اپنی کھیتی کچی کھا جائے",
          "urdu_m2": "اُس کو کھلیان کرتے وقت بالیں چننی پڑیں گی",
          "english_trans": "Whoever consumes his own standing crop while it is green / Will have to glean stray ears of corn at the time of harvest!",
          "footnotes": [],
          "study": {
            "notes_en": "Agricultural proverb: squandering spiritual capital in youth leaves one begging for scraps in the harvest of old age and eternity.",
            "notes_ur": "'خید' کچی اور ہری کھیتی کو کہتے ہیں۔ جو فصل پکنے سے پہلے ہی کچی کھا لے، کھلیان کے وقت اسے دوسروں کی گری پڑی بالیاں چننی پڑیں گی۔",
            "vocabulary": [
              {
                "persian": "خِیْد",
                "grammar": "اسم",
                "meaning_en": "green unripened crop",
                "meaning_ur": "کچی کھیتی، ہری گھاس",
                "urdu_cognates": "خید"
              },
              {
                "persian": "خِرْمَن",
                "grammar": "اسم",
                "meaning_en": "harvest, threshing floor",
                "meaning_ur": "کھلیان، اناج کا ڈھیر",
                "urdu_cognates": "خرمن، خرمنِ گل"
              }
            ]
          }
        },
        {
          "id": "entry_p16_08",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "پَنْدِ سَعْدِیْ بَگُوْشِ دِلْ بشنَوْ",
          "persian_m2": "رَہْ چُنِیْں اَسْتْ مَرْد بَاشْ وَ بَرَوْ",
          "urdu_m1": "سعدی کی نصیحت دل کے کان سے سن",
          "urdu_m2": "راستہ یہی ہے مرد بن اور چل",
          "english_trans": "Hearken unto Saadi's counsel with the ear of the heart! / This is the true path: be a man of courage and stride forth!",
          "footnotes": [],
          "study": {
            "notes_en": "'Mard bāsh': be a spiritual warrior, face reality with resolve.",
            "notes_ur": "'مرد باش و برو': ہمت پیدا کر اور راستے پر چل پڑ۔ راہِ سلوک میں بزدلی اور غفلت کی گنجائش نہیں۔",
            "vocabulary": []
          }
        },
        {
          "id": "entry_p16_09",
          "book_page": 14,
          "pdf_page": 16,
          "type": "prose",
          "persian": "بَعْد اَزْ تَاَمُّلْ مَصْلَحَتْ آں دِیْدَمْ کِہ دَرْ نِشِیْمَنِ عُزْلَتْ نِشِیْنَمْ ، وَ دَامَنِ صُحْبَتْ فَرَاہَمْ چِیْنَمْ ، وَ دَفْتَر اَزْ گُفْتَارْہَائے پَرِیْشَاں بِشُوْیَمْ ، وَ مَنْ بَعْد پَرِیْشَاں نَہ گُوْیَمْ ۔",
          "urdu_interlinear": "غور کے بعد میں نے یہ مناسب سمجھا کہ گوشہ نشین ہوؤں اور یار باشی سے دامن سمیٹ لوں اور فضول باتوں کا دفتر دھو دوں اور پھر بے ضرورت بات نہ کروں ۔",
          "english_trans": "After due deliberation, I deemed it expedient to retire into the chamber of seclusion, draw in the skirt of social companionship, wash the ledger clean of scattered discourses, and utter idle words no more.",
          "footnotes": [],
          "study": {
            "notes_en": "Saadi's vow of silence and retreat from society (*'uzlat*). In Islamic spirituality, 'khalwah' (seclusion) and 'samt' (silence) are the initial prerequisites for inward purification.",
            "notes_ur": "عزلت اور خاموشی کا پختہ عزم: دامنِ صحبت سمیٹنا اور فضول باتوں کے دفتر کو دھونا۔ سعدی نے طے کر لیا کہ اب کسی محفل میں سخن طرازی نہیں کریں گے۔",
            "vocabulary": [
              {
                "persian": "نِشِیْمَنِ عُزْلَت",
                "grammar": "مرکب اضافی",
                "meaning_en": "abode of seclusion",
                "meaning_ur": "تنہائی کا گوشہ",
                "urdu_cognates": "نشیمن، عزلت"
              }
            ]
          }
        },
        {
          "id": "entry_p16_10",
          "book_page": 14,
          "pdf_page": 16,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "زَبَاں بُرِیْدَہ بَکُنْجِے نِشَسْتَہ صُمٌّ بُکْم",
          "persian_m2": "بَہ اَزْ کَسِے کِہ نَبَاشَدْ زَبَانْش اَنْدَرْ حُکْم",
          "urdu_m1": "زبان کٹا ہوا گوشہ میں بہرا گونگا بنا بیٹھا ہوا",
          "urdu_m2": "اُس سے بہتر ہے جس کی زبان قابو میں نہ ہو",
          "english_trans": "A mute sitting deaf and dumb in a corner, with tongue cut out, / Is far better than one whose tongue is not held under control!",
          "footnotes": [],
          "study": {
            "notes_en": "'Summun bukm': Quranic allusion (Surah Al-Baqarah 2:18). Better to be physically mute than to have an undisciplined tongue that destroys both faith and fellowship.",
            "notes_ur": "'صمٌّ بکم' قرآنی اصطلاح ہے (بہرے اور گونگے)۔ بے قابو زبان رکھنے والے متکلم سے وہ گونگا ہزار گنا بہتر ہے جو خاموشی سے گوشے میں بیٹھا ہو۔",
            "vocabulary": [
              {
                "persian": "صُمٌّ بُکْم",
                "grammar": "مرکب توصیفی (عربی)",
                "meaning_en": "deaf and dumb",
                "meaning_ur": "گونگا اور بہرا",
                "urdu_cognates": "صم بکم"
              }
            ]
          }
        },
        {
          "id": "entry_p16_11",
          "book_page": 14,
          "pdf_page": 16,
          "type": "prose",
          "persian": "تَا یَکِے اَزْ دُوْسْتَاں کِہ دَرْ کَجَاوَہ ہَمْنِشِیْنِ مَنْ بُوْدے وَ دَرْ حُجْرَہ جَلِیْس ، بَرَسْمِ قَدِیْم اَزْ دَرْ دَرْ آمَدْ چَنْدَاں کِہ نِشَاطِ مُلَاعَبَتْ کَرْد وَ بِسَاطِ مُدَاعَبَتْ گُسْتَرَدْ جَوَابَشْ نَہ گُفْتَمْ وَ سَر اَزْ زَانُوْئے تَعَبُّدْ بَر نَگِرِفْتَمْ رَنْجِیْدَہ نِگَہْ کَرْد وَ گُفْت :",
          "urdu_interlinear": "یہاں تک کہ ایک دوست جو کجاوے میں میرا ہم نشین اور حجرہ میں ہم مجلس تھا ، پہلی عادت کے مطابق دروازے سے اندر آیا جس قدر بھی اُس نے کھیل کود کی خوشی کی کوشش کی اور مذاق کی بساط بچھائی میں نے اس کو جواب نہ دیا اور عبادت گزاری کی زانو سے سر نہ اٹھایا اس نے رنج سے مجھے دیکھا اور بولا :",
          "english_trans": "Until one of my friends, who had been my travelling-companion in the camel-litter and my intimate associate in the cell, entered the door according to his ancient custom. However much he engaged in playful mirth and spread out the carpet of jesting, I gave him no answer, nor did I lift my head from the knee of worship. He gazed upon me with sorrow and said:",
          "footnotes": [],
          "study": {
            "notes_en": "Introduction of the beloved companion. The camel-litter ('kajāwah') recalls shared journeys across the Islamic world. Saadi maintains his vow of silence, head bowed upon his knee.",
            "notes_ur": "'کجاوہ' اونٹ کی پشت پر سفر کرنے والا ڈول یا ہودج۔ سفر و حضر کا پرانا مخلص دوست جب ملاقات کے لیے آیا اور شوخی کی تو سعدی نے خاموشی برقرار رکھی اور سر نہ اٹھایا۔",
            "vocabulary": [
              {
                "persian": "کَجَاوَہ",
                "grammar": "اسم",
                "meaning_en": "camel-litter, pannier",
                "meaning_ur": "کجاوہ، اونٹ پر سواری کا جھولا",
                "urdu_cognates": "کجاوہ"
              },
              {
                "persian": "مُدَاعَبَت",
                "grammar": "اسم (عربی)",
                "meaning_en": "jesting, playful banter",
                "meaning_ur": "ہنسی مذاق، دل لگی",
                "urdu_cognates": "مداعبت"
              }
            ]
          }
        },
        {
          "id": "entry_p17_01",
          "book_page": 15,
          "pdf_page": 17,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "کَنُوْنَتْ کِہ اِمْکَانِ گُفْتَار ہَسْت",
              "persian_m2": "بِگُوْ اے بَرَادَرْ بِلُطْفْ وَ خُوْشِیْ",
              "urdu_m1": "اب جبکہ تجھ میں بات کرنے کی طاقت ہے",
              "urdu_m2": "اے بھائی نرمی اور خوشی سے بات کر لے"
            },
            {
              "persian_m1": "کِہ فَرْدَا چُوْ پَیْکِ اَجَلْ دَرْ رَسَد",
              "persian_m2": "بِحُکْمِ ضَرُوْرَتْ زَبَاں دَرْ کَشِیْ",
              "urdu_m1": "اس لئے کہ کل جب موت کا قاصد پہنچ جائے گا",
              "urdu_m2": "تو مجبورا تو زبان بند کر لے گا"
            }
          ],
          "english_trans": "Now while the power of speech is yet thine, / Speak, O brother, with kindness and joy! / For tomorrow, when the messenger of death arrives, / Thou wilt be compelled by necessity to hold thy peace!",
          "footnotes": [],
          "study": {
            "notes_en": "The companion turns Saadi's own philosophy of mortality back upon him: death will enforce eternal silence soon enough; while alive, speech used in kindness is a duty.",
            "notes_ur": "دوست کی ذہانت دیکھیے: اس نے سعدی ہی کے فلسفۂ مرگ کو بنیاد بنا کر کہا کہ کل جب موت آئے گی تو زبان خودبخود بند ہو جائے گی، آج جب بولنے کی قوت حاصل ہے تو خیر اور محبت کے بول بولنے چاہئیں۔",
            "vocabulary": [
              {
                "persian": "پَیْکِ اَجَل",
                "grammar": "مرکب اضافی",
                "meaning_en": "courier of death",
                "meaning_ur": "موت کا قاصد یا پیغام بر",
                "urdu_cognates": "پیک، اجل"
              }
            ]
          }
        },
        {
          "id": "entry_p17_02",
          "book_page": 15,
          "pdf_page": 17,
          "type": "prose",
          "persian": "کَسِے اَزْ مُتَعَلِّقَانِ مَنْشْ بَرْ حَسْبِ وَاقِعَہ مُطَّلِعْ گَرْدَانِیْد کِہ فُلَاں عَزْمْ کَرْدَہ اَسْت وَ نِیَّتِ جَزْمْ کِہ بَقِیَّتِ عُمْر مُعْتَکِفْ نِشِیْنَدْ وَ خَامُوْشِیْ گُزِیْنَدْ ، تَوْ نِیْز اَگَرْ تَوَانِیْ سَرِ خِوِیْشْ گِیْر وَ مُجَانَبَتْ پِیْشْ ۔ گُفْت : بَعِزَّتِ عَظِیْمْ وَ صُحْبَتِ قَدِیْمْ کِہ دَمْ بَر نَیَارَمْ وَ قَدَمْ بَر نَدَارَمْ مَگَرْ آنْگِہ کِہ سُخَنْ گُفْتَہ شَوَد بَعَادَتِ مَالُوْفْ وَ طَرِیْقِ مَعْرُوْفْ ، کِہ آزُرْدَنِ دِلِ دُوْسْتَاں جَہْلْ اَسْت وَ کَفَّارَتِ یَمِیْنْ سَہْلْ ، خِلَافِ رَاہِ صَوَابْ اَسْت وَ عَکْسِ رَائے اُوْلِی الْاَلْبَابْ : ذُوالْفَقَارِ عَلِیْ دَرْ نِیَامْ وَ زَبَانِ سَعْدِیْ دَرْ کَامْ ۔",
          "urdu_interlinear": "میرے متعلقین میں سے کسی نے اُس کو اصل واقعہ بتایا کہ اس نے تو پختہ ارادہ اور پکی نیت کر لی ہے کہ باقی عمر گوشہ نشین رہے گا اور خاموشی اختیار کرے گا۔ تجھ سے اگر ہو سکے تو تو بھی اپنا راستہ لے اور یکسوئی اختیار کر وہ بولا خدائے برتر کی عزت اور پرانی دوستی کی قسم کہ میں سانس بھی نہ لوں گا اور قدم بھی نہ اٹھاؤں گا جب تک کہ پہلی عادت اور قدیم طریقہ کے مطابق بات نہ ہو جائے اس لئے کہ دوستوں کا دل دکھانا نادانی ہے اور قسم کا کفارہ دینا آسان ہے ۔ درست رائے کے خلاف ہے اور عقلمندوں کی رائے کے برعکس : حضرت علیؓ کی ذوالفقار کا نیام میں رہنا اور سعدی کی زبان کا تالو سے لگنا ۔",
          "english_trans": "One of my household informed him of the true circumstance, saying: 'He has made a firm resolve and decisive intent to spend the remainder of his life secluded as a hermit, choosing perpetual silence. Thou too, if thou canst, take thy way and withdraw!' He replied: 'By the Majesty of the Almighty and our ancient companionship! I shall neither draw breath nor move a step unless he speaks to me according to our customary habit and well-known way! For wounding the heart of friends is folly, whereas the expiation of an oath is easy. It is contrary to the path of rectitude and the opposite of the judgment of men of understanding that the sword Zulfiqar of Ali should stay in its scabbard, or the tongue of Saadi remain tied to his palate!'",
          "footnotes": [
            "ذوالفقار حضرت علیؓ کی مشہور تلوار کا نام ہے۔"
          ],
          "study": {
            "notes_en": "The immortal comparison: Ali's sword Zulfiqar in its sheath balances Saadi's eloquence locked in silence. Just as Ali's sword was created for chivalric battle, Saadi's tongue was shaped for moral illumination.",
            "notes_ur": "دوست کا لاجواب استدلال: 'آزردنِ دلِ دوستاں جہل است و کفارتِ یمین سہل' (دوستوں کا دل دکھانا نادانی ہے جبکہ قسم توڑنے کا کفارہ دینا آسان ہے)۔ اور پھر یہ موازنہ کہ جس طرح حضرت علیؓ کی ذوالفقار کا نیام میں رہنا شایانِ شان نہیں اسی طرح سعدی کی زبان کا گنگ ہو جانا نامناسب ہے۔",
            "vocabulary": [
              {
                "persian": "مُعْتَکِف",
                "grammar": "اسمِ فاعل (عربی)",
                "meaning_en": "recluse, secluded in prayer",
                "meaning_ur": "گوشہ نشین، اعتکاف کرنے والا",
                "urdu_cognates": "معتکف، اعتکاف"
              },
              {
                "persian": "کَفَّارَتِ یَمِیْن",
                "grammar": "مرکب اضافی (عربی)",
                "meaning_en": "expiation for a broken oath",
                "meaning_ur": "قسم کا کفارہ",
                "urdu_cognates": "کفارہ، یمین (قسم)"
              },
              {
                "persian": "نِیَام",
                "grammar": "اسم",
                "meaning_en": "scabbard, sheath",
                "meaning_ur": "تلوار کا نیام",
                "urdu_cognates": "نیام"
              }
            ]
          }
        },
        {
          "id": "entry_p18_01",
          "book_page": 16,
          "pdf_page": 18,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "زَبَاں دَرْ دَہَانِ خِرَدْمَنْد چِیْسْت",
              "persian_m2": "کِلِیْدِ دَرِ گَنْجِ صَاحِبْ ہُنَرْ",
              "urdu_m1": "عقلمند کے منہ میں زبان کیا ہے",
              "urdu_m2": "ہنر مند کے خزانہ کے دروازہ کی کنجی"
            },
            {
              "persian_m1": "چُوْ دَرْ بَسْتَہ بَاشَدْ چَہ دَانَدْ کَسِے",
              "persian_m2": "کِہ جَوْہَرْ فَرُوْشْ اَسْت یَا پِیْلَہ وَر",
              "urdu_m1": "جب دروازہ بند ہو تو کسی کو کیا معلوم",
              "urdu_m2": "کہ موتی بیچنے والا ہے یا بساطی"
            }
          ],
          "english_trans": "What is the tongue in the mouth of the wise man? / It is the key to the portal of the master's treasury! / When the door is closed, how can anyone know / Whether he be a seller of precious jewels or a peddler of petty wares?",
          "footnotes": [],
          "study": {
            "notes_en": "Speech reveals inner intellect: so long as a person remains silent, his true stature is concealed. 'Jawhar-farōsh' (jeweler) contrasts with 'pīlah-war' (petty street peddler).",
            "notes_ur": "فارسی کا مشہور حکیمانہ قطعہ: زبان انسان کے باطنی جوہر کا پتہ دیتی ہے۔ جب تک دکان بند رہے کوئی نہیں جان سکتا کہ اندر موتیوں کا خزانہ ہے یا معمولی سودا سلف۔ بولنے سے ہی انسان کا ظرف ظاہر ہوتا ہے۔",
            "vocabulary": [
              {
                "persian": "کِلِیْد",
                "grammar": "اسم",
                "meaning_en": "key",
                "meaning_ur": "چابی، کنجی",
                "urdu_cognates": "کلید، کلیدی"
              },
              {
                "persian": "پِیْلَہ وَر",
                "grammar": "اسمِ فاعل مرکب",
                "meaning_en": "peddler, haberdasher",
                "meaning_ur": "چھوٹا سوداگر، پھیری والا، بساطی",
                "urdu_cognates": "پیلہ ور"
              }
            ]
          }
        },
        {
          "id": "entry_p18_02",
          "book_page": 16,
          "pdf_page": 18,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "اَگَرْ چِہ پِیْشِ خِرَدْمَنْد خَامُشِیْ اَدَبْ اَسْت",
              "persian_m2": "بِوَقْتِ مَصْلَحَتْ آں بَہ کِہ دَرْ سُخَنْ کُوْشِیْ",
              "urdu_m1": "عقلمند کے آگے چپ رہنا اگرچہ ادب ہے",
              "urdu_m2": "مصلحت کے وقت یہ بہتر ہے کہ تو بات کرنیکی کوشش کریگا"
            },
            {
              "persian_m1": "دُوْ چِیْز طِیْرَۂ عَقْلْ اَسْت دَمْ فُرُوْ بَسْتَن",
              "persian_m2": "بِوَقْتِ گُفْتَنْ وَ گُفْتَنْ بِوَقْتِ خَامُوْشِیْ",
              "urdu_m1": "دو باتیں عقل کا عیب ہیں، کہنے کے وقت",
              "urdu_m2": "چپ رہنا اور چپ رہنے کے وقت بولنا"
            }
          ],
          "english_trans": "Although in the presence of the wise silence is etiquette, / At the time of true benefit it is best that thou strivest in speech! / Two things are the very disgrace of intellect: to seal one's lips / At the time for speaking, and to speak at the time for silence!",
          "footnotes": [],
          "study": {
            "notes_en": "The doctrine of appropriate speech: timing is everything. Silence when truth needs defence is cowardice; speech when silence is called for is foolishness.",
            "notes_ur": "کلام اور سکوت کا توازن: 'دو چیز طیرۂ عقل است'۔ بولنے کے وقت خاموش رہنا اور خاموشی کے وقت بولنا دونوں عقل کے نقص ہیں۔",
            "vocabulary": [
              {
                "persian": "طِیْرَۂ عَقْل",
                "grammar": "مرکب اضافی",
                "meaning_en": "blemish / folly of the intellect",
                "meaning_ur": "عقل کی خامی، بے وقوفی",
                "urdu_cognates": "طیرہ، طیرگی"
              }
            ]
          }
        },
        {
          "id": "entry_p18_03",
          "book_page": 16,
          "pdf_page": 18,
          "type": "prose",
          "persian": "فِی الْجُمْلَہ زَبَاں اَزْ مُکَالَمَتِ اَوْ دَرْ کَشِیْدَنْ قُوَّتْ نَدَاشْتَمْ ، وَ رُوْئے اَزْ مُحَادَثَتْ بَگَرْدَانِیْدَنْ مُرُوَّتْ نَدَانِسْتَمْ ، کِہ یَارِ مُوَافِقْ بُوْد وَ مُحِبِّ صَادِقْ ۔",
          "urdu_interlinear": "خلاصہ یہ کہ اس کے ساتھ بات کرنے سے زبان روکنے کی مجھ میں قوت نہ رہی اور اس کی ہمکلامی سے منہ موڑنے کو میں نے آدمیت نہ سمجھی اس لئے کہ موافق یار اور سچا دوست تھا ۔",
          "english_trans": "In brief, I lacked the power to withhold my tongue from conversing with him, and I did not deem it chivalrous to turn my face away from his dialogue; for he was a congenial companion and a sincere friend.",
          "footnotes": [],
          "study": {
            "notes_en": "The social nature of compassion: genuine friendship overcomes solitary vows of austerity.",
            "notes_ur": "سعدی نے دوست کے اخلاص کے آگے ہتھیار ڈال دیے اور تسلیم کیا کہ مخلص دوست سے منہ موڑنا مروت اور شرافت کے خلاف ہے۔",
            "vocabulary": [
              {
                "persian": "مُرُوَّت",
                "grammar": "اسم (عربی)",
                "meaning_en": "chivalry, magnanimity, humanity",
                "meaning_ur": "شرافت، لحاظ، آدمیت",
                "urdu_cognates": "مروت، با مروت"
              }
            ]
          }
        },
        {
          "id": "entry_p18_04",
          "book_page": 16,
          "pdf_page": 18,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "شعر",
          "persian_m1": "چُوْ جَنْگْ آوَرِیْ بَا کَسِے بَرْ سِتِیْز",
          "persian_m2": "کِہ اَزْ وَے گُزِیْرَتْ بُوَدْ یَا گُرِیْز",
          "urdu_m1": "جب تو لڑے تو اُس سے لڑ",
          "urdu_m2": "جس سے تجھے چارہ کار ہو یا گریز کی گنجائش ہو",
          "english_trans": "When thou engagest in battle, contend with one / From whom thou hast either the prospect of victory or the avenue of retreat!",
          "footnotes": [],
          "study": {
            "notes_en": "Pragmatic psychology: do not battle with an intimate friend whom you cannot defeat and from whom you cannot flee.",
            "notes_ur": "سعدی مسکرا کر فرماتے ہیں کہ جھگڑا اس سے کرنا چاہیے جس سے بچنے کی کوئی راہ ہو، ایسے مخلص ساتھی سے کیا الجھنا جس کے بغیر چارہ ہی نہیں۔",
            "vocabulary": [
              {
                "persian": "گُزِیْر",
                "grammar": "اسم",
                "meaning_en": "remedy, alternative, choice",
                "meaning_ur": "چارہ کار، مخلصی",
                "urdu_cognates": "گزیر، ناگزیر"
              }
            ]
          }
        },
        {
          "id": "entry_p18_05",
          "book_page": 16,
          "pdf_page": 18,
          "type": "prose",
          "persian": "بِحُکْمِ ضَرُوْرَتْ سُخَنْ گُفْتَمْ وَ تَفَرُّجْ کُنَاں بِیْرُوْں رَفْتَمْ دَرْ فَصْلِ رَبِیْعْ کِہ صَوْلَتِ بَرْدْ آرَمِیْدَہ بُوْد وَ اَوَانِ دَوْلَتِ وَرْدْ رَسِیْدَہ ۔",
          "urdu_interlinear": "مجبوراً میں نے بات کر لی اور تفریح کے لئے باہر نکل پڑا بہار کا موسم تھا سردی کا حملہ ٹھنڈا پڑ چکا تھا اور گلاب کی حکومت کا موسم آ گیا تھا ۔",
          "english_trans": "Under the compulsion of necessity, I spoke, and I went forth taking a stroll in the season of spring, when the fury of the winter chill had subsided and the hour of the empire of the rose had arrived.",
          "footnotes": [],
          "study": {
            "notes_en": "Magical rhyming prose (saj'): 'صولتِ بَرد آرمیدہ بود و اوانِ دولتِ وَرد رسیدہ'. Notice the exquisite balance between 'برد' (cold) and 'ورد' (rose).",
            "notes_ur": "سجع نگاری کا شاہکار جملہ: 'صولتِ برد' (سردی کا حملہ) اور 'دولتِ ورد' (گلاب کی سلطنت)۔ موسمِ بہار کی آمد اور گلاب کے کھلنے کا شاعرانہ اعلان۔",
            "vocabulary": [
              {
                "persian": "صَوْلَت",
                "grammar": "اسم (عربی)",
                "meaning_en": "fury, onslaught, assault",
                "meaning_ur": "حملہ، دبدبہ، شدت",
                "urdu_cognates": "صولت (جیسے شوکت و صولت)"
              },
              {
                "persian": "بَرْد",
                "grammar": "اسم (عربی)",
                "meaning_en": "cold, chill",
                "meaning_ur": "سردی، ٹھنڈک",
                "urdu_cognates": "برودت، بارد"
              },
              {
                "persian": "وَرْد",
                "grammar": "اسم (عربی)",
                "meaning_en": "rose",
                "meaning_ur": "گلاب کا پھول",
                "urdu_cognates": "ورد (جیسے وردِ احمر)"
              }
            ]
          }
        },
        {
          "id": "entry_p18_06",
          "book_page": 16,
          "pdf_page": 18,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "اَوَّلِ اُرْدِیْ بِہِشْتْ مَاہِ جَلَالِیْ",
              "persian_m2": "بُلْبُلْ گُوْیَنْدَہ بَرْ مَنَابِرِ قُضْبَاں",
              "urdu_m1": "جلالی سن کے اردی بہشت مہینہ کا شروع",
              "urdu_m2": "شاخوں کے منبروں پر بلبل چہک رہی تھی"
            },
            {
              "persian_m1": "بَرْگِ سُرْخْ اَزْ نَمْ اُوْفْتَادَہ لَآلِیْ",
              "persian_m2": "ہَمْچُوْ عَرَقْ بَرْ عِذَارِ شَاہِدِ غَضْبَاں",
              "urdu_m1": "گلاب کے پھول پر شبنم کے موتی بکھرے تھے",
              "urdu_m2": "جیسے غصہ کی حالت میں معشوق کے رخسار پر پسینہ"
            }
          ],
          "english_trans": "It was the beginning of Urdibihisht, month of the Jalali era; / The nightingale was delivering sermons upon the pulpits of the boughs! / Dewdrops were scattered upon the red petals like pearls, / Resembling drops of sweat upon the cheek of an angry beauty!",
          "footnotes": [
            "اردی بہشت فارسی شمسی سال کا دوسرا مہینہ ہے جو وسطِ بہار (اپریل-مئی) کے مطابق ہے۔",
            "جلالی سال: سلطان جلال الدین ملک شاہ سلجوقی کے عہد میں ماہرینِ فلکیات (بشمول عمر خیام) کا تیار کردہ شمسی تقویم۔"
          ],
          "study": {
            "notes_en": "Historical and poetic precision: Urdibihisht (late April / early May) in the Jalali solar calendar. The nightingales perched on branches are likened to orators on minbars. The red rose with dew drops is compared with daring psychological realism to the perspiration on the flushed cheek of an irritated beloved.",
            "notes_ur": "سعدی کا لازوال موسمِ بہار کا منظر۔ شاخوں کو منبر اور بلبل کو خطیب کہا گیا ہے۔ پھول کی پنکھڑیوں پر شبنم کے قطروں کی تشبیہ معشوق کے غضبناک رخسار کے پسینے سے دی گئی ہے جو فارسی شاعری کی نادر ترین تشبیہات میں شمار ہوتی ہے۔",
            "vocabulary": [
              {
                "persian": "مَنَابِرِ قُضْبَاں",
                "grammar": "مرکب اضافی (عربی)",
                "meaning_en": "pulpits of the branches",
                "meaning_ur": "شاخوں کے منبر",
                "urdu_cognates": "منابر (منبر کی جمع)، قضبان"
              },
              {
                "persian": "شَاہِدِ غَضْبَاں",
                "grammar": "مرکب توصیفی",
                "meaning_en": "an angry beloved",
                "meaning_ur": "غصے میں بھرا ہوا معشوق",
                "urdu_cognates": "شاہد (حسین)، غضبان (غصے والا)"
              }
            ]
          }
        },
        {
          "id": "entry_p19_01",
          "book_page": 17,
          "pdf_page": 19,
          "type": "prose",
          "persian": "شَبْ رَا بَبُوْسْتَاں بَا یَکِے اَزْ دُوْسْتَاں اِتِّفَاقِ مَبِیْتْ اُفْتَاد ، مَوْضِعِے خُوْشْ وَ خُرَّمْ وَ دِرَخْتَاں دِلْ کَشْ وَ دَرْہَمْ ، گُفْتِے کِہ خُرْدَۂ مِیْنَا بَرْ خَاکَشْ رِیْخْتَہ ، وَ عِقْدِ ثُرَیَّا اَزْ تَاکَشْ آوِیْخْتَہ ۔",
          "urdu_interlinear": "رات کو باغ میں ایک دوست کے ساتھ شب گذارنے کا اتفاق ہوا ایک سرسبز و شاداب جگہ اور درختوں کے جھرمٹ دلکش اور دل چسپ درخت گویا کانچ کے ٹکڑے اس کی خاک پر بکھرے ہوئے اور ثریا کا گچھا اس کے انگوروں کی بیل میں لٹکا ہوا تھا ۔",
          "english_trans": "It so chanced that I spent the night in a garden with one of my friends—a pleasant and delightful spot, with trees intertwined and captivating. Thou wouldst have said that shards of enameled glass were scattered upon its soil, and that the necklace of the Pleiades was suspended from its grapevines!",
          "footnotes": [],
          "study": {
            "notes_en": "Astounding visual imagery: the garden floor sparkles with blossoms like crushed glass enamel ('khurdah-ye mīnā'), and the clusters of hanging grapes resemble the constellation Pleiades (''iqd-e surayyā').",
            "notes_ur": "'خردۂ مینا' یعنی رنگین شیشے یا کانچ کی کرچیاں۔ 'عقدِ ثریا' یعنی پروین ستاروں کا جھمکا۔ انگور کے خوشوں کو ثریا سے اور پھولوں کی زمین کو رنگین شیشے سے تشبیہ دی ہے۔",
            "vocabulary": [
              {
                "persian": "مَبِیْت",
                "grammar": "اسمِ ظرف / مصدر (عربی)",
                "meaning_en": "spending the night, night-lodging",
                "meaning_ur": "رات گزارنا، شب باشی",
                "urdu_cognates": "بیتوتت"
              },
              {
                "persian": "خُرْدَۂ مِیْنَا",
                "grammar": "مرکب اضافی",
                "meaning_en": "shards of enameled glass",
                "meaning_ur": "رنگین شیشے یا آبگینے کے ٹکڑے",
                "urdu_cognates": "خردہ، مینا"
              },
              {
                "persian": "عِقْدِ ثُرَیَّا",
                "grammar": "مرکب اضافی",
                "meaning_en": "cluster / necklace of the Pleiades",
                "meaning_ur": "ثریا ستاروں کا ہار یا گچھا",
                "urdu_cognates": "عقد، ثریا"
              }
            ]
          }
        },
        {
          "id": "entry_p19_02",
          "book_page": 17,
          "pdf_page": 19,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "رَوْضَةٌ مَاؤُھَا سَلْسَالٌ",
              "persian_m2": "دَوْحَةٌ سَجْعُ طَیْرِھَا مَوْزُوْنٌ",
              "urdu_m1": "ایک ایسا باغ جس کی نہر کا پانی جاری تھا",
              "urdu_m2": "ایسا درخت جس کے پرندوں کا گانا موزوں"
            },
            {
              "persian_m1": "آں پُر اَزْ لَالَہ ہَائے رَنْگَارَنْگْ",
              "persian_m2": "وِیْں پُر اَزْ مِیْوَہ ہَائے گُوْنَاگُوْں",
              "urdu_m1": "وہ رنگ برنگ کے لالوں سے پُر",
              "urdu_m2": "یہ طرح طرح کے میوؤں سے لدھا ہوا"
            },
            {
              "persian_m1": "بَاد دَرْ سَایَۂ دِرَخْتَانَشْ",
              "persian_m2": "گُسْتَرَانِیْدَہ فَرْشِ بُوْقَلَمُوْں",
              "urdu_m1": "ہوا نے اس کے درختوں کے سایہ میں",
              "urdu_m2": "رنگا رنگ فرش بچھا دیا تھا"
            }
          ],
          "english_trans": "A garden whose stream flowed limpid and sweet! / A grove whose birds' melodies were harmoniously measured! / The one brimful of colorful tulips, / The other laden with manifold fruits! / And the breeze in the shade of its trees / Had spread out a carpet of iridescent hues!",
          "footnotes": [],
          "study": {
            "notes_en": "Blending Arabic and Persian hemistichs seamlessly. 'Farsh-e bōqalamūn': a carpet of chameleon-like shifting colors, formed by blossoms fallen onto the grass.",
            "notes_ur": "عربی اور فارسی کی باہمی آمیزش۔ 'بوقلموں' ایسا ریشمی کپڑا جس کا رنگ بدلتی روشنی میں بدلتا رہتا ہے۔ درختوں سے گرے ہوئے رنگ برنگ پھولوں نے زمین پر بوقلموں کا فرش بچھا دیا تھا۔",
            "vocabulary": [
              {
                "persian": "سَلْسَال",
                "grammar": "صفت (عربی)",
                "meaning_en": "limpid, sweet, flowing smoothly",
                "meaning_ur": "صاف و شفاف، میٹھا پانی",
                "urdu_cognates": "سلسبیل"
              },
              {
                "persian": "بُوْقَلَمُوْں",
                "grammar": "اسم",
                "meaning_en": "chameleon, iridescent fabric, variegated",
                "meaning_ur": "رنگ برنگا، ہر لمحہ رنگ بدلنے والا",
                "urdu_cognates": "بوقلموں، بوقلمونی"
              }
            ]
          }
        },
        {
          "id": "entry_p19_03",
          "book_page": 17,
          "pdf_page": 19,
          "type": "prose",
          "persian": "بَامْدَادَاں کِہ خَاطِرِ بَازْ آمَدَن بَرْ رَائے نِشَسْتَن غَالِبْ آمَدْ دِیْدَمَشْ دَامَنِے گُلْ وَ رَیْحَانْ وَ سُنْبُلْ وَ ضَمِیْرَانْ فَرَاہَمْ آوَرْدَہ وَ آہَنْگِ رُجُوْعْ کَرْدَہ ، گُفْتَمْ : گُلِ بُوْسْتَاں رَا چُنَانْکِہ دَانِیْ بَقَائے وَ عَہْدِ گُلِسْتَاں رَا وَفَائے نَبَاشَدْ ، وَ حُکَمَاں گُفْتَہ اَنْد : ہَرْ چِہ نَپَایَدْ دِلْبَسْتَگِیْ رَا نَشَایَدْ ۔ گُفْت : طَرِیْقْ چِیْسْت ؟ گُفْتَمْ : بَرَائے نُزْہَتِ نَاظِرَاں وَ فُسْحَتِ حَاضِرَاں کِتَابِ گُلِسْتَاں تَوَاں تَصْنِیْفْ کَرْدَنْ کِہ بَادِ خِزَاں رَا بَرْ وَرَقِ اَوْ دَسْتِ تَطَاوُلْ نَبَاشَدْ وَ گَرْدِشِ زَمَاں عَیْشِ رَبِیْعَشْ رَا بِطَیْشِ خَرِیْفْ مُبَدَّلْ نَہ کُنْد ۔",
          "urdu_interlinear": "صبح کو جب واپسی کا خیال بیٹھنے کی رائے پر غالب آ گیا میں نے اسے دیکھا کہ وہ گل ، ریحان ، سنبل ، اور ضمیران سے دامن کو بھرے ہوئے ہے اور لوٹنے کا ارادہ کر رہا ہے میں نے اس سے کہا جیسا کہ تجھے معلوم ہے باغ کے پھول کو ٹکاؤ اور باغ کے زمانہ میں وفا نہیں ہوتی اور عقلمندوں نے کہا ہے جو ناپائیدار ہے دوستی کے لائق نہیں ہے اس نے کہا پھر کیا صورت ہے میں نے کہا دیکھنے والوں کی تفریح اور موجودہ لوگوں کی کشادگی کے لئے میں ایک ایسی گلستاں کتاب تصنیف کر سکتا ہوں جس کے پتوں پر خزاں کی ہوا کی دست درازی نہ ہو اور زمانہ کی گردش اس کے موسمِ بہار کی خوشگواری کو موسمِ خزاں کی ناگواری میں تبدیل نہ کر سکے ۔",
          "english_trans": "In the morning, when the inclination to return home prevailed over the desire to tarry, I saw that he had gathered a skirtful of roses, sweet basil, hyacinths, and wild marjoram, and was preparing to depart. I said to him: 'The flowers of the garden, as thou knowest, have no permanence, and the promise of the rose-bower has no fidelity; and the philosophers have declared: Whatever endures not is not worthy of the heart's attachment!' He asked: 'What then is the remedy?' I said: 'For the delight of beholders and the expansion of the hearts of those present, I can compose a book entitled *The Gulistan* (The Rose Garden), upon whose pages the hand of the autumn wind shall have no tyranny, and the turning of the spheres shall never transform the joy of its spring into the desolation of autumn!'",
          "footnotes": [],
          "study": {
            "notes_en": "The genesis of the *Gulistan*: Saadi contrasts natural roses—which wither in five days—with literary roses, which bloom eternally. The four herbs gathered by his friend (gul, rayhān, sunbul, damīrān) represent transient sensory pleasure, while the book offers perennial moral illumination.",
            "notes_ur": "کتابِ گلستان کے جنم کا تاریخی لمحہ! دوست باغ کے گل و ریحان چن کر دامن بھر رہا تھا، سعدی نے متوجہ کیا کہ باغ کے پھول چند گھڑیوں کے مہمان ہیں اور عقلمند ناپائیدار چیز سے دل نہیں لگاتے۔ پھر وہ ابدی تجویز پیش کی کہ میں ایک ایسی 'گلستاں' تصنیف کروں گا جس کے اوراق کو خزاں کی ہوا چھو بھی نہ سکے گی۔",
            "vocabulary": [
              {
                "persian": "ضَمِیْرَان",
                "grammar": "اسم",
                "meaning_en": "sweet basil, wild marjoram",
                "meaning_ur": "ایک خوشبودار بوٹی (نازبو/نافرمان)",
                "urdu_cognates": "ضمیران"
              },
              {
                "persian": "دَسْتِ تَطَاوُل",
                "grammar": "مرکب اضافی",
                "meaning_en": "hand of tyranny / encroachment",
                "meaning_ur": "دست درازی، ظلم کا ہاتھ",
                "urdu_cognates": "تطاول"
              },
              {
                "persian": "طَیْشِ خَرِیْف",
                "grammar": "مرکب اضافی",
                "meaning_en": "the unpleasantness / harshness of autumn",
                "meaning_ur": "خزاں کی ناگواری و اکھاڑ پچھاڑ",
                "urdu_cognates": "طیش، خریف"
              }
            ]
          }
        },
        {
          "id": "entry_p20_01",
          "book_page": 18,
          "pdf_page": 20,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "بَہ چَہ کَارْ آیَدَتْ زِ گُلْ طَبَقِے",
              "persian_m2": "اَزْ گُلِسْتَانِ مَنْ بِبَر وَرَقِے",
              "urdu_m1": "پھولوں کا طبق تیرے کہیں کام آئے گا",
              "urdu_m2": "میری گلستاں کا ایک ورق لے جا"
            },
            {
              "persian_m1": "گُلْ ہَمِیْں پَنْجْرُوْز وَ شَشْ بَاشَدْ",
              "persian_m2": "وِیْں گُلِسْتَاں ہَمِیْشَہ خُوْشْ بَاشَدْ",
              "urdu_m1": "پھول یہی پانچ چھ روز رہے گا",
              "urdu_m2": "اور یہ گلستاں ہمیشہ تازہ رہے گی"
            }
          ],
          "english_trans": "Of what use to thee will be a tray of perishable flowers? / Take rather a single leaf from my *Gulistan*! / A rose endures but five or six fleeting days, / But this *Rose Garden* shall remain fresh and delightful forever!",
          "footnotes": [],
          "study": {
            "notes_en": "The immortal signature couplet of the *Gulistan*, carved in the collective memory of world literature. A real rose withers in a week, but Saadi's prose and verse have remained fresh for over 750 years.",
            "notes_ur": "گلستانِ سعدی کا سب سے مشہور اور تاریخی شعر۔ ظاہری پھول تو پانچ چھ دن میں مرجھا جاتا ہے مگر سعدی کی گلستان ہمیشہ تر و تازہ اور شاداب رہے گی۔ آج ساڑھے سات سو سال بعد بھی اس پیشگوئی کی صداقت قائم ہے۔",
            "vocabulary": [
              {
                "persian": "طَبَق",
                "grammar": "اسم (عربی)",
                "meaning_en": "tray, platter, dish",
                "meaning_ur": "تھال، بڑا برتن",
                "urdu_cognates": "طبق"
              },
              {
                "persian": "وَرَق",
                "grammar": "اسم (عربی)",
                "meaning_en": "leaf (of a book or plant), page",
                "meaning_ur": "کتاب کا ورق، پتا",
                "urdu_cognates": "ورق، اوراق"
              }
            ]
          }
        },
        {
          "id": "entry_p20_02",
          "book_page": 18,
          "pdf_page": 20,
          "type": "prose",
          "persian": "حَالِے کِہ مَنْ اِیْں حِکَایَتْ بَگُفْتَمْ دَامَنِ گُلْ بَرِیْخْت وَ دَرْ دَامَنَمْ آوِیْخْت کِہ : اَلْکَرِیْمُ اِذَا وَعَدَ وَفٰی ۔ فَصْلِے دُوْ ہَمَاں رُوْز اِتِّفَاقِ بَیَاضْ اُفْتَاد دَرْ حُسْنِ مُعَاشَرَتْ وَ آدَابِ مُحَاوَرَتْ دَرْ لِبَاسِے کِہ مُتَکَلِّمَاں رَا بَکَارْ آیَدْ وَ مُتَرَسِّلَاں رَا بَلَاغَتْ اَفْزَایَدْ ، فِی الْجُمْلَہ ہَنُوْز اَزْ گُلِسْتَاں بَقِیَّتِے مَانْدَہ بُوْد کِہ کِتَابِ گُلِسْتَاں تَمَامْ شُد ، وَ اللہُ اَعْلَمُ وَ اَحْکَمُ بِالصَّوَابِ ۔",
          "urdu_interlinear": "جیسے ہی میں نے یہ بات کہی اُس نے پھولوں کا دامن چھوڑ دیا اور میرے دامن سے چمٹ گیا کہ شریف جب وعدہ کرتا ہے تو پورا کرتا ہے دو فصل اسی روز لکھنے کا موقع مل گیا میل جول کی خوبی اور بات چیت کرنے کے آداب کے بیان میں ایسی عبارت میں کہ بولنے والوں کے کام آئے اور خط و کتابت کرنے والوں کی بلاغت بڑھائے خلاصہ یہ کہ ابھی کچھ موسمِ بہار باقی تھا کہ کتابِ گلستاں پوری ہو گئی خدا درست بات کا سب سے زیادہ جاننے والا اور فیصلہ کرنیوالا ہے ۔",
          "english_trans": "The instant I uttered these words, he cast away the flowers from his skirt and clung to my robe, exclaiming: 'When the generous man promises, he fulfills!' That very day, the drafting of two chapters came to pass—on the excellence of social fellowship and the etiquette of conversation—in a garb suited to benefit speakers and enhance the eloquence of letter-writers. In short, while there yet remained something of the spring season, the book *The Gulistan* was brought to completion; and God is the most knowing and the supreme judge of what is right!",
          "footnotes": [],
          "study": {
            "notes_en": "'Biyād' (fair-copy / manuscript drafting). Saadi completes the entire masterpiece during the remaining weeks of that very spring season in 1258 CE.",
            "notes_ur": "'اتفاقِ بیاض افتاد': یعنی صاف خط میں مسودہ تیار ہو گیا۔ دوست نے فورا پھول پھینک دیے اور سعدی سے وعدہ وفا کرنے کی التجا کی۔ اسی روز دو ابواب کا خاکہ تیار ہوا اور موسمِ بہار ختم ہونے سے پہلے پوری گلستان مکمل ہو گئی۔",
            "vocabulary": [
              {
                "persian": "بَیَاض",
                "grammar": "اسم (عربی)",
                "meaning_en": "fair copy, notebook, draft",
                "meaning_ur": "صاف کاپی، مسودہ، بیاض",
                "urdu_cognates": "بیاض"
              },
              {
                "persian": "مُتَرَسِّلَان",
                "grammar": "اسمِ فاعل جمع (عربی)",
                "meaning_en": "epistolary writers, scribes, correspondents",
                "meaning_ur": "انشا پرداز، خط و کتابت کرنے والے",
                "urdu_cognates": "ترسل، رسائل"
              }
            ]
          }
        }
      ]
    },
    {
      "section_id": "madah_shahzada_saad",
      "title_ur": "ذِکْرِ پَادْشَاہْ زَادَۂ جَہَاں سَعْدِ بْنِ اَبِیْ بَکْرِ بْنِ سَعْدٍ نَوَّرَ اللہُ قَبْرَہُ",
      "title_en": "Dedication to the Prince of the World, Sa'd ibn Abi Bakr ibn Sa'd",
      "pdf_page": 20,
      "book_page": 18,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p20_03",
          "book_page": 18,
          "pdf_page": 20,
          "type": "prose",
          "persian": "وَ تَمَامْ آنْگِہ شَوَدْ بِحَقِیْقَتْ کِہ پَسَنْدِیْدَہ آیَدْ دَرْ بَارْگَاہِ جَہَاں پَنَاہْ ، سَایَۂ کِرْدْگَار ، پَرْتَوِ لُطْفِ پَرْوَرْدْگَار ، وَ ذُخْرِ زَمَاں ، وَ کَہْفِ اَمَانْ ، اَلْمُؤَیَّدُ مِنَ السَّمَاءِ ، اَلْمُظَفَّرُ عَلَی الْاَعْدَاءِ ، عَضُدُ الدَّوْلَةِ الْقَاھِرَةِ ، سِرَاجُ الْاُمَّةِ الْبَاھِرَةِ ، جَمَالُ الْاَنَامِ ، مَفْخَرُ الْاِسْلَامِ ، سَعْدُ ابْنُ الْاَتَابَکِ الْاَعْظَمِ شَہَنْشَاہِ مُعَظَّمْ ، مَوْلٰی مُلُوْکِ الْعَرَبِ وَ الْعَجَمِ ، سُلْطَانِ بَرِّ وَ بَحْر ، وَارِثِ مُلْکِ سُلَیْمَانْ ، اَتَابَکِ اَعْظَمْ ، مُظَفَّرُ الدُّنْیَا وَ الدِّیْنِ اَبُوْ بَکْرِ بْنِ سَعْدِ زَنْگِیْ ادام اللہ ایامہما ...",
          "urdu_interlinear": "اور یہ گلستاں حقیقتاً مکمل تو جب ہی ہوگی جب جہاں پناہ کے دربار میں پسند آ جائے جو خدا کا سایہ ہے خدا کی مہربانی کا عکس ہے زمانہ کا ذخیرہ ہے اَمن کی پناہ ہے جس کو آسمانی تائید حاصل ہے دشمنوں پر فتح مند ہے قاہر حکومت کا بازو ہے روشن امت کا چراغ ہے مخلوق کی زینت ہے اسلام کا فخر ہے اتابک اعظم کا بیٹا سعد ہے جو بڑا شہنشاہ ہے عرب اور عجم کے بادشاہوں کا سردار ہے خشکی اور تری کا بادشاہ ہے حضرت سلیمانؑ کے ملک کا وارث ہے اتابک اعظم دین اور دنیا کا فتح مند ابوبکر بن سعد زنگی خدا ان دونوں کے دنوں کو دراز کرے ...",
          "english_trans": "And it shall truly achieve completion only when it finds gracious acceptance in the court of the Refuge of the World—the Shadow of the Creator, the Radiance of the Sustainer's grace, the Treasure of the Age, the Haven of Peace, Supported by Heaven, Victorious over enemies, Arm of the Mighty Realm, Lamp of the Splendid Nation, Adornment of Mankind, Pride of Islam: Prince Sa'd, son of the Supreme Atabeg, the august King of Kings, Master of the monarchs of Arab and Persian lands, Sovereign of land and sea, Heir to the Kingdom of Solomon, the Greatest Atabeg, Champion of the World and the Faith, Abu Bakr ibn Sa'd ibn Zangi—may Allah prolong their days!",
          "footnotes": [],
          "study": {
            "notes_en": "Dedication to Prince Sa'd (after whom Sheikh Saadi took his pen name 'Saadi'). Prince Sa'd was the cultured heir apparent who tragically predeceased his father in 1260 CE.",
            "notes_ur": "شہزادہ سعد بن ابوبکر بن سعد زنگی کے نام انتساب۔ اسی شہزادے کی نسبت سے شیخ شرف الدین نے اپنا تخلص 'سعدی' اختیار کیا تھا۔ شاہی دربار کے لیے کلاسیکی القابات کا پرشکوہ عربی و فارسی مرقع۔",
            "vocabulary": [
              {
                "persian": "کَہْفِ اَمَان",
                "grammar": "مرکب اضافی (عربی)",
                "meaning_en": "cave of safety, haven of sanctuary",
                "meaning_ur": "امن کی پناہ گاہ، امن کی غار",
                "urdu_cognates": "کہف (اصحابِ کہف)، امان"
              },
              {
                "persian": "ذُخْرِ زَمَاں",
                "grammar": "مرکب اضافی (عربی)",
                "meaning_en": "treasure / reserve of the age",
                "meaning_ur": "زمانہ کا قیمتی سرمایہ و ذخیرہ",
                "urdu_cognates": "ذخیرہ، ذخر"
              }
            ]
          }
        }
      ]
    }
  ]
}

out_file = "data/batch_02_pages_011_020.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(batch_02, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {out_file} with {len(batch_02['sections'])} sections.")
