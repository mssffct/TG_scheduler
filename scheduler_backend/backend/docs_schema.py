from drf_yasg.openapi import Schema, TYPE_STRING, TYPE_OBJECT


error_response = Schema(type=TYPE_OBJECT, properties={
	'description': Schema(type=TYPE_STRING, description="error description")
})

success_response = Schema(type=TYPE_OBJECT, properties={
	'message': Schema(type=TYPE_STRING, description="error description")
})
