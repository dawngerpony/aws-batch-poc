#!/usr/bin/env python3

import os
import pysftp

host = os.getenv('SFTP_HOST', 'sftp')
port = int(os.getenv('SFTP_PORT', '22'))
username = 'foo'
password = 'pass'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
print("Connecting to {} on port {}".format(host, port))
with pysftp.Connection(host, username=username, password=password, port=port, cnopts=cnopts) as sftp:
    sftp.put("/files/test1.txt", "upload/test1.txt")
    print("File successfully uploaded.")
