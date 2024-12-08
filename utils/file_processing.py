python
import pandas as pd

class ExcelWriter:
    def write_to_excel(self, data, file_path):
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False)
