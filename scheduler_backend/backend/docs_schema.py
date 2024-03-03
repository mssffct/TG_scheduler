from drf_yasg.openapi import Schema, TYPE_STRING, TYPE_OBJECT


def get_error_response(description: str) -> Schema:
	return Schema(type=TYPE_OBJECT, properties={'description': Schema(type=TYPE_STRING, description=description)})


def get_success_response(description: str) -> Schema:
	return Schema(type=TYPE_OBJECT, properties={'message': Schema(type=TYPE_STRING, description=description)})


class DocsSchemaConstructor:
	def __init__(self, schema: bool = None, *args):
		self.construct_docs_schema(schema, args)

	@staticmethod
	def construct_docs_schema(schema: bool, args) -> dict | Schema:
		docs_schema = {}
		for item in args:
			docs_schema[item[0]] = Schema(type=item[1], description=item[2])
		if schema:
			return Schema(type=TYPE_OBJECT, properties=docs_schema)
		return docs_schema