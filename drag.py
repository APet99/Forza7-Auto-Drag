#  Copyright (c) 2021.
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
#  persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
#  Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#  COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#  End license text.

#
#
import os
import pyautogui as pyg
import cv2
import os
import time


def move_cursor(image: str, confidence_measure=0.75):
    """
    Moves the cursor to the location of something on the screen.
    :param image: The name and file extension of the image to search for on screen (ex. myImage.png)
    :param confidence_measure: From 0 - 1.0 how much confidence is required to assume true
    :return: The location of the found selection. If not found, returns None.
    """
    dir_to_images = os.path.join(os.getcwd(), 'images')
    try:
        location = pyg.locateCenterOnScreen(str(os.path.join(dir_to_images, image)), confidence=confidence_measure)
        pyg.moveTo(location)
        return location
    except Exception:
        pass

    return None


def is_on_screen(image: str, confidence_measure=0.75):
    """
    Determines if something is on the screen or not.
    :param image: :param image: The name and file extension of the image to search for on screen (ex. myImage.png)
    :param confidence_measure: From 0 - 1.0 how much confidence is required to assume true
    :return: The location of the found selection. If not found, returns None.
    """
    dir_to_images = os.path.join(os.getcwd(), 'images')
    try:
        location = pyg.locateCenterOnScreen(str(os.path.join(dir_to_images, image)), confidence=confidence_measure)
        return location
    except Exception:
        pass

    return None


def click_mouse():
    """
    Simulates a left click of the mouse
    """
    pyg.click(clicks=1)


if __name__ == "__main__":
    in_race = False
    while True:
        if not in_race:
            if move_cursor('StartRaceYellow.png', confidence_measure=.70) or move_cursor('StartRaceWhite.png',
                                                                                         confidence_measure=.70):
                pyg.dragRel(-25, 10, 1)
                pyg.dragRel(1, -1, .2)
                click_mouse()

                time.sleep(1)
                if not move_cursor('StartRaceYellow.png', confidence_measure=.70):
                    in_race = True

            elif move_cursor('RaceAgainWhite.png', confidence_measure=.70) or move_cursor('RaceAgainYellow.png',
                                                                                          confidence_measure=.70):
                pyg.dragRel(-25, 10, 1)
                pyg.dragRel(1, -1, .2)
                click_mouse()

                time.sleep(1)
                if not move_cursor('RaceAgain.png', confidence_measure=.70):
                    in_race = True

            if not in_race:
                time.sleep(1)
        else:
            while not is_on_screen('YellowLights3.png', confidence_measure=.90):
                # time.sleep(0.25) # If you launch too early, you can alter THIS value to add a delay before launching.
                pass

            pyg.keyDown('w')

            while not move_cursor('PostRaceContinue.png'):
                pass
                # In the future, support for manual shifting will be included.
                # if is_on_screen('TimeToShift3.png', confidence_measure=.80):
                #     pyg.press('num9')

            pyg.keyUp('w')
            pyg.press('enter')
            in_race = False
            time.sleep(.5)
