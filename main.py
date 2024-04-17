import cv2
import mediapipe as mp
import mouse
from math import dist
import pyvolume

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()
video = cv2.VideoCapture(0)
while True:
    _,frame = video.read()
    frame = cv2.resize(frame,(500,500))
    frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand.process(frame1)



    if result.multi_hand_landmarks:
        #print(float(str(result.multi_hand_landmarks[-1].landmark[0]).split('\n')[0].split(" ")[1]))
        distx0 = float(str(result.multi_hand_landmarks[-1].landmark[0]).split('\n')[0].split(" ")[1])
        disty0 = float(str(result.multi_hand_landmarks[-1].landmark[0]).split('\n')[1].split(" ")[1])
        distx8 = float(str(result.multi_hand_landmarks[-1].landmark[8]).split('\n')[0].split(" ")[1])
        disty8 = float(str(result.multi_hand_landmarks[-1].landmark[8]).split('\n')[1].split(" ")[1])
        distx7 = float(str(result.multi_hand_landmarks[-1].landmark[7]).split('\n')[0].split(" ")[1])
        disty7 = float(str(result.multi_hand_landmarks[-1].landmark[7]).split('\n')[1].split(" ")[1])
        distx4 = float(str(result.multi_hand_landmarks[-1].landmark[4]).split('\n')[0].split(" ")[1])
        disty4 = float(str(result.multi_hand_landmarks[-1].landmark[4]).split('\n')[1].split(" ")[1])

        print(dist([distx0,disty0],[distx8,disty8]))
        print(dist([distx0,disty0],[distx7,disty7]))
        a1 = dist([distx0,disty0],[distx8,disty8])
        b1 = dist([distx0,disty0],[distx7,disty7])
        c1 = dist([distx8,disty8],[distx4,disty4])
        print(int(c1*100));
        pyvolume.custom(int(c1*100))
        if(a1 < b1):
            print("mouse click is right")
            mouse.click("left")
            mouse.click("left")
        else:
            for hand_landmarks in result.multi_hand_landmarks:
                x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*1000)
                y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*1000)

                mouse.move(2*x, y, absolute=True, duration=0.6)
            #print(mouse.get_position());
                mp_drawing.draw_landmarks(frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    # if result.multi_handedness:
    #     for hand_landmarks in result.multi_handedness:
    #         print(hand_landmarks)
    cv2.imshow("image",frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()

