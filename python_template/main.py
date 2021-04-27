import granatum_sdk
import numpy as np

# Demonstration of a Gbox that transposes a Gene Expression Matrix
def main():
    # initialize the object used for importing/exporting data
    gn = granatum_sdk.Granatum()

    # get imports
    # imports can be accessed using keywords specified 
    # in the "injectInto" field of the arguments section
    # of the package.yaml file - in our case, "exampleImport"
    assay = gn.get_import("exampleImport")

    # our gn.get_import() returned an object of the "assay" class
    # this is a dictionary with 3 keywords: "matrix" contains the
    # gene expression values, "sampleIds" contain the cell IDs
    # and "geneIds" contain the gene IDs

    # get arguments
    # arguments can be accessed using keywords specified 
    # in the "injectInto" field of the arguments section
    # of the package.yaml file - in our case, "exampleArgument"
    example_arg = gn.get_arg("exampleArgument")

    # INSERT THE BODY OF YOUR SCRIPT HERE
    # for example, you may transpose the gene expression data as
    assay["matrix"] = np.array(assay.get("matrix")).T
    # then, this numpy array should be turned into a list 
    # of lists before exporting
    assay["matrix"] = assay["matrix"].tolist()

    # export results
    # here, we use keywords specified in the "extractFrom"
    # field in the exports section of the package.yaml file - in 
    # our case, "exampleExport"
    gn.export_statically(assay, "exampleExport")    
    gn.add_result("Example of a concluding message", data_type="markdown")
    gn.commit()

if __name__ == "__main__":
    main()
