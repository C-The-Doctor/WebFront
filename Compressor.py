from flask import Flask  , url_for , render_template , request , redirect
from flask.views import View
from flask import g
import os , random , string
from werkzeug.utils  import secure_filename
import time

app=Flask(__name__)


class HomeCenter(View):
    def dispatch_request(self):
      
        User = "Uni-Identified"
        return render_template('HomePage.html', User=User)

class ServicesCenter(View):
    def dispatch_request(self):
      
     
        User = "Uni-Identified"
        return render_template('Services.html', User=User )

class ContactCenter(View):
    def dispatch_request(self):
      
      
        User = "Uni-Identified"
        return render_template('ContactPage.html', User=User )



app.add_url_rule('/Home/', view_func=HomeCenter.as_view('root'))
app.add_url_rule('/Services/', view_func=ServicesCenter.as_view('Services'))
app.add_url_rule('/Contact/', view_func=ContactCenter.as_view('Contact'))





# Main Execution Block
# Rendering With Openssl : ADHOC
# Running This Script Requires The Following
         # Openssl Binary Value Should Be Set To Zero
         # Xml Parser :: Expat Should be of version > 2 Not Lower
         # For Systems With Low Expat Versions :
               #Serialization Is therefore defaulted to Json

if __name__=='__main__':

   # Database Creation Section
  # DB_InitializationWizard("/static/Databases/Doctored_Databases.db")

   app.run("0.0.0.0" , debug="False" )
