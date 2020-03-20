# -*- coding: utf-8 -*-

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez, @gybranperez 
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
from __future__ import unicode_literals
class InterfaceAttachments(object): 
    port_id = ""
    port_state = ""
    net_id = ""
    mac_addr = ""
    fixed_ips = [] 
    ip_address = ""
    subnetid = ""
    def __init__(self):
        port_id = ""
        port_state = ""
        net_id = ""
        mac_addr = ""
        fixed_ips = [] 
        
        
    def __str__(self):
        return 
        (
            " port_id:" + str(self.port_id) + "\n" +
            " port_state " + str(self.port_state)+ "\n" +
            " net_id " + str(self.net_id)+ "\n" +
            " mac_addr " + str(self.mac_addr)
        )
    def to_string(self):
        return 
        (
            " port_id:" + str(self.port_id) + "\n" +
            " port_state " + str(self.port_state)+ "\n" +
            " net_id " + str(self.net_id)+ "\n" +
            " mac_addr " + str(self.mac_addr)
        ) 
''' ******************************************************************************* '''



'''Clase generica para VolumeQuota'''
class VolumeQuota(object): 
    id = ""
    totalSnapshotsUsed = ""
    maxTotalBackups = ""
    maxTotalVolumeGigabytes  = ""
    maxTotalSnapshots = ""
    maxTotalBackupGigabytes = ""
    totalBackupGigabytesUsed = ""
    maxTotalVolumes = ""
    totalVolumesUsed = ""
    totalBackupsUsed = ""
    totalGigabytesUsed = ""
    labelMaxTotalVolumeGigabytes=""
    labelTotalGigabytesUsed=""
    
    
    def __init__(self):
        id = ""
        totalSnapshotsUsed = ""
        maxTotalBackups = ""
        maxTotalVolumeGigabytes  = ""
        maxTotalSnapshots = ""
        maxTotalBackupGigabytes = ""
        totalBackupGigabytesUsed = ""
        maxTotalVolumes = ""
        totalVolumesUsed = ""
        totalBackupsUsed = ""
        totalGigabytesUsed = ""
        
    def __str__(self):
        return (
            " id:" + str(self.id) + "\n" +
            " totalSnapshotsUsed " + str(self.totalSnapshotsUsed)+ "\n" +
            " maxTotalBackups " + str(self.maxTotalBackups)+ "\n" +
            " maxTotalVolumeGigabytes " + str(self.maxTotalVolumeGigabytes)+ "\n" +
            " maxTotalSnapshots " + str(self.maxTotalSnapshots)+ "\n" +
            " maxTotalBackupGigabytes " + str(self.maxTotalBackupGigabytes)+ "\n" +
            " totalBackupGigabytesUsed " + str(self.totalBackupGigabytesUsed)+ "\n" +
            " maxTotalVolumes " + str(self.maxTotalVolumes)+ "\n" +
            " totalVolumesUsed " + str(self.totalVolumesUsed)+ "\n" +
            " totalBackupsUsed " + str(self.totalBackupsUsed)+ "\n" +
            " totalGigabytesUsed " + str(self.totalGigabytesUsed)
            )
    def to_string(self):
         return (
            " id:" + str(self.id) + "\n" +
             " totalSnapshotsUsed " + str(self.totalSnapshotsUsed)+ "\n" +
            " maxTotalBackups " + str(self.maxTotalBackups)+ "\n" +
            " maxTotalVolumeGigabytes " + str(self.maxTotalVolumeGigabytes)+ "\n" +
            " maxTotalSnapshots " + str(self.maxTotalSnapshots)+ "\n" +
            " maxTotalBackupGigabytes " + str(self.maxTotalBackupGigabytes)+ "\n" +
            " totalBackupGigabytesUsed " + str(self.totalBackupGigabytesUsed)+ "\n" +
            " maxTotalVolumes " + str(self.maxTotalVolumes)+ "\n" +
            " totalVolumesUsed " + str(self.totalVolumesUsed)+ "\n" +
            " totalBackupsUsed " + str(self.totalBackupsUsed)+ "\n" +
            " totalGigabytesUsed " + str(self.totalGigabytesUsed) 
            ) 
''' ******************************************************************************* '''


'''Clase generica para ComputeQuota'''
class ComputeQuota(object): 
    id = ""
    injected_file_content_bytes = ""
    metadata_items = ""
    server_group_members  = ""
    server_groups = ""
    ram = ""
    floating_ips = ""
    key_pairs = ""
    instances = ""
    security_group_rules = ""
    injected_files = ""
    cores = ""
    fixed_ips = ""
    injected_file_path_bytes = ""
    security_groups  = ""
    
    
    def __init__(self):
        id = ""
        injected_file_content_bytes = ""
        metadata_items = ""
        server_group_members  = ""
        server_groups = ""
        ram = ""
        floating_ips = ""
        key_pairs = ""
        instances = ""
        security_group_rules = ""
        injected_files = ""
        cores = ""
        fixed_ips = ""
        injected_file_path_bytes = ""
        security_groups  = ""
        
    def __str__(self):
        return (
            " id:" + str(self.id) + "\n" +
            " injected_file_content_bytes " + str(self.injected_file_content_bytes)+ "\n" +
            " metadata_items " + str(self.metadata_items)+ "\n" +
            " server_group_members " + str(self.server_group_members)+ "\n" +
            " ram " + str(self.ram)+ "\n" +
            " floating_ips " + str(self.floating_ips)+ "\n" +
            " key_pairs " + str(self.key_pairs)+ "\n" +
            " instances " + str(self.instances)+ "\n" +
            " security_group_rules " + str(self.security_group_rules)+ "\n" +
            " injected_files " + str(self.injected_files)+ "\n" +
            " cores " + str(self.cores)+ "\n" +
            " fixed_ips " + str(self.fixed_ips)+ "\n" +
            " injected_file_path_bytes " + str(self.injected_file_path_bytes)+ "\n" +
            " security_groups " + str(self.security_groups) 
            )
    def to_string(self):
         return (
            " id:" + str(self.id) + "\n" +
            " injected_file_content_bytes " + str(self.injected_file_content_bytes)+ "\n" +
            " metadata_items " + str(self.metadata_items)+ "\n" +
            " server_group_members " + str(self.server_group_members)+ "\n" +
            " ram " + str(self.ram)+ "\n" +
            " floating_ips " + str(self.floating_ips)+ "\n" +
            " key_pairs " + str(self.key_pairs)+ "\n" +
            " instances " + str(self.instances)+ "\n" +
            " security_group_rules " + str(self.security_group_rules)+ "\n" +
            " injected_files " + str(self.injected_files)+ "\n" +
            " cores " + str(self.cores)+ "\n" +
            " fixed_ips " + str(self.fixed_ips)+ "\n" +
            " injected_file_path_bytes " + str(self.injected_file_path_bytes)+ "\n" +
            " security_groups " + str(self.security_groups) 
            ) 
