import os
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES = os.path.join(BASE_DIR, 'static')
print(STATICFILES)