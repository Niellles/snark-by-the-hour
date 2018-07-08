import configparser
from stackapi import StackAPI
import json
import csv
from html import unescape
from nltk.sentiment import SentimentIntensityAnalyzer as SentimentAnalyzer
from nltk import download as nltkdownload

config = configparser.ConfigParser()
config.read('config.ini')

# with open('example-response.json', 'w') as json_file:
# 	SO = StackAPI('stackoverflow', key=config['stackexchange_auth']['APP_KEY'])
# 	comments = SO.fetch('comments', filter='!SYD0m(jE6Fj-kEAE(R')
# 	json_file.write(json.dumps(comments))

# Use prefeteched response for testing purposes.
with open('example-response.json', 'r') as json_file:
	response = json.loads(json_file.read())

with open('data/comments.csv', 'w', newline='', encoding='utf-8') as commentfile:
	fieldnames = [
					'comment_id', 'creation_date', 'post_id', 'link', 'score', 'edited',
					'owner_reputation', 'owner_user_id', 'owner_user_type', 'owner_accept_rate','owner_display_name', 'owner_link',
					'reply_to_user', 'reply_to_user_reputation', 'reply_to_user_user_id','reply_to_user_user_type',
					'reply_to_user_accept_rate', 'reply_to_user_display_name','reply_to_user_link', 
					'num_links', 'num_code', 'body'
				]

	writer = csv.DictWriter(commentfile, fieldnames=fieldnames)
	writer.writeheader()

	for item in response['items']:
		# if item['score'] <= int(config['filters']['MIN_VOTES']):
		# 	continue

		item_parsed = {}

		for key, value in item.items():
			if type(value) is dict:
				prefix = key + "_"
				
				# print(value)
				for k,v in value.items():
					item_parsed[prefix+k] = v
			else:
				item_parsed[key] = value

		# Clean up special chars in some of the fields.
		for key in ['body', 'owner_display_name', 'reply_to_user_display_name']:
			try:
				item_parsed[key] = unescape(item_parsed[key])
			except KeyError: # item_parsed['reply_to_user_display_name'] isn't always set.
				pass
		
		#################################################################
		## Extract some (extra) features from the data that we've got. ##
		#################################################################

		# Add (bool) reply_to_user
		try:
			item['reply_to_user']
			item_parsed['reply_to_user'] = True
		except KeyError:
			item_parsed['reply_to_user'] = False

		#####
		## Count tags in body

		## TODO: count with preg_replace style kinda thing (into temp string for analysis) and return replacements into num_tag
		## TODO: Do the above in a loop if possible. 
		# Add comment link count 
		item_parsed['num_links'] = item_parsed['body'].count('<a')
		
		# Add comment code count
		item_parsed['num_code'] = item_parsed['body'].count('<code')


		#####
		## Text analysis
		for attempt in range(2):
			try:
				sentiment = SentimentAnalyzer().polarity_scores(item_parsed['body'])
				break
				
				# This seems as good a place as any to cite Hutto & Gilbert. Thanks guys, your work is greatly appreciated!
				# Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
			except LookupError:
				nltkdownload('vader_lexicon')
		else:
			exit('Couldn\'t download vader_lexicon package. Ending execution.')

		print(sentiment)
		break
		# print(item_parsed.keys())
		# exit(

		writer.writerow(item_parsed)