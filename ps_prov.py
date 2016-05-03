import sys
import argparse
import prov_util

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='PS provisioning Script Creator')
    parser.add_argument('-sp', dest='sp', help='Service Provider Name',
        default='sp1')
    parser.add_argument('-dn', dest='dn', 
        help='Domain number example mtlasdev55.net has domain number 55',
        default='55')
    parser.add_argument('-uc', help='user count how many users to provision',
        type=int)
    parser.add_argument('-gc', help='group count how many users to provision',
        default=1, type=int)    
    
    args = parser.parse_args()
    
    if args.uc is None:
        print("user count -uc is a mandatory argument")
        parser.print_help()
        sys.exit()
        
    prov_util.create_service_provider(args.sp, args.dn)
    
    prov_util.create_service_pack(args.sp)
    
    prov_util.create_groups(args.gc, args.uc, args.sp, args.dn)
    
    prov_util.create_users(args.gc, args.uc, args.sp, args.dn)
    
    