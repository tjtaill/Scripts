import sys
import subprocess


if __name__ == "__main__":
    """
    fs_search.py CommunicationBarringControl
    """
    # svn_url = 'https://beach.mtl.broadsoft.com/docs/Engineering/Releases'
    svn_url = 'https://beach.mtl.broadsoft.com/docs/Engineering'
    proc = subprocess.Popen('svn list -R %s' % svn_url, stdout=subprocess.PIPE, universal_newlines=True)

    for line in proc.stdout:
        l = line.rstrip()
        if line.endswith('doc') or l.endswith('docx'):
            if sys.argv[1] in line:
                print(line)
