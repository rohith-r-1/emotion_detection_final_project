import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # We simulate the API response so we don't need the actual server
        with patch('EmotionDetection.emotion_detection.requests.post') as mocked_post:
            mocked_post.return_value.status_code = 200
            mocked_post.return_value.text = '{"emotionPredictions": [{"emotion": {"joy": 0.9, "anger": 0.1, "disgust": 0, "fear": 0, "sadness": 0}}]}'
            
            result = emotion_detector('I am glad this happened')
            self.assertEqual(result['dominant_emotion'], 'joy')

if __name__ == "__main__":
    unittest.main()