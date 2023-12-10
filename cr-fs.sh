#!/bin/bash

# Default file creation flag
create_files=true

# Function to create directories
create_dir() {
    mkdir -p "$1"
}

# Function to create files
create_file() {
    if [ "$create_files" = true ]; then
        touch "$1"
    fi
}

# Parse command line arguments
while getopts ":n" opt; do
  case $opt in
    n)
      create_files=false
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Shift off the options and optional --
shift "$((OPTIND-1))"

# Project name is the first argument
project_name=$1

if [ -z "$project_name" ]; then
    echo "No project name specified"
    exit 1
fi

# Base project directory
base_dir="./$project_name"

# Creating directories
create_dir "$base_dir/AIOps"
create_dir "$base_dir/DevDocs"
create_dir "$base_dir/MLOps/AppliedML/1_ner_keyinfo"
create_dir "$base_dir/MLOps/AppliedML/2_anom_detect"
create_dir "$base_dir/MLOps/AppliedML/3_model_chain"
create_dir "$base_dir/MLOps/AppliedML/4_output_models"
create_dir "$base_dir/MLOps/mlops"
create_dir "$base_dir/MLOps/notebooks"
create_dir "$base_dir/MLOps/scripts"
create_dir "$base_dir/analyticsLake"
create_dir "$base_dir/dataEngineering/analysis"
create_dir "$base_dir/dataEngineering/final"
create_dir "$base_dir/dataEngineering/processing/parsing/logpai logparser 4953a44db58aeca8aad980c386075dfb8d96b871 logparser-LogCluster"
create_dir "$base_dir/dataEngineering/processing/parsing/src"
create_dir "$base_dir/dataEngineering/tools/pre-processing"
create_dir "$base_dir/devOps/kubeflow"
create_dir "$base_dir/devOps/kubernetes"
create_dir "$base_dir/devOps/log_tools"
create_dir "$base_dir/devOps/logs"
create_dir "$base_dir/devOps/mlops"
create_dir "$base_dir/devOps/models/1_ner_keyinfo"
create_dir "$base_dir/devOps/models/2_anom_detect"
create_dir "$base_dir/devOps/models/3_model_chain"
create_dir "$base_dir/devOps/models/4_outputs"
create_dir "$base_dir/devOps/notebooks"
create_dir "$base_dir/devOps/public"
create_dir "$base_dir/devOps/scripts"
create_dir "$base_dir/devOps/src/app/app_fn"
create_dir "$base_dir/devOps/src/tests"
create_dir "$base_dir/documentation"
create_dir "$base_dir/earth/api/controllers"
create_dir "$base_dir/earth/api/examples"
create_dir "$base_dir/earth/api/models"
create_dir "$base_dir/earth/globalAuth"
create_dir "$base_dir/earth/scripts"
create_dir "$base_dir/elasticDBMS/chromadb"
create_dir "$base_dir/elasticDBMS/elastic"
create_dir "$base_dir/obs_tools"
create_dir "$base_dir/omni_logs/aiops_logs"
create_dir "$base_dir/omni_logs/devops_logs"
create_dir "$base_dir/omni_logs/mlops_logs"
create_dir "$base_dir/public"
create_dir "$base_dir/src/app/arc/app_fn"
create_dir "$base_dir/testing"
create_dir "$base_dir/taskAutomation_DAGS"