''' ******************************************************************************* '''


'''Clase generica para los enlaces'''
class Links(object): 
    href = ""
    rel = ""
    def __init__(self):
        self.href = ""
        self.rel = ""
    def to_string(self):
        print("href:" + str(self.href))
        print("rel:" + str(self.rel)) 
''' ******************************************************************************* '''



'''Clase generica para los enlaces'''
class Allocationpools(object): 
    start = ""
    end = ""
    def __init__(self):
        self.start = ""
        self.end = ""
    def __str__(self):
        return ("start:" + str(self.start) + " end " + str(self.end))
    def to_string(self):
        return ("start:" + str(self.start) + " end " + str(self.end)) 
''' ******************************************************************************* '''


'''Clase generica para los enlaces'''
class Hostroutes(object): 
    nexthop = ""
    end = ""
    def __init__(self):
        self.nexthop = ""
        self.destination = ""
    def __str__(self):
        return ("nexthop:" + str(self.nexthop) + " destination " + str(self.destination))
    def to_string(self):
        return ("nexthop:" + str(self.nexthop) + " destination " + str(self.destination)) 
''' ******************************************************************************* '''



'''Clase generica para los enlaces'''
class Security_Group_Type_Rules(object): 
    name = ""
    ip_protocol = ""
    from_port=""
    to_port=""
    template=""
    id=""
    direction=""
    
    def __init__(self):
        self.name = ""
        self.ip_protocol = ""
    def __str__(self):
        return ("ID: "+str(self.id)+"\ntemplate "+str(self.template)+" name:" + str(self.name) + " ip_protocol " + str(self.ip_protocol)
                + " from_port " + str(self.from_port)+ " to_port " + str(self.to_port))
    def to_string(self):
        return ("template "+str(self.template)+" name:" + str(self.name) + " ip_protocol " + str(self.ip_protocol)
                + " from_port " + str(self.from_port)+ " to_port " + str(self.to_port)) 
''' ******************************************************************************* '''


'''Clase generica para los enlaces'''
class Attachments(object): 
    server_id = ""
    attachment_id = ""
    attached_at = ""
    host_name = ""
    volume_id = ""
    device = ""
    id = ""
    
    def __init__(self):
        self.server_id = ""
        self.attachment_id = ""
        self.attached_at = ""
        self.host_name = ""
        self.volume_id = ""
        self.device = ""
        self.id = ""
    def __str__(self):
        return ("server_id:" + str(self.server_id) + " attachment_id " + str(self.attachment_id) +
                " attached_at:" + str(self.attached_at) + " host_name " + str(self.host_name) +
                " volume_id:" + str(self.volume_id) + " device " + str(self.device) +
                " id:" + str(self.id)
                )
    def to_string(self):
        return ("server_id:" + str(self.server_id) + " attachment_id " + str(self.attachment_id) +
                " attached_at:" + str(self.attached_at) + " host_name " + str(self.host_name) +
                " volume_id:" + str(self.volume_id) + " device " + str(self.device) +
                " id:" + str(self.id)
                )
''' ******************************************************************************* '''

'''Clase generica para los ExternalGatewayInfo'''
class ExternalGatewayInfo(object): 
    network_id  =""
    enable_snat=""
    external_fixed_ips=""
    def __str__(self):
        return ("network_id:" + str(self.network_id) + " enable_snat " + str(self.enable_snat) +
                " external_fixed_ips:" + str(self.external_fixed_ips) 
                )
    def to_string(self):
        return ("network_id:" + str(self.network_id) + " enable_snat " + str(self.enable_snat) +
                " external_fixed_ips:" + str(self.external_fixed_ips)
                )
''' ******************************************************************************* '''
    
  

'''Clase generica para los ExternalGatewayInfo'''
class ExternalFixedIps(object): 
    subnet_id  =""
    ip_address=""
    subnet_name=""
    snat =""
    def __str__(self):
        return ("subnet_id:" + str(self.subnet_id) + " ip_address " + str(self.ip_address) 
                )
    def to_string(self):
        return ("subnet_id:" + str(self.subnet_id) + " ip_address " + str(self.ip_address)
                )
''' ******************************************************************************* '''
    



'''Clase generica para los enlaces'''
class URL_REST_OPS(object): 
    protocolo = ""
    ipAddress = ""
    port = ""
    version = ""
    projectId = ""
    cdnModulo = ""
    def __init__(self):
        self.href = ""
        self.rel = ""
    def to_string(self):
        print("href:" + str(self.href))
        print("rel:" + str(self.rel)) 
