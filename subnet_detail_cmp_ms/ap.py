# -*- coding: utf-8 -*-
''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
import sys
import json
import ast   # Cast
import flask
from flask import Flask, request, jsonify, make_response
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from cmpcomputo.integration.ops.services.subnet.subnetServices import EnsemblSubnetRestClientServices
try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError
APP = Flask(__name__)
APP.config["DEBUG"] = True

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
@APP.route('/', methods=['GET'])
def home():
    return '''<h1>CMP v2.0 Subnet Detail</h1>
<p>A prototype API for testing Cloud Cmp  Microservices v2.0 [api-ref/network/v2/]</p>'''

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
@APP.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message":"pong !  New version From CMP v2.0 Microservices "})

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
def obj_to_dict(obj):
    return obj.__dict__


''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
@APP.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
@APP.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
@APP.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
@APP.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''

@APP.route('/api/v1/resources/subnets/detail/<string:subnet_id>', methods=['GET'])
def Detail(subnet_id):
    try:
        content1 = request.get_data()
        if ('bytes' in str(type(content1))):
            content1 = ast.literal_eval(content1.decode("utf-8"))
        else:
            content1 = json.loads(content1.json())
        project_Id = content1['project_id']
        user = content1['user']
    except:
        project_Id=None
        user = None
    client = EnsemblSubnetRestClientServices()
    response=client.getDetail(subnet_id,project_Id, user)
    myRes =  response
    print(myRes)
    return myRes

if(__name__=="__main__"):
    APP.run(host="0.0.0.0", port=7002, debug=True)
