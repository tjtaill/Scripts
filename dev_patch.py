import sys
import os
import glob

if __name__ == "__main__":
    jar_file = sys.argv[1]
    class_list_file = sys.argv[2]
    create_jar = ["jar", "-cvf", jar_file ]
    update_jar = ["jar", "-uvf", jar_file ]
    classes = []
    with open(class_list_file) as f:
        for class_file in f:
            # split from com/ onward
            split_index = class_file.find('/com') + 1
            cf = class_file[split_index:]
            # strip newline and glob for inner classes
            cf = cf.rstrip('\n')
            bf = os.path.splitext(cf)[0]
            gf = bf + '*.class'
            inner_classes = glob.glob( gf )
            for cls in inner_classes:
                classes.append( cls )
    cls = ' '.join( classes )
    length = len(cls)
    # TODO split this as many times as needed insted of in half
    if length > 8000:
        half = len(classes) // 2
        cls1 = classes[0:half]
        cls2 = classes[half:]
        create_jar.extend( cls1 )
        command = ' '.join( create_jar )
        print(command)
        os.system( command )
        update_jar.extend( cls2 )
        command = ' '.join( update_jar )
        print(command)
        os.system( command )
    else:
        create_jar.extend( classes )        
        command = ' '.join( create_jar )
        print(command)
        os.system( command )
    
    
    
    