from latch.types import LatchAuthor, LatchMetadata, LatchParameter

metadata = LatchMetadata(
    display_name="CEMiTool",
    documentation="https://github.com/jvfe/cemitool_latch/blob/main/README.md",
    author=LatchAuthor(
        name="jvfe",
        github="https://github.com/jvfe",
    ),
    repository="https://github.com/jvfe/cemitool_latch",
    license="MIT",
)

metadata.parameters = {
    "sample_name": LatchParameter(
        display_name="Sample name",
        section_title="Expression Results",
        description="Text to identify the sample by. Will define output directory.",
    ),
    "expression_data": LatchParameter(
        display_name="Expression data",
        description="CSV file with a normalized expression matrix."
        "First column should correspond to gene identifiers while every other column should be a sample"
        "and its respective expression values",
    ),
    "sample_annotation": LatchParameter(
        display_name="Sample annotation",
        description="CSV file specifying sample names (1st column - Named 'SampleName')"
        "and the group they belong to (2nd column - Named 'Class'), which will be used to make contrasts",
    ),
    "pathways": LatchParameter(
        display_name="GMT file to perform over-representation analysis",
        section_title="Functional annotation data",
        description="A GMT file with pathways/terms and genes which will be used to perform ORA analysis.",
    ),
    "interaction_table": LatchParameter(
        display_name="CSV file of interactions between genes",
        description="CSV file with interaction data."
        "In one column a gene identifier and in the other, a gene it's linked to.",
    ),
}
