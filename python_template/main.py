import granatum_sdk
import numpy as np

# Demonstration of a Gbox that transposes a Gene Expression Matrix
def main():
    gn = granatum_sdk.Granatum()
    assay = gn.get_import("exampleImport")
    example_arg = gn.get_arg("exampleArgument")
    assay["matrix"] = np.array(assay.get("matrix")).T

    gn.export_statically(assay, "exampleExport")    
    gn.add_result("Matrix successfully transposed", data_type="markdown")
    gn.commit()

if __name__ == "__main__":
    main()
