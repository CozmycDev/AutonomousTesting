class FileFormatter:
    @staticmethod
    def format_file(file_name: str, content: str = None):
        if not content:
            raise ValueError("Content is required")
        try:
            with open(file_name, "w") as file:
                json.dump({"content": content}, file)
        except Exception as e:
            print(f"Error saving to file: {e}")
    
    @staticmethod
    def format_file_from_json(file_name: str):
        data = None
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"No JSON file found at {file_name}")
        except Exception as e:
            print(f"Error loading from file: {e}")

        return data.get("content", None)