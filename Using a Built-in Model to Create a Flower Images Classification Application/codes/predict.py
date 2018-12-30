from PIL import Image
import numpy as np
from model_service.tfserving_model_service import TfServingBaseService


class flowers_service(TfServingBaseService):

    def _preprocess(self, data):
        preprocessed_data = {}

        for k, v in data.items():
            for file_name, file_content in v.items():
                image1 = Image.open(file_content)
                image1 = np.array(image1, dtype=np.float32)
                image1.resize((1, 224, 224, 3))
                preprocessed_data[k] = image1

        return preprocessed_data
		
	
