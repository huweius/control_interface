import thread


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.image import AsyncImage
from callbacks.main_menu import *
from custom.widgets.picture_button import *
from custom.widgets.adjustments import BinaryAdjustment
from __root__ import *


class RecordingButtonsLayout(GridLayout):
    def __init__(self):
        super(RecordingButtonsLayout, self).__init__(cols=2)
        self.spacing = 10
        self.add_widget(PicturedButton(icon_path('video-camera.png'), default_callback, id='StartRecording'))
        self.add_widget(PicturedButton(icon_path('stop2.png'), default_callback, id='EndRecording'))


class MainMenuLayout(GridLayout):
    def __init__(self):
        super(MainMenuLayout, self).__init__(rows=4)

        self.padding = 10
        self.spacing = 10

        camera_control_button = Button(text='Lens Controls')
        camera_control_button.bind(on_release=camera_control_callback)
        self.add_widget(camera_control_button)

        movement_control_button = Button(text='Motion Controls')
        movement_control_button.bind(on_release=movement_control_callback)
        self.add_widget(movement_control_button)

        settings_button = Button(text='Settings')
        settings_button.bind(on_release=setting_callback)
        self.add_widget(settings_button)

        self.add_widget(RecordingButtonsLayout())


class LensControlMenuLayout(GridLayout):
    def __init__(self):
        super(LensControlMenuLayout, self).__init__(rows=4)

        self.padding = 10
        self.spacing = 10

        self.add_widget(BinaryAdjustment('Zooming', default_callback, default_callback))
        self.add_widget(BinaryAdjustment('Focusing', default_callback, default_callback))
        self.add_widget(PicturedButton(icon_path('undo2.png'), return_button_callback))

        self.add_widget(RecordingButtonsLayout())


class MotionControlMenuLayout(GridLayout):
    def __init__(self):
        super(MotionControlMenuLayout, self).__init__(rows=5)

        self.padding = 10
        self.spacing = 10

        self.add_widget(BinaryAdjustment('Height', default_callback, default_callback))
        self.add_widget(BinaryAdjustment('Panning', default_callback, default_callback))
        self.add_widget(BinaryAdjustment('Tilting', default_callback, default_callback))
        self.add_widget(PicturedButton(icon_path('undo2.png'), return_button_callback))

        self.add_widget(RecordingButtonsLayout())


class MainLayout(GridLayout):
    def __init__(self, handedness='right'):
        super(MainLayout, self).__init__(cols=2, background='white')
        # self.preview_screen = Camera()
        self.preview_screen = AsyncImage(source='http://www.president.gov.ua/storage/j-image-storage/01/89/38/94033d27b2015f3db8d5afa29ab92bb3_1444821939_large.png')
        self.menus = {'main': MainMenuLayout(), 'lens': LensControlMenuLayout(), 'motion': MotionControlMenuLayout()}
        if handedness == 'right':
            self.add_widget(self.preview_screen)
            self.add_widget(self.menus['main'])
            self.menu_index = 2
        else:
            self.add_widget(self.menus['main'])
            self.add_widget(self.preview_screen)
            self.menu_index = 1





class ControlInterface(App):

    def build(self):
        # self.build(super)

        return MainLayout(handedness='left')

if __name__ == '__main__':
    ControlInterface().run()