''' ******************************************************************************* '''



''' ****************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
class NetworkAddress(object):
    mac_addr = ""
    version = ""
    name=""
    addr=""     # IP de la Red 
    type=""     # Corresponde al tipo  si es fixed (Fija)   floating (Dinamica)  
    port_id=""
                # Detail
    
    def __init__(self, mac_addr="", version="", addr="", type="",name=""):
        self.mac_addr=mac_addr
        self.version=version
        self.addr=addr 
        self.type=type
        self.name = name
    def __str__(self):
        return str(self.name)+": "+str(self.addr)+": "+str(self.type)
    def to_string(self):
        print("Mac_addr_id:" + str(self.mac_addr))
        print("Version_id:" + str(self.version))
        print("Addr_id:" + str(self.addr))
        print("Type_id:" + str(self.type))
''' ******************************************************************************* '''

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
class FloatingIps(object):
    router_id = ""
    status=""
    description=""     
    tenant_id=""     
    created_at=""
    updated_at=""
    floating_network_id=""
    fixed_ip_address=""
    floating_ip_address=""
    revision_number=""
    project_id=""
    port_id=""
    id=""
    
    
    def __init__(self, id, floating_ip_address):
        self.id=id
        self.floating_ip_address=floating_ip_address
    def __str__(self):
        return "Id "+str(self.id)+": floating_ip_address "+str(self.floating_ip_address)
    def to_string(self):
        print("Id "+str(self.id))
        print("floating_ip_address "+str(self.floating_ip_address))

''' ****************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
class Port(object):
    port_id = ""
    name=""
    cidr=""
    admin_state_up=""     # IP de la Red 
    type=""     # Corresponde al tipo  si es fixed (Fija)   floating (Dinamica)  
    allowed_address_pairs_list=""
    binding_host_id=""
    binding_profile=""
    binding_vif_details=""
    binding_vif_type=""
    binding_vnic_type=""
    created_at=""
    data_plane_status=""
    data_plane_status=""
    description=""
    device_id=""
    device_owner=""
    dns_assignment=""
    dns_domain=""
    dns_name=""
    extra_dhcp_opts=""
    fixed_ips=""
    fixed_ips_subnet_id=""
    fixed_ips_ip_address=""
    allowed_address_pair_ip_address=""
    allowed_address_pair_mac_address=""
    id=""
    ip_allocation=""
    mac_address=""
    network_id=""
    port_security_enabled=""
    project_id=""
    revision_number=""
    qos_policy_id=""
    resource_request=""
    security_groups=""
    status=""
    tags=""
    tenant_id=""
    updated_at=""
    mac_learning_enabled=""
    
    def __init__(self, port_id, name):
        self.port_id=port_id
        self.name=name
    def __str__(self):
        return "Name "+str(self.name)+": IdPort "+str(self.port_id)+" device_owner "+str(self.device_owner) + " Ip Net "+str(self.network_id)+"]"
    def to_string(self):
        return "Name "+str(self.name)+": IdPort "+str(self.port_id)+" device_owner "+str(self.device_owner) + " Ip Net ["+str(self.network_id)+"]"

