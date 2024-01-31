from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

memo_schema = Schema(type=TYPE_OBJECT, properties={
	'importance': Schema(type=TYPE_STRING, description='memo importance level (high, middle, low)'),
	'theme': Schema(type=TYPE_STRING, description='memo theme'),
	'description': Schema(type=TYPE_STRING, description='memo description'),
	'time_to_send': Schema(type=TYPE_STRING, description='time_to_send'),
})
