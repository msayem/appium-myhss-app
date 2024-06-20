from appium.webdriver.appium_service import AppiumService


class AppiumServer(object):
    def __init__(self):
        self.appium_service = AppiumService()

    def start_server(self):
        try:
            if not self.appium_service.is_running:
                self.appium_service.start()
                print("Appium server started successfully")
            else:
                print("Appium server is already running")
        except Exception as e:
            print(f"Failed to start Appium server: {str(e)}")

    def stop_server(self):
        try:
            self.appium_service.stop()
            print("Appium server stopped successfully")
        except Exception as e:
            print(f"Failed to stop Appium server: {str(e)}")


if __name__ == "__main__":
    # Example usage
    appium_server = AppiumServer()
    appium_server.start_server()
    # Do your testing or application logic here...
    appium_server.stop_server()