''' ******************************************************************************* '''

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Clase que representa un Router Virtual
************************************************************************************ '''
class Router(object):
    
    ''' 
    @summary: Id del router 
    '''
    router_id = ""
    ''' 
    @summary: Nombre del router 
    '''
    name="" 
    ''' 
    @summary: Status del router 
    '''
    status=""
    ''' 
    @summary: Indica si la administracion esta habilitada 
    '''
    admin_state_up = ""
    ''' 
    @summary: Id del proyecto 
    '''
    project_id=""
    ''' 
    @summary: id del tenant 
    '''
    tenant_id=""
    ''' 
    @summary: Descripcion del Router 
    '''
    description="" 
    ''' 
    @summary: Zona de disponibilidad 
    '''
    availability_zones = ""
    ''' 
    @summary: Distribuido 
    '''
    distributed=""
    ''' 
    @summary: Informacion del gateway 
    '''
    updated_at=""
    admin_state_up=""
    external_gateway_info=""
    hasExternal_gateway_info=""
    nameExternal_gateway_info=""
    external_gateway_id=""
    external_gateway_list=""
    show_external_gateway_list=""
    isAdmin_state_up=""
    routes=""
    rt=""
    ecmp_count=""
    revision_number=""
    nuage_backhaul_rd=""
    nuage_backhaul_vnid=""
    nuage_backhaul_rt=""
    tunnel_type=""
    

    def __init__(self, router_id="", name="", status=None, admin_state_up=None, project_id=None, tenant_id=None, description=None, availability_zones=None, distributed=None, external_gateway_info=None, routes=None):
        self.router_id = router_id
        self.name=name
        self.status=status
        self.admin_state_up = admin_state_up
        self.project_id=project_id
        self.tenant_id=tenant_id
        self.description=description 
        self.availability_zones = availability_zones
        self.distributed=distributed
        self.external_gateway_info=external_gateway_info
        self.routes=routes
        self.rt=""
        self.nuage_backhaul_vnid=""
        
    def toString(self):
        print("router_id:" + str(self.router_id))
        print("name:" + str(self.name))
        print("status:" + str(self.status))
        print("admin_state_up:" + str(self.admin_state_up))
        print("project_id:" + str(self.project_id))
        print("tenant_id:" + str(self.tenant_id))
        print("description:" + str(self.description))
        print("availability_zones:" + str(self.availability_zones))
        print("distributed:" + str(self.distributed))
        print("external_gateway_info:" + str(self.external_gateway_info))
        print("routes:" + str(self.routes))

''' ************************************************************************************ '''

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class ImageLocation(object):
    url = ""
    metadata = ""
    
    def __init__(self):
        self.url = ""
        self.metadata = ""
        
    def toString(self):
        print(self.url)
        print(self.metadata)
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class Image(object):
    imageId = ""
    imageName = ""
    status = ""
    tags = ""
    container_format = ""
    created_at = ""
    disk_format = ""
    updated_at = ""
    visibility = ""
    min_disk = ""
    file = ""
    locations = ImageLocation()
    protected = ""
    size = ""
    size_gb = ""
    min_ram = ""
    schema = ""
    virtual_size = ""
    operating_system = ""
    description=""
    esWindows=""
    os_ext_img_size=""
    
    def __init__(self, imageId="", imageName=""):
        self.imageId = imageId
        self.imageName = imageName   
    def __str__(self):
        return (str(self.imageName) + "\n\t" + str(self.imageId) + "\n\t" + str(self.visibility)+ "\n\t" + str(self.size))
    def toString(self):
        print(self.imageId + " - " + self.imageName + "\t visibility :" + self.visibility)     
''' ******************************************************************************* '''


''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class Flavor(object):
    flavorId = ""
    flavorName = ""
    nameUpper = ""
    links = []
    disk=""
    disk_mb=""
    ephemeral=""
    original_name=""
    ram=0
    ramillete=""
    swap=""
    vcpus=""
    rxtx_factor = ""
    OS_FLV_EXT_DATA_ephemeral=""
    os_flavor_access_is_public =""
    OS_FLV_DISABLED_disabled = ""
    esWindows=""
    
    def __init__(self, flavorId="", flavorName=""):
        self.flavorId = flavorId
        self.flavorName = flavorName   
    def __str__(self):
        res = "Your Flavor ID: "+ str(self.flavorId) + ", Name: "+ str(self.flavorName) + " [ ram: " + str(self.ram) + ", No vcpus: " + str(self.vcpus) + ", disk: "+str(self.disk) +" ]"
        return str(res)
''' ******************************************************************************* '''

class Fault_Instance(object):
    message=""
    code=""
    details=""
    created=""
    def __init__(self):
        self.message=""
        self.code=""
        self.details=""
        self.created=""
    def __str__(self):
        return " message: "+str(self.message)+" code: "+str(self.code)+"/ details "+str(self.details)    
    def to_string(self):
        return 
        (
            " message:" + str(self.message) + "\n" +
            " code " + str(self.code)+ "\n" +
            " details " + str(self.details)+ "\n" +
            " created " + str(self.created)
        )        
        
class NuageEnterprise(object):
    enterprise_id = ""
    name=""
    def __init__(self, enterprise_id="",name=""):
        self.enterprise_id = enterprise_id
        self.name = name
    def toString(self):
        print("ID: " +self.enterprise_id  + 
              ", Name: " +self.name )
    
    def __str__(self):
        arreglo= "ID: " +str(self.enterprise_id ) +"\n" 
        arreglo+= "Name: " +str(self.name) 
        return arreglo
        
class ComputeInstance(object):
    instance_id = ""
    name=""
    description=""
    status=""
    instance_type = ""
    image_id = ""
    instance = ""
    key_name = ""
    state = ""
    monitoring  = "" 
    platform = "" 
    private_dns_name = "" 
    #private_ip_address = ""
    networkAddress = NetworkAddress() 
    networkAddressList = ""
    public_dns_name = "" 
    public_ip_address = "" 
    networkAddressExist = True
    security_groups = ""
    server_name  = ""
    hypervisor  = ""
    disk_config=""
    availability_zone=""
    host=""
    hostname=""
    power_state=""
    task_state=""
    hypervisor_hostname=""
    launched_at=""
    terminated_at=""
    accessIPv4=""
    accessIPv6=""
    created=""
    console_url=""
    floatingIp=""
    yourfloatingIp=""
    region=""
    addressesList={
            "private": [
                {
                    "OS-EXT-IPS-MAC:mac_addr": "aa:bb:cc:dd:ee:ff",
                    "OS-EXT-IPS:type": "fixed",
                    "addr": "0.0.0.0",
                    "version": 4
                }
            ]
        }
    # Flavor Object
    flavor = Flavor()
    # Imagen Object
    imagen = Image()
    hostId=""
    host_status=""
    key_name=""
    locked="false"
    metadataList={
            "My Server Name": "Apache1"
        }
    user_id=""
    imageName=""
    os_extended_volumes_volumes_attached=""
    fault=Fault_Instance()
    
    # The class "constructor" - It's actually an initializer 
    def __init__(self, 
                 instance_id="", 
                 instance_type="", 
                 image_id="",  
                 instance="", 
                 key_name="", 
                 state="",
                 monitoring="", 
                 platform="", 
                 private_dns_name="", 
                 networkAddressList="", 
                 public_dns_name="", 
                 public_ip_address="", 
                 security_groups="",
                 server_name="",
                 hypervisor="",
                 created=""):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.image_id = image_id
        self.instance =  instance
        self.key_name = key_name
        self.state = state
        self.monitoring  = monitoring 
        self.platform = platform 
        self.private_dns_name = private_dns_name 
        self.networkAddressList = networkAddressList 
        self.public_dns_name = public_dns_name 
        self.public_ip_address = public_ip_address 
        self.security_groups = security_groups
        self.server_name = server_name
        self.hypervisor=hypervisor
        self.created=created
    def toString(self):
        print("ID: " +self.instance_id  + 
              ", Name: " +self.name     +
              ", IP: " +self.public_ip_address+
              "instance_type: "+self.instance_type)
    
    def __str__(self):
        arreglo= "ID: " +str(self.instance_id) +"\n" 
        arreglo+= "Name: " +str(self.name) +"\n"
        arreglo+= "Public IP address (Ipv4): " +str(self.public_ip_address) +"\n"
        arreglo+= "Availability zone: " +str(self.availability_zone) +"\n"
        arreglo+= "State: " +str(self.state) +"\n"
        arreglo+= "Public DNS (Ipv4): " +str(self.public_dns_name) +"\n"
        arreglo+= "Monitoring: " +str(self.monitoring) +"\n"
        arreglo+= "instance_type: "+str(self.instance_type)+"\n"
        arreglo+= "volumes_attached: "+str(self.os_extended_volumes_volumes_attached)+"\n"
        
        return arreglo
    '''
        Get dummy of class
    '''        
    def getDummy(self):
        self.instance_id = "XXX"
        self.instance_type = "XXX"
        self.image_id = "XXX"
        self.key_name = "XXX"
        self.state = "XXX"
        self.monitoring  = "XXX" 
        self.platform = "XXX" 
        self.private_dns_name = "XXX" 
        self.private_ip_address = "XXX" 
        self.public_dns_name = "XXX" 
        self.public_ip_address = "XXX" 
        self.security_groups = "XXX"
        return self
''' ################################ END CLASS ################################# '''



