import cv2
import mediapipe as mp


w_cam, h_cam = 720, 640

cap = cv2.VideoCapture(0)

cap.set(3, w_cam)
cap.set(4, h_cam)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)


tips_ID = [4, 8, 12, 16, 20]


def count_Fingers(image, hand_landmarks, handNo=0):
    if hand_landmarks:
        landmarks = hand_landmarks[handNo].landmark
        print(landmarks)


def draw_handlandmarks(image, hand_landmarks):
    if hand_landmarks:
        for landmark in hand_landmarks:
            mp_drawing.draw_landmarks(
                image, landmark, mp_hands.HAND_CONNECTIONS)


while True:
    success, image = cap.read()

    image = cv2.flip(image, 1)

    # Detect Hand's Landmarks 21 points
    results = hands.process(image)

    hand_landmarks = results.multi_hand_landmarks

    draw_handlandmarks(image, hand_landmarks)

    count_Fingers(image, hand_landmarks)

    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()
