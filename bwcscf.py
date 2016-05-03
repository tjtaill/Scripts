if __name__ == "__main__":
    import subprocess as sp
           
    cmd = ' '.join(['cd C:\\svn\\working\\common\\developertools\\bwcscf', 
            '&', 'goCSCF.pl'])
    sp.Popen(["start", "cmd", "/k", cmd], shell = True)
