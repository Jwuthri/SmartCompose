import os
from typing import List

from loguru import logger

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MultiLabelBinarizer

from smart_compose.api.models.payload import SentimentPayload, payload_to_list
from smart_compose.api.models.prediction import SentimentPredictionResult
from smart_compose.api.core.messages import NO_VALID_PAYLOAD, INVALID_TEXT_SIZE

from smart_compose.config import MIN_LENGTH_TEXT, MAX_LENGTH_TEXT


class SentimentModel(object):

    def __init__(self, model: tf.keras.models, label_encoder: MultiLabelBinarizer):
        self._model = model
        self._encoder = label_encoder

    @classmethod
    def from_path(cls, model_dir: str) -> object:
        model_path = os.path.join(model_dir, "model_name")
        model = tf.keras.models.load_model(model_path)
        preprocessor_path = os.path.join(model_dir, "processor_name")
        preprocessor = tf.keras.models.load_model(preprocessor_path)

        return cls(model, preprocessor)

    @staticmethod
    def _pre_process(payload: SentimentPayload) -> List:
        logger.debug("Pre-processing payload...")
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)

        return result

    def _predict(self, inputs) -> np.ndarray:
        logger.debug("Predicting...")

        return self._model.predict(inputs)

    @staticmethod
    def _post_process(prediction: np.ndarray) -> SentimentPredictionResult:
        logger.debug("Post-processing prediction...")
        result = SentimentPredictionResult()

        return result

    def predict(self, payload: SentimentPayload) -> SentimentPredictionResult:
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        if MIN_LENGTH_TEXT > len(payload.text.split()) > MAX_LENGTH_TEXT:
            raise ValueError(INVALID_TEXT_SIZE.format(MIN_LENGTH_TEXT, MAX_LENGTH_TEXT))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        post_processed_result = self._post_process(prediction)

        return post_processed_result
