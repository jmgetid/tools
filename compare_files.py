import os
import sys
import getopt
import hashlib
import time

def main():
    # Compare the content of two directories
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:h", ["input=", "output=", "help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print __doc__
            sys.exit(0)
        elif opt in ("-i", "--input"):
            input_dir = arg
        elif opt in ("-o", "--output"):
            output_dir = arg

    print "input: " + input_dir
    print "output: " + output_dir

    input_dir_list_files = []
    analyze_input(input_dir, input_dir_list_files)
    check_output(output_dir, input_dir, input_dir_list_files)

def analyze_input(current_directory, input_dir_list_files):
    # Analyze directory
    files = os.listdir(current_directory)
    for filename in files:
        complete_filename = current_directory + '/' + filename
        if os.path.isdir(complete_filename):
            analyze_input(complete_filename, input_dir_list_files)
        else:
            complete_filename_md5 = md5(complete_filename)
            input_dir_list_files.append( { 'filename': complete_filename, 'md5': complete_filename_md5 })

def check_output(output_dir, input_dir, input_dir_list_files):
    for filedata in input_dir_list_files:
        output_filename = output_dir + filedata['filename'][len(input_dir):]
        if os.path.exists(output_filename) and (filedata['md5'] != md5(output_filename)):
            print filedata['filename'] + ';' + time.strftime(time.localtime(os.path.getmtime(filedata['filename']))) + ';' + output_filename + ';' + str(time.localtime(os.path.getmtime(output_filename)))

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if __name__ == "__main__":
    main()
