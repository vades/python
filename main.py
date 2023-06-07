from settings.config import cfg
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv('MYENV'))


print(cfg.app)
