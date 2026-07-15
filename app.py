"""
=========================================================
 Marketplace Calculator Pro
---------------------------------------------------------
 Entry Point
---------------------------------------------------------
 Author  : RickProduction
 Framework : PySide6
=========================================================
"""

import os
import sys

from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


class MarketplaceCalculatorApp:
    """
    Main Application Loader
    """

    def __init__(self):

        self.app = QApplication(sys.argv)

        self.configure_application()

        self.window = MainWindow()

    def configure_application(self):
        """
        Configure global application settings.
        """

        self.app.setApplicationName("Marketplace Calculator Pro")
        self.app.setApplicationVersion("1.0.0")
        self.app.setOrganizationName("RickProduction")

        # Default Font
        self.app.setFont(QFont("Segoe UI", 10))

        # Window Icon
        icon_path = os.path.join(
            "assets",
            "icons",
            "app.ico"
        )

        if os.path.exists(icon_path):
            self.app.setWindowIcon(QIcon(icon_path))

        self.load_stylesheet()

    def load_stylesheet(self):
        """
        Load Qt Style Sheet
        """

        style_path = os.path.join(
            "styles",
            "dark.qss"
        )

        if not os.path.exists(style_path):
            return

        file = QFile(style_path)

        if file.open(QFile.ReadOnly | QFile.Text):

            stream = QTextStream(file)

            self.app.setStyleSheet(stream.readAll())

            file.close()

    def run(self):

        self.window.show()

        sys.exit(self.app.exec())


if __name__ == "__main__":

    application = MarketplaceCalculatorApp()

    application.run()