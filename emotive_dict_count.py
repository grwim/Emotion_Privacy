import pdb
import csv
import tweet_processing
import svc_emotions
from nltk.tokenize import word_tokenize

def output_list_from_csv(emotion):
    filename = emotion + '.csv'

    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        synonym_list = list(reader)[0]
    return synonym_list

tweets_legacy= tweet_processing.clean("tweets_full.txt")
labels_legacy = svc_emotions.file_to_array("labels_full.txt")

emotion_list = ['anger', 'disgust', 'fear', 'joy', 'love', 'sadness', 'surprise',]

all_processed_tweets = []

count_TP = {'anger': 0,
                                    'disgust': 0,
                                    'fear': 0,
                                    'joy': 0,
                                    'love': 0,
                                    'sadness': 0,
                                    'surprise': 0}

count_FP = {'anger': 0,
                                    'disgust': 0,
                                    'fear': 0,
                                    'joy': 0,
                                    'love': 0,
                                    'sadness': 0,
                                    'surprise': 0}

count_FN = {'anger': 0,
                                    'disgust': 0,
                                    'fear': 0,
                                    'joy': 0,
                                    'love': 0,
                                    'sadness': 0,
                                    'surprise': 0}

dictionary_hit_count_TOTAL = {'anger': 0,
                                    'disgust': 0,
                                    'fear': 0,
                                    'joy': 0,
                                    'love': 0,
                                    'sadness': 0,
                                    'surprise': 0}

count_emotional_CORRECT = {'anger': 0,
                                    'disgust': 0,
                                    'fear': 0,
                                    'joy': 0,
                                    'love': 0,
                                    'sadness': 0,
                                    'surprise': 0}

count_tweets_per_emotion = {'anger': 0,
                                    'disgust': 0,
                                    'fear': 0,
                                    'joy': 0,
                                    'love': 0,
                                    'sadness': 0,
                                    'surprise': 0}

# load in each dictionary into a list

none_total = 0

# go through each tweet
for x in range(0, len(tweets_legacy)):

    tweet = tweets_legacy[x]
    tweet = word_tokenize(tweet)

    # reintilize dict hit counts
    dictionary_hit_count = {'anger': 0,
                                        'disgust': 0,
                                        'fear': 0,
                                        'joy': 0,
                                        'love': 0,
                                        'sadness': 0,
                                        'surprise': 0}


    # reset bool for whether any dictionary was hit for a tweet
    no_dict_hit = True

# count # of hits of each dictionary for a given tweet
    # for each word in tweet
    for word in tweet:
        # check word against each dictionary
        # go through each emotion dictinoary
        for emotion in emotion_list:
            snyonym_list = output_list_from_csv(emotion)
            if word in snyonym_list:
                no_dict_hit = False
                # increment count
                dictionary_hit_count[emotion] = dictionary_hit_count[emotion] + 1
                dictionary_hit_count_TOTAL[emotion] = dictionary_hit_count_TOTAL[emotion] + 1

# if no hit with any dict, then increment
    label_predicted = ''
    freq_max = 0
    if no_dict_hit:
        # label as 'none'
        label_predicted = 'none'
        none_total = none_total + 1
    else:
        # use max hit count to select best fitting dictionary
        label_predicted = max(dictionary_hit_count, key=dictionary_hit_count.get)
        freq_max = dictionary_hit_count[label_predicted]

#   ---- tweet, hit count, predicted label, actual label
    processed_tweet = []
    processed_tweet.append(tweet)
    processed_tweet.append(freq_max)
    processed_tweet.append(label_predicted)
    processed_tweet.append(labels_legacy[x])

    all_processed_tweets.append(processed_tweet)



# --- meta statistics ---
# count of total hits for each dictionary
# co occurence stats

# statistics for correct predictions for each emotion

# number tweets with 1 dict hit, 2 seperate dict hits, 3, etc.

