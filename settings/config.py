from libs.AppConfig import AppConfig as helper


class Config:
    pass


cfg = Config()
# App config
app_config_path = 'settings/config.json'
cfg.app = helper.read_config(app_config_path)
