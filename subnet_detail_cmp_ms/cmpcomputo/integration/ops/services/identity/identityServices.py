''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
import sys
import json
import traceback
import requests
from cmpcomputo.integration.ops.common.MetaData import AuthToken, ErrorMessage, Network, Subnet
from cmpcomputo.integration.ops.common.IdentityMetaData import UserProject, Project
from cmpcomputo.integration.ops.common.CloudService import CloudService

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: KIO Networks S.A. de C.V.
@license: KIO
@date:     10032020
@summary: Lista las imagenes en un template
********************************************************************************* '''
class AuthenticationServices(CloudService):
    def __init__(self, server='', reqs_per_sec=15):
        self.server = server
        self.reqs_per_sec = reqs_per_sec
        self.req_count = 0
        self.last_req = 0
    def validate_key(self,node,key):
        if key in node :
            return node[key]
        else:
            return ""
    ''' ****************************************************************************
    @author: Juan Carlos Perez Hernandez
    @contact: jcphgy@gmail.com; jperezh@kionetworks.com
    @copyright: KIO Networks S.A. de C.V.
    @license: KIO
    @date:     10032020
    @summary: Lista las imagenes en un template
    ********************************************************************************* '''
    def getAutenticaIdentidad(self,  userWithProjects=None):
        try:
            __OPS_API_KEYSTONE_IDENTITY_AUTH_ =   self._OPS_API_KEYSTONE_IDENTITY_AUTH 
            self.OPS_KEYSTONE_URL_TOKEN_ENDPOINT =__OPS_API_KEYSTONE_IDENTITY_AUTH_+self.API_MODULO_KEYSTONE_IDENTITY_AUTH
            if (userWithProjects != None):
                passwordUsr=userWithProjects.password
                nameUsr=userWithProjects.name
                self.authData='{ "auth": { "identity": { "methods": ["password"],"password": {"user": {"name": "'+nameUsr+'","domain": {"name": "Default"},"password": "'+passwordUsr+'"}}}}}'
            if (userWithProjects != None):
                response = requests.post(self.OPS_KEYSTONE_URL_TOKEN_ENDPOINT.format(self.OPS_CONTROLLER_IP), data=self.authData, verify=self.API_OPS_API_SSL_CERTIFICATE_VERIFY)
                jData = json.loads(response.content)
                if(response.ok):
                    projectId=jData[self.API_MODULO_KEYSTONE_IDENTITY_TOKEN][self.API_MODULO_KEYSTONE_IDENTITY_USER][self.API_MODULO_KEYSTONE_IDENTITY_NAME]
                    projectName=jData[self.API_MODULO_KEYSTONE_IDENTITY_TOKEN][self.API_MODULO_KEYSTONE_IDENTITY_USER][self.API_MODULO_KEYSTONE_IDENTITY_DOMAIN][self.API_MODULO_KEYSTONE_IDENTITY_NAME]
                    tokenId=response.headers[self.API_MODULO_KEYSTONE_IDENTITY_RESPONSE_HEADERS_SUBJECT_TOKEN]
                    userId=jData[self.API_MODULO_KEYSTONE_IDENTITY_TOKEN][self.API_MODULO_KEYSTONE_IDENTITY_USER][self.API_MODULO_KEYSTONE_IDENTITY_ID]
                    authToken=AuthToken(projectId,projectName,tokenId,userId)
                    return authToken
                else:
                    authToken= None
                    return authToken
            else:
                authToken= None
                return authToken
        except:
            except1 = sys.exc_info()[0]
            projectId=None
            projectName=None
            tokenId=None
            authToken=AuthToken(projectId,projectName,tokenId)
            authToken.errorMessage = ErrorMessage(" ConnectionError Max retries exceeded "+str(except1))
            traceback.print_exc()
            return authToken    