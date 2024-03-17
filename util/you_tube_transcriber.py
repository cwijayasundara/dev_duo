from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

formatter = TextFormatter()

response = YouTubeTranscriptApi.get_transcript("JhCl-GeT4jw&t=7s")

text_formatted = formatter.format_transcript(response)

print(text_formatted)
