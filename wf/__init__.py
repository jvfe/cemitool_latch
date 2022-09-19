import subprocess
from pathlib import Path

from latch import medium_task, message, workflow
from latch.resources.launch_plan import LaunchPlan
from latch.types import LatchDir, LatchFile

from .docs import metadata


@medium_task
def run_cemitool(
    sample_name: str,
    expression_data: LatchFile,
    sample_annotation: LatchFile,
    pathways: LatchFile,
    interaction_table: LatchFile,
) -> LatchDir:
    """
    Run the CEMiTool analysis pipeline, outputting an HTML report and result tables
    """

    output_directory = f"report_{sample_name}"
    output_dir_path = Path(output_directory).resolve()

    _cemitool_cmd = [
        "Rscript",
        "/root/cemitool.R",
        sample_name,
        expression_data.local_path,
        sample_annotation.local_path,
        pathways.local_path,
        interaction_table.local_path,
    ]

    message(
        "info",
        {
            "title": "Running CEMiTool",
            "body": f"Running CEMiTool. Command string: {' '.join(_cemitool_cmd)}",
        },
    )

    subprocess.run(
        _cemitool_cmd,
        check=True,
    )

    if output_dir_path.exists() == False:
        message(
            "error",
            {
                "title": "No output generated from CEMiTool!",
                "body": "CEMiTool ran but no output was generated. Check if input files are valid.",
            },
        )

    return LatchDir(str(output_dir_path), f"latch:///CEMiTool/{output_directory}")


@workflow(metadata)
def cemitool(
    sample_name: str,
    expression_data: LatchFile,
    sample_annotation: LatchFile,
    pathways: LatchFile,
    interaction_table: LatchFile,
) -> LatchDir:
    """Co-expression Modules Identification Tool

    CEMiTool
    ----

    The CEMiTool[^1] R package provides users with an easy-to-use method
    to automatically run gene co-expression analyses. In addition, it performs gene
    set enrichment analysis and over representation analysis for the gene modules
    returned by the analysis.

    Read more about it
    [here](http://bioconductor.org/packages/release/bioc/vignettes/CEMiTool/inst/doc/CEMiTool.html)

    [^1]: Russo, P.S.T., Ferreira, G.R., Cardozo, L.E. et al. CEMiTool: a Bioconductor
    package for performing comprehensive modular co-expression analyses.
    BMC Bioinformatics 19, 56 (2018). https://doi.org/10.1186/s12859-018-2053-1
    """
    return run_cemitool(
        sample_name=sample_name,
        expression_data=expression_data,
        sample_annotation=sample_annotation,
        pathways=pathways,
        interaction_table=interaction_table,
    )


LaunchPlan(
    cemitool,
    "Default expression data",
    {
        "sample_name": "default_expr",
        "expression_data": "s3://latch-public/test-data/4318/cemitool_expression_data.csv",
        "sample_annotation": "s3://latch-public/test-data/4318/cemitool_sample_annotation.csv",
        "pathways": "s3://latch-public/test-data/4318/cemitool_pathways.gmt",
        "interaction_table": "s3://latch-public/test-data/4318/cemitool_interactions.csv",
    },
)
