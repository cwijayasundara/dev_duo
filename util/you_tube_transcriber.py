from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from util.file_util import save_file_youtube

formatter = TextFormatter()

response = YouTubeTranscriptApi.get_transcript("JhCl-GeT4jw&t=7s")

text_formatted = formatter.format_transcript(response)

""" save the text_formatted to a file named 'docs/transcript.txt' """

# assuming text_formatted is defined and contains the text to be saved
filename = 'matt_transcript.txt'
directory = '../docs/'

save_file_youtube(text_formatted, filename, directory)

