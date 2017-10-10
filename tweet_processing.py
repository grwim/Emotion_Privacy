import re
import numpy as np
from collections import Counter
import pdb

# how many of 20 tweets selected for each emotion are 'emotion_rich'?

# clean(file_name)
# functions: clean_Mohammed_Format(file_name)
# get_Labels_Mohammed_Format(file_name)



def get_Labels_Mohammed_Format(file_name):
    file = open(file_name)
    labels = np.array([])

    for line in file:
        line = unicode(line,'utf-8')
        line = line.encode('unicode-escape')

        line = re.sub(r'\\n', "", line)

        line_listForm = []
        line_listForm = re.sub(r'[^\w\'] ', " ",  line).split() # convert into list of words

        labels = np.append( labels,  line_listForm[-1] )

    return labels



def clean(file_name):
    file = open(file_name)

    cleaned_tweets = np.array([])

    for line in file:

        emotion_rich = False

        line = unicode(line,'utf-8')
        line = line.encode('unicode-escape')

        line = re.sub(r'\\U0001f62c', "grimace_emoji", line)

        line = re.sub(r'\\r', "", line)
        line = re.sub(r'\\n', "", line)

        # ;) ; ) : ) :) : D :D  :( : ( : / :/

        if   bool (  re.search( r';\)', line) ):
            emotion_rich = True
        line = re.sub(r';\)', "winkeSmile_face", line)

        if   bool (  re.search( r'; \)', line) ):
            emotion_rich = True
        line = re.sub(r'; \)', "winkeSmile_face", line)

        if   bool (  re.search( r': \)', line) ):
            emotion_rich = True
        line = re.sub(r': \)', "smile_face", line)

        if   bool (  re.search( r':\)', line) ):
            emotion_rich = True
        line = re.sub(r':\)', "smile_face", line)

        if   bool (  re.search( r': \D', line) ):
            emotion_rich = True
        line = re.sub(r': \D', "smile_face", line)

        if   bool (  re.search( r':\D', line) ):
            emotion_rich = True
        line = re.sub(r':\D', "smile_face", line)

        #:(
        if   bool (  re.search( r':\(', line) ):
            emotion_rich = True
        line = re.sub(r':\(', "frown_face", line)

        #: (
        if   bool (  re.search( r': \(', line) ):
            emotion_rich = True
        line = re.sub(r': \(', "frown_face", line)

        # :/
        if   bool (  re.search( r':\\', line) ):
            emotion_rich = True
        line = re.sub(r':\D', "frown_face", line)

        #: /
        if   bool (  re.search( r': \\'  , line) ):
            emotion_rich = True
        line = re.sub(r':\D', "frown_face", line)

      # double left quotation mark
        line = re.sub(r'\\u201c', "", line)


        # grimace: \U0001f62c
        if   bool (  re.search( r'\\U0001f62c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f62c', "grimace_emoji", line)

        # grimmace_face_emoji    \U0001F601
        if   bool (  re.search( r'\\U0001f601', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f601', "grimmace_face_smile_eyes_emoji", line)
        # open_mouth_smile_emoji  \U0001F603
        if   bool (  re.search( r'\\U0001f603', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f603', "open_mouth_smile_emoji", line)

        # open_mouth_smile_eyes_emoji
        if   bool (  re.search( r'\\U0001f603', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f604', "open_mouth_smile_emoji", line)
        # grin_face_emoji
        if   bool (  re.search( r'\\U0001f600', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f600', "smile_face", line)
        # grin_face_emoji
        if   bool (  re.search( r'\\U0001f602', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f602', "tears_joy", line)

        if   bool (  re.search( r'\\U0001f605', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f605', "smile_openMouth_coldSweat", line)

        if   bool (  re.search( r'\\U0001f606', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f606', "smile_face", line)

        if   bool (  re.search( r'\\U0001f607', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f607', "smile_face", line)

        if   bool (  re.search( r'\\U0001f609', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f609', "wink_face", line)

        if   bool (  re.search( r'\\U0001f60a', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f60a', "smile_face", line)

        if   bool (  re.search( r'\\U0001f642', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f642', "smile_face", line)

        if   bool (  re.search( r'\\U0001f643', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f643', "upside_down_face", line)

        if   bool (  re.search( r'\\U263a', line) ):
            emotion_rich = True
        line = re.sub(r'\\U263a', "smile_face", line)

        if   bool (  re.search( r'\\Ufe0f', line) ):
            emotion_rich = True
        line = re.sub(r'\\Ufe0f', "smile_face", line)

        if   bool (  re.search( r'\\U0001f60b', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f60b', "delicious_food_savor", line)

        if   bool (  re.search( r'\\U0001f60c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f60c', "relieved_face", line)

        if   bool (  re.search( r'\\U0001f60d', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f60d', "smile_heartShapedEyes", line)

        if   bool (  re.search( r'\\U000fe32c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U000fe32c', "kiss_face", line)

        if   bool (  re.search( r'\\U0001f617', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f617', "kiss_face", line)

        if   bool (  re.search( r'\\U0001f619', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f619', "face_kiss", line)

        if   bool (  re.search( r'\\U0001f61a', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f61a', "face_kiss", line)

        if   bool (  re.search( r'\\U0001f44c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c', "OK_sign", line)

        if   bool (  re.search( r'\\U0001f44a', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44a', "fistHand_sign", line)

        if   bool (  re.search( r'\\U0001f629', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f629', "weary_face", line)

        if   bool (  re.search( r'\\U0001f63d', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f63d', "kissingCat_closedEyes", line)

        if   bool (  re.search( r'\\U0001f614', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f614', "pensive_face", line)

        if   bool (  re.search( r'\\U0001f64c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f64c', "both_hands_raised_celebration", line)

        if   bool (  re.search( r'\\U0001fe44d', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001fe44d', "thumbs_up_sign", line)

        if   bool (  re.search( r'\\U0001f44c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c\\U0001f3fc', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c\\U0001f3fc', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f3fc', line) ):
            emotion_rich = True
        line = re.sub(r'\U0001f3fc', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c\\U0001f3fb', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c\\U0001f3fb', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f3fb', line) ):
            emotion_rich = True
        ine = re.sub(r'\\U0001f3fb', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c', line) ):
            emotion_rich = True
        ine = re.sub(r'\\U0001f44c', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c\\U0001f3ff', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c\\U0001f3ff', "ok_hand_sign_black", line)

        if   bool (  re.search( r'\\U0001f609', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f609', "wink_face", line)

        if   bool (  re.search( r'\\U0001f637', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f637', "face_medical_mask", line)

        if   bool (  re.search( r'\\U0001f621', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f621', "pout_face", line)

        if   bool (  re.search( r'\\U0001F624', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001F624', "triumpLook_face", line)

        if   bool (  re.search( r'\\U0001f622', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f622', "cry_face", line)

        if   bool (  re.search( r'\\U0001f622', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f622', "cry_face", line)

        if   bool (  re.search( r'\\U0001f622', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f622', "withoutMouth_face", line)

        if   bool (  re.search( r'\\u270c\ufe0f', line) ):
            emotion_rich = True
        line = re.sub(r'\\u270c\ufe0f', "victory_hand", line)

        if   bool (  re.search( r'\\U0001f629', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f629', "weary_face", line)

        if   bool (  re.search( r'\\U0001F63D', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001F63D', "kiss_face", line)

        # remove links
        line = re.sub(r'^https?:\/\/.*[\r\n]*', '', line)

        #remove handles
        line = re.sub(r'@([A-Za-z0-9_]+)', '', line)


        # capitalization

        num_cap = sum(1 for c in line if c.isupper())
        num_low = sum(1 for c in line if c.islower())

        if not (num_low == 0 and num_cap == 0):
            if ( num_cap / ( num_cap + num_low )  > .80 ):  # if proportion of caps is greater than 80%
                # then add cap feature
                line = line + " high_cap"


        # exclemation points

        c = Counter(line)
        frequncies = reversed(c.most_common())

        for aTuple in frequncies:
            if aTuple[0] == '!':
                if int(aTuple[1]) >= 3:
                    emotion_rich = True
                    line = line + " extreme_exclemation"
                elif int(aTuple[1]) >= 1:
                    emotion_rich = True
                    line = line + " exclemation"

        line_listForm = []
        line_listForm = re.sub(r'[^\w\'] ', " ",  line).split() # convert into list of words

        words_toAppend = []
        for word in line_listForm: # double word if all caps
            if  word.isupper() and len(word) > 1:
                emotion_rich = True
                words_toAppend.append(word)

        for item in words_toAppend:
            line_listForm.append(item)

        # double hash-tagged words (remove hashtag)
        hashed = [ word for word in line_listForm if word.startswith("#") ]
        for word in hashed:
                line_listForm.append( word[1:] )
                line_listForm.append( word[1:] )

        indices_to_delete = []
        # remove hashtag version
        for i in range(len(line_listForm)):
            if line_listForm[i].startswith("#"):
                indices_to_delete.append(i)

        for index in reversed(indices_to_delete):
            del line_listForm[index]


        # make everything lower case
        for i in range(len(line_listForm)):
            line_listForm[i] = line_listForm[i].lower()

        # double emotion key words and their synonyms if they exist
        emotions_file = open("emotions_synonyms.txt")
        lines = emotions_file.readlines()
            # build dictionary of emotions and synonmys from file

        emotions_list = dict()
        for synonym_line in lines:
            synonym_line = synonym_line.rstrip("\n")
            words = synonym_line.split(",")
            emotion_curr = words[0]
            synonyms = words[1:]
            emotions_list[emotion_curr] = synonyms
        emotions_file.close()

        for word in line_listForm:
            words_toAppend = []
            if word == "anger":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "disgust":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "fear":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "joy":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "love":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "sadness":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "surprise":
                words_toAppend.append(word)
                emotion_rich = True
            elif word in emotions_list:
                emotion_rich = True
                words_toAppend.append(word)

        for word in words_toAppend:
            line_listForm.append(word)

        if emotion_rich:
            line_listForm.append("emotion_rich")

        line = ""

        for word in line_listForm:
            line = line + " " + word

        line = line[1:] # remove empty space at begining

            # line = line + " " + "emotion_rich"

        cleaned_tweets = np.append(cleaned_tweets,  line)

    file.close()

    outfile = open("clean_test.txt", 'w')


    for line in cleaned_tweets:
        outfile.write(line + "\n" )

    outfile.close()

    return cleaned_tweets






def clean_Mohammed_Format(file_name):

    file = open(file_name)

    cleaned_tweets = np.array([])

    for line_fresh in file:

        emotion_rich = False

        line_fresh = unicode(line_fresh,'utf-8')
        line_fresh = line_fresh.encode('unicode-escape')

        # ONLY FOR Mohammed data set
        line_fresh = re.sub(r'[\d]+:', "", line_fresh )
        line_fresh = re.sub(r'\\t', " ", line_fresh)
        line_fresh = re.sub(r'::', "", line_fresh)
        line_fresh = re.sub(r':', "", line_fresh)

        line_listForm = []
        line_listForm = re.sub(r'[^\w\'] ', " ",  line_fresh).split() # convert into list of words

        line_listForm = line_listForm[:-1]

        line = ""
        for word in line_listForm:
            line = line + " " + word

        line = line[1:] # remove empty space at begining
        # END only for Mohammed data set

        line = re.sub(r'\\U0001f62c', "grimace_emoji", line)

        line = re.sub(r'\\r', "", line)
        line = re.sub(r'\\n', "", line)

        # ;) ; ) : ) :) : D :D  :( : ( : / :/

        if   bool (  re.search( r';\)', line) ):
            emotion_rich = True
        line = re.sub(r';\)', "winkeSmile_face", line)

        if   bool (  re.search( r'; \)', line) ):
            emotion_rich = True
        line = re.sub(r'; \)', "winkeSmile_face", line)

        if   bool (  re.search( r': \)', line) ):
            emotion_rich = True
        line = re.sub(r': \)', "smile_face", line)

        if   bool (  re.search( r':\)', line) ):
            emotion_rich = True
        line = re.sub(r':\)', "smile_face", line)

        if   bool (  re.search( r': \D', line) ):
            emotion_rich = True
        line = re.sub(r': \D', "smile_face", line)

        if   bool (  re.search( r':\D', line) ):
            emotion_rich = True
        line = re.sub(r':\D', "smile_face", line)

        #:(
        if   bool (  re.search( r':\(', line) ):
            emotion_rich = True
        line = re.sub(r':\(', "frown_face", line)

        #: (
        if   bool (  re.search( r': \(', line) ):
            emotion_rich = True
        line = re.sub(r': \(', "frown_face", line)

        # :/
        if   bool (  re.search( r':\\', line) ):
            emotion_rich = True
        line = re.sub(r':\D', "frown_face", line)

        #: /
        if   bool (  re.search( r': \\'  , line) ):
            emotion_rich = True
        line = re.sub(r':\D', "frown_face", line)

      # double left quotation mark
        line = re.sub(r'\\u201c', "", line)


        # grimace: \U0001f62c
        if   bool (  re.search( r'\\U0001f62c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f62c', "grimace_emoji", line)

        # grimmace_face_emoji    \U0001F601
        if   bool (  re.search( r'\\U0001f601', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f601', "grimmace_face_smile_eyes_emoji", line)
        # open_mouth_smile_emoji  \U0001F603
        if   bool (  re.search( r'\\U0001f603', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f603', "open_mouth_smile_emoji", line)

        # open_mouth_smile_eyes_emoji
        if   bool (  re.search( r'\\U0001f603', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f604', "open_mouth_smile_emoji", line)
        # grin_face_emoji
        if   bool (  re.search( r'\\U0001f600', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f600', "smile_face", line)
        # grin_face_emoji
        if   bool (  re.search( r'\\U0001f602', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f602', "tears_joy", line)

        if   bool (  re.search( r'\\U0001f605', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f605', "smile_openMouth_coldSweat", line)

        if   bool (  re.search( r'\\U0001f606', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f606', "smile_face", line)

        if   bool (  re.search( r'\\U0001f607', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f607', "smile_face", line)

        if   bool (  re.search( r'\\U0001f609', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f609', "wink_face", line)

        if   bool (  re.search( r'\\U0001f60a', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f60a', "smile_face", line)

        if   bool (  re.search( r'\\U0001f642', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f642', "smile_face", line)

        if   bool (  re.search( r'\\U0001f643', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f643', "upside_down_face", line)

        if   bool (  re.search( r'\\U263a', line) ):
            emotion_rich = True
        line = re.sub(r'\\U263a', "smile_face", line)

        if   bool (  re.search( r'\\Ufe0f', line) ):
            emotion_rich = True
        line = re.sub(r'\\Ufe0f', "smile_face", line)

        if   bool (  re.search( r'\\U0001f60b', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f60b', "delicious_food_savor", line)

        if   bool (  re.search( r'\\U0001f60c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f60c', "relieved_face", line)

        if   bool (  re.search( r'\\U0001f60d', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f60d', "smile_heartShapedEyes", line)

        if   bool (  re.search( r'\\U000fe32c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U000fe32c', "kiss_face", line)

        if   bool (  re.search( r'\\U0001f617', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f617', "kiss_face", line)

        if   bool (  re.search( r'\\U0001f619', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f619', "face_kiss", line)

        if   bool (  re.search( r'\\U0001f61a', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f61a', "face_kiss", line)

        if   bool (  re.search( r'\\U0001f44c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c', "OK_sign", line)

        if   bool (  re.search( r'\\U0001f44a', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44a', "fistHand_sign", line)

        if   bool (  re.search( r'\\U0001f629', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f629', "weary_face", line)

        if   bool (  re.search( r'\\U0001f63d', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f63d', "kissingCat_closedEyes", line)

        if   bool (  re.search( r'\\U0001f614', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f614', "pensive_face", line)

        if   bool (  re.search( r'\\U0001f64c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f64c', "both_hands_raised_celebration", line)

        if   bool (  re.search( r'\\U0001fe44d', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001fe44d', "thumbs_up_sign", line)

        if   bool (  re.search( r'\\U0001f44c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c\\U0001f3fc', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c\\U0001f3fc', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f3fc', line) ):
            emotion_rich = True
        line = re.sub(r'\U0001f3fc', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c\\U0001f3fb', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c\\U0001f3fb', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f3fb', line) ):
            emotion_rich = True
        ine = re.sub(r'\\U0001f3fb', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c', line) ):
            emotion_rich = True
        ine = re.sub(r'\\U0001f44c', "ok_hand_sign", line)

        if   bool (  re.search( r'\\U0001f44c\\U0001f3ff', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f44c\\U0001f3ff', "ok_hand_sign_black", line)

        if   bool (  re.search( r'\\U0001f609', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f609', "wink_face", line)

        if   bool (  re.search( r'\\U0001f637', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f637', "face_medical_mask", line)

        if   bool (  re.search( r'\\U0001f621', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f621', "pout_face", line)

        if   bool (  re.search( r'\\U0001F624', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001F624', "triumpLook_face", line)

        if   bool (  re.search( r'\\U0001f622', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f622', "cry_face", line)

        if   bool (  re.search( r'\\U0001f622', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f622', "cry_face", line)

        if   bool (  re.search( r'\\U0001f622', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f622', "withoutMouth_face", line)

        if   bool (  re.search( r'\\u270c\ufe0f', line) ):
            emotion_rich = True
        line = re.sub(r'\\u270c\ufe0f', "victory_hand", line)

        if   bool (  re.search( r'\\U0001f629', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001f629', "weary_face", line)

        if   bool (  re.search( r'\\U0001F63D', line) ):
            emotion_rich = True
        line = re.sub(r'\\U0001F63D', "kiss_face", line)

        # remove links
        line = re.sub(r'^https?:\/\/.*[\r\n]*', '', line)

        #remove handles
        line = re.sub(r'@([A-Za-z0-9_]+)', '', line)


        # capitalization

        num_cap = sum(1 for c in line if c.isupper())
        num_low = sum(1 for c in line if c.islower())

        if not (num_low == 0 and num_cap == 0):
            if ( num_cap / ( num_cap + num_low )  > .80 ):  # if proportion of caps is greater than 80%
                # then add cap feature
                line = line + " high_cap"


        # exclemation points

        c = Counter(line)
        frequncies = reversed(c.most_common())

        for aTuple in frequncies:
            if aTuple[0] == '!':
                if int(aTuple[1]) >= 3:
                    emotion_rich = True
                    line = line + " extreme_exclemation"
                elif int(aTuple[1]) >= 1:
                    emotion_rich = True
                    line = line + " exclemation"

        line_listForm = []
        line_listForm = re.sub(r'[^\w\'] ', " ",  line).split() # convert into list of words

        words_toAppend = []
        for word in line_listForm: # double word if all caps
            if  word.isupper() and len(word) > 1:
                emotion_rich = True
                words_toAppend.append(word)

        for item in words_toAppend:
            line_listForm.append(item)

        # double hash-tagged words (remove hashtag)
        hashed = [ word for word in line_listForm if word.startswith("#") ]
        for word in hashed:
                line_listForm.append( word[1:] )
                line_listForm.append( word[1:] )

        indices_to_delete = []
        # remove hashtag version
        for i in range(len(line_listForm)):
            if line_listForm[i].startswith("#"):
                indices_to_delete.append(i)

        for index in reversed(indices_to_delete):
            del line_listForm[index]


        # make everything lower case
        for i in range(len(line_listForm)):
            line_listForm[i] = line_listForm[i].lower()

        # double emotion key words and their synonyms if they exist
        emotions_file = open("emotions_synonyms.txt")
        lines = emotions_file.readlines()
            # build dictionary of emotions and synonmys from file

        emotions_list = dict()
        for synonym_line in lines:
            synonym_line = synonym_line.rstrip("\n")
            words = synonym_line.split(",")
            emotion_curr = words[0]
            synonyms = words[1:]
            emotions_list[emotion_curr] = synonyms
        emotions_file.close()

        for word in line_listForm:
            words_toAppend = []
            if word == "anger":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "disgust":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "fear":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "joy":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "love":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "sadness":
                words_toAppend.append(word)
                emotion_rich = True
            elif word == "surprise":
                words_toAppend.append(word)
                emotion_rich = True
            elif word in emotions_list:
                emotion_rich = True
                words_toAppend.append(word)

        for word in words_toAppend:
            line_listForm.append(word)

        if emotion_rich:
            line_listForm.append("emotion_rich")

        line = ""

        for word in line_listForm:
            line = line + " " + word

        line = line[1:] # remove empty space at begining

            # line = line + " " + "emotion_rich"

        cleaned_tweets = np.append(cleaned_tweets,  line)

    file.close()

    outfile = open("clean_test.txt", 'w')

    for line in cleaned_tweets:
        outfile.write(line + "\n" )

    outfile.close()

    return cleaned_tweets

