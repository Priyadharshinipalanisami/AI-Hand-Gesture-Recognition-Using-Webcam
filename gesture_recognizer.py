import math


class GestureRecognizer:

    @staticmethod
    def distance(p1, p2):
        return math.sqrt(
            (p1.x - p2.x) ** 2 +
            (p1.y - p2.y) ** 2
        )

    def recognize(self, landmarks):

        # Landmark points
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]

        index_tip = landmarks[8]
        index_pip = landmarks[6]

        middle_tip = landmarks[12]
        middle_pip = landmarks[10]

        ring_tip = landmarks[16]
        ring_pip = landmarks[14]

        pinky_tip = landmarks[20]
        pinky_pip = landmarks[18]

        # Check finger extension
        index_extended = index_tip.y < index_pip.y
        middle_extended = middle_tip.y < middle_pip.y
        ring_extended = ring_tip.y < ring_pip.y
        pinky_extended = pinky_tip.y < pinky_pip.y

        # Thumb detection
        thumb_extended = (
            self.distance(thumb_tip, landmarks[5])
            >
            self.distance(thumb_ip, landmarks[5])
        )

        # -----------------------------
        # Open Hand
        # -----------------------------
        if (
            thumb_extended
            and index_extended
            and middle_extended
            and ring_extended
            and pinky_extended
        ):
            return "Open Hand"

        # -----------------------------
        # Fist
        # -----------------------------
        if (
            not thumb_extended
            and not index_extended
            and not middle_extended
            and not ring_extended
            and not pinky_extended
        ):
            return "Fist"

        # -----------------------------
        # Victory / Peace
        # -----------------------------
        if (
            index_extended
            and middle_extended
            and not ring_extended
            and not pinky_extended
        ):
            return "Victory / Peace"

        # -----------------------------
        # Thumbs Up
        # -----------------------------
        if (
            thumb_extended
            and not index_extended
            and not middle_extended
            and not ring_extended
            and not pinky_extended
        ):
            return "Thumbs Up"

        return "Unknown"