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

# DONT FORTGET ABOUT 'none

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

for emotion in emotion_list:
    tweet_count = 0
    print
    print
    print
    print
    print emotion
    for processed_tweet in all_processed_tweets:
        if emotion == processed_tweet[3]: # print all tweets that belong to that emotion
            tweet_count = tweet_count + 1

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

    # print total tweets for that emotion
    print 'Total ', emotion, ' tweets: ', tweet_count
    print 'True Positives from max dict hit method: ', count_TP[emotion]


# print none
tweet_count = 0
print
print
print 'none'
for processed_tweet in all_processed_tweets:
        if 'none' == processed_tweet[3]: # print all tweets that belong to that emotion
            tweet_count = tweet_count + 1

            if processed_tweet[2] == processed_tweet[3]: # if true positive
                count_TP[emotion] = count_TP[emotion] + 1

            for item in processed_tweet:
                if isinstance(item, list):
                    for x in item:
                        print x,
                    print
                else:
                    print item,
            print
            print

print 'Total none tweets: ', tweet_count
print 'True Positives from max dict hit method: ', count_TP[emotion]
print
print

# TO DO NEXT

# get total dictionary hits for each emotion
# and average emotional hits per dictionary
print '----- Macro Data -----'
print 'average dictionary hits for each emotion using ', tweet_count, ' tweets: '
for emotion in emotion_list:
    print emotion, ' dictionary hits: ', (dictionary_hit_count_TOTAL[emotion] / float(tweet_count))


# (break out: all, TP, FP ) across each emotion
# add functionality to print only correctly labelled, [TP]
# only ones that arent correct (ascribed the current emotion as label, but was wrong) [FP] --> (bad synonyms in dictionary)
# and ones that were labeled as 'none' [FN]   --> (need expansion of dictonary for that emotion)
for emotion in emotion_list:
    print
    print emotion
    print 'TP: ', count_TP[emotion]
    print 'FP: ', count_FP[emotion]
    print 'FN: ', count_FN[emotion]



# then, for each label (7 emotions, 1 non emotion )

    # organize tweets by actual labels

    # print tweets with that label, hit count, and emotion prediction off of dict hit count

# at end,
# columns for meta information (column for each emotion )