class ErrorMessage(object):
    error_message = ""
 
    
    def __init__(self, error_message ):
        self.error_message = error_message
 
    def toString(self):
        print(self.error_message)
     
            
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
    tokenId = None
    errorMessage =""
    userId = ""
    def __init__(self, projectId, projectName, tokenId, userId="None" ):
        self.projectId = projectId
        self.projectName = projectName
        self.tokenId = tokenId
        self.userId = userId
    def __str__(self):   
              return "\n Project id " +str(self.projectId) +"\n Project name " + str(self.projectName) + "\n Token id\n [" +str(self.tokenId)+"]"+ "\n User id : [" +str(self.userId)+"]"

        
    def toString(self):
        print(" Project id " +self.projectId +" Project name " + self.projectName + " Token id" +self.tokenId)
            
''' *******************************************************************************'''



''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class OpsUser(object):
    idUser=""
    name=""
    nameUpper=""
    enabled=""
    iddomain=""
    email=""
    status=""
    password_expires_at=""
    projectDomainName=""
    userName=""
    password=""
    projectName=""
    descripcion=""

    def __init__(self, idUser, name, enabled ):
        self.idUser=idUser
        self.name=name
        self.enabled=enabled
      

    def toString(self):
        print(self.idUser + " " + self.name+ " " + self.enabled)
        
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
@summary: Token de autenticacion
************************************************************************************ '''
class Securitygroups(object):
    securitygroups_id=""
    name=""
    description=""
    tenant_id=""
    isDelete = ""
    isRename = ""
    security_group_rules_list = "" # List

    def __init__(self,securitygroups_id="",name=""):
        self.securitygroups_id=securitygroups_id
        self.name=name
    
    def to_string(self):
        print("securitygroups_id: "+str(self.securitygroups_id))
        print("name: "+str(self.name))
         
''' ******************************************************************************* '''   
        
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
 "direction": "ingress",
        "port_range_min": "80",
        "ethertype": "IPv4",
        "port_range_max": "80",
        "protocol": "tcp",
        "remote_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5",
        "security_group_id": "a7734e61-b545-452d-a3cd-0189cbd9747a"
************************************************************************************ '''
class NewSGRule(object):
    direction=""
    name=""
    port_range_min=""
    port_range_max=""
    protocol=""
    ethertype=""
    security_group_id=""
    remote_group_id=""
    remote_ip_prefix=""
    description=""
    cidr=""
    metadata="ok"
    remoto_security_group_id=""
    sgRemoteRules=""
    def __init__(self,direction="egress",name="",port_range_min="80",port_range_max="80",protocol="tcp",ethertype="IPv4",security_group_id="",remote_group_id="",remote_ip_prefix="0.0.0.0/0",description=""):
        self.direction=direction
        self.name=name
        self.port_range_min=port_range_min
        self.port_range_max=port_range_max
        self.protocol=protocol
        self.ethertype=ethertype
        self.security_group_id=security_group_id
        self.remote_group_id=remote_group_id
        self.remote_ip_prefix=remote_ip_prefix
        self.description=description
    def __str__(self):   
              return "\nSecurity_group_id: "+str(self.security_group_id)+"\nRemot SG: "+str(self.remoto_security_group_id)+"\nProtocol: "+str(self.protocol)+"\nDirection: "+str(self.direction)+"\nEthertype: "+str(self.ethertype)+"\nRange Min: "+str(self.port_range_min)+"\nRange Max: "+str(self.port_range_max)+"\nRemote group id: "+str(self.remote_group_id)+"\nRemote ip prefix: "+str(self.remote_ip_prefix)
              
    def to_string(self):
              return "Protocol: "+str(self.protocol)+"\nDirection: "+str(self.direction)+"\nEthertype: "+str(self.ethertype)
        

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class SecurityGroupsRules(object):
    direction=""
    ethertype=""
    protocol=""
    securitygroupsrules_id=""
    port_range_max=""
    port_range_min=""
    port_range_min_y_max=""
    remote_group_id=""
    remote_ip_prefix=""
    security_group_id=""
    security_group_name=""
    project_id=""
    revision_number=""
    created_at=""
    updated_at=""
    tenant_id=""
    description=""

    def __init__(self,securitygroupsrules_id,direction,ethertype):
        self.securitygroupsrules_id=securitygroupsrules_id
        self.direction=direction
        self.ethertype=ethertype
    
    def to_string(self):
              return " Id: "+str(self.securitygroupsrules_id)+", direction"+str(self.direction)+" - ethertype: "+str(self.ethertype)

         
