from drf_yasg.openapi import Schema, TYPE_STRING, TYPE_OBJECT


def get_error_response(description: str) -> Schema:
	return Schema(type=TYPE_OBJECT, properties={'description': Schema(type=TYPE_STRING, description=description)})


def get_success_response(description: str) -> Schema:
	return Schema(type=TYPE_OBJECT, properties={'message': Schema(type=TYPE_STRING, description=description)})
