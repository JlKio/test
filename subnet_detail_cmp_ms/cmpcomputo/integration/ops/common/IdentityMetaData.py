# -*- coding: utf-8 -*-
''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
from __future__ import unicode_literals


''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class AuthToken(object):
    projectId = ""
    projectName = ""
    tokenId = ""
    def __init__(self, projectId, projectName, tokenId ):
        self.projectId = projectId
        self.projectName = projectName
        self.tokenId = tokenId
        
    def toString(self):
        print(self.projectId)
        print(self.projectName)
        print(self.tokenId)
            
''' *******************************************************************************'''

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class CloudCredential(object):

    ipAddress="10.0.50.230"
    userDomainName="Default"
    projectDomainName="admin"
    userName="admin"
    password="do7ey7g"
    projectName="admin"

    def __init__(self, ipAddress, userDomainName, projectDomainName, userName, password, projectName ):
        self.ipAddress=ipAddress
        self.userDomainName=userDomainName
        self.projectDomainName=projectDomainName
        self.userName=userName
        self.password=password
        self.projectName=projectName

    def toString(self):
        print(self.ipAddress)
        print(self.userDomainName)
        print(self.userName)
        print(self.projectDomainName)
        print(self.password)
        print(self.projectName)
''' *******************************************************************************'''

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una Politica de Calidad de Servicio QoS
************************************************************************************ '''
class Policie(object):
    project_id=""
    tenant_id=""
    policie_id=""
    name=""
    description=""
    revision_number=""
    shared=""

    def __init__(self, project_id,tenant_id,policie_id,name,description,revision_number,shared):
        self.project_id=project_id
        self.tenant_id=tenant_id
        self.policie_id=""
        self.name=name
        self.description=description
        self.revision_number=revision_number
        self.shared=shared        
''' ******************************************************************************* '''
        
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una Politica de Calidad de Servicio QoS
************************************************************************************ '''
class Role(object):
    role_id=""
    name=""
    description=""
    def __init__(self, role_id=0,name="",description=""):
        self.role_id=role_id
        self.name=name
        self.description=description

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una Politica de Calidad de Servicio QoS
************************************************************************************ '''
class Group(object):
    group_id=""
    name=""
    description=""
    def __init__(self, group_id,name="",description=""):
        self.group_id=group_id
        self.name=name
        self.description=description

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una Politica de Calidad de Servicio QoS
************************************************************************************ '''
class Project(object):
    proyect_id=""
    parent_id=""
    role_id=""
    name=""
    domain_id=""
    description=""
    projects=""
    enabled=""
    links=""
    def __init__(self, proyect_id="",name="",description=""):
        self.proyect_id=proyect_id
        self.name=name
        self.description=description
    def __str__(self):
        return str(self.name)+" : "+str(self.proyect_id)

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una Politica de Calidad de Servicio QoS  User
************************************************************************************ '''
class User(object):
    user_id=""
    name=""
    description=""
    enabled=""
    password=""
    def __init__(self, user_id="",name="",description="",enabled="",password=""):
        self.user_id=user_id
        self.name=name
        self.description=description
        self.enabled=enabled
        self.password=password

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una Politica de Calidad de Servicio QoS  User
************************************************************************************ '''
class RespuestaSrv(object):
    mensajeid=""
    objeto=""
    def __init__(self, mensajeid,objeto):
        self.mensajeid=mensajeid
        self.objeto=objeto
''' ******************************************************************************* '''
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una Politica de Calidad de Servicio QoS  User
************************************************************************************ '''
class RespObjeto(object):
    generico=""
    server=""
    url=""
    listado=""
    page_title=""
    def __init__(self, generico="",server="",url="",listado="",page_title=""):
        self.generico=generico
        self.server=server
        self.url=url
        self.listado=listado
        self.page_title=page_title
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una Politica de Calidad de Servicio QoS  User
************************************************************************************ '''
class UserProject(object):
    name = ""
    id = ""
    enabled = ""
    links = ""
    projects = []
    project_id_default  =""
    projectId = ""
    project_name_default  =""
    password = ""
    userId = ""
    tokenId = ""
    def __init__(self):
        self.name = ""
        self.id = ""
        self.password_expires_at = ""
        self.enabled = ""
        self.links = ""
        self.password  = ""
        self.projectId = ""
    def showProjects(self):
        listaProyectos = "Proyectitos de  " + str(self.name)
        for proy in self.projects:
            listaProyectos = listaProyectos + "\n" + str(proy)
        return listaProyectos
    def __str__(self):
        listaProyectos = ""
        #print("self.projects "+str(type(self.projects)))
        if(self.projects != None):
            if len(self.projects)>0:
                listaProyectos = "Projects de  " + str(self.name)
                for proy in self.projects:
                    listaProyectos = listaProyectos + "\t" + str(proy)
            else:
                listaProyectos = "Este usuario no tiene proyectos Quizas apenas va iniciar"
        else:
            listaProyectos = "Este usuario no tiene proyectos warning"
        return str(self.name)+ "\n projectId [" +str(self.projectId) +"]\n  "+listaProyectos