''' ******************************************************************************* '''        

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class KeyPairs(object):
    keypairs_name=""
    public_key=""
    security_group_rules_list = "" # List
    def __init__(self,keypairs_name):
        self.keypairs_name=keypairs_name
    
    def to_string(self):
        print("name: "+str(self.keypairs_name))
        print("public_key"+str(self.public_key))
        
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class ConsoleInstance(object):
    url=""
    type=""
    def __init__(self,url):
        self.url=url
    
    def to_string(self):
        print("name: "+str(self.url))
         
''' ******************************************************************************* '''    
        
class Interfaces(object):
    network_id=""
    networkname=""
    subnet_id=""
    subnetname=""
    subnetsassociated=""
    description=""
    cidr=""  #10.80.0.0/24
    networkaddress=""
    gatewayip=""
    hostroutes="" #Lista de host routes
    subnetpool="" 
    ipallocationpools=""  
    dhcpenable=""
    additionalroutes=""
    dnsnameservers=""
    def __init__(self,network_id,networkname,subnet_id,subnetname):
        self.network_id=network_id
        self.networkname=networkname
        self.subnet_id=subnet_id
        self.subnetname=subnetname
    def __str__(self):
        return "network_id: "+str(self.network_id)+" networkname: "+str(self.networkname)+"\n subnet_id: "+str(self.subnet_id)+" subnetname: "+str(self.subnetname)+"\ncidr ["+str(self.cidr)+"]"
    def to_string(self):
        return "network_id: "+str(self.network_id)+" networkname: "+str(self.networkname)+"\n subnet_id: "+str(self.subnet_id)+" subnetname: "+str(self.subnetname)+"\ncidr ["+str(self.cidr)+"]"

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class Network(object):
    network_id=""
    name=""
    created_at=""
    availability_zone_list = "" # List
    dns_domain=""
    port_security_enabled=""
    project_id=""
    qos_policy_id=""
    revision_number=""
    router_external=""
    router_external_YES_NO=""
    shared=""
    shared_YES_NO=""
    status=""
    subnet_list="" #List
    tenant_id=""
    updated_at=""
    vlan_transparent=""
    description=""
    admin_state_up=""
    admin_state_up_or_down=""
    mtu=""
    provider_network_type=""
    provider_physical_network=""
    provider_segmentation_id=""

    def __init__(self,network_id,name,created_at="", availability_zone_list="", dns_domain="", port_security_enabled="", project_id="", qos_policy_id="", revision_number="", router_external="", shared="", status="", subnet_list="", tenant_id="", updated_at="", vlan_transparent="", description="",admin_state_up="",mtu=""):
        self.network_id=network_id
        self.name=name
        self.created_at=created_at
        self.availability_zone_list=availability_zone_list
        self.dns_domain=dns_domain
        self.port_security_enabled=port_security_enabled
        self.project_id=project_id
        self.qos_policy_id=qos_policy_id
        self.revision_number=revision_number
        self.router_external=router_external
        self.shared=shared
        self.status=status
        self.subnet_list=subnet_list
        self.tenant_id=tenant_id
        self.updated_at=updated_at
        self.vlan_transparent=vlan_transparent
        self.description=description
        self.admin_state_up=admin_state_up
        self.mtu=mtu
    def __str__(self):
       return " network_id: "+str(self.network_id)+"\nname: "+str(self.name)+"\nShared: "+str(self.shared)+"\nsubnet_list: "+str(len(self.subnet_list))
     
        
''' ******************************************************************************* '''


''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Objeto que representa a una subnet
************************************************************************************ '''
class Subnet(object):
    subnet_id=""
    name=""
    description=""
    enable_dhcp="False" 
    network_id=""
    tenant_id=""
    created_at=""
    dns_nameservers=""
    updated_at=""
    ipv6_ra_mode="None"
    allocation_pools=[{'start':'0.0.0.0','end':'0.0.0.0'}] #List of public ip
    gateway_ip="0.0.0.0"
    revision_number="0"
    ipv6_address_mode="None"
    ip_version="4"
    host_routes=[""] #Lista de host routes
    cidr=""  #10.80.0.0/24
    project_id=""
    subnetpool_id="None"
    
    def __init__(self,subnet_id,name,description,enable_dhcp,network_id,tenant_id,created_at,dns_nameservers,updated_at,ipv6_ra_mode,allocation_pools,gateway_ip,revision_number,ipv6_address_mode,ip_version,host_routes,cidr,project_id,subnetpool_id):
        self.subnet_id=subnet_id
        self.name=name
        self.description=description
        self.enable_dhcp=enable_dhcp 
        self.network_id=network_id
        self.tenant_id=tenant_id
        self.created_at=created_at
        self.dns_nameservers=dns_nameservers
        self.updated_at=updated_at
        self.ipv6_ra_mode=ipv6_ra_mode
        self.allocation_pools=allocation_pools
        self.gateway_ip=gateway_ip
        self.revision_number=revision_number
        self.ipv6_address_mode=ipv6_address_mode
        self.ip_version=ip_version
        self.host_routes=host_routes
        self.cidr=cidr
        self.project_id=project_id
        self.subnetpool_id=subnetpool_id
        
    def __str__(self):
        return " SubNet id: " + str(self.subnet_id)+"\nname: "+str(self.name)+"\ncidr: "+str(self.cidr)+"\nallocation_pools total: " +str(len(self.allocation_pools))+ " dhcp: "+str(self.enable_dhcp)
    
    def to_string(self):
        return " Subnet id: "+str(self.subnet_id)+" Name: "+str(self.name)+"\nCidr: "+str(self.cidr)+"\nallocation_pools: "+str(len(self.allocation_pools))

''' ******************************************************************************* '''


''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Clase que representa un Gateway Virtual
************************************************************************************ '''
class Gateway(object):

    ''' 
    @summary: Indica si NAT esta habilitado 
    '''
    enable_snat = ""
    ''' 
    @summary: Zona de disponibilidad 
    '''
    availability_zones = "" # Zona de disponibilidad
    ''' 
    @summary: Descripcion del Router 
    '''
    description="" # Descripción 
    
    def __init__(self, enable_snat, availability_zones, description):
        self.enable_snat=enable_snat
        self.availability_zones=availability_zones
        self.description=description 

    def to_string(self):
        print("enable_snat:" + str(self.enable_snat))
        print("availability_zones:" + str(self.availability_zones))
        print("description:" + str(self.description))

