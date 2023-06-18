from filestack import Client, Filelink

class FileSharer:
    """Requires FileStack API key, which you can get by registering for free FileStack account"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.filestack_client = Client(api_key)   # filestack.com API key

    def share(self, file_path: str) -> str:
        """Uploads file to filestack and returns URL string"""

        new_filelink = self.filestack_client.upload(filepath=file_path)
        # print(new_filelink.url)
        return new_filelink.url