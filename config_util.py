class File(BaseFileSection):
    def __init__(self, file_name: str, save_path: str, content: str = None):
        super().__init__("File", {"content": content} if content is not None else {"content": ""})
        self.file_name = file_name
        self.save_path = save_path

    @property
    def data(self) -> Dict[str, Any]:
        return super().data or {}

    def get_value(self) -> str:
        return self.data["content"]

    def save_to_file(self):
        import json
        try:
            with open(self.save_path, "w") as file:
                json.dump(self.data, file)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self):
        self._load_from_file(self.file_name)

file = File("example.txt", "path/to/file")
print(file.save_to_json)