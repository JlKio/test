''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
import json
import datetime
import requests
from cmpcomputo.integration.ops.common.MetaData import  Subnet
from cmpcomputo.integration.ops.common.IdentityMetaData import UserProject
from cmpcomputo.integration.ops.common.CloudService import ComputeService
from cmpcomputo.integration.ops.services.identity.identityServices import AuthenticationServices
''' *****************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license:  MIT  
@date:     10032020
@summary:  Devuelve un listado de las sub redes de una red principal
*****************************************************************'''
class EnsemblSubnetRestClientServices(ComputeService, AuthenticationServices):
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
    def parse_subnet(self, dictionary):
        try:
            subnet_id=self.validate_key(dictionary,"id")
            nameid=str(subnet_id)[0:8]
            name=self.validate_key(dictionary,"name")
            hasname=False if (name == None) or (len(name.strip())<1) else True
            name=name if hasname else nameid
            description=self.validate_key(dictionary,"description")
            enable_dhcp=self.validate_key(dictionary,"enable_dhcp")
            network_id=self.validate_key(dictionary,"network_id")
            tenant_id=self.validate_key(dictionary,"tenant_id")
            created_at_cadena=self.validate_key(dictionary,"created_at")
            dns_nameservers=self.validate_key(dictionary,"dns_nameservers")
            nEsta_T=created_at_cadena.find("T")
            cOnlyDate=""
            if (nEsta_T>8):
                cOnlyDate = created_at_cadena[0:nEsta_T]
            else:
                cOnlyDate = created_at_cadena[0:9]
            created_at=cOnlyDate
            updated_at=self.validate_key(dictionary,"updated_at")
            ipv6_ra_mode=self.validate_key(dictionary,"ipv6_ra_mode")
            allocation_pools=self.validate_key(dictionary,"allocation_pools")
            gateway_ip=self.validate_key(dictionary,"gateway_ip")
            revision_number=self.validate_key(dictionary,"revision_number")
            ipv6_address_mode=self.validate_key(dictionary,"ipv6_address_mode")
            ip_version=self.validate_key(dictionary,"ip_version")
            host_routes=self.validate_key(dictionary,"host_routes") #Lista
            cidr=self.validate_key(dictionary,"cidr")
            project_id=self.validate_key(dictionary,"project_id")
            subnetpool_id=self.validate_key(dictionary,"subnetpool_id")
            neutron_subnet= Subnet(subnet_id,name,description,enable_dhcp,network_id,tenant_id,created_at,dns_nameservers,updated_at,ipv6_ra_mode,allocation_pools,gateway_ip,revision_number,ipv6_address_mode,ip_version,host_routes,cidr,project_id,subnetpool_id)
            return neutron_subnet
        except:
            neutron_subnet=None
            return neutron_subnet    
    ''' *****************************************************************
    @author: Juan Carlos Perez Hernandez
    @contact: jcphgy@gmail.com; jperezh@kionetworks.com
    @copyright: Kion Networks S.A. de C.V.
    @license: MIT
    @date:     10032020
    @summary:  Devuelve un listado de las sub redes de una red principal
    *****************************************************************'''
    def getSubnetDetail(self, subnet_id=None, userWithProjects = None):
        fecha=datetime.datetime.today()
        fecha= str(fecha).split(" ")
        data = {}
        data['status'] = 400
        data['hora'] = fecha[1]       
        data['fecha'] = fecha[0]   
        data['result'] = 'ok'
        data['success']= False
        objSubnet = {"message":"error"}
        neutron_subnet=self.parse_subnet(objSubnet)
        data['Detail'] = neutron_subnet 
        if userWithProjects.tokenId != None:
            tokenId = userWithProjects.tokenId
            try:
                _OPS_API_NEUTRON_NETWORK_LIST_SUBNETS_DETAIL = self._CMP_OPS_API_NEUTRON_NETWORK_
                _NEUTRON_NETWORK_LIST_SUBNETS_DETAIL =_OPS_API_NEUTRON_NETWORK_LIST_SUBNETS_DETAIL+self.API_MODULO_SUBNETS+self.API_MODULO_DIAGONAL+str(subnet_id)
                restHeaders = {'X-Auth-Token':tokenId,'Content-type':'application/json'}
                responseSubnetDetail = requests.get(_NEUTRON_NETWORK_LIST_SUBNETS_DETAIL,headers=restHeaders, verify=self.API_OPS_API_SSL_CERTIFICATE_VERIFY)
                status=str(responseSubnetDetail).split("[")[1].split("]")[0]
                istatus=int(status)
                data['status'] = istatus
                if (istatus>=300 and istatus<399):
                        data["message"]="Urgent notification error ["+str(istatus)+ "] notify admin"
                        response=data
                        return response
                if (istatus>=400 and istatus<499) :
                    if (istatus<=410 ) :
                            responseContent = json.loads(responseSubnetDetail.content) 
                            existeNeutronError  = responseContent.get("NeutronError")
                            if(existeNeutronError != None):
                                data["message"]=responseContent["NeutronError"]["message"]
                                response=data
                                return response
                            else:
                                data["message"]="Urgent notification error ["+str(istatus)+ "] notify admin"
                                responseContent = json.loads(responseSubnetDetail.content) 
                                existeNeutronError  = responseContent.get("NeutronError")
                                if(existeNeutronError != None):
                                    data["message"]+=responseContent["NeutronError"]["message"]
                                    response=data
                                    return response
                if (istatus>=500 and istatus<699) :
                        data["message"]="Urgent notification error ["+str(istatus)+ "] notify admin"
                        response=data
                        return response 
                if (istatus>=200 and istatus<205  ):
                    responseContent = json.loads(responseSubnetDetail.content) 
                    if "subnet" in responseContent:
                        objSubnet= responseContent["subnet"]
                        neutron_subnet=self.parse_subnet(objSubnet)
                        data['Detail'] = neutron_subnet.__dict__
                        data['success']= True
                        data["message"]="Show ok"
                        response=data
                        return response
                    else:
                        data["message"]='Houston please have problem Started except getNetwork Subnet Detail'
                        return response
                else:
                    data["message"]='Houston have problem Started except getNetworkDetail'
                    response=data
                    return response
            except:
                response=data
                return response
        else:
            response=data
            return response    
            
  
    ''' ****************************************************************************
    @author: Juan Carlos Perez Hernandez
    @contact: jcphgy@gmail.com; jperezh@kionetworks.com
    @copyright: KIO Networks S.A. de C.V.
    @license: KIO
    @date:     10032020
    @summary: Lista las imagenes en un template
    ********************************************************************************* '''
    def getDetail(self, subnet_id=None,  project_Id=None, user=None,):
        data = {}
        data['status'] = 400
        data['result'] = ''
        data['success']= False
        data['ok']= False
        data['Content'] = []
        if (subnet_id==None):
            data["message"]='subnet_id is empty'
            return data
        if(user == None):
            data["message"]='user name is empty'
            return data
        else:
            user_name = user
        if(project_Id == None):
            data["message"]='project is empty'
            return data
        else:
            projectId = project_Id   
        userWithProjects = UserProject()
        userWithProjects.name   =   user_name
        userWithProjects.password   =   self.CMP_USER_PASSWORD
        userWithProjects.projectId  =   projectId
        authen_user = self.getAutenticaIdentidad(userWithProjects)
        if (authen_user):
            if authen_user:
                userWithProjects.userId  = authen_user.userId
                userWithProjects.tokenId = authen_user.tokenId
                data  = self.getSubnetDetail(subnet_id,  userWithProjects)
                return data