activate_this = 'D:/shabaka/venv/Scripts/activate.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('D:/shabaka/venv/Lib/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('D:/shabaka/venv')
sys.path.append('D:/shabaka/venv/shop')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Predictor.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
