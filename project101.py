import os 
import dropbox
from dropbox.files import WriteMode

class TransferData:
    
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relativePath  = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rp') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'BVojgdUQZ7ZZW0Iub8mxY7IR7ADiRhVVBVojgdUQZ7ZZW0Iub8mxY7IR7ADiRhVV'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the path for the transfer to happen: "))
    file_to = str(input("Enter the path to upload into dropbox: "))
    
main()