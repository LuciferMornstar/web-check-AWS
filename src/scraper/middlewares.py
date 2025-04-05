class CustomUserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers['User-Agent'] = 'Your Custom User Agent'
        
class CustomRetryMiddleware:
    def process_response(self, request, response, spider):
        if response.status != 200:
            return request
        return response

class CustomDownloaderMiddleware:
    def process_request(self, request, spider):
        # Custom processing before the request is sent
        return None

    def process_response(self, request, response, spider):
        # Custom processing after the response is received
        return response

    def process_exception(self, request, exception, spider):
        # Handle exceptions that occur during the request
        return None