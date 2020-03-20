# -*- coding: utf-8 -*-
''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
from __future__ import unicode_literals
import requests
import logging
import json
import traceback
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
''' ****************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar
********************************************************************************* '''

class CloudService(object):
    OPS_KEYSTONE_URL_TOKEN_ENDPOINT=""
    #OPS_CONTROLLER_IP_NETWORKS = "https://kiokloudhub.kionetworks.com:5696/v2.0/"
    OPS_CONTROLLER_IP = "https://kiokloudhub.kionetworks.com:55357"
    
    _OPS_PROTOCOLO_COMUNICACION_="http"
    _OPS_DOS_PUNTOS_=":"
    _OPS_BARRAS_INCLINADAS_="//"
    _OPS_NOMBRE_SERVIDOR_="vrrp.kcs.cloud"

    _OPS_PUERTO_KEYSTONE_IDENTITY_INTERNAL_="35357"
    _OPS_PUERTO_NOVA_COMPUTE_INTERNAL_="8774"
    _OPS_PUERTO_NEUTRON_NETWORK_INTERNAL_="9696"
    _OPS_PUERTO_CINDER_="8776"
    _OPS_PUERTO_VOLUME_="8776"
    _OPS_PUERTO_ORCHESTRATION_HEAT_INTERNAL_="8004"
    _OPS_PUERTO_GLANCE_="9292"
    _OPS_PUERTO_IMAGES_="9292"
    _OPS_PUERTO_SECURITY_GROUPS_RULES_="9696"
    _OPS_PUERTO_SECURITY_GROUPS_="9696"
    _OPS_BARRA_INCLINADA_="/"
    _OPS_PROTOCOLO_HTTPS_="https"

    #  Inicia la configuracion del local
    #  _________________________________
    
    
    _OPS_PROTOCOLO_COMUNICACION_="https"
    _OPS_NOMBRE_SERVIDOR_="kiokloudhub.kionetworks.com"
    _OPS_PUERTO_KEYSTONE_IDENTITY_INTERNAL_="55357"
    _OPS_PUERTO_NOVA_COMPUTE_INTERNAL_="5774"
    _OPS_PUERTO_CINDER_="5776"
    _OPS_PUERTO_VOLUME_="5776"
    _OPS_PUERTO_GLANCE_="5292"
    _OPS_PUERTO_IMAGES_="5292"
    _OPS_PUERTO_NEUTRON_NETWORK_INTERNAL_="5696"
    _OPS_PUERTO_SECURITY_GROUPS_RULES_="5696"
    _OPS_PUERTO_SECURITY_GROUPS_="5696"
    
    
    #  Finaliza la configuracion local
    
    
    API_MODULO_DIAGONAL="/"
    API_INTERROGACION="?"
    API_IGUAL="="
    API_TRUE="true"
    API_OPS_API_SSL_CERTIFICATE_VERIFY=False 
    API_AMPERSAND="&"
    
    API_MODULO_KEYSTONE_IDENTITY_AUTH="auth/tokens?nocatalog"
    API_MODULO_KEYSTONE_IDENTITY_USERS ="users"
    API_MODULO_KEYSTONE_IDENTITY_PROJECTS ="projects"
    API_MODULO_KEYSTONE_IDENTITY_GROUPS ="groups"
    API_MODULO_KEYSTONE_IDENTITY_ROLES ="roles"
    API_MODULO_KEYSTONE_IDENTITY_ID="id"
    API_MODULO_KEYSTONE_IDENTITY_NAME="name"
    API_MODULO_KEYSTONE_IDENTITY_DOMAIN="domain"
    API_MODULO_KEYSTONE_IDENTITY_USER="user" 
    API_MODULO_KEYSTONE_IDENTITY_TOKEN ="token"
    API_MODULO_KEYSTONE_IDENTITY_PROJECT ="project"
    API_MODULO_KEYSTONE_IDENTITY_RESPONSE_HEADERS_SUBJECT_TOKEN = "X-Subject-Token"
    API_MODULO_SERVERS="servers"
    API_MODULO_SERVERS_DETAIL_="detail"
    API_MODULO_SERVER_INSTANCE_DETAIL_ERROR_="ERROR"
    API_MODULO_SERVER_INSTANCE_DETAIL_ERROR_FAULT="fault"
    API_MODULO_SERVERS_DETAIL=API_MODULO_DIAGONAL+API_MODULO_SERVERS+API_MODULO_DIAGONAL+API_MODULO_SERVERS_DETAIL_
    API_MODULO_SERVERS_ACTION_REBOOT = "reboot"
    API_MODULO_SERVERS_ACTION_REBOOT_TYPE = "type"
    API_MODULO_SERVERS_ACTION_APAGADO_DURO = "HARD"
    API_MODULO_SERVERS_ACTION_APAGADO_SUAVE = "SOFT"
    API_MODULO_SERVERS_ACTION_REMOVE_FLOATINGIP = "removeFloatingIp"
    API_MODULO_SERVERS_ACTION_REMOVE_FLOATINGIP_ADDRESS = "address"
    API_MODULO_SERVERS_ACTION_RESIZE = "resize"
    API_MODULO_SERVERS_ACTION_RESIZE_FLAVOR_REF = "flavorRef" 
    API_MODULO_SERVERS_ACTION_RESIZE_OS_DCF_DISKCONFIG = "OS-DCF:diskConfig"
    API_MODULO_SERVERS_ACTION_RESIZE_OS_DCF_DISKCONFIG_VALUE_AUTO = "AUTO"
    API_MODULO_SERVERS_ACTION_RESIZE_OS_DCF_DISKCONFIG_VALUE_MANUAL = "MANUAL"
    API_MODULO_SERVERS_ACTION_RESIZE_CONFIRM_OPERATION = "null"
    API_MODULO_SERVERS_ACTION_REVERT_RESIZE = "revertResize"
    API_MODULO_SERVERS_ACTION_CONFIRM_RESIZE = "confirmResize"
    API_MODULO_SERVERS_ACTION_RESIZE_SIN_FLAVOR_EN_VM = 999
    API_MODULO_SERVERS_ACTION_GET_VNC_CONSOLE = "os-getVNCConsole"
    API_MODULO_SERVERS_ACTION_GET_VNC_CONSOLE_TYPE="type"
    API_MODULO_SERVERS_ACTION_GET_VNC_CONSOLE_TYPE_NOVNC = "novnc"
    API_MODULO_SERVERS_ACTION_GET_VNC_CONSOLE_TYPE_RDP = "rdp"
    API_MODULO_FLAVOR="flavors"
    API_MODULO_FLAVOR_DETAIL=API_MODULO_DIAGONAL+"flavors"+API_MODULO_DIAGONAL+"detail"
    API_MODULO_IMAGES=API_MODULO_DIAGONAL+"images"
    API_MODULO_OS_AVAILABILITY_ZONE=API_MODULO_DIAGONAL+"os-availability-zone"
    API_MODULO_OS_KEY_PAIRS="os-keypairs"
    API_MODULO_SECURITY_GROUP="security-groups"
    API_MODULO_SECURITY_GROUP_RULES="security-group-rules"
    API_MODULO_VOLUMES="volumes"
    API_MODULO_VOLUMES_ACTION="action"
    API_MODULO_FLAVOR_ACTION_CREATE = "flavor"
    API_MODULO_FLAVOR_ACTION_CREATE_NAME = "name"
    API_MODULO_FLAVOR_ACTION_CREATE_RAM = "ram"
    API_MODULO_FLAVOR_ACTION_CREATE_VCPUS = "vcpus"
    API_MODULO_FLAVOR_ACTION_CREATE_DISK = "disk"
    API_MODULO_FLAVOR_ACTION_CREATE_DESC = "description"
    API_MODULO_FLAVOR_ACTION_CREATE_IS_PUBLIC = "os-flavor-access:is_public"
    API_MODULO_FLAVOR_ACTION_ACTION = "action"
    API_MODULO_FLAVOR_ACTION_ADD_TENANT_ACCESS = "addTenantAccess"
    API_MODULO_FLAVOR_ACTION_ADD_TENANT= "tenant"
    API_MODULO_FLAVOR_ACTION_CREATE_IS_PUBLIC_FALSE="false"
    API_MODULO_NETWORKS="networks"
    API_MODULO_SUBNETS="subnets"
    API_MODULO_ROUTERS="routers"
    API_MODULO_SECURITY_GROUPS="security-groups"
    API_MODULO_PORTS="ports"
    API_MODULO_FLOATINGIPS="floatingips"
    API_MODULO_FLOATINGIPS_POOLS="floatingip_pools"
    API_MODULO_SERVERS_OS_INTERFACE="os-interface"                  
    API_MODULO_STACK="stacks"
    API_MODULO_COMPUTE_QUOTA = "os-quota-sets"
    API_MODULO_COMPUTE_DEFAULTS = "defaults"
    API_MODULO_COMPUTE_DETAIL = "detail"
    API_MODULO_COMPUTE_LIMITS = "limits"
    API_MODULO_CINDER_LIMITS = "limits"
    API_MODULO_SERVERS="servers"
    API_MODULO_SERVERS_DETAIL_="detail"
    API_MODULO_SERVER_INSTANCE_DETAIL_ERROR_="ERROR"
    API_MODULO_SERVER_INSTANCE_DETAIL_ERROR_FAULT="fault"
    API_MODULO_SERVERS_DETAIL=API_MODULO_DIAGONAL+API_MODULO_SERVERS+API_MODULO_DIAGONAL+API_MODULO_SERVERS_DETAIL_
    
    API_MODULO_NETWORKS="networks"
    API_MODULO_SUBNETS="subnets"
    API_MODULO_ROUTERS="routers"
    API_MODULO_SECURITY_GROUPS="security-groups"
    API_MODULO_PORTS="ports"
    API_MODULO_FLOATINGIPS="floatingips"
    API_MODULO_FLOATINGIPS_POOLS="floatingip_pools"
    API_MODULO_SERVERS_OS_INTERFACE="os-interface"                  
    API_MODULO_STACK="stacks"
    API_MODULO_COMPUTE_QUOTA = "os-quota-sets"
    API_MODULO_COMPUTE_DEFAULTS = "defaults"
    API_MODULO_COMPUTE_DETAIL = "detail"
    API_MODULO_COMPUTE_LIMITS = "limits"
    API_MODULO_CINDER_LIMITS = "limits"
    API_OCTOPUS_SERVICE_KEY="serviceKey"
    API_OPERATION_ADD_INTERFACE_TO_ROUTER     = "add_router_interface"
    API_OPERATION_REMOVE_INTERFACE_TO_ROUTER  = "remove_router_interface"
    API_OPS_FILTERING_FIELD_TENANT_ID = "tenant_id"
    API_OPS_FILTERING_FIELD_NETWORK_ID = "network_id"
    API_OPS_FILTERING_FIELD_NETWORK_NAME = "name"
    API_OPS_FILTERING_FIELD_ADMIN_STATE_UP = "admin_state_up"
    API_OPS_FILTERING_FIELD_SHARED = "shared"
    API_OPS_FILTERING_FIELD_DEVICE_ID = "device_id"
    API_OPS_FILTERING_FIELD_DEVICE_OWNER = "device_owner"
    API_OPS_FILTERING_FIELD_DEVICE_MAC_ADDRESS = "mac_address"
    API_OPS_FILTERING_FIELD_FIXED_IPS = "fixed_ips"
    API_OPS_FILTERING_FIELD_PORT_Id = "port_id"
    API_OPS_FILTERING_FIELD_PORT_ACTIVE = "ACTIVE"
    API_OPS_FILTERING_FIELD_NONE = "None"
    API_OPS_FILTERING_FIELD_FLOATING = "floating"
    API_OPS_FILTERING_FIELD_ROUTER_EXTERNAL = "router:external"
    API_OPS_FILTERING_FIELD_ADDRESSES = "addresses"
    API_OPS_FILTERING_FIELD_VERSION = "version"
    API_OPS_FILTERING_FIELD_ADDR = "addr"
    API_OPS_FILTERING_FIELD_OS_EXT_IPS_TYPE = "OS-EXT-IPS:type"
    API_OPS_COMPUTE_INSTANCE_CREATE_SOURCE_TYPE_IMAGE =  "image"
    API_OPS_COMPUTE_INSTANCE_CREATE_DESTINATION_TYPE_VOLUME = "volume"
    API_OPS_COMPUTE_INSTANCE_CREATE_DELETE_TERMINATION_TRUE = True
    API_OPS_COMPUTE_INSTANCE_LIST_DETAIL_FIELD_ID="id"
    API_OPS_COMPUTE_INSTANCE_LIST_DETAIL_FIELD_NAME="name"
    API_OPS_COMPUTE_INSTANCE_LIST_DETAIL_FIELD_STATUS="status"
    API_OPS_COMPUTE_INSTANCE_LIST_DETAIL_ERROR_FAULT_FIELD_MESSAGE="message"
    API_OPS_COMPUTE_INSTANCE_LIST_DETAIL_ERROR_FAULT_FIELD_CODE="code"
    API_OPS_COMPUTE_INSTANCE_LIST_DETAIL_ERROR_FAULT_FIELD_DETAILS="details"
    API_OPS_COMPUTE_INSTANCE_LIST_DETAIL_ERROR_FAULT_FIELD_CREATED="created"
    
    _URL_OPS_= _OPS_PROTOCOLO_COMUNICACION_+_OPS_DOS_PUNTOS_+_OPS_BARRAS_INCLINADAS_+_OPS_NOMBRE_SERVIDOR_+_OPS_DOS_PUNTOS_

    _OPS_VERSION_API_KEYSTONE_IDENTITY_v3="v3"
    _OPS_API_KEYSTONE_IDENTITY_AUTH=_URL_OPS_+_OPS_PUERTO_KEYSTONE_IDENTITY_INTERNAL_+_OPS_BARRA_INCLINADA_+_OPS_VERSION_API_KEYSTONE_IDENTITY_v3+_OPS_BARRA_INCLINADA_

    
    _OPS_VERSION_API_NEUTRON_NETWORK_v2_0="v2.0"
    _CMP_OPS_API_NEUTRON_NETWORK_=_URL_OPS_+_OPS_PUERTO_NEUTRON_NETWORK_INTERNAL_+_OPS_BARRA_INCLINADA_+_OPS_VERSION_API_NEUTRON_NETWORK_v2_0+_OPS_BARRA_INCLINADA_

    
    
    _OPS_VERSION_API_KEYSTONE_IDENTITY_v3="v3"
    _OPS_BARRA_INCLINADA_="/"
    
    CMP_USER_PASSWORD = "s5wasyHnFZI8AGL1Ulrm" 
    
    
    def __init__(self):
        print("Cloud Service")
   
class ComputeService(CloudService):

    def __init__(self):
        print("Compute Service")

    def getInstanceName(self):
        pass

    def computeService(self):
        pass

    def getInstanceList(self, cloud_type, state):
        pass

    def getInstanceDummyList(self, cloud_type, state):
        pass

    def getObjectFromJson(self,jsonString):
        pass

    def createInstance(self,imageTypeId, instanceType, instanceName,minCount, maxCount, networkId, subnetId, enableAutoAsignPublicIp, iamRole, enableTerminationProtection, enableMonitoring, availabilityZone,securityGroupIds,tenancy):
        pass

    def getImageList(self, regionId):
        pass

    def getRegionList(self):
        pass

    def getNetwork(self,regionName):
        pass

    def deleteInstance(self,instanceId):
        pass
