"""
Version: 1.5

Summary: 3D model reconstruction based on automaticly extracted ROI and gamma correction image set

Author: suxing liu

Author-email: suxingliu@gmail.com

USAGE:

python pipeline.py -p /path_to_image_folder/ -ft jpg

parameter list:

argument:
("-p", "--path", required = True,    help = "path to image file")
("-ft", "--filetype", required = True,    help = "Image filetype")


"""

import subprocess, os
import sys
import argparse



def execute_script(cmd_line):
    """execute script inside program"""
    
    process = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()

    output = process.communicate()[0]
    exitCode = process.returncode

    if (exitCode == 0):
        return output
    else:
        raise ProcessException(cmd_line, exitCode, output)
   
        



def pipeline(current_path):
    """execute pipeline scripts"""
    
    #/opt/code/bbox_seg.py -p /home/suxingliu/frame-interpolation/test-image/ -ft jpg
    
    # step 1 : Region of Interest extraction
    ROI_seg = "python /opt/code/bbox_seg.py -p " + current_path + " -ft " + str(ext)
    
    print("Extracting Region of Interest from input images...\n")
    
    execute_script(ROI_seg)

    
    # step 2 : gamma_correction 
    #gamma_correction = "python /opt/code/gamma_correction.py -p " + current_path + "segmented/" 
    
    #print("Luminance enhancement by gamma_correction method...\n")
    
    #execute_script(gamma_correction)
    
    # step 3: compute 3D model from preprocessed image set
    compute_3d_model = "/opt/code/vsfm/bin/VisualSFM sfm+pmvs " + current_path + "segmented/" 
    
    #singularity exec --overlay file.img shub://lsx1980/vsfm-master /opt/code/vsfm/bin/VisualSFM sfm+pmvs /$root/$path_to_your_image_file_folder/
    execute_script(compute_3d_model)


if __name__ == '__main__':
    
    # construct the argument and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required = True,    help = "path to image file")
    ap.add_argument("-ft", "--filetype", required = False,  default = 'jpg', help = "image filetype")
    args = vars(ap.parse_args())
    
    
    # setting path to model file
    file_path = args["path"]
    ext = args['filetype']

    # execute the main pipeline
    pipeline(file_path)
    
    
