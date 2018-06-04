import os

# initialize varaibles
mp3list = list()
mp3dict = dict()

# Create function to search directories for mp3 files
def build_mp3_list(dir1):
    for f1 in os.listdir(dir1):
        if os.path.isdir(f1):
            build_mp3_list(os.path.join(dir1,f1))
        if f1[-4:] == '.txt':   # This could be changed to .mp3 to look for mp3 files
            mp3list.append(os.path.join(dir1,f1))

    
# Build checksum dictionary for mp3s
def build_chksum_dict(mp3_list):
    for file1 in mp3_list:
        chksum = get_md5sum(file1).split(' ')
        mp3dict.setdefault(chksum[0],[]).append(file1)

        
# Create a function to get the md5sum for the file
def get_md5sum(file1):
    cmd = 'md5sum ' + file1
    # print(cmd)
    fp = os.popen(cmd)
    res = fp.read()
    fp.close()
    return res
    

# Find Duplicates
def find_duplicates(dict1):
    for i in dict1:
        if len(dict1[i]) > 1:
            print("Duplicate files:")
            print("Chksum value: {}".format(i))
            print(dict1[i])
            if run_diff(dict1[i]):
                print("Diff shows they are the same")
            
# Create function to call the diff command
def run_diff(files):
    print()
    cmd = 'diff '
    diffs = 0
    for i in range(1, len(files)):
        cmd = cmd + str(files[0]) + ' ' + str(files[i])
        print(cmd)
        fp = os.popen(cmd)
        res = fp.read()
        diffs += len(res)
        fp.close()
    if len(res) == 0:
        return True
    return False

print("Changed the file type to '.txt' to make it easier to test.\n")
build_mp3_list(os.getcwd())
build_chksum_dict(mp3list)
print("Show the mp3 files: \n{}\n".format(mp3list))
find_duplicates(mp3dict)
