from drf_yasg import openapi


memo_schema = openapi.Schema(type=openapi.TYPE_OBJECT, properties={
	'importance': openapi.Schema(type=openapi.TYPE_STRING, description='memo importance level (high, middle, low)'),
	'theme': openapi.Schema(type=openapi.TYPE_STRING, description='memo theme'),
	'description': openapi.Schema(type=openapi.TYPE_STRING, description='memo description'),
	'time_to_send': openapi.Schema(type=openapi.TYPE_STRING, description='time_to_send'),
})
