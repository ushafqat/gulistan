import json
import os

batch_04 = {
  "batch_info": {
    "batch_id": 4,
    "pages_pdf": [31, 40],
    "pages_book": [29, 38],
    "title_ur": "باب اول: در سیرتِ پادشاہاں — حکایات ۳ تا ۷ (صفحات ۲۹ تا ۳۸)",
    "title_en": "Chapter 1: On the Manners of Kings — Stories 3 to 7 (Pages 29 to 38)"
  },
  "sections": [
    {
      "section_id": "bab1_hikayat_03_conclusion",
      "title_ur": "باب اول: تکملہ حکایت ۳ — حسدِ برادران اور دس درویش بمقابلہ دو بادشاہ",
      "title_en": "Chapter 1: Conclusion of Story 3 — Sibling Envy & The Proverb of Kings and Dervishes",
      "pdf_page": 31,
      "book_page": 29,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p29_01",
          "book_page": 29,
          "pdf_page": 31,
          "type": "prose",
          "persian": "بَرَادَرَانَشْ حَسَدْ بُرْدَنْدْ، وَ زَہْر دَرْ طَعَامَشْ کَرْدَنْدْ، خَواہَرَشْ اَزْ غُرْفَہ بِدِیْدْ، وَ دَرِیْچَہ بَرْ ہَمْ زَدْ، پِسَر بَفِرَاسَتْ دَرْ یَافْتْ، دَسْتْ اَزْ طَعَامْ بَازْ کَشِیْدْ وَ گُفْت: مَحَالَسْتْ کَہ ہُنَرْمَنْدَاں بِمِیْرَنْدْ، وَ بﮯ ہُنَرَاں جَائے اِیْشَاں گِیْرَنْد۔ شِعْر:",
          "urdu_interlinear": "اُس کے بھائیوں نے حسد کیا اور اُس کے کھانے میں زہر ملا دیا۔ اُس کی بہن نے کھڑکی سے دیکھ لیا اور کھڑکی بجا دی۔ شہزادہ ذہانت سے سمجھ گیا کھانے سے ہاتھ کھینچ لیا اور کہنے لگا کہ یہ تو ناممکن بات ہے کہ ہنرمند مر جائیں اور بے ہنر ان کی جگہ سنبھال لیں۔",
          "english_trans": "His brothers became envious and mixed poison in his food. His sister saw this from a lattice window and rattled the shutter. The prince, understanding through intuition, withdrew his hand from the food and said: 'It is impossible that the talented should perish and the talentless take their place!'",
          "footnotes": [],
          "study": {
            "notes_en": "The motif of sibling jealousy echoes the Joseph story. The sister's subtle warning via the shutter (*darīchah bar ham zad*) saves the prince's life.",
            "notes_ur": "بھائیوں نے حسد کی آگ میں زہر دیا مگر بہن کی ہوشیاری اور شہزادے کی فراست نے جان بچائی۔ سعدی کا مقولہ ہے کہ باہنر کو مٹایا نہیں جا سکتا۔",
            "vocabulary": [
              {
                "persian": "غُرْفَہ",
                "grammar": "اسم (عربی)",
                "meaning_en": "upper chamber, lattice window, balcony",
                "meaning_ur": "بالاخانہ، جھروکا، کھڑکی",
                "urdu_cognates": "غرفہ"
              },
              {
                "persian": "دَرِیْچَہ",
                "grammar": "اسم مصغر",
                "meaning_en": "small window, shutter",
                "meaning_ur": "چھوٹی کھڑکی، دریچہ",
                "urdu_cognates": "دریچہ"
              }
            ]
          }
        },
        {
          "id": "entry_p29_02",
          "book_page": 29,
          "pdf_page": 31,
          "type": "couplet",
          "header_persian": "شِعْر",
          "header_urdu": "شعر",
          "persian_m1": "کَسْ نَیَایَدْ بَہ زِیْرِ سَایَۂ بُوْمْ",
          "persian_m2": "وَر ہُمَا اَزْ جَہَاں شَوَدْ مَعْدُوْمْ",
          "urdu_m1": "الو کے سایہ میں کوئی آنا پسند نہ کرے",
          "urdu_m2": "اگرچہ ہما دنیا سے ناپید ہو جائے",
          "english_trans": "No one will seek shelter beneath the shadow of an owl, / Even though the royal Homa should vanish entirely from the world!",
          "footnotes": [],
          "study": {
            "notes_en": "The Huma (auspicious bird of royal fortune) is contrasted with the owl (*būm*, omen of ruin). Inherent baseness can never substitute for innate nobility.",
            "notes_ur": "'ہما' سعد اور مبارک پرندہ مانا جاتا ہے جس کے سائے سے بادشاہی ملتی ہے، جبکہ 'بوم' (الو) نحوست اور ویرانی کی علامت ہے۔ اگر ہما نہ بھی رہے تب بھی کوئی الو کا سایہ قبول نہیں کرتا۔",
            "vocabulary": [
              {
                "persian": "بُوْم",
                "grammar": "اسم",
                "meaning_en": "owl",
                "meaning_ur": "الو",
                "urdu_cognates": "بوم"
              },
              {
                "persian": "ہُمَا",
                "grammar": "اسمِ علم",
                "meaning_en": "Huma (mythical bird of fortune)",
                "meaning_ur": "ہما (مبارک پرندہ)",
                "urdu_cognates": "ہما، ہمایوں"
              }
            ]
          }
        },
        {
          "id": "entry_p29_03",
          "book_page": 29,
          "pdf_page": 31,
          "type": "prose",
          "persian": "پِدَرْ رَا اَزِیْں حَالْ آگَہِیْ دَادَنْدْ، بَرَادَرَانَشْ رَا بِخْوَانْدْ وَ گُوْشْمَالِ بَوَاجِبْ دَادْ، پَسْ ہَرْ یَکِے رَا اَزْ اَطْرَافِ بِلَادْ حِصَّۂ مَرْضِیْ مُعَیَّنْ کَرْد، تَا فِتْنَہ فَرُوْ نِشَسْتْ، وَ نِزَاعْ بَرْخَاسْتْ، کَہ: دَہْ دَرْوِیْش دَرْ گِلِیْمِے بِخُسْبَنْدْ، وَ دُوْ پَادْشَاہ دَرْ اِقْلِیْمِے نَگُنْجَنْدْ۔ قِطْعَہ:",
          "urdu_interlinear": "لوگوں نے باپ کو یہ قصہ بتایا اُس کے بھائیوں کو بلایا اور مناسب سزا دی پھر ملک کے اطراف میں سے ہر ایک کیلئے اُس کی پسند کے مطابق ایک حصہ مقرر کر دیا چنانچہ فتنہ ختم ہوا اور جھگڑا جاتا رہا کیونکہ دس فقیر ایک کمبلی میں سو جاتے ہیں اور دو بادشاہ ایک ولایت میں نہیں سماتے۔",
          "english_trans": "They informed the father of this affair. He summoned the brothers and administered suitable chastisement. Then to each of them he assigned a satisfactory portion from the border provinces of the realm, so that strife subsided and dispute ceased; for: 'Ten dervishes can sleep beneath a single blanket, but two kings cannot be contained within an entire kingdom!'",
          "footnotes": [],
          "study": {
            "notes_en": "'Dah darwēsh dar gilīmē bikhusband, va dō pādshāh dar iqlīmē nagunjand': one of the most famous sociopolitical aphorisms of Saadi, contrasting the contentment of spiritual poverty with the insatiable ambition of worldly monarchs.",
            "notes_ur": "سعدی کا لازوال ضرب المثل قول ہے کہ دس فقیر تو ایک کمبل میں رات گزار لیتے ہیں لیکن دو بادشاہ پوری سلطنت میں بھی ایک دوسرے کو برداشت نہیں کر سکتے۔",
            "vocabulary": [
              {
                "persian": "گُوْشْمَال",
                "grammar": "اسمِ مرکب",
                "meaning_en": "chastisement, ear-twisting, reprimand",
                "meaning_ur": "سزا، تنبیہ، کان کھینچنا",
                "urdu_cognates": "گوشمالی"
              },
              {
                "persian": "گِلِیْم",
                "grammar": "اسم",
                "meaning_en": "blanket, rough wool rug",
                "meaning_ur": "کمبلی، لوئی",
                "urdu_cognates": "گلیم، گلیم بخت"
              }
            ]
          }
        },
        {
          "id": "entry_p29_04",
          "book_page": 29,
          "pdf_page": 31,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "نِیْمْ نَانے گَرْ خُوْرَدْ مَرْدِ خُدَائے",
              "persian_m2": "بَذْلِ دَرْوِیْشَاں کُنَدْ نِیْمِے دِگَرْ",
              "urdu_m1": "مردِ خدا اگر آدھی روٹی کھاتا ہے",
              "urdu_m2": "تو دوسری آدھی فقیروں پر خرچ کر دیتا ہے"
            },
            {
              "persian_m1": "مُلْکِ اِقْلِیْمِے بَگِیْرَدْ پَادْشَاہْ",
              "persian_m2": "ہَمْچُنَاں دَرْ بَنْدِ اِقْلِیْمِے دِگَرْ",
              "urdu_m1": "اگر بادشاہ ایک ولایت کی حکومت حاصل کر لیتا ہے",
              "urdu_m2": "تو اسی طرح دوسری ولایت کی فکر میں لگا رہتا ہے"
            }
          ],
          "english_trans": "If a man of God eats half a loaf of bread, / He bestows the other half upon dervishes! / But though a monarch conquers an entire continent, / He remains just as bent upon conquering yet another!",
          "footnotes": [],
          "study": {
            "notes_en": "The spiritual economy of generosity vs. the imperial thirst for ceaseless conquest. A dervish shares half his meager bread, while an emperor of seven climes remains spiritually impoverished by greed.",
            "notes_ur": "مردِ خدا آدھی روٹی بھی بانٹ کر کھاتا ہے جبکہ بادشاہ ایک ملک فتح کر کے دوسرے ملک کی ہوس میں مبتلا رہتا ہے۔ قناعت ہی حقیقی امیری ہے۔",
            "vocabulary": [
              {
                "persian": "بَذْل",
                "grammar": "مصدر (عربی)",
                "meaning_en": "bestowing, munificence, sharing",
                "meaning_ur": "عطا کرنا، بخشش، خیرات",
                "urdu_cognates": "بذل و بخشش"
              },
              {
                "persian": "اِقْلِیْم",
                "grammar": "اسم (یونانی/عربی)",
                "meaning_en": "clime, realm, continent",
                "meaning_ur": "ملک، ولایت، خطہ",
                "urdu_cognates": "اقلیم، ہفت اقلیم"
              }
            ]
          }
        }
      ]
    },
    {
      "section_id": "bab1_hikayat_04",
      "title_ur": "باب اول: حکایت ۴ — پہاڑی قزاق، قیدی لڑکا اور 'عاقبت گرگ زادہ گرگ شود'",
      "title_en": "Chapter 1: Story 4 — The Mountain Robbers & 'A Wolf's Cub Becomes a Wolf'",
      "pdf_page": 31,
      "book_page": 29,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p29_05",
          "book_page": 29,
          "pdf_page": 31,
          "type": "prose",
          "header_persian": "حِکَایَت ۴",
          "header_urdu": "حکایت ۴",
          "persian": "طَائِفَۂ دُزْدَانِ عَرَبْ بَرْ سَرِ کُوْہے نِشَسْتَہ بُوْدَنْدْ، وَ مَنْفَذِ کَارْوَاں بَسْتَہ، وَ رَعِیَّتِ بِلْدَاں اَزْ مَکَائِدِ اِیْشَاں مَرْعُوْبْ، وَ لَشْکَرِ سُلْطَانْ مَغْلُوْبْ، بِحُکْمِ آنْکَہ مَلَاذِ مَنِیْع اَزْ قُلَّۂ کُوْہے گِرِفْتَہ بُوْدَنْدْ، وَ مَأْمَن وَ مَلْجَائے خُوْد کَرْدَہ، مُدَبِّرَانِ مَمَالِکِ آنْ طَرَفْ دَرْ دَفْعِ مَضَرَّتِ اِیْشَاں مُشَاوَرَتْ کَرْدَنْدْ، کَہ: اَگَرْ اِیْں طَائِفَہ...",
          "urdu_interlinear": "عرب کے چوروں کا ایک گروہ ایک پہاڑ کی چوٹی پر قبضہ جمائے بیٹھا تھا اور قافلہ کا راستہ بند کر دیا تھا اور شہروں کی رعایا اُس کے مکر و فریب سے ڈرتی تھی اور بادشاہ کا لشکر عاجز تھا چونکہ اُس نے ایک پہاڑ کی چوٹی پر محفوظ جائے پناہ بنا لی تھی اور اُس کو اپنا ٹھکانا اور پناہ گاہ بنا لیا تھا اُن اطراف کے شہروں کے عقلمندوں نے اُس کی نقصان رسانی کے رفع کرنے کا مشورہ کیا کہ اگر یہ گروہ...",
          "english_trans": "A band of Arab robbers had established themselves upon the summit of a mountain, blocking the passage of caravans. The inhabitants of the countryside were terrified of their stratagems, and the Sultan's troops were baffled, because the bandits had secured an impregnable refuge upon the mountain crest, making it their stronghold and asylum. The governors of those realms held counsel to avert their menace, saying: 'If this band...'",
          "footnotes": [],
          "study": {
            "notes_en": "Hikayat 4 is one of the most celebrated philosophical explorations of Nature versus Nurture in world literature: whether innate disposition (*tiynat*) can be transformed by education (*tarbiyat*).",
            "notes_ur": "حکایت ۴ سعدی کی سب سے زیادہ پڑھی جانے والی حکایتوں میں سے ہے جس میں انسانی جبلت اور تربیت کے اثرات پر گہری اخلاقی بحث کی گئی ہے۔",
            "vocabulary": [
              {
                "persian": "مَنْفَذ",
                "grammar": "اسمِ ظرف (عربی)",
                "meaning_en": "pass, corridor, outlet",
                "meaning_ur": "راستہ، گزرگاہ",
                "urdu_cognates": "منفذ"
              },
              {
                "persian": "مَلَاذِ مَنِیْع",
                "grammar": "ترکیبِ توصیفی (عربی)",
                "meaning_en": "impregnable refuge, fortified asylum",
                "meaning_ur": "محفوظ پناہ گاہ، ناقابلِ تسخیر قلعہ",
                "urdu_cognates": "ملاذ، منیع"
              }
            ]
          }
        },
        {
          "id": "entry_p30_01",
          "book_page": 30,
          "pdf_page": 32,
          "type": "prose",
          "persian": "بَرِیْں نَسَقْ رُوْزْگَارے مُدَاوَمَتْ نَمَایَنْدْ، مُقَاوَمَتْ مُمْتَنِعْ گَرْدَدْ۔ مَثْنَوِیْ:",
          "urdu_interlinear": "اسی طور پر چند دن جما رہے گا تو پھر مقابلہ ناممکن ہو جائے گا۔",
          "english_trans": "'...continues in this manner for any length of time, resistance to them will become impossible!'",
          "footnotes": [],
          "study": {
            "notes_en": "Prudential governance: nip dangerous rebellions in the bud before they grow unmanageable.",
            "notes_ur": "برائی کو اس کے آغاز ہی میں ختم کر دینا چاہیے ورنہ وقت گزرنے کے ساتھ وہ ناقابلِ تسخیر بن جاتی ہے۔",
            "vocabulary": [
              {
                "persian": "مُدَاوَمَت",
                "grammar": "مصدر (عربی)",
                "meaning_en": "perseverance, continuation",
                "meaning_ur": "دوام، ہمیشگی، جمے رہنا",
                "urdu_cognates": "مداومت"
              }
            ]
          }
        },
        {
          "id": "entry_p30_02",
          "book_page": 30,
          "pdf_page": 32,
          "type": "stanza",
          "header_persian": "مَثْنَوِیْ",
          "header_urdu": "مثنوی",
          "lines": [
            {
              "persian_m1": "دَرَخْتے کَہ اَکْنُوْں گِرِفْتَسْتْ پَائے",
              "persian_m2": "بَہ نِیْرُوْئے شَخْصے بَرْ آیَدْ زِ جَائے",
              "urdu_m1": "جس درخت نے کہ ابھی جڑ پکڑی ہے",
              "urdu_m2": "ایک آدمی کی طاقت سے اکھڑ جائیگا"
            },
            {
              "persian_m1": "وَ گَرْ ہَمْچُنَاں رُوْزْگَارے ہِلِیْ",
              "persian_m2": "بَگَرْدُوْنَشْ اَزْ بِیْخْ بَرْ نَگْسَلِیْ",
              "urdu_m1": "اور اگر تو اسی طرح اُس کو ایک زمانہ تک چھوڑ دے گا",
              "urdu_m2": "تو گردوں کے ذریعہ بھی اس کو جڑ سے نہیں اکھاڑ سکتا"
            },
            {
              "persian_m1": "سَرِ چَشْمَہ شَایَدْ گِرِفْتَنْ بَہ مِیْلْ",
              "persian_m2": "چُو پُرْ شُدْ نَشَایَدْ گُذَشْتَنْ بَہ پِیْلْ",
              "urdu_m1": "چشمہ کا سوراخ ایک سلائی سے بند کیا جا سکتا ہے",
              "urdu_m2": "جب وہ بھر جائے تو ہاتھی کے ذریعہ بھی اس کو عبور نہیں کیا جا سکتا"
            }
          ],
          "english_trans": "A sapling that has only recently taken root / May be uprooted by the strength of a single man; / But if thou leavest it thus for a season, / Thou canst not tear it up with a windlass! / The head of a spring may be blocked with a slender needle; / Yet when it swells to a flood, it cannot be crossed even upon an elephant!",
          "footnotes": [
            "گردوں گاڑی کے معنی میں لایا گیا ہے۔ یہ لفظ چرخی کے معنی میں بھی آتا ہے۔ ۱۲"
          ],
          "study": {
            "notes_en": "'Sar-e chashmah shāyad giriftan ba mīl / Chū pur shud nashāyad guzashtan ba pīl': iconic Persian proverbs on preemptive action. A trickle can be plugged with a pin; a torrent stops even an elephant.",
            "notes_ur": "سعدی کے مشہور ترین اشعار میں سے ہیں کہ چشمے کا دہانہ سلائی سے روکا جا سکتا ہے لیکن جب وہ دریا بن جائے تو ہاتھی بھی پار نہیں کر سکتا۔ برائی کو آغاز میں روکنا آسان ہوتا ہے۔",
            "vocabulary": [
              {
                "persian": "مِیْل",
                "grammar": "اسم",
                "meaning_en": "needle, slender bodkin, stylus",
                "meaning_ur": "سلائی، باریک کیل",
                "urdu_cognates": "سرمے کی سلائی"
              },
              {
                "persian": "بِیْخ",
                "grammar": "اسم",
                "meaning_en": "root, foundation",
                "meaning_ur": "جڑ، بنیاد",
                "urdu_cognates": "بیخ کنی"
              }
            ]
          }
        },
        {
          "id": "entry_p30_03",
          "book_page": 30,
          "pdf_page": 32,
          "type": "prose",
          "persian": "سُخَنْ بَرِیْں مُقَرَّرْ شُدْ کَہ یَکِے رَا بَہ جُسْتَنِ اِیْشَاں بَرْ گُمَاشْتَنْدْ، وَ فُرْصَتْ نِگَاہ مِیْ دَاشْتَنْدْ، تَا وَقْتِیْکَہ بَرْ سَرِ قَوْمے رَانْدَہ بُوْدَنْدْ، وَ مَقَامْ خَالِیْ مَانْدَہ، تَنے چَنْد مَرْدَانِ وَاقِعَہ دِیْدَہ وَ جَنْگْ آزمُوْدَہ رَا بِفِرِسْتَادَنْدْ، تَا دَرْ شِعْبِ جَبَلْ پِنْہَاں شُدَنْدْ، شَبَانْگَاہِے کَہ دُزْدَاں بَازْ آمَدَنْدْ سَفَرْ کَرْدَہ وَ غَارَتْ آوَرْدَہ، سِلَاحْ اَزْ تَنْ بِکُشَادَنْدْ، وَ رَخْتِ غَنِیْمَتْ بِنَہَادَنْدْ، نُخُسْتِیْنْ دُشْمَنے کَہ بَرْ سَرِ اِیْشَاں تَاخْتْ آوَرْدْ خَوَابْ بُوْد، چُنْدَانْکَہ پَاسے اَزْ شَبْ بَگُذَشْتْ۔ شِعْر:",
          "urdu_interlinear": "یہ فیصلہ ہوا کہ ایک شخص کو اُن کی سراغ رسانی پر مقرر کر دیا اور موقع کے متلاشی رہے جس وقت وہ ایک قوم پر چڑھائی کرنے گیا ہوا تھا اور قیام گاہ خالی تھی چند آدمی جو تجربہ کار اور جنگ آزمودہ کو روانہ کر دیا چنانچہ وہ پہاڑ کی گھاٹیوں میں چھپ گئے۔ رات کے وقت جب چور واپس آئے سفر کئے ہوئے اور لوٹ کا مال لئے ہوئے تو انہوں نے بدن سے ہتھیار کھول دیئے اور لوٹ کا مال ایک طرف رکھ دیا سب سے پہلا دشمن جو اُن پر حملہ آور ہوا نیند تھی یہاں تک کہ شب کا ایک حصہ گذر گیا۔",
          "english_trans": "It was resolved to dispatch a spy to track their movements, watching for an opportunity. When the robbers had marched out against a tribe and their lair stood empty, they sent several seasoned, battle-hardened warriors who concealed themselves in the mountain defiles. At nightfall, when the robbers returned weary from their expedition laden with plunder, they stripped off their armor and laid down their booty. The first enemy that assaulted them was sleep; and when a watch of the night had passed...",
          "footnotes": [],
          "study": {
            "notes_en": "Tactical ambush: the robbers let down their guard after plundering. Saadi poetically personifies slumber (*khwāb*) as the robbers' first and deadliest enemy.",
            "notes_ur": "جنگی حکمتِ عملی کی دلکش تصویر کشی کہ لوٹ مار سے تھکے ہوئے ڈاکو جب سو گئے تو نیند ان کا پہلا دشمن بن کر ان پر حاوی ہو گئی۔",
            "vocabulary": [
              {
                "persian": "شِعْبِ جَبَل",
                "grammar": "ترکیبِ اضافی (عربی)",
                "meaning_en": "mountain cleft, ravine, defile",
                "meaning_ur": "پہاڑ کا درہ، گھاٹی",
                "urdu_cognates": "شعبِ ابی طالب"
              },
              {
                "persian": "پَاس",
                "grammar": "اسم",
                "meaning_en": "a watch of the night (approx. 3 hours)",
                "meaning_ur": "پہر، رات کا حصہ",
                "urdu_cognates": "پاس، پہر"
              }
            ]
          }
        },
        {
          "id": "entry_p30_04",
          "book_page": 30,
          "pdf_page": 32,
          "type": "couplet",
          "header_persian": "شِعْر",
          "header_urdu": "شعر",
          "persian_m1": "قُرْصِ خُوْرْشِیْد دَرْ سِیَاہِیْ شُدْ",
          "persian_m2": "یُوْنُسْ اَنْدَرْ دَہَانِ مَاہِیْ شُدْ",
          "urdu_m1": "سورج کی ٹکلی سیاہی میں چلی گئی جیسا کہ",
          "urdu_m2": "حضرت یونس علیہ السلام مچھلی کے پیٹ میں چلے گئے",
          "english_trans": "The sun's golden disk sank deep into darkness, / Just as Prophet Jonah entered the mouth of the whale!",
          "footnotes": [
            "یونس علیہ السلام ایک پیغمبر تھے جو اس خوف سے کہ شاید میری قوم میری تکذیب کرے قوم کے درمیان سے نکل کر چلے گئے اور ایک کشتی میں سوار ہوئے تین روز کشتی میں چکر لگا ہے دفعتاً ایک بڑی مچھلی نے دریا میں سے سر نکالا اور کشتی کو روک لیا۔ ملاح نے کہا کہ اس کشتی میں کوئی گنہگار ہے جب تک اس کو ہم مچھلی کے حوالے نہ کر دیں گے کشتی نہ چلے گی اخیر قرعہ اندازی ہوئی قرعہ آپکے نام کا نکلا چنانچہ لوگوں نے آپ کو مچھلی کے سامنے ڈال دیا اور مچھلی (باقی صفحہ آئندہ)"
          ],
          "study": {
            "notes_en": "Astronomical metaphor of nightfall linked to the Quranic story of Prophet Yunus (Jonah) entering the whale's mouth.",
            "notes_ur": "غروبِ آفتاب اور رات کی گہری تاریکی کو حضرت یونسؑ کے مچھلی کے پیٹ میں جانے سے تشبیہ دی گئی ہے۔",
            "vocabulary": [
              {
                "persian": "قُرْص",
                "grammar": "اسم (عربی)",
                "meaning_en": "disk, orb (of the sun)",
                "meaning_ur": "ٹکلی، دائرہ، قرصِ آفتاب",
                "urdu_cognates": "قرص"
              },
              {
                "persian": "مَاہِی",
                "grammar": "اسم",
                "meaning_en": "fish, whale",
                "meaning_ur": "مچھلی",
                "urdu_cognates": "ماہی، ماہی گیر"
              }
            ]
          }
        },
        {
          "id": "entry_p31_01",
          "book_page": 31,
          "pdf_page": 33,
          "type": "prose",
          "persian": "مَرْدَانِ دِلَاوَرْ اَزْ کَمِیْنْ گَاہْ بَدَرْ جَسْتَنْدْ، وَ دَسْتِ یَکَاں یَکَاں بَرْ کَتِفْ بَسْتَنْدْ، بَامْدَادَاں بَدَرْگَاہِ مَلِکْ حَاضِرْ آوَرْدَنْدْ، ہَمَہ رَا بَہ کُشْتَنْ فَرْمُوْد، اِتِّفَاقاً دَر آں مِیَاں جَوَانے بُوْدْ کَہ مِیْوَۂ عُنْفُوَانِ شَبَابَشْ نَوْ رَسِیْدَہ، وَ سَبْزَۂ گُلِسْتَانِ عِذَارَشْ نَوْ دَمِیْدَہ، یَکِے اَزْ وُزَرَاں پَائے تَخْتِ مَلِکْ رَا بَبُوْسِیْدْ، وَ رُوْئے شَفَاعَتْ بَرْ زَمِیْنْ نَہَادْ وَ گُفْت: اِیْں پِسَر ہَمْچُنَاں اَزْ بَاغِ زِنْدَگَانِیْ بَرْ نَخُوْرْدَہ اَسْتْ، وَ اَزْ رَیْعَانِ جَوَانِیْ تَمَتُّعْ نَیَافْتَہ، تَوَقُّعْ بَہ کَرَمْ وَ اَخْلَاقِ خُدَاوَنْدِیْ آنْسْتْ کَہ بَہ بَخْشِیْدَنِ خُوْنِ او بَرْ بَنْدَہ مِنَّتْ نَہِیْ۔ مَلِکْ رُوْے اَزِیْں سُخَنْ دَرْ ہَمْ آوَرْدْ، وَ مُوَافِقِ رَائے بُلَنْدَشْ نَیَامَدْ، وَ گُفْت:",
          "urdu_interlinear": "بہادر لوگ اپنے چھپاؤ کی جگہ سے باہر نکل آئے اور ایک ایک کے ہاتھ مونڈھوں سے باندھ دیئے صبح کو بادشاہ کے دربار میں حاضر کر دیا۔ سب کو مار ڈالنے کا حکم فرمایا اتفاقاً ان میں ایک نوجوان بھی تھا کہ اُس کی آغازِ جوانی کا میوہ تازہ تھا اور اس کے رخسار کے باغ کا سبزہ نیا نیا اگا تھا۔ ایک وزیر نے بادشاہ کے تخت کے پائے کو چوما اور سفارش کا چہرہ زمین پر رکھا اور کہا اس لڑکے نے ابھی زندگی کے باغ کا پھل بھی نہیں چکھا ہے اور جوانی کی ابتداء سے نفع نہیں اٹھایا ہے شاہی اخلاق و کرم سے توقع یہ ہے کہ اس کا خون معاف فرما کر اس خادم پر احسان فرمائیں گے بادشاہ کو اس بات سے غصہ آ گیا اور یہ بات اُس کی بلند رائے کے موافق نہ پڑی اور کہا",
          "english_trans": "The valiant warriors leaped from their ambush and bound the hands of each robber behind his back. At daybreak they presented them at the King's court; he commanded them all to be put to death. It chanced that among them was a youth, the fruit of the flower of whose youth was newly ripening, and the down upon the garden of his cheeks had newly sprouted. One of the ministers kissed the foot of the throne, laid his face of intercession upon the earth, and said: 'This boy hath not yet tasted of the garden of life, nor enjoyed the prime of his youth! It is hoped from royal clemency that by sparing his blood, Your Majesty will lay an obligation upon this servant.' The king frowned at these words, and it agreed not with his exalted judgment, and he said:",
          "footnotes": [
            "(بقیہ حاشیہ صفحہ گذشتہ) آپ کو نگل گئی اُس وقت آپ کو تین قسم کی تاریکیوں سے سابقہ ہوا۔ ۱۔ رات، ۲۔ دریا کی تاریکی، ۳۔ مچھلی کے پیٹ کی تاریکی، چالیس روز کے بعد مچھلی نے بحکمِ الٰہی آپ کو اُگل کر دریا کے کنارے پر ڈال دیا۔"
          ],
          "study": {
            "notes_en": "The lyrical description of youth: 'Mīwah-ye 'unfuwān-e shabābash naw rasīdah' (the fruit of his early youth newly ripened) and 'sabzah-ye gulistān-e 'idhārash naw damīdah' (the first down on the garden of his cheek).",
            "notes_ur": "سعدی نے نوجوان کے حسن اور ناتجربہ کاری کو نہایت خوبصورت تشبیہات میں بیان کیا ہے: نوخیز جوانی اور رخسار پر پہلی سبزی (خط کا آغاز)۔ وزیر نے اسی معصومیت پر رحم کھا کر سفارش کی۔",
            "vocabulary": [
              {
                "persian": "عُنْفُوَان",
                "grammar": "اسم (عربی)",
                "meaning_en": "prime, bloom, onset (of youth)",
                "meaning_ur": "آغاز، شباب کا ابتدائی زمانہ",
                "urdu_cognates": "عنفوانِ شباب"
              },
              {
                "persian": "عِذَار",
                "grammar": "اسم (عربی)",
                "meaning_en": "cheek, side of face",
                "meaning_ur": "رخسار، گال",
                "urdu_cognates": "عذار"
              }
            ]
          }
        },
        {
          "id": "entry_p31_02",
          "book_page": 31,
          "pdf_page": 33,
          "type": "couplet",
          "header_persian": "فَرْد",
          "header_urdu": "فرد",
          "persian_m1": "پَرْتَوِ نِیْکَاں نَہ گِیْرَدْ ہَرْ کَہ بُنْیَادَشْ بَدَسْتْ",
          "persian_m2": "تَرْبِیَتْ نَا اَہْلْ رَا چُوں گِرْدَگَاں بَرْ گُنْبَدَسْتْ",
          "urdu_m1": "جس کی بنیاد بری ہے وہ بھلوں کا سایہ بھی اپنے پر نہیں پڑنے دیتا",
          "urdu_m2": "نااہل کی تربیت کرنا ایسا ہے جیسا کہ گنبد پر اخروٹ",
          "english_trans": "The light of the virtuous affects not him whose foundation is corrupt: / To train the unworthy is like rolling walnuts upon a dome!",
          "footnotes": [],
          "study": {
            "notes_en": "'Girdakān bar gunbad' (walnuts upon a dome): an enduring Persian proverb for completely wasted effort that cannot stick.",
            "notes_ur": "'گردگاں بر گنبد' فارسی کی مشہور مثل ہے یعنی گنبد پر اخروٹ پھینکنا جو کبھی ٹھہرتا نہیں۔ نااہل اور بد اصل پر تربیت کا کوئی اثر قائم نہیں رہتا۔",
            "vocabulary": [
              {
                "persian": "گِرْدَگَان",
                "grammar": "اسم",
                "meaning_en": "walnut",
                "meaning_ur": "اخروٹ",
                "urdu_cognates": "گردگان"
              }
            ]
          }
        },
        {
          "id": "entry_p31_03",
          "book_page": 31,
          "pdf_page": 33,
          "type": "prose",
          "persian": "نَسْل وَ تَبَارِ اِیْنَانْ مُنْقَطِعْ کَرْدَن اَوْلَىٰ تَرَسْتْ، کَہ آتَشْ کُشْتَن وَ اَخْگَرْ گُذَاشْتَن، وَ اَفْعٰیْ کُشْتَن وَ بَچَّہ اَشْ نِگَاہ دَاشْتَن کَارِ خِرَدْمَنْدَاں نِیْسْتْ۔ قِطْعَہ:",
          "urdu_interlinear": "ان کی نسل و جڑ کو کاٹ ڈالنا ہی زیادہ بہتر ہے کیونکہ آگ کو بجھانا اور چنگاری چھوڑ دینا اور سانپ کو مارنا اور اس کے بچے کو حفاظت سے رکھنا عقلمندوں کا کام نہیں ہے۔",
          "english_trans": "'It is far better to cut off their race and stock; for to quench a fire while leaving a living ember, or to slay a viper while sparing its brood, is not the conduct of the wise!'",
          "footnotes": [],
          "study": {
            "notes_en": "The sovereign's ruthless realism: evil must be eradicated completely, for a single spared spark can reignite a conflagration.",
            "notes_ur": "بادشاہ کی دلیل ہے کہ چنگاری کو باقی چھوڑنا آگ بھڑکانے کے مترادف ہے اور سانپ کے بچے کو پالنا اپنی موت کو دعوت دینا ہے۔",
            "vocabulary": [
              {
                "persian": "اَخْگَر",
                "grammar": "اسم",
                "meaning_en": "spark, live ember",
                "meaning_ur": "چنگاری، دہکتا کوئلہ",
                "urdu_cognates": "اخگر"
              },
              {
                "persian": "اَفْعٰی",
                "grammar": "اسم (عربی)",
                "meaning_en": "viper, poisonous serpent",
                "meaning_ur": "زہریلا سانپ، افعی",
                "urdu_cognates": "افعی"
              }
            ]
          }
        },
        {
          "id": "entry_p31_04",
          "book_page": 31,
          "pdf_page": 33,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "اَبْر گَرْ آبِ زِنْدَگِیْ بَارَدْ",
              "persian_m2": "ہَرْگِزْ اَزْ شَاخِ بِیْد بَرْ نَخُوْرِیْ",
              "urdu_m1": "اگر بادل آبِ حیات برسائے",
              "urdu_m2": "تو بھی تو بید کی شاخ کا پھل نہیں کھائے گا"
            },
            {
              "persian_m1": "بَا فُرُوْ مَایَہ رُوْزْگَار مَبَرْ",
              "persian_m2": "کَزْ نَےِ بُوْرِیَا شَکَرْ نَخُوْرِیْ",
              "urdu_m1": "کمینے کے ساتھ وقت ضائع نہ کر",
              "urdu_m2": "کیونکہ بوریئے کے نل سے تو شکر نہیں کھائے گا !"
            }
          ],
          "english_trans": "Though the cloud should rain the Water of Life itself, / Never shalt thou gather fruit from the branch of a willow! / Waste not thy days in the company of the base-born: / For never shalt thou extract sugar from a common reed-mat!",
          "footnotes": [],
          "study": {
            "notes_en": "Nature limits potential: a willow (*bēd*) remains sterile even if irrigated by the Water of Life (*āb-e zindagī*), and common matting reeds (*nay-e būriyā*) can never produce sugar cane.",
            "notes_ur": "بید کا درخت پھل نہیں دیتا خواہ اسے آبِ حیات ہی کیوں نہ پلایا جائے۔ اسی طرح چٹائی کا بانس کبھی گنا نہیں بن سکتا جس سے شکر ملے۔ کم اصل انسان بھی اچھی صحبت سے جوہر نہیں بدل سکتا۔",
            "vocabulary": [
              {
                "persian": "بِیْد",
                "grammar": "اسم",
                "meaning_en": "willow tree (sterile of fruit)",
                "meaning_ur": "بید کا درخت",
                "urdu_cognates": "بیدِ مجنوں"
              },
              {
                "persian": "بُوْرِیَا",
                "grammar": "اسم",
                "meaning_en": "reed mat",
                "meaning_ur": "چٹائی، بوریا",
                "urdu_cognates": "بوریا نشین"
              }
            ]
          }
        },
        {
          "id": "entry_p32_01",
          "book_page": 32,
          "pdf_page": 34,
          "type": "prose",
          "persian": "وَزِیْر اِیْں سُخَنْ بِشْنِیْدْ، وَ طَوْعاً وَ کَرْہاً بَپَسَنْدِیْد، وَ بَرْ حُسْنِ رَائے مَلِکْ آفَرِیْنْ خَوَانْد، وَ گُفْت: آنْچِہ خُدَاوَنْد دَامَ مُلْکُہٗ فَرْمُوْد عَیْنِ صَوَابْسْتْ، وَ مَسْئَلَۂ بﮯ جَوَاب، کَہ اَگَرْ دَرْ صُحْبَتِ آں بَدَاں تَرْبِیَتْ یَافْتے، طِیْنَتِ اِیْشَاں گِرِفْتے، وَ یَکِے اَزْ اِیْشَاں شُدے، اَمَّا بَنْدَہ اُمِیْدْوَارَسْتْ کَہ بَہ صُحْبَتِ صَالِحَاں تَرْبِیَتْ پَذِیْرَدْ، وَ خُوْئے خِرَدْمَنْدَاں گِیْرَدْ، کَہ ہَنُوْزْ طِفْلَسْتْ، وَ سِیْرَتِ بَغْیْ وَ عِنَادِ آں قَوْم دَرْ نِہَادِ او تَمَکُّنْ نَشُدَہ، وَ دَرْ حَدِیْثْ سْت: کُلُّ مَوْلُوْدٍ یُّوْلَدُ عَلَى الْفِطْرَةِ، فَأَبَوَاہُ یُہَوِّدَانِہٖ اَوْ یُنَصِّرَانِہٖ اَوْ یُمَجِّسَانِہٖ۔ قِطْعَہ:",
          "urdu_interlinear": "وزیر نے یہ بات سنی اور چار و ناچار پسند کی اور بادشاہ کی رائے کی خوبی کی تعریف کی اور کہا جو کچھ بادشاہ دام ملکہ نے فرمایا بالکل صحیح ہے اور بات ناقابلِ انکار اس لئے کہ اگر اُن بُروں کی صحبت میں پلتا تو اُن کی فطرت اختیار کرتا اور ان میں ہی کا ایک ہوتا لیکن غلام کو امید ہے کہ نیکوں کی صحبت کا اثر قبول کرے گا اور عقلمندوں کی عادت اختیار کر لے گا اس لئے کہ ابھی بچہ ہے اور اُس قوم کی سرکشی اور دشمنی کی عادت نے اُس کی طبیعت میں جڑ نہیں پکڑی اور حدیث شریف میں آیا ہے ہر بچہ اسلام پر پیدا ہوتا ہے پھر اس کے ماں باپ اس کو یہودی یا نصرانی یا مجوسی بنا ڈالتے ہیں",
          "english_trans": "The minister heard this discourse and assented to it, willy-nilly, praising the excellence of the King's judgment, and saying: 'What my Lord — may his kingdom endure! — hath spoken is the very truth and an unanswerable premise: had he been reared in the company of those villains, he would have adopted their disposition and become one of them. But this servant hopes that in the fellowship of the righteous he will receive wholesome discipline and acquire the habits of the wise, for he is yet a child; the rebellious and perverse nature of that band hath not yet taken firm root in his temperament. And in the sacred Hadith it is related: \"Every newborn child is born upon the pure primordial nature (fitrah); then his parents turn him into a Jew, a Christian, or a Magian!\"'",
          "footnotes": [],
          "study": {
            "notes_en": "The minister marshals the famous Prophetic Hadith of *Fitrah* (innate primordial purity) to argue that the youth's environment can reshape him before wicked habits calcify.",
            "notes_ur": "وزیر نے حدیثِ نبوی 'کُلُّ مَوْلُوْدٍ یُّوْلَدُ عَلَى الْفِطْرَةِ' پیش کی کہ ہر بچہ فطرتاً پاکیزہ پیدا ہوتا ہے، برے اثرات بعد میں پڑتے ہیں۔ ابھی اس کی عمر کم ہے اور نیک صحبت اس کی تقدیر بدل سکتی ہے۔",
            "vocabulary": [
              {
                "persian": "طَوْعاً وَ کَرْہاً",
                "grammar": "مرکب عطفی (عربی)",
                "meaning_en": "willingly or unwillingly, perforce",
                "meaning_ur": "خوشی سے یا ناخوشی سے، چار و ناچار",
                "urdu_cognates": "طوعاً و کرہاً"
              },
              {
                "persian": "تَمَکُّن",
                "grammar": "مصدر (عربی)",
                "meaning_en": "firm establishment, taking root",
                "meaning_ur": "مضبوط ہونا، جڑ پکڑنا",
                "urdu_cognates": "تمکن"
              }
            ]
          }
        },
        {
          "id": "entry_p32_02",
          "book_page": 32,
          "pdf_page": 34,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "پِسَرِ نُوْح بَا بَدَاں بِنِشَسْتْ",
              "persian_m2": "خَانْدَانِ نُبُوَّتَشْ گُمْ شُدْ",
              "urdu_m1": "حضرت نوح کے بیٹے نے بُروں کے ساتھ نشست و برخاست اختیار کی",
              "urdu_m2": "اُس سے نبوت کا خاندان چھوٹ گیا"
            },
            {
              "persian_m1": "سَگِ اَصْحَابِ کَہْفْ رُوْزے چَنْد",
              "persian_m2": "پَئے نِیْکَاں گِرِفْتْ، مَرْدُمْ شُدْ",
              "urdu_m1": "اصحابِ کہف کے کتے نے چند روز",
              "urdu_m2": "نیکوں کی صحبت اختیار کی، آدمی بن گیا"
            }
          ],
          "english_trans": "The son of Noah sat with the wicked: / And his lineage of prophethood was lost! / The dog of the Companions of the Cave for a few days / Followed in the footsteps of the righteous, and became as a human!",
          "footnotes": [
            "حضرت نوح ایک پیغمبر کا نام ہے جن کے زمانے میں ایک زبردست طوفان آیا تھا ان کا بیٹا کنعان حضرت نوح کے دشمنوں کے ساتھ میل جول رکھتا تھا اور باپ کی مخالفت کرتا تھا جسکا نتیجہ یہ ہوا کہ دوسرے دشمنوں کی طرح وہ بھی طوفان میں غرق ہو گیا۔ ۱۲",
            "اصحابِ کہف سات آدمی تھے جنہوں نے ایک ظالم مشرک بادشاہ کے خوف سے شہر چھوڑ کر ایک غار میں جا کر پناہ لی تھی اور ان کے ساتھ ایک کتا تھا جس کو قطمیر کہا جاتا تھا اُن سب کا مکمل قصہ کتبِ سیر میں مرقوم ہے۔ ۱۲"
          ],
          "study": {
            "notes_en": "Two profound spiritual archetypes of companionship (*suhbat*): Canaan (son of Noah) ruined by wicked company despite prophetic lineage, and the dog of the Seven Sleepers (*Qitmīr*) elevated by accompanying saintly believers.",
            "notes_ur": "صحبت کے اثر کا زبردست تقابل: کنعان نوحؑ کا بیٹا ہو کر بھی بد صحبت کی وجہ سے ہلاک ہوا، جبکہ اصحابِ کہف کا کتا نیک بندوں کا وفادار بن کر تاریخ میں امر ہو گیا۔",
            "vocabulary": [
              {
                "persian": "نُبُوَّت",
                "grammar": "اسم (عربی)",
                "meaning_en": "prophethood",
                "meaning_ur": "پیغمبری، نبوت",
                "urdu_cognates": "نبوت، نبی"
              },
              {
                "persian": "مَرْدُم",
                "grammar": "اسم",
                "meaning_en": "human, gentle folk",
                "meaning_ur": "آدمی، شریف انسان",
                "urdu_cognates": "مردم، مردم شناس"
              }
            ]
          }
        },
        {
          "id": "entry_p32_03",
          "book_page": 32,
          "pdf_page": 34,
          "type": "prose",
          "persian": "اِیْں بَگُفْتْ، وَ طَائِفَۂ اَزْ نُدَمَائے مَلِکْ بَا وَے بَہ شَفَاعَتْ یَارْ شُدَنْدْ، تَا مَلِکْ اَزْ سَرِ خُوْنِ او دَرْگُذَشْتْ، وَ گُفْت: بَخْشِیْدَمْ اَگَرْچِہ مَصْلَحَتْ نَہ دِیْدَمْ۔ رُبَاعِیْ:",
          "urdu_interlinear": "اُس نے یہ کہا اور بادشاہ کے مصاحبوں میں سے ایک جماعت نے سفارش کرنے میں اس کا ساتھ دیا چنانچہ بادشاہ نے اُس کے قتل کا ارادہ چھوڑ دیا اور فرمایا میں نے معاف کیا اگرچہ مناسب نہ سمجھا۔",
          "english_trans": "He spoke thus, and a company of the King's courtiers joined him in intercession, until the King remitted his capital sentence, saying: 'I grant him pardon, though I deem it not expedient!'",
          "footnotes": [],
          "study": {
            "notes_en": "The sovereign yields to consensus against his better instinct, foreshadowing tragic consequences.",
            "notes_ur": "بادشاہ نے درباریوں کی متفقہ سفارش پر ناگواری کے باوجود قیدی لڑکے کی جان بخشی کر دی مگر ساتھ ہی واضح کر دیا کہ یہ فیصلہ عقل کے خلاف ہے۔",
            "vocabulary": [
              {
                "persian": "نُدَمَاء",
                "grammar": "اسم جمع (ندیم کی جمع)",
                "meaning_en": "courtiers, table companions",
                "meaning_ur": "ہم نشین، مصاحبین",
                "urdu_cognates": "ندیم"
              }
            ]
          }
        },
        {
          "id": "entry_p33_01",
          "book_page": 33,
          "pdf_page": 35,
          "type": "stanza",
          "header_persian": "رُبَاعِیْ",
          "header_urdu": "رباعی",
          "lines": [
            {
              "persian_m1": "دَانِیْ کَہ چِہ گُفْتْ زَالْ بَا رُسْتَمِ گُرْد؟",
              "persian_m2": "دُشْمَنْ نَہ تَوَاں حَقِیْر وَ بﮯ چَارَہ شِمُرْد",
              "urdu_m1": "تجھے معلوم ہے کہ زال نے رستم پہلوان سے کیا کہا",
              "urdu_m2": "دشمن کو بے چارہ اور کمزور نہ سمجھنا چاہیئے"
            },
            {
              "persian_m1": "دِیْدِیْمْ بَسے کَہ آبِ سَرْ چَشْمَۂ خُرْد",
              "persian_m2": "چُوں بِیْشْتَر آمَدْ، شُتُر وَ بَار بِبُرْد",
              "urdu_m1": "ہم نے بہت سی مرتبہ دیکھا ہے کہ چھوٹے سے چشمے کا پانی",
              "urdu_m2": "جب زیادہ ہو گیا تو اونٹ اور بوجھ کو بہا لے گیا !"
            }
          ],
          "english_trans": "Dost thou know what Zal said to the champion Rustam? / 'Never deem an enemy contemptible and helpless!' / We have often seen the water of a tiny rill / Swell till it swept away camel and load!",
          "footnotes": [
            "زال رستم کے باپ کا نام تھا۔ کہا جاتا ہے کہ اس کے تمام جسم پر سفید بال تھے اور اسی وجہ سے اُس کا نام زال رکھا گیا تھا۔ یہ بھی مشہور ہے کہ اس کو ایک سیمرغ نے پالا تھا۔ ۱۲"
          ],
          "study": {
            "notes_en": "Sage counsel from heroic Iranian folklore: King Zal's warning to his son Rustam. Never underestimate a small or young enemy.",
            "notes_ur": "رستم کے باپ زال کی نصیحت کہ کسی دشمن کو کمزور اور بے وقعت مت سمجھو۔ چھوٹا سا چشمہ بھی بپھر کر پورے قافلے اور اونٹوں کو بہا لے جاتا ہے۔",
            "vocabulary": [
              {
                "persian": "گُرْد",
                "grammar": "اسم صفت",
                "meaning_en": "champion, hero, brave warrior",
                "meaning_ur": "پہلوان، بہادر، سورما",
                "urdu_cognates": "گرد"
              }
            ]
          }
        },
        {
          "id": "entry_p33_02",
          "book_page": 33,
          "pdf_page": 35,
          "type": "prose",
          "persian": "فِی الْجُمْلَہ، پِسَر رَا بَنَازْ وَ نِعْمَتْ بَرْ آوَرْدَنْدْ، وَ اُسْتَادِ اَدِیْبْ رَا بَتَرْبِیَتِ او نَصْبْ کَرْدَنْدْ، تَا حُسْنِ خِطَابْ، وَ رَدِّ جَوَابْ، وَ آدَابِ خِدْمَتِ مُلُوْکَشْ دَرْ آمُوْخْتَنْدْ، وَ دَرْ نَظَرِ ہَمْگِنَاں پَسَنْد آمَدْ، بَارے وَزِیْر اَزْ شَمَائِلِ او دَرْ حَضْرَتِ سُلْطَانْ شَمَۂ مِیْ گُفْتْ کَہ: تَرْبِیَتِ عَاقِلَاں دَرْ وَے اَثَرْ کَرْدَہ اَسْتْ، وَ جَہْلِ قَدِیْم اَزْ جِبِلَّتِ او بَدَرْ بُرْدَہ، مَلِکْ رَا اَزِیْں سُخَنْ تَبَسُّمْ آمَدْ، وَ گُفْت:",
          "urdu_interlinear": "خلاصہ یہ کہ لڑکے کو ناز و نعمت سے پرورش کیا اور ادب سکھانیوالا اُستاد اس کو پڑھانے سکھانے کے لئے مقرر کر دیا چنانچہ اُنہوں نے بات چیت کا سلیقہ، جواب دینے کا طریقہ، اور بادشاہوں کی خدمت کے طریقے اسکو سکھائے اور سب اسکو پسند کرنے لگے۔ ایک مرتبہ وزیر اُس کے اخلاق کا تھوڑا سا ذکر بادشاہ کے دربار میں کر رہا تھا اور کہہ رہا تھا کہ عقلمندوں کے سکھانے پڑھانے نے اس میں اثر کیا ہے اور پرانی نادانی اُس کی طبیعت سے دور کر دی ہے۔ بادشاہ اس بات پر مسکرایا اور کہنے لگا",
          "english_trans": "In short, they brought up the youth in luxury and comfort, assigning an accomplished tutor to instruct him, until they taught him elegant address, apt replies, and the courtly etiquette of serving kings, so that he won the approval of all. Once the minister was recounting some of his pleasing qualities before the Sultan, asserting that the education of the wise had taken effect upon him and purged the primitive savagery from his nature. The King smiled at these words and remarked:",
          "footnotes": [],
          "study": {
            "notes_en": "The illusion of complete transformation: courtly polish mask inner instinct. The King remains skeptical of superficial refinement.",
            "notes_ur": "وزیر نے لڑکے کی ظاہری ترقی دیکھ کر سمجھا کہ اس کی فطرت بدل چکی ہے اور دربار میں اس کی تعریف کی، لیکن بادشاہ فطرت کے چھپے اثرات سے باخبر تھا۔",
            "vocabulary": [
              {
                "persian": "شَمَائِل",
                "grammar": "اسم جمع (شمال کی جمع)",
                "meaning_en": "dispositions, virtues, manners",
                "meaning_ur": "اخلاق، عادات، خوبیاں",
                "urdu_cognates": "شمائل، شمائلِ ترمذی"
              },
              {
                "persian": "جِبِلَّت",
                "grammar": "اسم (عربی)",
                "meaning_en": "innate nature, constitution",
                "meaning_ur": "فطرت، خمیر، سرشت",
                "urdu_cognates": "جبلت، جبلی"
              }
            ]
          }
        },
        {
          "id": "entry_p33_03",
          "book_page": 33,
          "pdf_page": 35,
          "type": "couplet",
          "header_persian": "بَیْت",
          "header_urdu": "بیت",
          "persian_m1": "عَاقِبَتْ گُرْگْ زَادَہ گُرْگْ شَوَدْ",
          "persian_m2": "گَرْچِہ بَا آدَمِیْ بُزُرْگْ شَوَدْ",
          "urdu_m1": "انجام کار بھیڑیئے کا بچہ بھیڑیا ہوتا ہے",
          "urdu_m2": "اگرچہ انسان کے ساتھ پل کر بڑا ہوا ہو",
          "english_trans": "In the end, the wolf's cub will become a wolf, / Even though it hath grown up among men!",
          "footnotes": [],
          "study": {
            "notes_en": "''Āqibat gurg-zādah gurg shavad / Gar-chih bā ādamī buzurg shavad': arguably the single most quoted proverb from the Gulistan across Persian, Urdu, Turkish, and Arabic.",
            "notes_ur": "سعدی کا ضرب المثل شعر: 'عاقبت گرگ زادہ گرگ شود، گرچہ با آدمی بزرگ شود'۔ کتے اور بھیڑیے کی فطرت انسانوں میں پلنے کے باوجود بدل نہیں سکتی، موقع پاتے ہی خصلت ظاہر ہو جاتی ہے۔",
            "vocabulary": [
              {
                "persian": "گُرْگْ زَادَہ",
                "grammar": "مرکب توصیفی",
                "meaning_en": "wolf's whelp, wolf cub",
                "meaning_ur": "بھیڑیے کا بچہ",
                "urdu_cognates": "گرگ"
              }
            ]
          }
        },
        {
          "id": "entry_p33_04",
          "book_page": 33,
          "pdf_page": 35,
          "type": "prose",
          "persian": "سَالْ دُوْ بَرِیْں بَرْ آمَدْ، طَائِفَۂ اَوْبَاشِ مَحَلَّتْ دَرْ وَے پَیْوَسْتَنْدْ، وَ عَقْدِ مُوَافَقَتْ بَسْتَنْدْ، تَا بَہ وَقْتِ فُرْصَتْ وَزِیْر رَا وَ ہَرْ دُوْ پِسَرَشْ رَا بِکُشْتْ، وَ نِعْمَتِ بﮯ قِیَاسْ بَرْ دَاشْتْ، وَ دَرْ مَغَارَۂ دُزْدَاں بَہ جَائے پِدَرْ بِنِشَسْتْ، وَ عَاصِیْ شُدْ، مَلِکْ دَسْتِ تَحَسُّرْ بَدَنْدَاں گِرِفْتْ وَ گُفْت: قِطْعَہ:",
          "urdu_interlinear": "دو سال اس بات کو گذر گئے۔ محلے کے بدمعاشوں کا ایک گروہ اس سے میل کھا گیا اور انہوں نے اس سے دوستی کا معاہدہ باندھ لیا آخر موقع پا کر اس نے وزیر کو اور اس کے دونوں لڑکوں کو مار ڈالا اور لا تعداد دولت لے کر چلا گیا اور باپ کی جگہ چوروں کی گھاٹی میں رہنے لگا اور باغی ہو گیا بادشاہ نے افسوس سے انگلی دانتوں میں دبا لی اور فرمایا",
          "english_trans": "A couple of years passed. A gang of neighborhood ruffians allied themselves with him and forged a pact of mutual treachery. When the opportunity presented itself, the youth murdered the minister and both of his sons, seized untold riches, fled to the robbers' cavern to occupy his father's seat, and turned rebel! The King bit the finger of regret with his teeth, and exclaimed:",
          "footnotes": [],
          "study": {
            "notes_en": "The dramatic denouement confirms the King's initial foresight. The youth repays the minister's mercy with patricide and robbery.",
            "notes_ur": "دو سال بعد حقیقت کھل گئی؛ لڑکے نے اسی محسن وزیر اور اس کے بیٹوں کا قتل کر کے خزانہ لوٹا اور ڈاکوؤں کا سردار بن گیا۔ بادشاہ کا اندیشہ حرف بہ حرف سچ نکلا۔",
            "vocabulary": [
              {
                "persian": "اَوْبَاش",
                "grammar": "اسم جمع (عربی)",
                "meaning_en": "ruffians, rogues, scoundrels",
                "meaning_ur": "بدمعاش، اوباش لوگ",
                "urdu_cognates": "اوباش"
              },
              {
                "persian": "دَسْتِ تَحَسُّر",
                "grammar": "ترکیبِ اضافی",
                "meaning_en": "hand/finger of deep regret",
                "meaning_ur": "حسرت اور افسوس کا ہاتھ دانتوں میں دبانا",
                "urdu_cognates": "تحسر، حسرت"
              }
            ]
          }
        },
        {
          "id": "entry_p34_01",
          "book_page": 34,
          "pdf_page": 36,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "شَمْشِیْرِ نِیْکْ زَ آہَنِ بَدْ چُوں کُنَدْ کَسِے؟",
              "persian_m2": "نَاکَسْ بَہ تَرْبِیَتْ نَہ شَوَدْ اَے حَکِیْم کَسْ",
              "urdu_m1": "برے لوہے سے عمدہ تلوار کوئی کیسے بنائے",
              "urdu_m2": "اے عقلمند سکھانے پڑھانے سے نالائق لائق نہیں ہو سکتا"
            },
            {
              "persian_m1": "بَارَاں کَہ دَرْ لَطَافَتِ طَبْعَشْ خِلَافْ نِیْسْتْ",
              "persian_m2": "دَرْ بَاغْ لَالَہ رُوْیَدْ وَ دَرْ شُوْرَہ بُوْمْ خَسْ",
              "urdu_m1": "بارش جس کی طبیعت کے پاکیزہ ہونے میں کوئی اختلاف نہیں",
              "urdu_m2": "باغ میں لالہ اور شوریلی زمین میں جھاڑ اگاتی ہے !"
            }
          ],
          "english_trans": "How can anyone forge a fine sword from vile iron? / Never, O sage, can training turn a worthless man into a worthy one! / Rain, in whose sweet purity there is no doubt: / Makes tulips bloom in the garden, yet breeds only weeds in brackish soil!",
          "footnotes": [
            "شورہ بوم وہ زمین جس میں زراعت نہ ہو سکے۔ وہ زمین جس میں کھار زیادہ ہو۔ اور اُس کو اوسر یا بنجر کہتے ہیں۔ ۱۲"
          ],
          "study": {
            "notes_en": "'Bārān kih dar latāfat-e tab'ash khilāf nēst / Dar bāgh lālah rūyad va dar shōrah-būm khas': Rain falling upon fertile loam produces red tulips (*lālah*), but falling upon salt-crusted wasteland (*shōrah-būm*) yields only noxious brambles.",
            "notes_ur": "سعدی کا شاہکار تمثیلی شعر ہے کہ بارش کا پانی ہر جگہ ایک جیسا برستا ہے مگر باغ میں پھول کھلتے ہیں اور بنجر و کھاری زمین میں صرف کانٹے دار جھاڑیاں اگتی ہیں۔ اصل قابلیت زمین (فطرت) کی ہوتی ہے۔",
            "vocabulary": [
              {
                "persian": "شُوْرَہ بُوْم",
                "grammar": "اسمِ مرکب",
                "meaning_en": "brackish soil, salt marsh, barren wasteland",
                "meaning_ur": "شور والی زمین، بنجر، اوسر زمین",
                "urdu_cognates": "شورہ، شورہ زمین"
              },
              {
                "persian": "خَس",
                "grammar": "اسم",
                "meaning_en": "weed, thorn, rubbish",
                "meaning_ur": "کوڑا کرکٹ، جھاڑ، خس و خاشاک",
                "urdu_cognates": "خس و خاشاک"
              }
            ]
          }
        },
        {
          "id": "entry_p34_02",
          "book_page": 34,
          "pdf_page": 36,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "زَمِیْنِ شُوْرَہ سُنْبُلْ بَرْ نَیَارَدْ",
              "persian_m2": "دَرْو تُخْمِ عَمَلْ ضَائِعْ مَگَرْدَاں",
              "urdu_m1": "شوریلی زمین سنبل نہیں اگا سکتی",
              "urdu_m2": "اُس میں کوشش کا بیج ضائع نہ کر"
            },
            {
              "persian_m1": "نِکُوْئِیْ بَا بَدَاں کَرْدَنْ چُنَاں سْتْ",
              "persian_m2": "کَہ بَدْ کَرْدَنْ بَہ جَائے نِیْکْ مَرْدَاں",
              "urdu_m1": "بدوں کے ساتھ نیکی کرنا ایسا ہی ہے",
              "urdu_m2": "جیسے نیکوں کے ساتھ بدی کرنا !"
            }
          ],
          "english_trans": "Brackish soil will never bring forth hyacinths: / Waste not the seed of thy labor upon it! / Doing good unto the wicked / Is equivalent to doing evil unto the righteous!",
          "footnotes": [
            "سنبل بعض کے نزدیک بالچھڑ اور بعض کے نزدیک ایک نیلگوں تیز بو پھول کا درخت ہے۔ ۱۲"
          ],
          "study": {
            "notes_en": "'Nīkū'ī bā badān kardan chunān-ast / Kih bad kardan ba-jāye nīk-mardān': Charity misplaced upon incorrigible predators empowers them to harm the innocent.",
            "notes_ur": "سعدی کا لازوال اخلاقی اصول کہ بروں کے ساتھ رعایت اور احسان کرنا درحقیقت نیکوں کے حق میں ظلم کے مترادف ہوتا ہے۔",
            "vocabulary": [
              {
                "persian": "سُنْبُل",
                "grammar": "اسم",
                "meaning_en": "hyacinth, fragrant flower",
                "meaning_ur": "سنبل کا خوشبودار پھول",
                "urdu_cognates": "سنبل"
              }
            ]
          }
        }
      ]
    },
    {
      "section_id": "bab1_hikayat_05",
      "title_ur": "باب اول: حکایت ۵ — سرہنگ زادہ، حاسدوں کی سازش اور آفتاب کا نور",
      "title_en": "Chapter 1: Story 5 — The Colonel's Son & The Envy of Colleagues",
      "pdf_page": 36,
      "book_page": 34,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p34_03",
          "book_page": 34,
          "pdf_page": 36,
          "type": "prose",
          "header_persian": "حِکَایَت ۵",
          "header_urdu": "حکایت ۵",
          "persian": "سَرْہَنْگْ زَادَہ رَا دِیْدَمْ بَرْ دَرْ سَرَائے اَغْلَمِشْ کَہ عَقْل وَ کَیَاسَتْ وَ فَہْم وَ فِرَاسَتے زَائِدُ الْوَصْفْ دَاشْتْ، ہَمْ اَزْ عَہْدِ خُرْدِیْ آثَارِ بُزُرْگِیْ دَرْ نَاصِیَۂ او پَیْدَا۔ فَرْد:",
          "urdu_interlinear": "میں نے ایک سپاہی زادہ کو اغلش کے دروازہ پر دیکھا جو کہ عقل، سمجھ، دانائی اور ذہانت ناقابلِ بیان رکھتا تھا۔ بچپن ہی سے بڑائی کے نشانات اُس کی پیشانی سے ظاہر تھے۔",
          "english_trans": "I saw the son of an officer at the gate of Aghlamish's palace, possessing intelligence, sagacity, understanding, and discernment beyond description. Even from his tender childhood, the marks of greatness shone visibly upon his brow.",
          "footnotes": [
            "سَر ہنگ۔ سردارِ لشکر۔ نقیب۔ چوب دار۔ ۱۲",
            "اغلش بضم الف۔ ترکی لفظ ہے۔ ایک بادشاہ کا نام ہے۔ ۱۲"
          ],
          "study": {
            "notes_en": "Hikayat 5 introduces a meritorious young officer rising through competence, triggering malicious envy from his colleagues.",
            "notes_ur": "حکایت ۵ میں ایک قابل اور ہونہار نوجوان کی دربار میں ترقی اور اس پر حاسدوں کی بے جا حسد و سازشوں کا احوال بیان کیا گیا ہے۔",
            "vocabulary": [
              {
                "persian": "سَرْہَنْگ",
                "grammar": "اسمِ منصب",
                "meaning_en": "military commander, colonel, officer",
                "meaning_ur": "فوجی افسر، سردارِ لشکر",
                "urdu_cognates": "سرحنگ، سرہنگ"
              },
              {
                "persian": "کَیَاسَت",
                "grammar": "اسم (عربی)",
                "meaning_en": "shrewdness, sagacity, acumen",
                "meaning_ur": "دانائی، ہوشیاری",
                "urdu_cognates": "کیاست، زیرک و کَیِّس"
              }
            ]
          }
        },
        {
          "id": "entry_p34_04",
          "book_page": 34,
          "pdf_page": 36,
          "type": "couplet",
          "header_persian": "فَرْد",
          "header_urdu": "فرد",
          "persian_m1": "بَالَائے سَرَشْ زِ ہُوْشْمَنْدِیْ",
          "persian_m2": "مِیْ تَافْتْ سِتَارَۂ بُلَنْدِیْ",
          "urdu_m1": "اُس کے سر پر ہوشمندی کی وجہ سے",
          "urdu_m2": "بڑائی کا ستارہ چمک رہا تھا",
          "english_trans": "Above his head, through his brilliant acumen, / Shone the auspicious star of lofty fortune!",
          "footnotes": [],
          "study": {
            "notes_en": "Astrological imagery of eminent fortune (*sitārah-ye bulandī*) reflecting inner intellect.",
            "notes_ur": "نوجوان کی ہوشمندی اور غیر معمولی ذہانت اس کے شاندار مستقبل اور بلند اقبالی کی گواہی دے رہی تھی۔",
            "vocabulary": [
              {
                "persian": "ہُوْشْمَنْدِی",
                "grammar": "اسم کیفیت",
                "meaning_en": "acumen, sagacity, intelligence",
                "meaning_ur": "عقلمندی، ہوشیاری",
                "urdu_cognates": "ہوشمند"
              }
            ]
          }
        },
        {
          "id": "entry_p34_05",
          "book_page": 34,
          "pdf_page": 36,
          "type": "prose",
          "persian": "فِی الْجُمْلَہ، مَقْبُوْلِ نَظَرِ سُلْطَانْ آمَدْ کَہ جَمَالِ صُوْرَتْ وَ مَعْنٰی دَاشْتْ، وَ خِرَدْمَنْدَاں گُفْتَہ اَنْد: تَوَانْگَرِیْ بَہ دِلَسْتْ نَہ بَہ مَال، وَ بُزُرْگِیْ بَہ عَقْلَسْتْ نَہ بَہ سَال۔ اَبْنَائے جِنْسِ او بَرْ مَنْصَبِ او حَسَدْ بُرْدَنْدْ، وَ بَہ خِیَانَتے مُتَّہَمْ کَرْدَنْدْ، وَ دَرْ کُشْتَنِ او سَعْیِ بﮯ فَائِدَہ نَمُوْدَنْدْ۔ مِصْرَعْ:",
          "urdu_interlinear": "خلاصہ یہ کہ بادشاہ کی نظر پر چڑھ گیا چونکہ ظاہری و باطنی حسن رکھتا تھا اور عقلمندوں نے کہا ہے مالداری دل سے ہے نہ کہ مال سے اور بڑائی عقل سے ہے نہ کہ عمر سے اس کے ہم پیشہ اُس کے مرتبہ پر جلنے لگے اور ایک خیانت کی اُس پر تہمت لگائی اور اس کے مار ڈالے جانے میں بے نتیجہ کوشش کی",
          "english_trans": "In brief, he found favor in the eyes of the Sultan, for he possessed both outer comeliness and inner virtue. And the sages have said: 'True wealth resides in the heart, not in riches; and greatness lies in wisdom, not in years!' His peers grew envious of his station, accused him falsely of treason, and exerted fruitless efforts to have him put to death.",
          "footnotes": [
            "بعض نسخوں میں ہنر است یعنی مالداری ہنر کے اکثر نسخوں میں تونگری بہ دل است لکھا ہے اُس سے مراد یہ ہے کہ تونگری ہمت پر موقوف ہے۔ ۱۲"
          ],
          "study": {
            "notes_en": "'Tawāngarī ba-dil-ast nah ba-māl, va buzurgī ba-'aql-ast nah ba-sāl': profound proverb establishing virtue as an internal state independent of material assets or biological age.",
            "notes_ur": "امارت کا تعلق مال و دولت سے نہیں بلکہ دل کے غنی ہونے سے ہے، اور بزرگی سالوں کی گنتی سے نہیں بلکہ عقل و فہم سے حاصل ہوتی ہے۔",
            "vocabulary": [
              {
                "persian": "تَوَانْگَرِی",
                "grammar": "اسم کیفیت",
                "meaning_en": "wealth, richness, independence",
                "meaning_ur": "مالداری، تونگری، خود کفالت",
                "urdu_cognates": "توانگر"
              }
            ]
          }
        },
        {
          "id": "entry_p35_01",
          "book_page": 35,
          "pdf_page": 37,
          "type": "couplet",
          "header_persian": "مِصْرَعْ",
          "header_urdu": "مصرع",
          "persian_m1": "دُشْمَنْ چِہ کُنَدْ چُوں مِہْرْبَاں بَاشَدْ دُوْسْت؟",
          "persian_m2": "دُشْمَنْ چِہ کُنَدْ چُوں مِہْرْبَاں بَاشَدْ دُوْسْت؟",
          "urdu_m1": "جب دوست مہربان ہو تو دشمن کیا کر سکتا ہے",
          "urdu_m2": "جب دوست مہربان ہو تو دشمن کیا کر سکتا ہے",
          "english_trans": "What harm can a foe inflict when the Sovereign Friend is benevolent?",
          "footnotes": [],
          "study": {
            "notes_en": "A classical hemistich with double meaning: earthly patrons and the Divine Protector ('Dūst' meaning God in Sufi idiom).",
            "notes_ur": "جب حقیقی دوست یعنی اللہ تعالیٰ یا حکمران مہربان ہو تو دشمنوں کی سازشیں ریت کی دیوار ثابت ہوتی ہیں۔",
            "vocabulary": [
              {
                "persian": "مِہْرْبَان",
                "grammar": "صفت",
                "meaning_en": "kind, gracious, loving",
                "meaning_ur": "مہربان، کرم فرمانے والا",
                "urdu_cognates": "مہربان، مہربانی"
              }
            ]
          }
        },
        {
          "id": "entry_p35_02",
          "book_page": 35,
          "pdf_page": 37,
          "type": "prose",
          "persian": "مَلِکْ پُرْسِیْد کَہ: مُوْجِبِ خَصْمِیِ اِیْشَاں دَرْ حَقِّ تُوْ چِیْسْتْ؟ گُفْت: دَرْ سَایَۂ دَوْلَتِ خُدَاوَنْدِیْ دَامَ مُلْکُہٗ ہَمْگِنَاں رَا رَاضِیْ کَرْدَمْ، مَگَرْ حَسُوْدَاں کَہ رَاضِیْ نَمِیْ شَوَنْدْ، اِلَّا بِزَوَالِ نِعْمَتِ مَنْ، وَ دَوْلَتْ وَ اِقْبَالِ خُدَاوَنْدِیْ بَاقِیْ بَادْ۔ قِطْعَہ:",
          "urdu_interlinear": "بادشاہ نے دریافت کیا تجھ سے اُن کی دشمنی کا کیا سبب ہے اُس نے کہا بادشاہی حکومت کے زیر سایہ خدا اُسے ہمیشہ برقرار رکھے میں نے سب کو راضی کر لیا ہے بجز حاسدوں کے کیونکہ وہ تب ہی راضی ہوں گے جب مجھ سے نعمتیں چھن جائیں۔ خدا کرے شاہی حکومت اور دبدبہ ہمیشہ باقی رہے۔",
          "english_trans": "The King inquired: 'What is the cause of their hostility toward thee?' He replied: 'Beneath the shadow of Your Majesty's reign — may it endure! — I have satisfied all men, except the envious; for they will never be satisfied until my prosperity vanishes! May the royal realm and fortune ever endure!'",
          "footnotes": [],
          "study": {
            "notes_en": "The pathology of envy (*hasad*): an envious person's pain can never be appeased by generosity; they can find satisfaction only in the destruction of the other's blessings.",
            "notes_ur": "حسد کی نفسیات کا لاجواب تجزیہ ہے کہ انسان ہر شخص کو راضی کر سکتا ہے لیکن حاسد اس وقت تک راضی نہیں ہوتا جب تک دوسرے کی نعمت چھن نہ جائے۔",
            "vocabulary": [
              {
                "persian": "خَصْمِی",
                "grammar": "اسم کیفیت",
                "meaning_en": "enmity, hostility",
                "meaning_ur": "دشمنی، عداوت",
                "urdu_cognates": "خصومت، خصم"
              },
              {
                "persian": "حَسُوْد",
                "grammar": "صفتِ مبالغہ (عربی)",
                "meaning_en": "extremely envious, jealous",
                "meaning_ur": "حاسد، جلنے والا",
                "urdu_cognates": "حسود، حسد"
              }
            ]
          }
        },
        {
          "id": "entry_p35_03",
          "book_page": 35,
          "pdf_page": 37,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "تَوَانَمْ اِیْنْکَہ نَیَازَارَمْ اَنْدَرُوْنِ کَسِے",
              "persian_m2": "حَسُوْد رَا چِہ کُنَمْ کَوْزْ خُوْد بَرَنْجْ دَرَسْتْ",
              "urdu_m1": "میں یہ کر سکتا ہوں کہ کسی کا دل نہ دُکھاؤں",
              "urdu_m2": "میں حاسد کا کیا کروں وہ تو خود بخود رنج میں ہے"
            },
            {
              "persian_m1": "بِمِیْر تَا بَرِہِیْ اَے حَسُوْدْ کِیْں رَنْجِیْسْتْ",
              "persian_m2": "کَہ اَزْ مَشَقَّتِ او جُزْ بَہ مَرْگْ نَتْوَاں رَسْتْ",
              "urdu_m1": "اے حاسد تو مر جا تا کہ تو رہائی پائے اس لئے کہ یہ رنج تو ایسا ہے",
              "urdu_m2": "کہ اُس کی تکلیف سے موت کے سوا چھٹکارا نہیں ہو سکتا"
            }
          ],
          "english_trans": "I am able to refrain from grieving the heart of any man; / But what can I do with the envious, who is afflicted within himself? / Die, O envious one, that thou mayest find release! / For from this torment there is no deliverance save through death!",
          "footnotes": [],
          "study": {
            "notes_en": "'Bimīr tā barihī ay hasūd': Saadi's biting critique of envy. Envy is a self-inflicted sickness of the soul that only the grave can cure.",
            "notes_ur": "حاسد پر کڑا طنز کہ میں کسی کو دکھ نہ پہنچانے کا ذمہ دار ہو سکتا ہوں مگر حاسد تو خود اپنی جلن کے عذاب میں مبتلا ہے، اور اس کا علاج سوائے موت کے کچھ نہیں۔",
            "vocabulary": [
              {
                "persian": "نَیَازَارَم",
                "grammar": "فعل مضارع منفی",
                "meaning_en": "I do not distress, I do not grieve",
                "meaning_ur": "میں نہ ستاؤں، نہ دکھاؤں",
                "urdu_cognates": "آزار، آزار رسانی"
              }
            ]
          }
        },
        {
          "id": "entry_p35_04",
          "book_page": 35,
          "pdf_page": 37,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "شُوْر بَخْتَاں بَہ آرزُوْ خَواہَنْدْ",
              "persian_m2": "مُقْبِلَاں رَا زَوَالِ نِعْمَتْ وَ جَاہْ",
              "urdu_m1": "بدبخت تمنا سے نصیب وروں کے",
              "urdu_m2": "مرتبہ اور نعمت کا زوال چاہتے ہیں"
            },
            {
              "persian_m1": "گَرْ نَہ بِیْنَدْ بَہ رُوْز شَبْ پَرَّہ چَشْمْ",
              "persian_m2": "چَشْمَۂ آفْتَابْ رَا چِہ گُنَاہْ؟",
              "urdu_m1": "اگر توندھے کی بیماری والا دن میں نہ دیکھے",
              "urdu_m2": "تو اس میں آفتاب کی ٹکلی کا کیا قصور ہے"
            },
            {
              "persian_m1": "رَاسْتْ خَواہِیْ ہَزَار چَشْمْ چُنَاں",
              "persian_m2": "کُوْر بِہْ تَر کَہ آفْتَابْ سِیَاہْ",
              "urdu_m1": "اگر تو سچ کہلوانا چاہے تو ایسی ہزار آنکھوں کا",
              "urdu_m2": "اندھا ہو جانا آفتاب کے سیاہ ہونے سے بہتر ہے"
            }
          ],
          "english_trans": "The wretched yearn in their covetousness / For the ruin of the fortune and dignity of the prosperous! / If the day-blind bat beholds not by day: / What fault is that of the fountain of the sun? / If thou wouldst hear the truth: a thousand such eyes / Are far better blind than that the glorious sun should be darkened!",
          "footnotes": [
            "آفتاب کے ساتھ چشمہ کا لفظ اس واسطے لایا جاتا ہے کہ وہ روشنی کا منبع ہے۔"
          ],
          "study": {
            "notes_en": "'Chashmah-ye āftāb rā chih gunāh?': the bat (*shab-parrah*) cannot tolerate daylight, but that implies no defect in the sun. A magnificent metaphor vindicating triumphant merit over dark resentment.",
            "notes_ur": "چمگادڑ کو دن میں نظر نہ آئے تو اس میں سورج کا کیا قصور؟ سعدی فرماتے ہیں کہ ایسی ہزار آنکھیں اندھی ہو جائیں تو بہتر ہے مگر سورج کا ماند پڑنا ناممکن ہے۔ سچائی اور کمال حاسدوں کی بے بصری سے بے نیاز ہوتے ہیں۔",
            "vocabulary": [
              {
                "persian": "شَبْ پَرَّہ",
                "grammar": "اسمِ مرکب",
                "meaning_en": "bat, day-blind creature",
                "meaning_ur": "چمگادڑ، توندھا پرندہ",
                "urdu_cognates": "شب پرہ"
              },
              {
                "persian": "شُوْر بَخْت",
                "grammar": "صفتِ مرکب",
                "meaning_en": "ill-fated, wretched, unfortunate",
                "meaning_ur": "بد بخت، سیاہ بخت",
                "urdu_cognates": "شور بخت"
              }
            ]
          }
        }
      ]
    },
    {
      "section_id": "bab1_hikayat_06",
      "title_ur": "باب اول: حکایت ۶ — ظالم بادشاہ کی بربادی اور شاہنامہ کا سبق",
      "title_en": "Chapter 1: Story 6 — The Tyrant King & The Moral of the Shahnameh",
      "pdf_page": 38,
      "book_page": 36,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p36_01",
          "book_page": 36,
          "pdf_page": 38,
          "type": "prose",
          "header_persian": "حِکَایَت ۶",
          "header_urdu": "حکایت ۶",
          "persian": "یَکِے اَزْ مُلُوْکِ عِجَمْ رَا حِکَایَتْ کُنَنْدْ کَہ دَسْتِ تَطَاوُلْ بَرْ مَالِ رَعِیَّتْ دِرَازْ کَرْدَہ بُوْدْ، وَ جَوْر وَ اَذِیَّتْ آغَازْ، تَا بَجَائے کَہ خَلْق اَزْ مَکَائِدِ ظُلْمَشْ بَہ جَہَاں بَرْ رَفْتَنْدْ، وَ اَزْ کُرْبَتِ جَوْرَشْ رَاہِ غُرْبَتْ گِرِفْتَنْدْ، چُوں رَعِیَّتْ کَمْ شُدْ، اِرْتِفَاعِ وِلَایَتْ نُقْصَانْ پَذِیْرُفْتْ، وَ خَزِیْنَہ تِہِیْ مَانْد، وَ دُشْمَنَاں طَمَعْ کَرْدَنْدْ، وَ زُوْرْ آوَرْدَنْدْ۔",
          "urdu_interlinear": "عجم کے بادشاہوں میں سے ایک بادشاہ کا قصہ بیان کرتے ہیں کہ اُس نے رعایا کے مال پر دست درازی کر رکھی تھی اور ظلم و ستم شروع کر دیا تھا یہاں تک کہ رعایا اُس کے ظلم کی سختیوں سے دوسری جگہ چلی گئی اور اُس کے ظلم کی مصیبت سے مسافرت کا راستہ اختیار کر لیا جب رعایا کم ہو گئی تو حکومت کی آمدنی میں گھاٹا آیا اور خزانہ خالی ہو گیا دشمنوں کو اس ملک کے فتح کر نیکا لالچ پیدا ہو گیا اور وہ زور پکڑ گئے۔",
          "english_trans": "They relate of one of the kings of Persia that he had stretched forth the hand of extortion upon the property of his subjects, inaugurating oppression and torment, until the people fled abroad through the hardship of his tyranny and took the path of exile from the grief of his injustice. When the population dwindled, the revenues of the realm decreased, the treasury became depleted, and enemies grew covetous and advanced in force!",
          "footnotes": [
            "عجم۔ ایران و توران اور بعض کے نزدیک علاوہ عرب کے تمام ملک عجم ہے۔ ۱۲"
          ],
          "study": {
            "notes_en": "Hikayat 6 demonstrates the economic and military catastrophe caused by tyrannical rule: taxing the peasantry into exile destroys revenue and invites foreign conquest.",
            "notes_ur": "حکایت ۶ میں جبر و استبداد کا عبرتناک انجام دکھایا گیا ہے۔ جب حکمران عوام کو لوٹتا ہے تو رعایا ہجرت کر جاتی ہے، خراج بند ہوتا ہے، خزانہ خالی ہو جاتا ہے اور بیرونی دشمن ملک پر قابض ہو جاتے ہیں۔",
            "vocabulary": [
              {
                "persian": "تَطَاوُل",
                "grammar": "مصدر (عربی)",
                "meaning_en": "encroachment, extortion, overreaching",
                "meaning_ur": "دست درازی، جبر، زیادتی",
                "urdu_cognates": "تطاول"
              },
              {
                "persian": "اِرْتِفَاع",
                "grammar": "اسم (عربی)",
                "meaning_en": "revenue, yield, income of a province",
                "meaning_ur": "آمدنی، لگان، محصول",
                "urdu_cognates": "ارتفاع"
              }
            ]
          }
        },
        {
          "id": "entry_p36_02",
          "book_page": 36,
          "pdf_page": 38,
          "type": "stanza",
          "header_persian": "قِطْعَہ",
          "header_urdu": "قطعہ",
          "lines": [
            {
              "persian_m1": "ہَرْ کَہ فَرْیَادْرَسِ رُوْزِ مُصِیْبَتْ خَواہَدْ",
              "persian_m2": "گُوْ دَرْ اَیَّامِ سَلَامَتْ بَہ جَوَانْمَرْدِیْ کُوْشْ",
              "urdu_m1": "جو شخص مصیبت کے وقت اپنا مدد گار چاہے",
              "urdu_m2": "اُس کو کہہ دو کہ سلامتی کے وقت شرافت سے کام لے"
            },
            {
              "persian_m1": "بَنْدَۂ حَلْقَہ بَہ گُوْش اَرْ نَنَوَازِیْ، بَرَوَدْ",
              "persian_m2": "لُطْفْ کُنْ، لُطْفْ کَہ بَیْگَانَہ شَوَدْ حَلْقَہ بَہ گُوْشْ",
              "urdu_m1": "اگر تو تابعدار غلام پر بھی مہربانی نہ کریگا تو وہ بھی بھاگ جائیگا",
              "urdu_m2": "مہربانی کر مہربانی تو غیر بھی فرمانبردار ہو جائے گا"
            }
          ],
          "english_trans": "Whoever desires a helper on the day of adversity: / Tell him to practice magnanimity in the days of peace! / If thou treatest not with kindness even a loyal ring-eared slave, he will flee: / Show kindness, show kindness! For by kindness a stranger will become thy devoted slave!",
          "footnotes": [
            "حلقہ بگوش سے مراد مطیع اور فرمانبردار ہے۔ پہلے زمانے میں رسم تھی کہ ایران میں جب غلام خریدتے تھے تو اُس کے کان میں کوئی حلقہ وغیرہ ڈال دیتے تھے اور یہ غلامی کا نشان تھا۔ ۱۲"
          ],
          "study": {
            "notes_en": "'Bandah-ye halqah ba-gōsh': the ring in the ear was the ancient Near Eastern mark of lifelong bondage. Saadi notes that even slaves desert cruel masters, whereas generous kindness wins the unconditional loyalty of strangers.",
            "notes_ur": "'حلقہ بگوش' یعنی وہ غلام جس کے کان میں اطاعت کا کڑا پڑا ہو۔ سعدی فرماتے ہیں کہ ظلم سے اپنے بھی بھاگ کھڑے ہوتے ہیں جبکہ احسان و سخاوت سے پرائے بھی جاں نثار خادم بن جاتے ہیں۔",
            "vocabulary": [
              {
                "persian": "حَلْقَہ بَہ گُوْش",
                "grammar": "صفتِ مرکب",
                "meaning_en": "ear-ringed slave, submissive servant",
                "meaning_ur": "مطیع، فرمانبردار، غلام",
                "urdu_cognates": "حلقہ بگوش"
              },
              {
                "persian": "جَوَانْمَرْدِی",
                "grammar": "اسم کیفیت",
                "meaning_en": "chivalry, magnanimity, generosity",
                "meaning_ur": "جوانمردی، فیاضی، شرافت",
                "urdu_cognates": "جوانمرد، جوانمردی"
              }
            ]
          }
        },
        {
          "id": "entry_p36_03",
          "book_page": 36,
          "pdf_page": 38,
          "type": "prose",
          "persian": "بَارے دَرْ مَجْلِسِ او کِتَابِ شَاہْنَامَہ مِیْ خَوَانْدَنْدْ، دَرْ زَوَالِ مَمْلَکَتِ ضَحَّاکْ وَ عَہْدِ فَرِیْدُوْں، وَزِیْر مَلِکْ رَا پُرْسِیْد کَہ: ہِیْچْ تَوَاں دَانِسْتَنْ کَہ فَرِیْدُوْں کَہ گَنْجْ وَ مُلْکْ وَ حَشَمْ نَدَاشْتْ چِگُوْنَہ مَمْلَکَتْ بَرْ وَے مُقَرَّرْ شُدْ؟ گُفْت: چُنَانْکَہ شَنِیْدِیْ، خَلْقے بَرْ وَے بَتَعَصُّبْ گِرْدْ آمَدَنْدْ، وَ تَقْوِیَتْ کَرْدَنْدْ، پَادْشَاہِیْ یَافْتْ۔ گُفْت: اَے مَلِکْ! چُوں گِرْدْ آمَدَنِ خَلْقے مُوْجِبِ پَادْشَاہِیْ اَسْت، تُوْ خَلْق رَا بَرَائے چِہ پَرِیْشَاں مِیْ کُنِیْ؟ مَگَرْ سَرِ پَادْشَاہِیْ کَرْدَنْ نَدَارِیْ؟ فَرْد:",
          "urdu_interlinear": "ایک مرتبہ اُس کی مجلس میں کتاب شاہنامہ پڑھ رہے تھے ضحاک بادشاہ کی حکومت کی بربادی اور فریدوں کی حکومت کا بیان تھا وزیر نے بادشاہ سے پوچھا کیا جناب سمجھ سمجھے کہ فریدوں جس کے پاس نہ خزانہ تھا نہ لشکر کس طرح اُس کو حکومت مل گئی اُس نے کہا اسیطرح جیسا کہ تم نے سنا کہ رعایا اُس کی طرفداری میں جمع ہو گئی اور اسے مضبوط کر دیا اُس نے بادشاہی حاصل کرلی۔ وزیر نے کہا اے بادشاہ جب رعایا کا اکٹھا ہو جانا بادشاہی ملنے کا سبب ہے تو تو رعایا کو کیوں بھگا رہا ہے شاید تیرا بادشاہی کرنے کا خیال نہیں ہے",
          "english_trans": "Once in his presence they were reading the book Shahnameh, reciting the downfall of the kingdom of Zahhak and the rise of Faridun. The minister asked the king: 'Can one comprehend how Faridun, who possessed neither treasure nor domain nor army, had sovereignty confirmed upon him?' The king answered: 'Even as thou hast heard: the populace rallied around him in solidarity and reinforced him, and so he gained the throne.' The minister replied: 'O king! If the rallying of the populace is the very cause of kingship, wherefore scatterest thou the populace? Hast thou perhaps no desire to reign?'",
          "footnotes": [
            "شاہ نامہ ایک کتاب ہے جو فردوسی طوسی کی تصنیف ہے اور اس میں ایران کے قدیم بادشاہوں کا حال درج ہے۔ ۱۲",
            "ضحاک ایران کے ایک ظالم بادشاہ کا نام ہے جو جمشید کی مملکت پر قابض ہو گیا تھا۔ ۵؎ فریدوں ایک عادل اور منتظم بادشاہ تھا جس نے ضحاک کو شکست دی تھی اور سلطنت پر قبضہ کر لیا تھا۔"
          ],
          "study": {
            "notes_en": "A brilliant dialectical trap: the tyrant acknowledges that Faridun overthrew Zahhak through popular support, allowing the minister to demand why the tyrant is actively alienating his own subjects.",
            "notes_ur": "وزیر نے شاہنامہ کے تاریخی واقعے سے بادشاہ کو لاجواب کیا کہ جب عوام کی حمایت ہی بادشاہی کا زینہ ہے تو پھر تم اپنی رعایا کو ظلم سے منتشر اور بیزار کیوں کر رہے ہو؟",
            "vocabulary": [
              {
                "persian": "حَشَم",
                "grammar": "اسم جمع (عربی)",
                "meaning_en": "retinue, army, servants",
                "meaning_ur": "خدمت گار، لشکر، حشم",
                "urdu_cognates": "جاہ و حشم"
              },
              {
                "persian": "تَعَصُّب",
                "grammar": "مصدر (عربی)",
                "meaning_en": "solidarity, taking sides, partisanship",
                "meaning_ur": "طرفداری، یکجہتی، حمیت",
                "urdu_cognates": "تعصب"
              }
            ]
          }
        },
        {
          "id": "entry_p37_01",
          "book_page": 37,
          "pdf_page": 39,
          "type": "couplet",
          "header_persian": "فَرْد",
          "header_urdu": "فرد",
          "persian_m1": "ہَمَاں بِہْ کَہ لَشْکَر بَہ جَاں پَرْوَرِیْ",
          "persian_m2": "کَہ سُلْطَانْ بَہ لَشْکَر کُنَدْ سَرْوَرِیْ",
          "urdu_m1": "یہی بہتر ہے کہ لشکر کو تو جان لگا کر پالے",
          "urdu_m2": "کیونکہ بادشاہ لشکر ہی کے ذریعہ بادشاہی کرتا ہو",
          "english_trans": "Far better is it that thou cherish the soldier with thy very soul: / For a monarch exercises dominion solely through his army!",
          "footnotes": [],
          "study": {
            "notes_en": "The military pillar of medieval statecraft: kings rule through loyal armies, and armies stay loyal only through prompt pay and generous care.",
            "notes_ur": "فوج کی دلجوئی اور حق رسانی بادشاہت کی بقا کا لازمی ستون ہے۔ سپاہی خوشحال ہوں گے تو سلطنت محفوظ رہے گی۔",
            "vocabulary": [
              {
                "persian": "سَرْوَرِی",
                "grammar": "اسم کیفیت",
                "meaning_en": "lordship, sovereignty, rule",
                "meaning_ur": "حکمرانی، سرداری",
                "urdu_cognates": "سروری، سرور"
              }
            ]
          }
        },
        {
          "id": "entry_p37_02",
          "book_page": 37,
          "pdf_page": 39,
          "type": "prose",
          "persian": "مَلِکْ گُفْت: مُوْجِبِ گِرْدْ آمَدَنِ سِپَاہْ وَ رَعِیَّتْ وَ لَشْکَر چِہ بَاشَدْ؟ گُفْت: پَادْشَاہ رَا کَرَمْ بَایَدْ تَا بَدَوْ گِرْدْ آیَنْدْ، وَ رَحْمَتْ تَا دَرْ پَنَاہِ دَوْلَتَشْ اَیْمِنْ نِشِیْنَنْدْ، وَ تُرَا اِیْں ہَرْ دُوْ نِیْسْتْ۔ مَثْنَوِیْ:",
          "urdu_interlinear": "بادشاہ نے کہا کہ لشکر اور رعایا کے اکٹھا کرنے کا کیا طریقہ ہے وزیر نے کہا بادشاہ کو بخشش کرنی چاہئے تاکہ لوگ اس کے پاس جمع ہو جائیں اور رحم کرنا چاہئے تاکہ لوگ اسکی حکومت کے زیر سایہ بیخوف ہو کر رہیں اور تجھ میں یہ دونوں باتیں نہیں ہیں۔",
          "english_trans": "The King asked: 'What causes the soldier and subject to rally?' The minister answered: 'A king must have generosity so that they assemble about him, and mercy so that they dwell secure beneath the shadow of his rule; and thou possessest neither of these!'",
          "footnotes": [],
          "study": {
            "notes_en": "The two cardinal imperial virtues according to Saadi: Generosity (*karam*) to attract people, and Mercy (*rahmat*) to make them feel secure.",
            "notes_ur": "رعایا کو اپنا بنانے کے دو بنیادی اصول ہیں: داد و دہش (سخاوت) جس سے لوگ کھنچے آئیں، اور عدل و رحمت جس سے وہ بے خوف رہیں۔ ظالم کے پاس یہ دونوں نہیں ہوتے۔",
            "vocabulary": [
              {
                "persian": "کَرَم",
                "grammar": "اسم (عربی)",
                "meaning_en": "generosity, bounty, munificence",
                "meaning_ur": "سخاوت، بخشش، کرم",
                "urdu_cognates": "کرم، کریم"
              }
            ]
          }
        },
        {
          "id": "entry_p37_03",
          "book_page": 37,
          "pdf_page": 39,
          "type": "stanza",
          "header_persian": "مَثْنَوِیْ",
          "header_urdu": "مثنوی",
          "lines": [
            {
              "persian_m1": "نَہ کُنَدْ جَوْرْ پِیْشَہ سُلْطَانِیْ",
              "persian_m2": "کَہ نَیَایَدْ زِ گُرْگْ چُوْپَانِیْ",
              "urdu_m1": "ظالم بادشاہی کیا نہیں کرتا ہے",
              "urdu_m2": "کیونکہ بھیڑیئے سے چرواہے کا کام نہیں ہو سکتا"
            },
            {
              "persian_m1": "پَادْشَاہِے کَہ طَرْحِ ظُلْمْ فِگَنْدْ",
              "persian_m2": "پَائے دِیْوَارِ مُلْکِ خِوِیْشْ بِکَنْدْ",
              "urdu_m1": "جس بادشاہ نے ظلم کی بنیاد ڈالی",
              "urdu_m2": "اُس نے اپنی ہی حکومت کی دیوار کی جڑ کھود دی ہے"
            }
          ],
          "english_trans": "An oppressor can never sustain sovereign rule: / For the shepherd's care comes not from the wolf! / The monarch who lays the foundation of tyranny / Hath undermined the base of the wall of his own kingdom!",
          "footnotes": [],
          "study": {
            "notes_en": "'Nah kunad jawr-pēshah sultānī / Kih nayāyad zi gurg chūpānī': A ruler practicing tyranny is like expecting a wolf to shepherd sheep. Oppression digs out the very foundation of the throne.",
            "notes_ur": "ظالم کبھی پائیدار حکومت نہیں کر سکتا، جیسے بھیڑیا کبھی چرواہا نہیں بن سکتا۔ جو بادشاہ ظلم کرتا ہے وہ دراصل اپنی ہی سلطنت کی جڑیں کاٹتا ہے۔",
            "vocabulary": [
              {
                "persian": "جَوْرْ پِیْشَہ",
                "grammar": "صفتِ مرکب",
                "meaning_en": "practicing tyranny, oppressor",
                "meaning_ur": "ظالم، ستم پیشہ",
                "urdu_cognates": "جور و جفا"
              },
              {
                "persian": "چُوْپَان",
                "grammar": "اسم",
                "meaning_en": "shepherd",
                "meaning_ur": "چرواہا، گڈریا",
                "urdu_cognates": "چوپان"
              }
            ]
          }
        },
        {
          "id": "entry_p37_04",
          "book_page": 37,
          "pdf_page": 39,
          "type": "prose",
          "persian": "مَلِکْ رَا پَنْدِ وَزِیْرِ نَاصِحْ مُوَافِقِ طَبْعِ مُخَالِفْ نَیَامَدْ، وَ رُوْے اَزْ سُخَنَشْ دَرْ ہَمْ کَشِیْدْ، وَ بَزِنْدَاں فِرِسْتَادْ، وَ بَسے بَرْ نَیَامَدْ کَہ بَنِیْ عَمَّانِ سُلْطَانْ بَمُنَازَعَتْ بَرْخَاسْتَنْدْ، وَ بَہ مُقَاوَمَتْ لَشْکَر آرَاسْتَنْدْ، وَ مُلْکِ پِدَرْ خَوَاسْتَنْدْ، قَوْمے کَہ اَزْ دَسْتِ تَطَاوُلِ اِیْں بَہ جَاں رَسِیْدَہ بُوْدَنْدْ، وَ پَرِیْشَاں شُدَہ، بَرْ اِیْشَاں گِرْدْ آمَدَنْدْ وَ تَقْوِیَتْ کَرْدَنْدْ، تَا مُلْک اَزْ تَصَرُّفِ اِیْں بَدَرْ رَفْتْ، وَ بَرْ آنَاں مُقَرَّرْ شُدْ۔ مَثْنَوِیْ:",
          "urdu_interlinear": "ناصح وزیر کی نصیحت بادشاہ کی مخالف طبیعت کے موافق نہ پڑی اور اس کی بات سے منہ چڑھا لیا اور اس کو جیل خانہ بھیج دیا۔ کچھ ہی زمانہ گذرا تھا کہ بادشاہ کے چچیرے بھائی جھگڑے کے لئے اٹھ کھڑے ہوئے اور مقابلہ کے لئے لشکر تیار کیا اور باپ کا ملک مانگا جو قوم کہ اس کی دست درازی سے عاجز آ چکی تھی اور ماری ماری پھر رہی تھی ان کے پاس اکٹھا ہو گئی اور مدد کی چنانچہ حکومت اس کے قبضہ سے نکل گئی اور اُن کے ہاتھ آ گئی۔",
          "english_trans": "The counsel of the sincere minister did not suit the perverse nature of the king; he scowled at his words and cast him into prison. But ere long, the Sultan's cousins rose in rebellion, marshaled troops for resistance, and demanded their ancestral kingdom. The populace, who had been brought to despair by his extortions and scattered in distress, flocked to their banner and reinforced them, until the realm slipped from his grasp and was confirmed upon his rivals!",
          "footnotes": [],
          "study": {
            "notes_en": "The historical inevitability of retribution: when an oppressor imprisons truthful counselors, discontented subjects join dynastic pretenders (*banī 'ammān*), swiftly toppling the crown.",
            "notes_ur": "ناصح وزیر کو قید کرنے کا نتیجہ یہ نکلا کہ چچا زاد بھائیوں کی بغاوت میں مظلوم عوام ان کے ساتھ مل گئے اور ظالم بادشاہ کا تخت پلٹ دیا گیا۔",
            "vocabulary": [
              {
                "persian": "بَنِیْ عَمَّان",
                "grammar": "مرکب اضافی (عربی)",
                "meaning_en": "cousins, paternal uncle's sons",
                "meaning_ur": "چچیرے بھائی، عم زاد",
                "urdu_cognates": "ابن عم"
              }
            ]
          }
        },
        {
          "id": "entry_p38_01",
          "book_page": 38,
          "pdf_page": 40,
          "type": "stanza",
          "header_persian": "مَثْنَوِیْ",
          "header_urdu": "مثنوی",
          "lines": [
            {
              "persian_m1": "پَادْشَاہِے کَوْ رَوَا دَارَدْ سِتَمْ بَرْ زِیْرْدَسْتْ",
              "persian_m2": "دُوْسْتْدَارَشْ رُوْزِ سَخْتِیْ دُشْمَنِ زُوْرْآوَرَسْتْ",
              "urdu_m1": "جو بادشاہ کمزور پر ظلم کرنا جائز رکھے",
              "urdu_m2": "اُس کا دوست بھی مصیبت کے وقت اُسکا زبردست دشمن بن جاتا ہے"
            },
            {
              "persian_m1": "بَا رَعِیَّتْ صُلْح کُنْ وَزْ جَنْگِ خَصْمْ اَیْمِنْ نِشِیْنْ",
              "persian_m2": "زَانْکَہ شَاہَنْشَاہِ عَادِلْ رَا رَعِیَّتْ لَشْکَرَسْتْ",
              "urdu_m1": "رعایا کے ساتھ صلح کر اور دشمن کی لڑائی سے بیخوف ہو کر بیٹھ",
              "urdu_m2": "اس لئے کہ منصف بادشاہ کی تو رعایا ہی لشکر ہے"
            }
          ],
          "english_trans": "A monarch who tolerates oppression upon the defenseless / Will find his very friends turned into formidable foes on the day of trial! / Make peace with thy subjects and sit secure from the warfare of enemies: / For to a just Emperor, his subjects are his very army!",
          "footnotes": [],
          "study": {
            "notes_en": "'Zān-kih shāhanshāh-e 'ādil rā ra'iyyat lashkar-ast': The eternal maxim of Persian political ethics. A just ruler's subjects are his invincible garrison; when subjects love their sovereign, no external enemy can prevail.",
            "notes_ur": "سعدی کا لازوال سیاسی قول کہ عادل بادشاہ کی اصل فوج اس کی رعایا ہوتی ہے۔ جب رعایا مطمئن ہو تو بادشاہ کو بیرونی دشمنوں سے کوئی خطرہ نہیں رہتا۔",
            "vocabulary": [
              {
                "persian": "زِیْرْدَسْت",
                "grammar": "صفتِ مرکب",
                "meaning_en": "subordinate, powerless, underling",
                "meaning_ur": "ماتحت، کمزور، رعایا",
                "urdu_cognates": "زیردست"
              }
            ]
          }
        },
        {
          "id": "entry_p38_02",
          "book_page": 38,
          "pdf_page": 40,
          "type": "couplet",
          "header_persian": "فَرْد",
          "header_urdu": "فرد",
          "persian_m1": "گَزَنْدِ زِیْرْدَسْتَاں بَخَوْرْ زِیْنَہَارْ",
          "persian_m2": "بِتَرْسْ اَزْ زَبَر دَسْتِیِ رُوْزْگَارْ",
          "urdu_m1": "خبردار کمزوروں کے ساتھ غم خواری کر",
          "urdu_m2": "زمانہ کی زبردستی سے ڈر",
          "english_trans": "Beware! Show sympathy and forbear hurting the weak: / Fear the sudden turning and overwhelming force of Time!",
          "footnotes": [],
          "study": {
            "notes_en": "Warning on the vicissitudes of Time (*rōzgār*): power shifts suddenly, and the tyrant of today becomes the helpless wretch of tomorrow.",
            "notes_ur": "کمزوروں کو ستانے سے توبہ کرو کیونکہ زمانے کا پلٹا بہت بے رحم ہوتا ہے اور اقتدار کبھی ایک جیسا نہیں رہتا۔",
            "vocabulary": [
              {
                "persian": "زِیْنَہَار",
                "grammar": "کلمۂ تحذیر",
                "meaning_en": "beware! take care!",
                "meaning_ur": "خبردار! ہوشیار!",
                "urdu_cognates": "زنہار"
              }
            ]
          }
        }
      ]
    },
    {
      "section_id": "bab1_hikayat_07",
      "title_ur": "باب اول: حکایت ۷ — جہاز میں غلام کی بے قراری اور سکّان کا سہارا",
      "title_en": "Chapter 1: Story 7 — The Terrified Slave in the Ship & The Lesson of the Rudder",
      "pdf_page": 40,
      "book_page": 38,
      "content_type": "bilingual_text",
      "entries": [
        {
          "id": "entry_p38_03",
          "book_page": 38,
          "pdf_page": 40,
          "type": "prose",
          "header_persian": "حِکَایَت ۷",
          "header_urdu": "حکایت ۷",
          "persian": "پَادْشَاہِے بَا غُلَامِے عَجَمِیْ دَرْ کِشْتِیْ نِشَسْتْ، وَ غُلَامْ دِیْگَر دَرْیَا رَا نَہ دِیْدَہ بُوْدْ، وَ مِحْنَتِ کِشْتِیْ نَیَازْمُوْدَہ، گِرْیَہ وَ زَارِیْ آغَازْ نَہَادْ، وَ لَرْزَہ بَرْ اَنْدَامَشْ اُفْتَادْ، مَلِکْ رَا عَیْش اَزْ وَے مُنَغَّصْ بُوْدْ، کَہ طَبْعِ نَازُکْ تَحَمُّلِ مِثْلِ اِیْں صُوْرَتْ نَہ بَنْدَدْ، چَارَہ نَدَانِسْتَنْدْ، دَر آں کِشْتِیْ حَکِیْمے بُوْد، مَلِکْ رَا گُفْت: اَگَرْ فَرْمَاں دَہِیْ، او رَا بَہ طَرِیْقِے خَامُوْشْ گَرْدَانَمْ؟ گُفْت: غَایَتِ لُطْفْ وَ کَرَمْ بَاشَدْ۔ بِفَرْمُوْدْ تَا غُلَامْ رَا بَہ دَرْیَا اَنْدَاخْتَنْدْ، چَنْد نَوْبَتْ غُوْطَہ خُوْرْد، اَزَاں پَسْ مُوْیَشْ گِرِفْتَنْدْ وَ پِیْشِ کِشْتِیْ آوَرْدَنْدْ، وَ بَہ دُوْ دَسْتْ دَرْ سُکَّانِ کِشْتِیْ آوِیْخْتْ، چُوں بَرْ آمَدْ بَہ گُوْشَۂ نِشَسْتْ وَ قَرَارْ یَافْتْ۔ مَلِکْ رَا عَجَبْ آمَدْ، پُرْسِیْد کَہ: حِکْمَتْ چِہ بُوْد؟ گُفْت: اَزْ اَوَّلْ مِحْنَتِ غَرْقْ شُدَنْ...",
          "urdu_interlinear": "ایک بادشاہ ایک عجمی غلام کے ساتھ کشتی میں سوار ہوا ۔ اور غلام نے کبھی دریا نہ دیکھا تھا اور نہ کشتی کی تکلیفیں اٹھائی تھیں اس نے رونا دھونا شروع کر دیا اور اس کا بدن کانپنے لگا جس سے بادشاہ کا مزا کرکرا ہو گیا تھا اس لئے کہ نازک طبیعت اس جیسی باتوں کی برداشت نہیں کر سکتی لوگوں کی سمجھ میں کوئی تدبیر نہ آئی اس کشتی میں ایک عقلمند تھا وہ بادشاہ سے بولا اگر حکم ہو تو ایک طریقے سے اُسے خاموش کر دوں بادشاہ نے کہا بڑی مہربانی ہوگی اُس عقلمند نے حکم دیا چنانچہ لوگوں نے غلام کو دریا میں پھینک دیا غلام نے چند غوطے کھائے اس کے بعد لوگوں نے اس کے سر کے بال پکڑے اور کشتی کے آگے لائے وہ غلام دونوں ہاتھوں سے کشتی کے دنبالہ میں لٹک گیا جب دریا سے نکلا تو ایک گوشہ میں بیٹھ گیا اور اسکو سکون ہو گیا بادشاہ کو تعجب ہوا اُس نے دریافت کیا اس میں کیا دانائی تھی عقلمند نے جواب دیا غلام نے اس سے پہلے ڈوبنے کی...",
          "english_trans": "A king embarked on a ship with a Persian slave who had never before seen the sea nor experienced the distress of a voyage. He began to weep and wail, and trembling seized his limbs. The King's pleasure was spoiled by him, for a delicate temperament cannot endure such disturbances; yet no one knew how to pacify him. On that vessel chanced to be a philosopher, who said to the King: 'If thou commandest, I will silence him by a certain method.' The King replied: 'It will be an act of utmost kindness!' The sage directed that the slave be thrown into the sea. He plunged beneath the waves several times; then they seized him by the hair, dragged him toward the ship, and with both hands he clung desperately to the rudder! When they hauled him aboard, he sat quietly in a corner and rested in utter peace. The King was astonished and asked: 'What wisdom lay in this?' The philosopher replied: 'At first, he had never experienced the anguish of drowning...'",
          "footnotes": [
            "سُکّان کشتی یا جہاز کی ایک لکڑی۔ بعض کے نزدیک اُس کو دنبالہ کہتے ہیں۔ ۱۲"
          ],
          "study": {
            "notes_en": "Hikayat 7 (or 8 in standard counting): One of Saadi's most celebrated psychological insights. A person does not appreciate safety until he has tasted real peril: 'Qadr-e 'āfiyat kasē dānad kih ba-musēbatē giriftār āyad'.",
            "notes_ur": "مشہور تمثیل ہے کہ جب تک انسان بڑی مصیبت (ڈوبنے) کا مزا نہ چکھ لے وہ چھوٹی تکلیف (کشتی کے جھٹکوں) سے شکایت کرتا رہتا ہے۔ جب دریا میں غوطے کھا کر کشتی کا تختہ ملا تو اسی کشتی کو غنیمت جان کر خاموش بیٹھ گیا۔ قدرِ عافیت مصیبت جھیلنے کے بعد ہی معلوم ہوتی ہے۔",
            "vocabulary": [
              {
                "persian": "مُنَغَّص",
                "grammar": "اسم مفعول (عربی)",
                "meaning_en": "spoiled, troubled, disrupted",
                "meaning_ur": "ناگوار، مکدر، کرکرا",
                "urdu_cognates": "منغص"
              },
              {
                "persian": "سُکَّان",
                "grammar": "اسم (عربی)",
                "meaning_en": "rudder, helm of a ship",
                "meaning_ur": "کشتی کا پتوار، دنبالہ",
                "urdu_cognates": "سکان"
              },
              {
                "persian": "غُوْطَہ",
                "grammar": "اسم",
                "meaning_en": "plunge, dive under water",
                "meaning_ur": "ڈبکی، غوطہ کھانا",
                "urdu_cognates": "غوطہ، غوطہ زن"
              }
            ]
          }
        }
      ]
    }
  ]
}

out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data/batch_04_pages_031_040.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(batch_04, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {out_path}")
