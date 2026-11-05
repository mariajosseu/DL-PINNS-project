# DTU HPC workflow

## One-time environment setup on a compute node

```bash
cd ~/projects/DL-PINNS-project
module load python3/3.11.13
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

PyTorch is deliberately installed separately: choose a GPU build compatible with
the DTU GPU driver using https://pytorch.org/get-started/locally/ .
The setup above alone does not install PyTorch.
Do not copy a Mac virtual environment onto HPC.

## Update the HPC copy

Push your changes from your Mac first, then on HPC:

```bash
cd ~/projects/DL-PINNS-project
git pull --ff-only
module load python3/3.11.13
source .venv/bin/activate
```

Reinstall dependencies only when they change. For short GPU checks, enter an
interactive GPU node with `a100sh`, then change to the project folder and load
the module and environment again. Use batch jobs for training.

## Before adding a batch script

Choose your training entry point and resource requirements. A batch script must
load the Python module and activate the environment itself. Create its log
folder before submission. Do not manually override CUDA_VISIBLE_DEVICES.

Keep the working copy unchanged while jobs are queued or running. Record the
Git commit, seed, configuration, package versions and checkpoints per run.
Scratch storage is not backed up: preserve important results separately.

DTU documentation: https://www.hpc.dtu.dk/?page_id=4788
