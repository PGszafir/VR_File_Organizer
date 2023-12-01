from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
from pyzbar.pyzbar import decode

class QRCodeScannerApp(App):
    def build(self):
        # Inicjalizacja obiektu kamery
        self.cap = cv2.VideoCapture(0)  # 0 oznacza użycie pierwszej dostępnej kamery

        # Sprawdzamy, czy kamera została poprawnie otwarta
        if not self.cap.isOpened():
            print("Błąd: Nie można otworzyć kamery.")
            self.stop()

        self.layout = BoxLayout(orientation='vertical')

        # Wczytaj obraz video_image
        self.video_image = cv2.imread('zdjecie.png')

        # Dodaj przyciski do interfejsu użytkownika
        scan_button = Button(text='Skanuj', on_press=self.scan_qr_code)
        generate_button = Button(text='Generuj kody QR', on_press=self.generate_qr_code)

        self.layout.add_widget(scan_button)
        self.layout.add_widget(generate_button)

        # Utwórz widżet do wyświetlania obrazu
        self.image_widget = Image()

        # Dodaj widżet obrazu do interfejsu użytkownika
        self.layout.add_widget(self.image_widget)

        # Uruchom cykliczne odświeżanie obrazu z kamery
        Clock.schedule_interval(self.update, 1.0 / 30.0)

        return self.layout

    def scan_qr_code(self, instance):
        decoded_objects = decode(self.current_frame)

        for obj in decoded_objects:
            rect_points = obj.polygon
            if len(rect_points) == 4:
                rect_points = [(int(point.x), int(point.y)) for point in rect_points]

                if self.video_image is not None and self.video_image.shape[0] > 0 and self.video_image.shape[1] > 0:
                    roi = self.current_frame[rect_points[0][1]:rect_points[2][1], rect_points[0][0]:rect_points[2][0]]

                    if roi.shape[0] > 0 and roi.shape[1] > 0:
                        video_image_resized = cv2.resize(self.video_image, (roi.shape[1], roi.shape[0]))

                        self.current_frame[rect_points[0][1]:rect_points[2][1],
                        rect_points[0][0]:rect_points[2][0]] = video_image_resized

    def generate_qr_code(self, instance):
        # Tutaj możesz dodać kod do generowania kodów QR
        pass

    def update(self, dt):
        # Odczytaj obraz z kamery
        ret, frame = self.cap.read()

        # Sprawdź, czy odczyt z kamerki powiódł się
        if not ret:
            print("Błąd: Brak obrazu z kamery.")
            self.stop()

        self.current_frame = frame

        # Konwersja obrazu do formatu tekstury Kivy
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tobytes()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # Wyświetl obraz
        self.image_widget.texture = texture1

    def on_stop(self):
        # Zwolnij zasoby i zamknij okno z obrazem
        self.cap.release()

if __name__ == '__main__':
    QRCodeScannerApp().run()