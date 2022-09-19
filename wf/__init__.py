import subprocess

from latch import medium_task, workflow
from latch.types import LatchFile

from .docs import metadata


@medium_task
def run_cemitool(input_file: LatchFile) -> LatchFile:
    """
    You can run R files as a subprocess:

        subprocess.run(
            [
                "Rscript",
                "path/to/your_script.R",
                "command_line_arg_1",
                "command_line_arg_2",
                ...
            ],
            check=True,
        )
    """

    subprocess.run(
        [
            "Rscript",
            "/root/cemitool.R",
        ],
        check=True,
    )


@workflow(metadata)
def cemitool(input_file: LatchFile) -> LatchFile:
    """Co-expression Modules Identification Tool

    CEMiTool
    ----

    The CEMiTool R package provides users with an easy-to-use method
    to automatically run gene co-expression analyses. In addition, it performs gene
    set enrichment analysis and over representation analysis for the gene modules
    returned by the analysis.
    """
    return run_cemitool(input_file=input_file)
