import maya.OpenMayaUI as omui

def maya_main_window():
    """Return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)

class GeneratorUI(QtWidgets.QDialog):

    def __init__(self):
        """Constructor"""
        # Passing the object SimpleUI as an argument to super()
        # makes this line python 2 and 3 compatible
        super(GeneratorUI, self).__init__(parent=maya_main_window())
        self.scene = mayautils.SceneFile()
        self.setWindowTitle("Level Generator")
        self.resize(200, 500)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.title_lbl = QtWidgets.QLabel("Level Generator")
        self.title_lbl.setStyleSheet("font: bold 20px")
        