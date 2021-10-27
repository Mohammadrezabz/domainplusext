import re
import os  
url = input ('enter host address [www.example.com] \n ')

ext_ziping = ['.arc','.arj','.as','.b64','.btoa','.bz','.cab','.cpt','.gz','.hqx','.iso','.lha','.lhz','.mim','.mme','.pak','.pf','.rar','.rpm','.sea','.sit','.sitx','.tar.gz','.tbz','.tbz2','.tgz','.uu','.uue','.z','.zip','.zipx','.zoo' ]



def only_domain(domain_name) :
    just_domain = re.sub(r"(https://www.|https://|www.)",r"",domain_name)
    return just_domain 

subs_path = input ('Enter Path To Subdomains Lists : \n ')
subs_path = os.path.expanduser(subs_path)

with open (f'word_{url}.txt','a+') as output:
    for ex in ext_ziping :
        output.write(url + ex + '\n')
    for ex in ext_ziping :
        output.write(only_domain(url) + ex + '\n')
    with open (subs_path,'r') as subdomains:
        sub = subdomains.readlines()
        for s in sub :        
            s = s.rstrip()
            output.write(only_domain(s) + ex + '\n')


