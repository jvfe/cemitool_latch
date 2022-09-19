#!/usr/bin/env Rscript

library(CEMiTool)

args <- commandArgs(trailingOnly = TRUE)

sample_name <- args[1]

expr_data_path <- args[2]
sample_annotation_path <- args[3]
gmt_data_path <- args[4]
int_df_path <- args[5]

output_report <- paste0("./report_", sample_name)

expr_data <- read.csv(expr_data_path)
sample_annotation <- read.csv(sample_annotation_path)
gmt_data <- read_gmt(gmt_data_path)
int_df <- read.csv(int_df_path)

rownames(expr_data) <- expr_data[, 1]
expr_data <- expr_data[, -1]

cem <-
  cemitool(
    expr = expr_data,
    annot = sample_annotation,
    gmt = gmt_data,
    interactions = int_df,
    filter = TRUE,
    plot = TRUE,
    verbose = TRUE
  )

generate_report(cem, directory = output_report, force = TRUE)

write_files(cem, directory=paste0(output_report, "/tables"), force = TRUE)
