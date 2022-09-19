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
    "input_file": LatchParameter(
        display_name="Input File",
        batch_table_column=True,
    ),
}
