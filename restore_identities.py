if __name__ == "__main__":     
    identities_content = \
"""<?xml version="1.0" encoding="utf-8"?>
<identities>
<subscriber>
  <publicUserIdentity>sip:5146976608@mtlasdev55.net</publicUserIdentity>
  <phoneNumber>5146976608</phoneNumber>
  <deviceURI>5146976608@192.168.22.64:5060</deviceURI>
  <displayName>john8 north</displayName>
  <assertedIdentity>5146976608@mtlasdev55.net</assertedIdentity>
  <location>IEEE-802.11b;isp=abc;network=4011</location>
  <network>mtlasdev55.net</network>
  <pcfa>ecf=rf.server.mtl.broadsoft.com</pcfa>
  <bwuser>y</bwuser>
</subscriber>

<subscriber>
  <publicUserIdentity>sip:5146976605@mtlasdev55.net</publicUserIdentity>
  <phoneNumber>5146976608</phoneNumber>
  <deviceURI>5146976605@10.9.55.11:5065</deviceURI>
  <displayName>john8 north</displayName>
  <assertedIdentity>5146976605@mtlasdev55.net</assertedIdentity>
  <location>IEEE-802.11b;isp=abc;network=4011</location>
  <network>mtlasdev55.net</network>
  <pcfa>ecf=rf.server.mtl.broadsoft.com</pcfa>
  <bwuser>y</bwuser>      
</subscriber>

<subscriber>
  <publicUserIdentity>sip:5146976607@mtlasdev55.net</publicUserIdentity>
  <phoneNumber>5146976607</phoneNumber>
  <deviceURI>5146976607@192.168.22.64:5060</deviceURI>
  <displayName>john7 north</displayName>
  <assertedIdentity>5146976607@mtlasdev55.net</assertedIdentity>
  <location>IEEE-802.11b;isp=abc;network=4011</location>
  <network>mtlasdev55.net</network>
  <pcfa>ecf=rf.server.mtl.broadsoft.com</pcfa>
  <bwuser>y</bwuser>
</subscriber>

<subscriber>
  <publicUserIdentity>sip:5146976603@mtlasdev55.net</publicUserIdentity>
  <phoneNumber>5146976603</phoneNumber>
  <deviceURI>5146976603@10.9.55.37:5060</deviceURI>
  <displayName>john3 north</displayName>
  <assertedIdentity>5146976603@mtlasdev55.net</assertedIdentity>
  <location>IEEE-802.11b;isp=abc;network=4011</location>
  <network>mtlasdev55.net</network>
  <pcfa>ecf=rf.server.mtl.broadsoft.com</pcfa>
  <bwuser>y</bwuser>
</subscriber>

<subscriber>
  <publicUserIdentity>sip:5146976604@mtlasdev55.net</publicUserIdentity>
  <phoneNumber>5146976604</phoneNumber>
  <deviceURI>5146976604@10.9.55.31:5060</deviceURI>
  <displayName>john4 north</displayName>
  <assertedIdentity>5146976604@mtlasdev55.net</assertedIdentity>
  <location>IEEE-802.11b;isp=abc;network=4011</location>
  <network>mtlasdev55.net</network>
  <bwuser>y</bwuser>
</subscriber>

<subscriber>
  <publicUserIdentity>sip:5146976606@mtlasdev55.net</publicUserIdentity>
  <phoneNumber>5146976606</phoneNumber>
  <deviceURI>5146976606@10.9.55.31:5060</deviceURI>
  <displayName>john6 north</displayName>
  <assertedIdentity>5146976606@mtlasdev55.net</assertedIdentity>
  <location>IEEE-802.11b;isp=abc;network=4011</location>
  <network>mtlasdev55.net</network>
  <bwuser>y</bwuser>
</subscriber>

</identities>
"""
        
    with open('C:\\svn\\working\\common\\developertools\\bwcscf\identities.xml', 'w') as identities_file:
        identities_file.write(identities_content)  

    
    
                
                