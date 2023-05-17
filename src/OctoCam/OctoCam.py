import octoprint.plugin


class OctoNDI(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info('This Is the OctoNDI plugin')