''' ************************************************************************************ '''
    
    
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Clase que representa una direccion IP
************************************************************************************ '''
class IpAddress(object):
    
    ''' 
    @summary: Direccion IP 
    '''
    ip_address = ""
    ''' 
    @summary: Id de la subred 
    '''
    subnet_id = "" # Zona de disponibilidad
    ''' 
    @summary: Version del protocolo IpV4=4 o IPv6=6
    '''
    version="4" # Version del protocolo 
    ''' 
    @summary: Tipo de ip Fixed o Float (Fija o Flotante) 
    '''
    ip_type = "Fixed"
    
    def __init__(self, ip_address, subnet_id, version, ip_type):
        self.ip_address=ip_address
        self.subnet_id=subnet_id
        self.version=version 
        self.ip_type=ip_type
        
    def to_string(self):
        print("ip_address:" + str(self.ip_address))
        print("subnet_id:" + str(self.subnet_id))
        print("version:" + str(self.version))
        print("ip_type:" + str(self.ip_type))

        
''' ************************************************************************************ '''
    
    
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa los Ruteos en un Router
************************************************************************************ '''
class Routes(object):
    destination = ""
    nexthop = ""
    rd=""
    def __init__(self, destination="", nexthop=""):
        self.destination = destination
        self.nexthop = nexthop        
''' ******************************************************************************* '''



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
@summary: Representa una tarjeta de red de una VM
************************************************************************************ '''
class Nic(object):
   host_device=""
   network_id=""
   type=""
   switch_uuid=""
   port=""
   mac_type="ASSIGNED"
   state="CONNECTED"
   start_connected=True
   mac_address=""
   type="PCNET32"

   def __init__(self, host_device, network_id, type, switch_uuid, port, mac_type, state, start_connected, mac_address):
       self.host_device=host_device
       self.network_id=network_id
       self.type=type
       self.switch_uuid=switch_uuid
       self.port=port
       self.mac_type=mac_type
       self.state=state
       self.start_connected=start_connected
       self.mac_address=mac_address
       self.type=type
''' ******************************************************************************* '''
       

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Representa una IP Flotante
************************************************************************************ '''
class FloatingIp(object):
    
    id=""
    status=""
    router_id=""
    description=""
    dns_domain=""
    dns_name=""
    created_at=""
    updated_at=""
    revision_number=""
    project_id=""
    tenant_id=""
    floating_network_id=""
    fixed_ip_address=""
    floating_ip_address=""
    port_id=""
    
    def __init__(self,id,
                    status,
                    router_id,
                    description,
                    dns_domain,
                    dns_name,
                    created_at,
                    updated_at,
                    revision_number,
                    project_id,
                    tenant_id,
                    floating_network_id,
                    fixed_ip_address,
                    floating_ip_address,
                    port_id):
        self.id=id
        self.status=status
        self.router_id=router_id
        self.description=description
        self.dns_domain=dns_domain
        self.dns_name=dns_name
        self.created_at=created_at
        self.updated_at=updated_at
        self.revision_number=revision_number
        self.project_id=project_id
        self.tenant_id=tenant_id
        self.floating_network_id=floating_network_id
        self.fixed_ip_address=fixed_ip_address
        self.floating_ip_address=floating_ip_address
        self.port_id=port_id
''' ******************************************************************************* '''
        

''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class AvailabilityZone(object):
    zoneId = ""
    zoneName = ""
    def __init__(self, zoneId, zoneName):
        self.zoneId = zoneId
        self.zoneName = zoneName        
''' ******************************************************************************* '''
        
''' *******************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Token de autenticacion
************************************************************************************ '''
class AvailabilityZoneAws(object):
    regionId = ""
    regionName = ""
    intancesList = ""
    def __init__(self,  regionName):
        
        self.regionName = regionName        
''' ******************************************************************************* '''    

class Aws_Buckets(object):
    Name=""
    CreationDate=""
    def __init__(self,Name="",CreationDate=""):
        self.Name=Name
        self.CreationDate=CreationDate
    def __str__(self):
        return self.Name + " - " + str(self.CreationDate)
        
''' ****************************************************************************
@author: Juan Carlos Perez Hernandez
@contact: jcphgy@gmail.com; jperezh@kionetworks.com
@copyright: Kion Networks S.A. de C.V.
@license: MIT
@summary: Visualizar 
********************************************************************************* '''
class Volumen_Attachments(object):
    server_id = ""
    attachment_id = ""
    attached_at = ""
    host_name = ""
    volume_id = ""
    device = ""
    id = ""
    compute_instance=""
    def __init__(self):
        self.server_id = ""
        self.attachment_id = ""
        self.attached_at = ""
        self.host_name = ""
        self.volume_id = ""
        self.device = ""
        self.id = ""
    def to_string(self):
        print("server_id:" + str(self.server_id))
        print("host_name:" + str(self.host_name)) 
