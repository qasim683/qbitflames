import os 
import time 
import traceback 
import signal 
import sys 
 
from django.core.wsgi import get_wsgi_application 
 
sys.path.append('/var/www/django_apache2') 
# adjust the Python version in the line below as needed 
sys.path.append('/var/www/django_apache2/env') 
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qbit.settings") 
 
try: 
    application = get_wsgi_application() 
except Exception: 
    # Error loading applications 
    if 'mod_wsgi' in sys.modules: 
        traceback.print_exc() 
        os.kill(os.getpid(), signal.SIGINT) 
        time.sleep(2.5) 
