import threading

from src.neuro_comma.predict import RepunctPredictor


class ModelCache(object):
    """ """
    __shared_state = {
        "_model": None,
        "_lock": threading.Lock()
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def load_model(self):
        if self._model is None:
            with self._lock:
                if self._model is None:
                    # загружаем модель
                    self._model = RepunctPredictor('repunct-model_ft', model_weights='weights_ep1_9741.pt')

    @property
    def model(self) -> RepunctPredictor:
        self.load_model()
        return self._model
