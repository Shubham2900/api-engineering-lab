import json

class WatermarkManager:
    def __init__(self, file_path="../state/watermark.json"):
        self.file_path = file_path

    def get(self, pipeline_name):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        return data.get(pipeline_name)

    def set(self, pipeline_name, watermark):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        data[pipeline_name] = watermark

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)