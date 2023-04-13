import rename_factor as rf

class Renamegine :
    def __init__(self) -> None:
        # INITIALISATION
        self.folderpath = ""
        self.listpath = []
        self.currentpath = ""

    def list_video_folder(self, path):
        self.folderpath = path
        self.listpath = rf.list_video(path)
        rf.create_folder_out(path)

    def rename_current_file(self, theme, tags, delete = True):
        try :
            new_name = rf.make_new_name(
                theme, 
                tags, 
                rf.get_number_name(self.currentpath)
            )
            print(new_name)
            rf.copy_file_out(self.currentpath, new_name, path=self.folderpath)
            if delete :
                rf.del_file(self.currentpath, path=self.folderpath)
            self.listpath.remove(self.currentpath)
            self.currentpath = ""
        except Exception as e :
            print("ERROR rename current file : ", e)
            raise ValueError('ERROR rename current file :' + e)
    
    def choose_current_file(self, file):
        if file in self.listpath :
            self.currentpath = file
        else :
            raise ValueError("Ce path n'existe pas !")
    
    def cutdetect(self, file):
        try :
            fileinfo = rf.separation_file_folder(file)
            # print("fileinfo[0]" + fileinfo[0])
            # print("fileinfo[1]" + fileinfo[1])
            rf.detect_cut_file(fileinfo[0], fileinfo[1])
            rf.del_file(fileinfo[0], fileinfo[1])
            self.list_video_folder(fileinfo[1])
        except Exception as e :
            print(e)
            raise SystemError('ERROR rename current file :' + e)

    
    def get_current_path(self):
        return self.folderpath + '/' + self.currentpath


if __name__ == '__main__' : 
    rengine = Renamegine()
    rengine.list_video_folder("C:/Users/Lancelot/Desktop/DEV_PRO/rename_video/ex")
    print(rengine.listpath)
    rengine.choose_current_file(rengine.listpath[0])
    rengine.rename_current_file(
        "test", 
        ["oariaa", "bonjour"], 
        delete = False
    )