''' ******************************************************************************* '''
class Volume_Image_Metadata(object):
    hw_vif_model = ""
    description = ""
    tags = ""
    container_format = ""
    min_ram = ""
    vmware_disktype = ""
    disk_format = ""
    image_name = ""
    image_id = ""
    vmware_adaptertype = ""
    checksum = ""
    min_disk = ""
    size = ""
    def __init__(self):
        self.hw_vif_model = ""
        self.description = ""
        self.tags = ""
        self.container_format = ""
        self.min_ram = ""
        self.vmware_disktype = ""
        self.disk_format = ""
        self.image_name = ""
        self.image_id = ""
        self.vmware_adaptertype = ""
        self.checksum = ""
        self.min_disk = ""
        self.size = ""
    def to_string(self):
        print(" hw_vif_model :" + str(self.hw_vif_model))
        print(" description :" + str(self.description))
        print(" tags :" + str(self.tags))
        print(" container_format :" + str(self.container_format))
        print(" min_ram :" + str(self.min_ram))
        print(" vmware_disktype :" + str(self.vmware_disktype))
        print(" disk_format :" + str(self.disk_format))
        print(" image_name :" + str(self.image_name))
        print(" image_id :" + str(self.image_id))
        print(" vmware_adaptertype :" + str(self.vmware_adaptertype))
        print(" checksum :" + str(self.checksum))
        print(" min_disk :" + str(self.min_disk))
        print(" size :" + str(self.size))
        
class Volumen_Metadata(object):
    readonly = ""
    attached_mode  = ""
    def __init__(self):
        self.readonly = ""
        self.attached_mode  = "" 
    def to_string(self):
        print("readonly:" + str(self.readonly))
        print("attached_mode:" + str(self.attached_mode)) 
''' ******************************************************************************* '''            
        
class Volumen(object):
    attachments = Volumen_Attachments()
    links = Links()
    volume_image_metadata=Volume_Image_Metadata()
    availability_zone = ""
    encrypted = ""
    updated_at = ""
    replication_status = ""
    snapshot_id = ""
    id = ""
    size = ""
    user_id = ""
    os_vol_tenant_attr_tenant_id = ""
    os_vol_host_attr_host=""
    metadata = Volumen_Metadata()
    status = ""
    volume_image_metadata = ""
    description = ""
    multiattach = ""
    source_volid = ""
    consistencygroup_id = ""
    name = ""
    bootable = ""
    created_at = ""
    volume_type = ""
    device=""
    isDetachment=False
    def __init__(self):
        self.attachments = ""
        self.links = ""
        self.availability_zone = ""
        self.encrypted = ""
        self.updated_at = ""
        self.replication_status = ""
        self.snapshot_id = ""
        self.id = ""
        self.size = ""
        self.user_id = ""
        self.os_vol_tenant_attr_tenant_id = ""
        self.metadata = ""
        self.status = ""
        self.volume_image_metadata = ""
        self.description = ""
        self.multiattach = ""
        self.source_volid = ""
        self.consistencygroup_id = ""
        self.name = ""
        self.bootable = ""
        self.created_at = ""
        self.volume_type = ""
        
    def to_string(self):
        print("id:" + str(self.id) + "name:" + str(self.name)) 
''' ******************************************************************************* '''
       
class json_response(object):
    status_code =""
    success=""
    status=""
    data=""
    message=""
    reason=""
    link= Links()
    
    def __init__(self):
        self.status=""
        self.data=[]
        self.success=False
        self.message=""
        self.reason=""
        self.link = Links();
        self.status_code =""
    def __str__(self):
        return " Status: "+str(self.status)+"/"+str(self.status_code)+" - Success: "+str(self.success)+" - "+str(self.message)+"\nReason: "+str(self.reason)+"\nData: "+str(self.data)
        
class Stack(object):
    stack_id=""
    stack_name=""
    description=""
    creation_time=""
    stack_user_project_id=""
    stack_status_reason=""
    stack_owner=""
    stack_statu=""
    link= Links()
    

    
    def __init__(self):
        self.stack_id=""
        self.stack_name=""
        self.description=""
        self.creation_time=""
        self.stack_user_project_id=""
        self.stack_status_reason=""
        self.stack_owner=""
        self.stack_statu=""
        link= Links()
    def __str__(self):
        return " ID: "+str(self.stack_id)+" stack_name: "+str(self.stack_name)+"/ status "+str(self.stack_status_reason)    
   
    
    
class SummaryDashboard(object):
    InstancesTotal=0
    InstancesUsage=0
    InstancePercent=""
    InstancesTypeProgressBar=""
    NetworksTotal=0
    NetworksUsage=0
    NetworksPercent=""
    NetworksTypeProgressBar=""
    VcpusTotal=0
    VcpusUsage=0
    VcpusPercent=""
    VcpusTypeProgressBar=""
    DiskTotal=0
    DiskUsage=0
    labelMaxTotalVolumeGigabytes=""
    labelTotalGigabytesUsed=""
    DiskPercent=""
    DiskTypeProgressBar=""
    maxTotalVolumes=0
    totalVolumesUsed=0
    VolumesPercent=""
    VolumesTypeProgressBar=""
    RamTotal=0
    RamUsage=0
    RamPercent=""
    RamtTypeProgressBar=""
    FloatingIpsUsage=0
    FloatingIpsTotal=0
    FloatingPercent=""
    FloatingTypeProgressBar=""
    link= Links()
    
    def __init__(self):
        self.InstancesTotal=0
        self.InstancesUsage=0
        self.NetworksTotal=0
        self.NetworksUsage=0
        self.VcpusTotal=0
        self.VcpusUsage=0
        self.DiskTotal=0
        self.DiskUsage=0
        self.RamTotal=0
        self.RamUsage=0
        self.link= Links()
    def __str__(self):
        return " Instances [Total: "+str(self.InstancesTotal)+" Usage: "+str(self.InstancesUsage)+" ], "+" Networks [Total: "+str(self.NetworksTotal)+" Usage: "+str(self.NetworksUsage)+" ], "
    