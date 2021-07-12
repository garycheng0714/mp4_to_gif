import cloudconvert

PAYLOAD = {
        "tasks": {
            'import-1': {
                'operation': 'import/upload'
            },
            "convert": {
                "operation": "convert",
                "input_format": "mp4",
                "output_format": "gif",
                "engine": "ffmpeg",
                "input": "import-1",
                "video_codec": "gif",
                "fps": 8,
                "filename": "fail.gif"
            },
            "export-1": {
                "operation": "export/url",
                "input": "convert"
            }
        }
    }


class CloudConvert:

    cloudconvert.configure(
        api_key='')

    def __init__(self, filename):
        self.job = cloudconvert.Job.create(payload=PAYLOAD)
        self.filename = filename

    def convert(self):
        self.__upload()
        self.__download()

    def __upload(self):
        upload_task_id = self.job['tasks'][0]['id']

        upload_task = cloudconvert.Task.find(id=upload_task_id)
        cloudconvert.Task.upload(file_name=self.filename, task=upload_task)
        cloudconvert.Task.wait(id=upload_task_id)

    def __download(self):
        exported_url_id = self.job['tasks'][2]['id']

        res = cloudconvert.Task.wait(id=exported_url_id)  # Wait for job completion
        file = res.get("result").get("files")[0]
        cloudconvert.download(filename=file['filename'], url=file['url'])
