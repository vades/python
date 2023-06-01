from libs.commonutils import CommonUtils as cu


class Config:
    pass


cfg = Config()
# App config
app_config_path = 'settings/config.json'
cfg.app = cu.read_json(app_config_path)
