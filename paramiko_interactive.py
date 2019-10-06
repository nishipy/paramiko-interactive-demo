class Interactive:
    import credentials
    import paramiko
    def __init__(self):
       self.PORT = self.credentials.PORT
       self.USER = self.credentials.USER
       self.PEM  = self.credentials.PEM
       self.FDISK_CMD = 'sudo fdisk /dev/sda'
    
    def fdisk_test(self, hosts):
        rd = {}
        for host in hosts:
            ssh = self.paramiko.SSHClient()
            ssh.set_missing_host_key_policy(self.paramiko.AutoAddPolicy())
            ssh.connect(host, self.PORT, self.USER, key_filename=self.PEM)
            stdin, stdout, _ = ssh.exec_command(self.FDISK_CMD)
            stdin.write('m\n')
            stdin.flush()
            stdin.write('q\n')
            stdin.flush()
            output = stdout.readlines()
            rd[host] = output
        return rd