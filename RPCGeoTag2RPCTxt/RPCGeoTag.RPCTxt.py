import os
import warnings
from pathlib import Path
import gdal
import argparse

def RFMtoTxt(raster, inputPath ,outputPath=None):
    """

    Args:
        rasterPath:
        outputPath:

    Returns:

    """

    dirName = os.path.dirname(__file__)

    try:
        text_file = open(os.path.join(os.path.join(dirName, "RFM_lib"), "RFM.txt"), 'r')
        line_list = text_file.readlines()
        data = {}

        for i in range(10):
            data[line_list[i][0:-2]] = raster.GetMetadata('RPC').get(line_list[i][0:-2])

        lineNum = raster.GetMetadata('RPC').get("LINE_NUM_COEFF").split(" ")

        for i in range(10, 30):
            data[line_list[i][0:-2]] = lineNum[i - 10]

        lineDen = raster.GetMetadata('RPC').get("LINE_DEN_COEFF").split(" ")

        for i in range(30, 50):
            data[line_list[i][0:-2]] = lineDen[i - 30]

        sampNum = raster.GetMetadata('RPC').get("SAMP_NUM_COEFF").split(" ")

        for i in range(50, 70):
            data[line_list[i][0:-2]] = sampNum[i - 50]

        sampDen = raster.GetMetadata('RPC').get("SAMP_DEN_COEFF").split(" ")

        for i in range(70, 90):
            data[line_list[i][0:-2]] = sampDen[i - 70]

        dataList = []

        for key, value in data.items():
            temp = [key, value]
            dataList.append(temp)
        print(dataList)

        if outputPath:
            outputFilePath = os.path.join(outputPath, Path(inputPath).stem + "_RFM.txt")
        else:
            outputFilePath = os.path.join(os.path.dirname(inputPath), Path(inputPath).stem + "_RFM.txt")
        print(outputFilePath)
        with open(outputFilePath, "w") as f:
            for listitem in dataList:
                f.write('%s: %s\n' % (listitem[0], listitem[1]))
    except :
        warnings.warn("RFM_lib folder does not exist, check the installation again !!")

    return


def RunConv(args):
    inputFolder = args.inputPath
    outputFolder = args.outputPath
    gdal.UseExceptions()
    files = os.listdir(inputFolder)

    for file_ in files:
        filePath_ = os.path.join(inputFolder,file_)
        try:
            raster = gdal.Open(filePath_)
            rpcs = raster.GetMetadata('RPC')
            if bool(rpcs):
                print("Raster:", file_,"contain RPC tag")
                RFMtoTxt(raster=raster,inputPath= filePath_,outputPath=outputFolder)
            else:
                print("Raster:", file_,"does not contain RPC tag")

        except:
            print(file_, "Not a raster")
            continue
    return

def main():
    parser = argparse.ArgumentParser(description="Extract RPC tag from raster tag and write a corresponding RPC.txt file ")
    parser.add_argument("-inputPath", help="Directory path containing raster files", type=str,
                        required=True)
    parser.add_argument("-outputPath",
                        help="Directory path where all RPC.txt files will be stored, if this argument kept empty the rpc.txt files will be stored in the same input directory ",
                        type=str, required=False)
    parser.set_defaults(func=RunConv)
    args = parser.parse_args()
    args.func(args)
if __name__ == "__main__":
    ## Commend line tool
    main()

    ## If you want to use the script instead of the command line tool, comment line 103 and uncomment the lines from 106 tp 112
    ## Provide the inputPath and the outputPAth (optional)
    # class Args:
    #     def __init__(self):
    #         self.inputPath= "E:\OneDrive - California Institute of Technology\\0000-Temp covid 19\Samples"
    #         self.outputPath=""
    #
    # args = Args()
    # RunConv(args=args)

