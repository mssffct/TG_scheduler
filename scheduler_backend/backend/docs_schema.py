from drf_yasg import openapi as op


error_response = op.Schema(type=op.TYPE_OBJECT, properties={
	'description': op.Schema(type=op.TYPE_STRING, description="error description")
})

success_response = op.Schema(type=op.TYPE_OBJECT, properties={
	'message': op.Schema(type=op.TYPE_STRING, description="error description")
})
