import sys
import json
from watson_developer_cloud import ToneAnalyzerV3
from .credentials import watson_credentials, youtube_credentials
import requests
from operator import itemgetter


def get_comments(video):
	print(video)
	url = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&videoId='+ video +'&key=' + youtube_credentials['api_key']

	print('url', url)
	r = requests.get(url)
	comment_dict = list()
	for item in r.json()['items']:
		the_comment = {"text": item['snippet']['topLevelComment']['snippet']['textOriginal']}
		comment_dict.append(the_comment)

	return json.dumps(comment_dict)




def sentiment_analysis(words):

	tone_analyzer = ToneAnalyzerV3(
	username=watson_credentials['username'],
	password=watson_credentials['password'],
	version='2016-02-11')

	return_sentiment = json.dumps(tone_analyzer.tone(text=words, sentences=False), indent=2)
	return_sentiment = json.loads(return_sentiment)
	comment_template_object = []
	for tone in return_sentiment['document_tone']['tone_categories']:
		tone_obj = {}
		tone_obj['category_name'] = tone['category_name']
		tone_obj['category_id'] = tone['category_id']

		print(comment_template_object)
		score_list = list()
		for score in tone['tones']:
			score_obj = {}
			score_obj['score'] = score['score']
			score_obj['tone_id'] = score['tone_id']
			score_obj['tone_name'] = score['tone_name']

			score_list.append(score_obj)

		sorted_score = sorted(score_list, key=itemgetter('score'), reverse=True)
		tone_obj['scores'] = sorted_score

		comment_template_object.append(tone_obj)

	return json.dumps(comment_template_object)


def main(video):

	comments = get_comments(video)

	sentiment = sentiment_analysis(comments)

	return sentiment