total_tweet_count = 0
for emotion in emotion_list:
    emotion_tweet_count = 0
    print
    print
    print
    print
    print emotion
    for processed_tweet in all_processed_tweets:
        if emotion == processed_tweet[3]: # print all tweets that belong to that emotion
            emotion_tweet_count = emotion_tweet_count + 1
            total_tweet_count = total_tweet_count + 1

            # processed_tweet[2] != 'none' & processed_tweet[3] != 'none'
            if  ((processed_tweet[2]  != 'none' ) & (processed_tweet[3] != 'none')):
                count_emotional_CORRECT[emotion] = count_emotional_CORRECT[emotion] + 1

            if processed_tweet[2] == processed_tweet[3]: # if true positive
                count_TP[emotion] = count_TP[emotion] + 1

            # ascribed label is emotional and the real label is none
            elif ((processed_tweet[2] != 'none') & (processed_tweet[3] == 'none')):
                 count_FP[emotion] = count_FP[emotion] + 1

            # ascribed label is none and the real label is emototional
            elif (processed_tweet[2] == 'none') & (processed_tweet[3] != 'none'):
                 count_FN[emotion] = count_FN[emotion] + 1

            for item in processed_tweet:
                if isinstance(item, list):
                    for x in item:
                        print x,
                    print
                else:
                    print item,
            print
            print
    count_tweets_per_emotion[emotion] = emotion_tweet_count

    # print total tweets for that emotion
    print 'Total ', emotion, ' tweets: ', count_tweets_per_emotion[emotion]
    print 'True Positives from max dict hit method: ', count_TP[emotion]


# print none
print
print
print 'none'
none_tweet_count = 0
count_none_TP = 0
count_none_FP = 0
count_none_FN = 0

for processed_tweet in all_processed_tweets:
        if 'none' == processed_tweet[3]: # print all tweets that belong to that emotion
            total_tweet_count = total_tweet_count + 1
            none_tweet_count = none_tweet_count + 1

            if processed_tweet[2] == processed_tweet[3]: # if true positive
                count_none_TP = count_none_TP + 1
            if ((processed_tweet[2] == 'none') & (processed_tweet[3] != 'none')): # if true positive
                count_none_FP = count_none_FP + 1
            if ((processed_tweet[2] != 'none') & (processed_tweet[3] == 'none')): # if true positive
                count_none_FN = count_none_FN + 1

            for item in processed_tweet:
                if isinstance(item, list):
                    for x in item:
                        print x,
                    print
                else:
                    print item,
            print
            print

print 'Total none tweets: ', none_tweet_count
print 'TP [Correctly labelled as none]: ', count_none_TP
print 'FP [Ascribed label is none and the real label is emotional]: ', count_none_FP
print 'FN [Ascribed label is emotional and the real label is none]:', count_none_FN
print

# get total dictionary hits for each emotion
# and average emotional hits per dictionary
print '----- Macro Data -----'
print 'average dictionary hits for each emotion using ', total_tweet_count, ' tweets: '
for emotion in emotion_list:
    print emotion, ' dictionary hits: ', (dictionary_hit_count_TOTAL[emotion] / float(count_tweets_per_emotion[emotion]))


# (break out: all, TP, FP ) across each emotion
for emotion in emotion_list:
    print
    print emotion, ': ', count_tweets_per_emotion[emotion]
    print 'Correctly labeled emotion: ', count_TP[emotion]
    print 'TP [Correctly labelled as emotional]: ', count_emotional_CORRECT[emotion]
    print 'FP [Ascribed label is emotional and the real label is none]: ', count_FP[emotion]
    print 'FN [Ascribed label is none and the real label is emotional]: ', count_FN[emotion]

print
print 'Total none tweets: ', none_tweet_count
print 'TP [Correctly labelled as none]: ', count_none_TP
print 'FP [Ascribed label is none and the real label is emotional]: ', count_none_FP
print 'FN [Ascribed label is emotional and the real label is none]:', count_none_FN

